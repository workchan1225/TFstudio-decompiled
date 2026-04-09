# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: commontypes.pyc (Python 3.11)

import sys
from  import model
from error import FFIError
COMMON_TYPES = { }

try:
    from _cffi_backend import _get_common_types
    _get_common_types(COMMON_TYPES)
except ImportError:
    pass

COMMON_TYPES['FILE'] = model.unknown_type('FILE', '_IO_FILE')
COMMON_TYPES['bool'] = '_Bool'
COMMON_TYPES['float _Complex'] = '_cffi_float_complex_t'
COMMON_TYPES['double _Complex'] = '_cffi_double_complex_t'
for _type in model.PrimitiveType.ALL_PRIMITIVE_TYPES:
    if _type.endswith('_t'):
        COMMON_TYPES[_type] = _type
    del _type
    _CACHE = { }
    
    def resolve_common_type(parser, commontype):
        pass
    # WARNING: Decompyle incomplete

    
    def win_common_types():
        return {
            'UNICODE_STRING': model.StructType('_UNICODE_STRING', [
                'Length',
                'MaximumLength',
                'Buffer'], [
                model.PrimitiveType('unsigned short'),
                model.PrimitiveType('unsigned short'),
                model.PointerType(model.PrimitiveType('wchar_t'))], [
                -1,
                -1,
                -1]),
            'PUNICODE_STRING': 'UNICODE_STRING *',
            'PCUNICODE_STRING': 'const UNICODE_STRING *',
            'TBYTE': 'set-unicode-needed',
            'TCHAR': 'set-unicode-needed',
            'LPCTSTR': 'set-unicode-needed',
            'PCTSTR': 'set-unicode-needed',
            'LPTSTR': 'set-unicode-needed',
            'PTSTR': 'set-unicode-needed',
            'PTBYTE': 'set-unicode-needed',
            'PTCHAR': 'set-unicode-needed' }

    if sys.platform == 'win32':
        COMMON_TYPES.update(win_common_types())
        return None
    return None
