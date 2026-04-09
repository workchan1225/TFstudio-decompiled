# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parse_comment.pyc (Python 3.11)

from typing import TYPE_CHECKING
from utils.constants import JSONReturnType
from utils.json_context import ContextValues
if TYPE_CHECKING:
    from json_parser import JSONParser

def parse_comment(self = None):
    '''
    Parse code-like comments:

    - "# comment": A line comment that continues until a newline.
    - "// comment": A line comment that continues until a newline.
    - "/* comment */": A block comment that continues until the closing delimiter "*/".

    The comment is skipped over and an empty string is returned so that comments do not interfere
    with the actual JSON elements.
    '''
    char = self.get_char_at()
    termination_characters = [
        '\n',
        '\r']
    if ContextValues.ARRAY in self.context.context:
        termination_characters.append(']')
    if ContextValues.OBJECT_VALUE in self.context.context:
        termination_characters.append('}')
    if ContextValues.OBJECT_KEY in self.context.context:
        termination_characters.append(':')
# WARNING: Decompyle incomplete
