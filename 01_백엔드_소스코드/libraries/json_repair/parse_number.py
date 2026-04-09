# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parse_number.pyc (Python 3.11)

from typing import TYPE_CHECKING
from utils.constants import JSONReturnType
from utils.json_context import ContextValues
NUMBER_CHARS: set[str] = set('0123456789-.eE/,_')
if TYPE_CHECKING:
    from json_parser import JSONParser

def parse_number(self = None):
    number_str = ''
    char = self.get_char_at()
    is_array = self.context.current == ContextValues.ARRAY
# WARNING: Decompyle incomplete
