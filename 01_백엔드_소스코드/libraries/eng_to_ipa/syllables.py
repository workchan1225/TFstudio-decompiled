# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: syllables.pyc (Python 3.11)

import re
import os
import json
from eng_to_ipa import transcribe
phones_json = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources', 'phones.json'), 'r')
PHONES = json.load(phones_json)
None(None, None)
