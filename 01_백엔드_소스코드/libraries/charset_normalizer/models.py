# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

from __future__ import annotations
from encodings.aliases import aliases
from hashlib import sha256
from json import dumps
from re import sub
from typing import Any, Iterator, List, Tuple
from constant import RE_POSSIBLE_ENCODING_INDICATION, TOO_BIG_SEQUENCE
from utils import iana_name, is_multi_byte_encoding, unicode_range

class CharsetMatch:
    
    def __init__(self, payload, guessed_encoding, mean_mess_ratio = None, has_sig_or_bom = None, languages = None, decoded_payload = (None, None), preemptive_declaration = ('payload', 'bytes', 'guessed_encoding', 'str', 'mean_mess_ratio', 'float', 'has_sig_or_bom', 'bool', 'languages', 'CoherenceMatches', 'decoded_payload', 'str | None', 'preemptive_declaration', 'str | None')):
        self._payload = payload
        self._encoding = guessed_encoding
        self._mean_mess_ratio = mean_mess_ratio
        self._languages = languages
        self._has_sig_or_bom = has_sig_or_bom
        self._unicode_ranges = None
        self._leaves = []
        self._mean_coherence_ratio = 0
        self._output_payload = None
        self._output_encoding = None
        self._string = decoded_payload
        self._preemptive_declaration = preemptive_declaration

    
    def __eq__(self = None, other = None):
