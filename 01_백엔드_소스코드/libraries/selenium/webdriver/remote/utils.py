# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import json
from typing import Any

def dump_json(json_struct = None):
    return json.dumps(json_struct)


def load_json(s = None):
    return json.loads(s)
