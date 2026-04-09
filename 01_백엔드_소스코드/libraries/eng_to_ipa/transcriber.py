# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcriber.pyc (Python 3.11)

import re
from os.path import join, abspath, dirname
import eng_to_ipa.stress as eng_to_ipa
import sqlite3
from collections import defaultdict

class Transcriber:
    
    def __init__(self, mode, stress = ('sql', 'both')):
        self._mode = mode
        self.stress = stress
        self.c = None

    _mode = (lambda self: self.mode)()
    _mode = (lambda self, value: if value.lower() == 'sql':
conn = sqlite3.connect(join(abspath(dirname(__file__)), './resources/CMU_dict.db'))self.c = conn.cursor()self.mode = '')()
