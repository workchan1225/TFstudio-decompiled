# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

'''
    pygments.util
    ~~~~~~~~~~~~~

    Utility functions.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from io import TextIOWrapper
split_path_re = re.compile('[/\\\\ ]')
doctype_lookup_re = re.compile('\n    <!DOCTYPE\\s+(\n     [a-zA-Z_][a-zA-Z0-9]*\n     (?: \\s+      # optional in HTML5\n     [a-zA-Z_][a-zA-Z0-9]*\\s+\n     "[^"]*")?\n     )\n     [^>]*>\n', re.DOTALL | re.MULTILINE | re.VERBOSE)
tag_re = re.compile('<(.+?)(\\s.*?)?>.*?</.+?>', re.IGNORECASE | re.DOTALL | re.MULTILINE)
xml_decl_re = re.compile('\\s*<\\?xml[^>]*\\?>', re.I)

class ClassNotFound(ValueError):
    """Raised if one of the lookup functions didn't find a matching class."""
    pass


class OptionError(Exception):
    '''
    This exception will be raised by all option processing functions if
    the type or value of the argument is not correct.
    '''
    pass


def get_choice_opt(options, optname, allowed, default, normcase = (None, False)):
    '''
    If the key `optname` from the dictionary is not in the sequence
    `allowed`, raise an error, otherwise return it.
    '''
    string = options.get(optname, default)
    if normcase:
        string = string.lower()
    if string not in allowed:
        raise OptionError('Value for option {} must be one of {}'.format(optname, ', '.join(map(str, allowed))))
    return string


def get_bool_opt(options, optname, default = (None,)):
    '''
    Intuitively, this is `options.get(optname, default)`, but restricted to
    Boolean value. The Booleans can be represented as string, in order to accept
    Boolean value from the command line arguments. If the key `optname` is
    present in the dictionary `options` and is not associated with a Boolean,
    raise an `OptionError`. If it is absent, `default` is returned instead.

    The valid string values for ``True`` are ``1``, ``yes``, ``true`` and
    ``on``, the ones for ``False`` are ``0``, ``no``, ``false`` and ``off``
    (matched case-insensitively).
    '''
    string = options.get(optname, default)
    if isinstance(string, bool):
        return string
    if None(string, int):
        return bool(string)
    if not None(string, str):
        raise OptionError(f'''Invalid type {string!r} for option {optname}; use 1/0, yes/no, true/false, on/off''')
    if string.lower() in ('1', 'yes', 'true', 'on'):
        return True
    if None.lower() in ('0', 'no', 'false', 'off'):
        return False
    raise None(f'''Invalid value {string!r} for option {optname}; use 1/0, yes/no, true/false, on/off''')


def get_int_opt(options, optname, default = (None,)):
    '''As :func:`get_bool_opt`, but interpret the value as an integer.'''
    string = options.get(optname, default)
    
    try:
        return int(string)
    except TypeError:
        raise OptionError(f'''Invalid type {string!r} for option {optname}; you must give an integer value''')
        except ValueError:
            raise OptionError(f'''Invalid value {string!r} for option {optname}; you must give an integer value''')



def get_list_opt(options, optname, default = (None,)):
    '''
    If the key `optname` from the dictionary `options` is a string,
    split it at whitespace and return it. If it is already a list
    or a tuple, it is returned as a list.
    '''
    val = options.get(optname, default)
    if isinstance(val, str):
        return val.split()
    if None(val, (list, tuple)):
        return list(val)
    raise None(f'''Invalid type {val!r} for option {optname}; you must give a list value''')


def docstring_headline(obj):
    if not obj.__doc__:
        return ''
    res = None
    for line in obj.__doc__.strip().splitlines():
        if line.strip():
            res.append(' ' + line.strip())
            continue
        return ''.join(res).lstrip()


def make_analysator(f):
    '''Return a static text analyser function that returns float values.'''
    pass
# WARNING: Decompyle incomplete


def shebang_matches(text, regex):
    """Check if the given regular expression matches the last part of the
    shebang if one exists.

        >>> from pygments.util import shebang_matches
        >>> shebang_matches('#!/usr/bin/env python', r'python(2\\.\\d)?')
        True
        >>> shebang_matches('#!/usr/bin/python2.4', r'python(2\\.\\d)?')
        True
        >>> shebang_matches('#!/usr/bin/python-ruby', r'python(2\\.\\d)?')
        False
        >>> shebang_matches('#!/usr/bin/python/ruby', r'python(2\\.\\d)?')
        False
        >>> shebang_matches('#!/usr/bin/startsomethingwith python',
        ...                 r'python(2\\.\\d)?')
        True

    It also checks for common windows executable file extensions::

        >>> shebang_matches('#!C:\\\\Python2.4\\\\Python.exe', r'python(2\\.\\d)?')
        True

    Parameters (``'-f'`` or ``'--foo'`` are ignored so ``'perl'`` does
    the same as ``'perl -e'``)

    Note that this method automatically searches the whole string (eg:
    the regular expression is wrapped in ``'^$'``)
    """
    index = text.find('\n')
    if index >= 0:
        first_line = text[:index].lower()
    else:
        first_line = text.lower()
# WARNING: Decompyle incomplete


def doctype_matches(text, regex):
    '''Check if the doctype matches a regular expression (if present).

    Note that this method only checks the first part of a DOCTYPE.
    eg: \'html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\'
    '''
    m = doctype_lookup_re.search(text)
# WARNING: Decompyle incomplete


def html_doctype_matches(text):
    '''Check if the file looks like it has a html doctype.'''
    return doctype_matches(text, 'html')

_looks_like_xml_cache = { }

def looks_like_xml(text):
    '''Check if a doctype exists or if we have some tags.'''
    if xml_decl_re.match(text):
        return True
    key = None(text)
# WARNING: Decompyle incomplete


def surrogatepair(c):
    '''Given a unicode character code with length greater than 16 bits,
    return the two 16 bit surrogate pair.
    '''
    return (55232 + (c >> 10), 56320 + (c & 1023))


def format_lines(var_name, seq, raw, indent_level = (False, 0)):
    '''Formats a sequence of strings for output.'''
    lines = []
    base_indent = ' ' * indent_level * 4
    inner_indent = ' ' * (indent_level + 1) * 4
    lines.append(base_indent + var_name + ' = (')
    if raw:
        for i in seq:
            lines.append(inner_indent + i + ',')
    for i in seq:
        r = repr(i + '"')
        lines.append(inner_indent + r[:-2] + r[-1] + ',')
        lines.append(base_indent + ')')
        return '\n'.join(lines)


def duplicates_removed(it, already_seen = ((),)):
    '''
    Returns a list with duplicates removed from the iterable `it`.

    Order is preserved.
    '''
    lst = []
    seen = set()
    for i in it:
        if i in seen or i in already_seen:
            continue
        lst.append(i)
        seen.add(i)
        return lst


class Future:
    '''Generic class to defer some work.

    Handled specially in RegexLexerMeta, to support regex string construction at
    first use.
    '''
    
    def get(self):
        raise NotImplementedError



def guess_decode(text):
    '''Decode *text* with guessed encoding.

    First try UTF-8; this should fail for non-UTF-8 encodings.
    Then try the preferred locale encoding.
    Fall back to latin-1, which always works.
    '''
    
    try:
        text = text.decode('utf-8')
        return (text, 'utf-8')
    except UnicodeDecodeError:
        import locale
        prefencoding = locale.getpreferredencoding()
        text = text.decode()
        return 
        except (UnicodeDecodeError, LookupError):
            return 



def guess_decode_from_terminal(text, term):
