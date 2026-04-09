# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_encoding.pyc (Python 3.11)

'''Encoding related utilities.'''
import re
_cescape_chr_to_symbol_map = { }
_cescape_chr_to_symbol_map[9] = '\\t'
_cescape_chr_to_symbol_map[10] = '\\n'
_cescape_chr_to_symbol_map[13] = '\\r'
_cescape_chr_to_symbol_map[34] = '\\"'
_cescape_chr_to_symbol_map[39] = "\\'"
_cescape_chr_to_symbol_map[92] = '\\\\'
_cescape_unicode_to_str = range(0, 256)()
for byte, string in _cescape_chr_to_symbol_map.items():
    _cescape_unicode_to_str[byte] = string
    _cescape_byte_to_str = (lambda .0: [ '\\%03o' % i for i in .0 ]) + range(127, 256)()
    for byte, string in _cescape_chr_to_symbol_map.items():
        _cescape_byte_to_str[byte] = string
        del byte
        del string
        
        def CEscape(text = (lambda .0: [ '\\%03o' % i for i in .0 ]), as_utf8 = range(0, 32)()):
            '''Escape a bytes string for use in an text protocol buffer.

  Args:
    text: A byte string to be escaped.
    as_utf8: Specifies if result may contain non-ASCII characters.
        In Python 3 this allows unescaped non-ASCII Unicode characters.
        In Python 2 the return value will be valid UTF-8 rather than only ASCII.
  Returns:
    Escaped string (str).
  '''
            pass
        # WARNING: Decompyle incomplete

        _CUNESCAPE_HEX = re.compile('(\\\\+)x([0-9a-fA-F])(?![0-9a-fA-F])')
        
        def CUnescape(text = None):
            '''Unescape a text string with C-style escape sequences to UTF-8 bytes.

  Args:
    text: The data to parse in a str.
  Returns:
    A byte string.
  '''
            
            def ReplaceHex(m):
                if len(m.group(1)) & 1:
                    return m.group(1) + 'x0' + m.group(2)
                return None.group(0)

            result = _CUNESCAPE_HEX.sub(ReplaceHex, text)
            return result.encode('utf-8').decode('unicode_escape').encode('raw_unicode_escape')

        return None
