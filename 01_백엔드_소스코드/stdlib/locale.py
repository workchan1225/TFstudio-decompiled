# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: locale.pyc (Python 3.11)

__doc__ = "Locale support module.\n\nThe module provides low-level access to the C lib's locale APIs and adds high\nlevel number formatting APIs as well as a locale aliasing engine to complement\nthese.\n\nThe aliasing engine includes support for many commonly used locale names and\nmaps them to values suitable for passing to the C lib's setlocale() function. It\nalso includes default encodings for all supported locale names.\n\n"
import sys
import encodings
import encodings.aliases as encodings
import re
import _collections_abc
from builtins import str as _builtin_str
import functools
__all__ = [
    'getlocale',
    'getdefaultlocale',
    'getpreferredencoding',
    'Error',
    'setlocale',
    'resetlocale',
    'localeconv',
    'strcoll',
    'strxfrm',
    'str',
    'atof',
    'atoi',
    'format',
    'format_string',
    'currency',
    'normalize',
    'LC_CTYPE',
    'LC_COLLATE',
    'LC_TIME',
    'LC_MONETARY',
    'LC_NUMERIC',
    'LC_ALL',
    'CHAR_MAX',
    'getencoding']

def _strcoll(a, b):
    ''' strcoll(string,string) -> int.
        Compares two strings according to the locale.
    '''
    return (a > b) - (a < b)


def _strxfrm(s):
    ''' strxfrm(string) -> string.
        Returns a string that behaves for cmp locale-aware.
    '''
    return s


try:
    from _locale import *
except ImportError:
    CHAR_MAX = 127
    LC_ALL = 6
    LC_COLLATE = 3
    LC_CTYPE = 0
    LC_MESSAGES = 5
    LC_MONETARY = 4
    LC_NUMERIC = 1
    LC_TIME = 2
    Error = ValueError
    
    def localeconv():
        ''' localeconv() -> dict.
            Returns numeric and monetary locale-specific parameters.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def setlocale(category, value = (None,)):
        ''' setlocale(integer,string=None) -> string.
            Activates/queries locale processing.
        '''
        if value not in (None, '', 'C'):
            raise Error('_locale emulation only supports "C" locale')
        return 'C'


if 'strxfrm' not in globals():
    strxfrm = _strxfrm
if 'strcoll' not in globals():
    strcoll = _strcoll
_localeconv = localeconv
_override_localeconv = { }
localeconv = (lambda : d = _localeconv()if _override_localeconv:
d.update(_override_localeconv)d)()

def _grouping_intervals(grouping):
    pass
# WARNING: Decompyle incomplete


def _group(s, monetary = (False,)):
    conv = localeconv()
    if monetary:
        if not 'mon_thousands_sep':
            thousands_sep = conv['thousands_sep']
            if monetary:
                if not 'mon_grouping':
                    grouping = conv['grouping']
                    if not grouping:
                        return (s, 0)
                    if None[-1] == ' ':
                        stripped = s.rstrip()
                        right_spaces = s[len(stripped):]
                        s = stripped
                    else:
                        right_spaces = ''
    left_spaces = ''
    groups = []
    for interval in _grouping_intervals(grouping):
        if s or s[-1] not in '0123456789':
            left_spaces = s
            s = ''
        else:
            groups.append(s[-interval:])
            s = s[:-interval]
        if s:
            groups.append(s)
    groups.reverse()
    return (left_spaces + thousands_sep.join(groups) + right_spaces, len(thousands_sep) * (len(groups) - 1))


def _strip_padding(s, amount):
    lpos = 0
# WARNING: Decompyle incomplete

_percent_re = re.compile('%(?:\\((?P<key>.*?)\\))?(?P<modifiers>[-#0-9 +*.hlL]*?)[eEfFgGdiouxXcrs%]')

def _format(percent, value, grouping, monetary = (False, False), *additional):
    if additional:
        formatted = percent % ((value,) + additional)
    else:
        formatted = percent % value
    if percent[-1] in 'eEfFgGdiu':
        formatted = _localize(formatted, grouping, monetary)
    return formatted


def _localize(formatted, grouping, monetary = (False, False)):
    if '.' in formatted:
        seps = 0
        parts = formatted.split('.')
        if grouping:
            (parts[0], seps) = _group(parts[0], monetary = monetary)
        if monetary:
            if not 'mon_decimal_point':
                decimal_point = localeconv()['decimal_point']
                formatted = decimal_point.join(parts)
                if seps:
                    formatted = _strip_padding(formatted, seps)
                else:
                    seps = 0
                    if grouping:
                        (formatted, seps) = _group(formatted, monetary = monetary)
                    if seps:
                        formatted = _strip_padding(formatted, seps)
    return formatted


def format_string(f, val, grouping, monetary = (False, False)):
    '''Formats a string in the same way that the % formatting would use,
    but takes the current locale into account.

    Grouping is applied if the third parameter is true.
    Conversion uses monetary thousands separator and grouping strings if
    forth parameter monetary is true.'''
    percents = list(_percent_re.finditer(f))
    new_f = _percent_re.sub('%s', f)
    if isinstance(val, _collections_abc.Mapping):
        new_val = []
        for perc in percents:
            if perc.group()[-1] == '%':
                new_val.append('%')
                continue
            new_val.append(_format(perc.group(), val, grouping, monetary))
    if not isinstance(val, tuple):
        val = (val,)
    new_val = []
    i = 0
# WARNING: Decompyle incomplete


def format(percent, value, grouping, monetary = (False, False), *additional):
    '''Deprecated, use format_string instead.'''
    import warnings
    warnings.warn("This method will be removed in a future version of Python. Use 'locale.format_string()' instead.", DeprecationWarning, stacklevel = 2)
    match = _percent_re.match(percent)
    if match or len(match.group()) != len(percent):
        raise ValueError('format() must be given exactly one %%char format specifier, %s not valid' % repr(percent))
# WARNING: Decompyle incomplete


def currency(val, symbol, grouping, international = (True, False, False)):
    '''Formats val according to the currency settings
    in the current locale.'''
    conv = localeconv()
    if international:
        if not 'int_frac_digits':
            digits = conv['frac_digits']
            if digits == 127:
                raise ValueError("Currency formatting is not possible using the 'C' locale.")
            s = _localize(f'''{abs(val):
