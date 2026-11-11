"""Real-source extraction and failure-boundary tests; no corpus annotations."""
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NormalisationTests(unittest.TestCase):
    def run_cli(self, output, *args, config=None):
        return subprocess.run(
            [sys.executable, '-m', 'lit_pattern.normalise', '--config',
             str(config or ROOT / 'config/pipeline.json'), '--output', str(output), *args],
            cwd=ROOT, capture_output=True, text=True,
        )

    def test_lossless_deterministic_extraction_and_review_queue(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'normalised'
            result = self.run_cli(out)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((out / 'source.csv').read_bytes(),
                             (ROOT / 'literary_and_video_patterns.csv').read_bytes())
            patterns = list(csv.DictReader(io.StringIO((out / 'patterns.csv').read_text())))
            self.assertEqual(len(patterns), 59)
            self.assertEqual(patterns[0]['pattern_id'], 'GEN01')
            self.assertEqual({p['status'] for p in patterns}, {'proposed'})
            self.assertIn('definition', patterns[0])
            self.assertNotIn('related_patterns', patterns[0])
            candidates = list(csv.DictReader(io.StringIO((out / 'relation_candidates.csv').read_text())))
            self.assertTrue(any(r['listed_by_pattern_id'] == 'VID07' and
                                r['related_pattern_id'] == 'STR10' for r in candidates))
            self.assertEqual(list(csv.DictReader(io.StringIO((out / 'relations.csv').read_text()))), [])
            review = json.loads((out / 'review_items.json').read_text())
            self.assertTrue(any(r['kind'] == 'indicator_segmentation' for r in review))
            self.assertTrue(any(r['kind'] == 'relation_typing' for r in review))
            manifest = json.loads((out / 'manifest.json').read_text())
            self.assertEqual(manifest['source_sha256'], hashlib.sha256((out / 'source.csv').read_bytes()).hexdigest())
            before = {p.name: p.read_bytes() for p in out.iterdir()}
            self.assertEqual(self.run_cli(out).returncode, 0)
            self.assertEqual(before, {p.name: p.read_bytes() for p in out.iterdir()})
            self.assertEqual(self.run_cli(out, '--check').returncode, 0)

    def test_stale_or_extra_output_is_detected_by_check(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'normalised'
            self.assertEqual(self.run_cli(out).returncode, 0)
            (out / 'patterns.csv').write_text('tampered')
            result = self.run_cli(out, '--check')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('patterns.csv', result.stderr)

    def test_rejects_unowned_or_source_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            (out / 'keep.txt').write_text('keep')
            result = self.run_cli(out)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('unowned', result.stderr)
            self.assertEqual((out / 'keep.txt').read_text(), 'keep')
        result = self.run_cli(ROOT)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('source', result.stderr)

    def test_invalid_source_and_configuration_fail_explicitly(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            config = json.loads((ROOT / 'config/pipeline.json').read_text())
            config['annotation_schema'] = str(ROOT / 'schemas/annotation.schema.json')
            config['source'] = str(temp / 'source.csv')
            source = (ROOT / 'literary_and_video_patterns.csv').read_text(encoding='utf-8-sig')
            for name, content, error in [
                ('duplicate-header', source.replace('pattern_id,label_type', 'pattern_id,pattern_id', 1), 'header'),
                ('duplicate-id', source.replace('GEN02,', 'GEN01,', 1), 'duplicate'),
                ('bad-endpoint', source.replace('DEV01; DEV04', 'BAD99; DEV04', 1), 'BAD99'),
                ('missing-value', source.replace('GEN01,genre,Comedy,', 'GEN01,genre,,', 1), 'label'),
            ]:
                with self.subTest(name=name):
                    (temp / 'source.csv').write_text(content)
                    config['source_sha256'] = hashlib.sha256((temp / 'source.csv').read_bytes()).hexdigest()
                    path = temp / 'pipeline.json'; path.write_text(json.dumps(config))
                    result = self.run_cli(temp / 'out', config=path)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(error, result.stderr)
            path.write_text('{"source":"a","source":"b"}')
            result = self.run_cli(temp / 'out', config=path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('duplicate JSON key', result.stderr)

    def test_unowned_manifest_and_extra_files_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'out'; out.mkdir()
            (out / 'manifest.json').write_text('{}')
            (out / 'patterns.csv').write_text('user data')
            result = self.run_cli(out)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('unowned', result.stderr)
            self.assertEqual((out / 'patterns.csv').read_text(), 'user data')
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / 'out'; self.assertEqual(self.run_cli(out).returncode, 0)
            (out / 'keep.txt').write_text('keep')
            for args in [(), ('--check',)]:
                result = self.run_cli(out, *args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('unexpected', result.stderr)
                self.assertEqual((out / 'keep.txt').read_text(), 'keep')

    def test_explicit_typed_relations_and_invalid_source_namespace(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            config = json.loads((ROOT / 'config/pipeline.json').read_text())
            config['source'] = str(ROOT / 'literary_and_video_patterns.csv')
            config['relation_decisions'] = [{'source':'VID07','target':'STR10',
                'relation_type':'co_occurs_with','rationale':'Invented extraction test decision'}]
            path = temp / 'pipeline.json'; path.write_text(json.dumps(config))
            out = temp / 'out'; result = self.run_cli(out, config=path)
            self.assertEqual(result.returncode, 0, result.stderr)
            relations = list(csv.DictReader(io.StringIO((out / 'relations.csv').read_text())))
            self.assertEqual(len(relations), 1)
            self.assertEqual(relations[0]['symmetric'], 'true')
            config['source'] = str(temp / 'source.csv')
            data = (ROOT / 'literary_and_video_patterns.csv').read_text(encoding='utf-8-sig').replace('GEN01,', 'INVALID,', 1)
            (temp / 'source.csv').write_text(data)
            config['source_sha256'] = hashlib.sha256((temp / 'source.csv').read_bytes()).hexdigest()
            path.write_text(json.dumps(config))
            result = self.run_cli(out, config=path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('pattern_id', result.stderr)

    def test_source_digest_mismatch_and_missing_config_fail(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            config = json.loads((ROOT / 'config/pipeline.json').read_text())
            config['source'] = str(ROOT / 'literary_and_video_patterns.csv')
            config['source_sha256'] = '0' * 64
            path = temp / 'pipeline.json'; path.write_text(json.dumps(config))
            result = self.run_cli(temp / 'out', config=path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('checksum', result.stderr)
            self.assertNotEqual(self.run_cli(temp / 'out', config=temp / 'missing.json').returncode, 0)


if __name__ == '__main__':
    unittest.main()
