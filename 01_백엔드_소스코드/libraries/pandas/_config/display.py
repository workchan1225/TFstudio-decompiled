# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: display.pyc (Python 3.11)

'''
Unopinionated display configuration.
'''
from __future__ import annotations
import locale
import sys
from pandas._config import config as cf
_initial_defencoding: 'str | None' = None

def detect_console_encoding():
    '''
    Try to find the most capable encoding supported by the console.
    slightly modified from the way IPython handles the same issue.
    '''
    global _initial_defencoding
    encoding = None
    
    try:
        if not sys.stdout.encoding:
            encoding = sys.stdin.encoding
        else:
            except (AttributeError, OSError):
                pass
            if encoding or 'ascii' in encoding.lower():
                
                try:
                    encoding = locale.getpreferredencoding()
                except locale.Error:
                    pass

                if encoding or 'ascii' in encoding.lower():
                    encoding = sys.getdefaultencoding()

    if not _initial_defencoding:
        _initial_defencoding = sys.getdefaultencoding()
    return encoding

pc_encoding_doc = '\n: str/unicode\n    Defaults to the detected encoding of the console.\n    Specifies the encoding to be used for strings returned by to_string,\n    these are generally strings meant to be displayed on the console.\n'
cf.config_prefix('display')
cf.register_option('encoding', detect_console_encoding(), pc_encoding_doc, validator = cf.is_text)
None(None, None)
return None
with None:
    if not None:
        pass
