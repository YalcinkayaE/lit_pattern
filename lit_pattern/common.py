"""Strict file/configuration loading shared by the pipeline commands."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ImportError as exc:
    raise SystemExit(
        'error: jsonschema is required; install requirements.txt with '
        '`python3 -m pip install -r requirements.txt`'
    ) from exc

ROOT = Path(__file__).resolve().parents[1]


class InputError(ValueError):
    """A user input, configuration, or persisted artifact is invalid."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True,
                       allow_nan=False) + '\n').encode('utf-8')


def read_json(path: Path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise InputError(f'{path}: duplicate JSON key {key!r}')
            result[key] = value
        return result

    def invalid_constant(value):
        raise InputError(f'{path}: invalid JSON constant {value}')

    def finite_float(value):
        number = float(value)
        if not math.isfinite(number):
            raise InputError(f'{path}: non-finite JSON number {value}')
        return number

    try:
        return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs,
                          parse_constant=invalid_constant, parse_float=finite_float)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise InputError(f'{path}: {exc}') from exc


def json_path(parts) -> str:
    return '$' + ''.join(f'[{p}]' if isinstance(p, int) else f'.{p}' for p in parts)


def load_config(path: Path) -> dict:
    value = read_json(path)
    schema = read_json(ROOT / 'schemas/pipeline.schema.json')
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise InputError(f'invalid pipeline schema: {exc.message}') from exc
    errors = sorted(Draft202012Validator(schema).iter_errors(value),
                    key=lambda e: str(list(e.path)))
    if errors:
        error = errors[0]
        raise InputError(f'configuration {json_path(error.path)}: {error.message}')
    return value


def configured_path(config_path: Path, value: str) -> Path:
    return (config_path.resolve().parent / value).resolve()
