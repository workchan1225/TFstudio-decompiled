# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from typing import Any

class MissingValueType:
    
    def __repr__(self = None):
        return '<MISSING_VALUE>'

    
    def __deepcopy__(self = None, memo = None):
        return self


MISSING_VALUE = MissingValueType()
JSONReturnType = dict[(str, Any)] | list[Any] | str | float | int | bool | None
STRING_DELIMITERS: list[str] = [
    '"',
    "'",
    '“',
    '”']
