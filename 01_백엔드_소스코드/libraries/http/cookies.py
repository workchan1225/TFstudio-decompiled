# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cookies.pyc (Python 3.11)

'''
Here\'s a sample session to show how to use this module.
At the moment, this is the only documentation.

The Basics
----------

Importing is easy...

   >>> from http import cookies

Most of the time you start by creating a cookie.

   >>> C = cookies.SimpleCookie()

Once you\'ve created your Cookie, you can add values just as if it were
a dictionary.

   >>> C = cookies.SimpleCookie()
   >>> C["fig"] = "newton"
   >>> C["sugar"] = "wafer"
   >>> C.output()
   \'Set-Cookie: fig=newton\\r\\nSet-Cookie: sugar=wafer\'

Notice that the printable representation of a Cookie is the
appropriate format for a Set-Cookie: header.  This is the
default behavior.  You can change the header and printed
attributes by using the .output() function

   >>> C = cookies.SimpleCookie()
   >>> C["rocky"] = "road"
   >>> C["rocky"]["path"] = "/cookie"
   >>> print(C.output(header="Cookie:"))
   Cookie: rocky=road; Path=/cookie
   >>> print(C.output(attrs=[], header="Cookie:"))
   Cookie: rocky=road

The load() method of a Cookie extracts cookies from a string.  In a
CGI script, you would use this method to extract the cookies from the
HTTP_COOKIE environment variable.

   >>> C = cookies.SimpleCookie()
   >>> C.load("chips=ahoy; vienna=finger")
   >>> C.output()
   \'Set-Cookie: chips=ahoy\\r\\nSet-Cookie: vienna=finger\'

The load() method is darn-tootin smart about identifying cookies
within a string.  Escaped quotation marks, nested semicolons, and other
such trickeries do not confuse it.

   >>> C = cookies.SimpleCookie()
   >>> C.load(\'keebler="E=everybody; L=\\\\"Loves\\\\"; fudge=\\\\012;";\')
   >>> print(C)
   Set-Cookie: keebler="E=everybody; L=\\"Loves\\"; fudge=\\012;"

Each element of the Cookie also supports all of the RFC 2109
Cookie attributes.  Here\'s an example which sets the Path
attribute.

   >>> C = cookies.SimpleCookie()
   >>> C["oreo"] = "doublestuff"
   >>> C["oreo"]["path"] = "/"
   >>> print(C)
   Set-Cookie: oreo=doublestuff; Path=/

Each dictionary element has a \'value\' attribute, which gives you
back the value associated with the key.

   >>> C = cookies.SimpleCookie()
   >>> C["twix"] = "none for you"
   >>> C["twix"].value
   \'none for you\'

The SimpleCookie expects that all values should be standard strings.
Just to be sure, SimpleCookie invokes the str() builtin to convert
the value to a string, when the values are set dictionary-style.

   >>> C = cookies.SimpleCookie()
   >>> C["number"] = 7
   >>> C["string"] = "seven"
   >>> C["number"].value
   \'7\'
   >>> C["string"].value
   \'seven\'
   >>> C.output()
   \'Set-Cookie: number=7\\r\\nSet-Cookie: string=seven\'

Finis.
'''
import re
import string
import types
__all__ = [
    'CookieError',
    'BaseCookie',
    'SimpleCookie']
_nulljoin = ''.join
_semispacejoin = '; '.join
_spacejoin = ' '.join

class CookieError(Exception):
    pass

_LegalChars = string.ascii_letters + string.digits + "!#$%&'*+-.^_`|~:"
_UnescapedChars = _LegalChars + ' ()/<=>?@[]{}'
_Translator = set(range(256)) - set(map(ord, _UnescapedChars))()
_Translator.update({
    ord('\\'): '\\\\',
    ord('"'): '\\"' })
_is_legal_key = re.compile('[%s]+' % re.escape(_LegalChars)).fullmatch

def _quote(str):
    '''Quote a string for use in a cookie header.

    If the string does not need to be double-quoted, then just return the
    string.  Otherwise, surround the string in doublequotes and quote
    (with a \\) special characters.
    '''
    pass
# WARNING: Decompyle incomplete

_OctalPatt = re.compile('\\\\[0-3][0-7][0-7]')
_QuotePatt = re.compile('[\\\\].')

def _unquote(str):
    pass
# WARNING: Decompyle incomplete

_weekdayname = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun']
_monthname = [
    None,
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec']

def _getdate(future, weekdayname, monthname = (0, _weekdayname, _monthname)):
    gmtime = gmtime
    time = time
    import time
    now = time()
    (year, month, day, hh, mm, ss, wd, y, z) = gmtime(now + future)
    return '%s, %02d %3s %4d %02d:%02d:%02d GMT' % (weekdayname[wd], day, monthname[month], year, hh, mm, ss)


class Morsel(dict):
    '''A class to hold ONE (key, value) pair.

    In a cookie, each such pair may have several attributes, so this class is
    used to keep the attributes associated with the appropriate key,value pair.
    This class also includes a coded_value attribute, which is used to hold
    the network representation of the value.
    '''
    _reserved = {
        'expires': 'expires',
        'path': 'Path',
        'comment': 'Comment',
        'domain': 'Domain',
        'max-age': 'Max-Age',
        'secure': 'Secure',
        'httponly': 'HttpOnly',
        'version': 'Version',
        'samesite': 'SameSite' }
    _flags = {
        'secure',
        'httponly'}
    
    def __init__(self):
        self._key = None
        self._value = None
        self._coded_value = None
        for key in self._reserved:
            dict.__setitem__(self, key, '')
            return None

    key = (lambda self: self._key)()
    value = (lambda self: self._value)()
    coded_value = (lambda self: self._coded_value)()
    
    def __setitem__(self, K, V):
        K = K.lower()
        if K not in self._reserved:
            raise CookieError(f'''Invalid attribute {K!r}''')
        dict.__setitem__(self, K, V)

    
    def setdefault(self, key, val = (None,)):
        key = key.lower()
        if key not in self._reserved:
            raise CookieError(f'''Invalid attribute {key!r}''')
        return dict.setdefault(self, key, val)

    
    def __eq__(self, morsel):
