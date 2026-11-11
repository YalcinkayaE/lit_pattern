"""Invented conformance records, never pilot or taxonomy evidence."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def bundle(pattern='STR05', modality='literature'):
    config = json.loads((ROOT / 'config/pipeline.json').read_text())
    locator = {'type': 'text', 'reference': 'invented chapter 1 paragraph 1'}
    later = {'type': 'text', 'reference': 'invented chapter 2 paragraph 1'}
    if modality == 'video':
        locator = {'type': 'timestamp', 'start': 1, 'end': 2}
        later = {'type': 'timestamp', 'start': 10, 'end': 12}
    roles = {'STR05': ['cue','later_event'], 'STR09':['setup','payoff'],
             'STR06':['misleading_cue','invited_inference','corrective_evidence'],
             'STR07':['claim','disconfirming_evidence'],
             'STR10':['knowledge_state']}.get(pattern, ['support'])
    evidence = [{'evidence_id': f'e{i}', 'kind':'paraphrase', 'description':'Invented conformance evidence',
                 'locator': deepcopy(locator if i == 0 else later), 'role': role}
                for i, role in enumerate(roles)]
    if pattern == 'STR10':
        evidence[0].update(kind='knowledge_state', knowledge=[
            {'holder':'audience','information':'The invitation was forged','knows':True},
            {'holder':'recipient','information':'The invitation was forged','knows':False}])
    annotation = {'annotation_id':'a1','work_id':'w1','unit_id':'u1','pattern_id':pattern,
                  'pattern_version':config['pattern_version'],'schema_version':config['schema_version'],
                  'presence':'present','rationale':'Invented rationale for conformance only',
                  'reviewer':'r1','modality':modality,'created_at':'2026-11-11T12:00:00Z',
                  'evidence':evidence}
    if pattern == 'STR09': annotation['connection'] = 'The introduced element causes the later consequence'
    events = [] if pattern == 'STR10' else [
        {'event_id':f'event{i}','annotation_id':'a1','evidence_id':e['evidence_id'],
         'presentation_order':i,'role':'setup' if i == 0 else 'consequence'}
        for i,e in enumerate(evidence)]
    return {'schema_version':config['schema_version'],'source_sha256':config['source_sha256'],
            'works':[{'work_id':'w1','title':'Invented test work','version':'fixture-1','modality':modality}],
            'units':[{'unit_id':'u1','work_id':'w1','unit_type':'scene','locator':locator}],
            'reviewers':[{'reviewer_id':'r1'}], 'annotations':[annotation],
            'events':events,'adjudications':[]}


class AnnotationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.catalogue = Path(cls.temp.name) / 'catalogue'
        cls.generated = subprocess.run([sys.executable,'-m','lit_pattern.normalise','--config',
            str(ROOT/'config/pipeline.json'),'--output',str(cls.catalogue)],cwd=ROOT,capture_output=True,text=True)
        if cls.generated.returncode: raise AssertionError(cls.generated.stderr)

    @classmethod
    def tearDownClass(cls): cls.temp.cleanup()

    def cli(self, value, *, raw=None, catalogue=None):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'annotations.json'
            path.write_text(json.dumps(value) if raw is None else raw)
            result = subprocess.run([sys.executable,'-m','lit_pattern.validate','--config',
                str(ROOT/'config/pipeline.json'),'--catalogue',str(catalogue or self.catalogue),
                '--input',str(path)],cwd=ROOT,capture_output=True,text=True)
            return result

    def assert_error(self, value, code, path):
        result = self.cli(value)
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(any(e['code'] == code and e['path'] == path for e in report['errors']), report)

    def test_positive_literary_video_sequential_and_knowledge_cases(self):
        for pattern, modality in [('STR05','literature'),('STR09','video'),('STR06','literature'),
                                  ('STR07','literature'),('STR10','video'),('DEV02','literature')]:
            with self.subTest(pattern=pattern,modality=modality):
                result = self.cli(bundle(pattern,modality))
                self.assertEqual(result.returncode,0,result.stderr+result.stdout)
                report = json.loads(result.stdout)
                self.assertEqual(report['errors'],[])
                self.assertEqual(report['counts']['annotations'],1)
                self.assertEqual(report['counts']['present'],1)
                self.assertIn('validator_version',report)

    def test_eight_named_failure_paths_from_validation_plan(self):
        b=bundle(); b['annotations'][0].update(presence='absent',evidence=[])
        self.assert_error(b,'inspection_required','$.annotations[0].evidence')
        b=bundle(); b['annotations'][0]['evidence'][1]['locator']=deepcopy(b['annotations'][0]['evidence'][0]['locator'])
        self.assert_error(b,'distinct_locators','$.annotations[0].evidence')
        b=bundle('STR09'); del b['annotations'][0]['connection']
        self.assert_error(b,'connection_required','$.annotations[0].connection')
        b=bundle('STR06'); b['annotations'][0]['evidence'].pop()
        self.assert_error(b,'evidence_roles','$.annotations[0].evidence')
        b=bundle('STR10'); del b['annotations'][0]['evidence'][0]['knowledge']
        self.assert_error(b,'knowledge_required','$.annotations[0].evidence[0].knowledge')
        b=bundle(); b['events'][0]['annotation_id']='missing'
        self.assert_error(b,'unknown_annotation','$.events[0].annotation_id')
        b=bundle(); b['annotations'][0]['pattern_version']='unsupported'
        self.assert_error(b,'pattern_version','$.annotations[0].pattern_version')
        b=bundle(); b['annotations']=[]; b['events']=[]
        result=self.cli(b); self.assertEqual(result.returncode,0,result.stderr+result.stdout)
        self.assertEqual(json.loads(result.stdout)['counts']['absent'],0)

    def test_uncertain_absent_and_not_applicable_do_not_require_positive_roles(self):
        b=bundle(); a=b['annotations'][0]; a['presence']='uncertain'; a['evidence']=a['evidence'][:1]; b['events']=[]
        self.assertEqual(self.cli(b).returncode,0)
        a['presence']='absent'; a['evidence'][0].update(kind='inspection',inspection_scope='Both relevant chapters',adequacy='Both linked parts inspected')
        self.assertEqual(self.cli(b).returncode,0)
        a['presence']='not_applicable'; a['evidence']=[]
        self.assertEqual(self.cli(b).returncode,0)

    def test_reference_integrity_ids_order_spans_and_knowledge(self):
        cases=[]
        b=bundle(); b['works'].append(deepcopy(b['works'][0])); cases.append((b,'duplicate_id','$.works[1].work_id'))
        b=bundle(); b['annotations'][0]['unit_id']='missing'; cases.append((b,'unknown_unit','$.annotations[0].unit_id'))
        b=bundle(); b['annotations'][0]['reviewer']='missing'; cases.append((b,'unknown_reviewer','$.annotations[0].reviewer'))
        b=bundle(); b['events'][1]['presentation_order']=0; cases.append((b,'duplicate_order','$.events[1].presentation_order'))
        b=bundle(); b['events'][0]['evidence_id']='missing'; cases.append((b,'unknown_evidence','$.events[0].evidence_id'))
        b=bundle('STR09','video'); b['units'][0]['locator']['end']=0; cases.append((b,'locator_span','$.units[0].locator'))
        b=bundle('STR10'); b['annotations'][0]['evidence'][0]['knowledge'][1]['knows']=True
        cases.append((b,'knowledge_asymmetry','$.annotations[0].evidence[0].knowledge'))
        b=bundle(); b['events'][0]['presentation_order']=2; cases.append((b,'event_order','$.annotations[0].evidence'))
        b=bundle(); b['adjudications']=[{'adjudication_id':'j1','annotation_ids':['missing'],'reviewer':'r1','decision':'uncertain','rationale':'Invented rationale'}]
        cases.append((b,'unknown_annotation','$.adjudications[0].annotation_ids[0]'))
        for b,code,path in cases:
            with self.subTest(code=code,path=path): self.assert_error(b,code,path)

    def test_unrelated_evidence_cannot_supply_required_distinct_locators(self):
        b = bundle()
        a = b['annotations'][0]
        a['evidence'][1]['locator'] = deepcopy(a['evidence'][0]['locator'])
        extra = deepcopy(a['evidence'][0])
        extra.update(evidence_id='unrelated', role='unrelated', locator={'type':'text','reference':'invented unrelated page'})
        a['evidence'].append(extra)
        self.assert_error(b, 'distinct_locators', '$.annotations[0].evidence')

    def test_checked_in_fixtures_and_tampered_catalogue(self):
        fixture_set = json.loads((ROOT/'tests/fixtures/annotation_cases.json').read_text())
        for case in fixture_set['cases']:
            b = json.loads((ROOT/'tests/fixtures'/case['path']).read_text())
            result = self.cli(b)
            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        with tempfile.TemporaryDirectory() as temp:
            import shutil
            catalogue = Path(temp)/'catalogue'
            shutil.copytree(self.catalogue, catalogue)
            (catalogue/'patterns.csv').write_text('tampered')
            result = self.cli(bundle(), catalogue=catalogue)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('patterns.csv', result.stderr)

    def test_unlinked_required_role_cannot_satisfy_event_order(self):
        b = bundle()
        b['events'][1]['evidence_id'] = b['events'][0]['evidence_id']
        self.assert_error(b, 'event_order', '$.annotations[0].evidence')

    def test_minute_only_timestamp_is_not_rfc3339_date_time(self):
        b = bundle()
        b['annotations'][0]['created_at'] = '2026-11-11T12:00Z'
        self.assert_error(b, 'schema', '$.annotations[0].created_at')

    def test_required_sequence_evidence_must_be_linked_and_distinct(self):
        b = bundle('STR07')
        b['events'][1]['evidence_id'] = b['events'][0]['evidence_id']
        self.assert_error(b, 'sequence_roles', '$.annotations[0].evidence')
        b = bundle()
        a = b['annotations'][0]
        a['evidence'][1]['locator'] = deepcopy(a['evidence'][0]['locator'])
        extra = deepcopy(a['evidence'][0])
        extra.update(evidence_id='unlinked', locator={'type':'text','reference':'invented other page'})
        a['evidence'].append(extra)
        self.assert_error(b, 'distinct_locators', '$.annotations[0].evidence')

    def test_overflowing_json_numbers_and_invalid_zone_offsets_fail(self):
        b = bundle('STR09', 'video')
        raw = json.dumps(b).replace('"end": 12', '"end": 1e309', 1)
        result = self.cli(b, raw=raw)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('non-finite', result.stderr)
        b = bundle()
        b['annotations'][0]['created_at'] = '2026-11-11T12:00:00+00:99'
        self.assert_error(b, 'schema', '$.annotations[0].created_at')
        b['annotations'][0]['created_at'] = '2026-11-11t12:00:00z'
        result = self.cli(b)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_external_dynamic_reference_is_rejected_before_validation(self):
        from lit_pattern.common import InputError
        from lit_pattern.validate import annotation_schema
        with tempfile.TemporaryDirectory() as temp:
            schema = Path(temp)/'schema.json'
            schema.write_text(json.dumps({'$schema':'https://json-schema.org/draft/2020-12/schema',
                                          '$dynamicRef':'https://example.invalid/schema'}))
            with self.assertRaisesRegex(InputError, 'local references'):
                annotation_schema({'_annotation_schema':str(schema)})

    def test_structure_malformed_json_stale_catalogue_and_dependency(self):
        b=bundle(); b['annotations'][0]['created_at']='yesterday'
        self.assert_error(b,'schema','$.annotations[0].created_at')
        b=bundle('STR09','video'); b['units'][0]['locator']['start']=True
        self.assert_error(b,'schema','$.units[0].locator')
        b=bundle(); b['annotations'][0]['surprise_field']='bad'
        self.assert_error(b,'schema','$.annotations[0]')
        for raw in ['{bad', '{"schema_version":"a","schema_version":"b"}', '{"value":NaN}']:
            result=self.cli({},raw=raw); self.assertNotEqual(result.returncode,0); self.assertIn('error:',result.stderr)
        result=self.cli(bundle(),catalogue=ROOT/'missing-catalogue')
        self.assertNotEqual(result.returncode,0); self.assertIn('stale or missing',result.stderr)
        result=subprocess.run([sys.executable,'-S','-m','lit_pattern.validate','--help'],cwd=ROOT,capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0); self.assertIn('jsonschema is required',result.stderr)


if __name__ == '__main__': unittest.main()
