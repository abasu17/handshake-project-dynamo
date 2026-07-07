#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

set +e
pytest /tests/test_outputs.py -rA
status=$?
set -e

if [ "$status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
  echo 1 > /app/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
  echo 0 > /app/reward.txt
fi

python3 - <<'PY'
import json
from pathlib import Path

reward = Path('/logs/verifier/reward.txt').read_text(encoding='utf-8').strip()
passed = reward == '1'
ctrf = {
    'results': {
        'tool': {'name': 'pytest'},
        'summary': {
            'tests': 4,
            'passed': 4 if passed else 0,
            'failed': 0 if passed else 4,
            'skipped': 0,
        },
        'tests': [],
    }
}
Path('/logs/verifier/ctrf.json').write_text(json.dumps(ctrf, indent=2) + '\n', encoding='utf-8')
PY

exit "$status"
