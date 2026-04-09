# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: string.pyc (Python 3.11)

'''A collection of string constants.

Public module variables:

whitespace -- a string containing all ASCII whitespace
ascii_lowercase -- a string containing all ASCII lowercase letters
ascii_uppercase -- a string containing all ASCII uppercase letters
ascii_letters -- a string containing all ASCII letters
digits -- a string containing all ASCII decimal digits
hexdigits -- a string containing all ASCII hexadecimal digits
octdigits -- a string containing all ASCII octal digits
punctuation -- a string containing all ASCII punctuation characters
printable -- a string containing all ASCII characters considered printable

'''
__all__ = [
    'ascii_letters',
    'ascii_lowercase',
    'ascii_uppercase',
    'capwords',
    'digits',
    'hexdigits',
    'octdigits',
    'printable',
    'punctuation',
    'whitespace',
    'Formatter',
    'Template']
import _string
whitespace = ' \t\n\r\x0b\x0c'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
printable = digits + ascii_letters + punctuation + whitespace

def capwords(s, sep = (None,)):
