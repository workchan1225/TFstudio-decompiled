# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gettext.pyc (Python 3.11)

'''Internationalization and localization support.

This module provides internationalization (I18N) and localization (L10N)
support for your Python programs by providing an interface to the GNU gettext
message catalog library.

I18N refers to the operation by which a program is made aware of multiple
languages.  L10N refers to the adaptation of your program, once
internationalized, to the local language and cultural habits.

'''
import operator
import os
import re
import sys
__all__ = [
    'NullTranslations',
    'GNUTranslations',
    'Catalog',
    'bindtextdomain',
    'find',
    'translation',
    'install',
    'textdomain',
    'dgettext',
    'dngettext',
    'gettext',
    'ngettext',
    'pgettext',
    'dpgettext',
    'npgettext',
    'dnpgettext']
_default_localedir = os.path.join(sys.base_prefix, 'share', 'locale')
_token_pattern = re.compile('\n        (?P<WHITESPACES>[ \\t]+)                    | # spaces and horizontal tabs\n        (?P<NUMBER>[0-9]+\\b)                       | # decimal integer\n        (?P<NAME>n\\b)                              | # only n is allowed\n        (?P<PARENTHESIS>[()])                      |\n        (?P<OPERATOR>[-*/%+?:]|[><!]=?|==|&&|\\|\\|) | # !, *, /, %, +, -, <, >,\n                                                     # <=, >=, ==, !=, &&, ||,\n                                                     # ? :\n                                                     # unary and bitwise ops\n                                                     # not allowed\n        (?P<INVALID>\\w+|.)                           # invalid token\n    ', re.VERBOSE | re.DOTALL)

def _tokenize(plural):
    pass
# WARNING: Decompyle incomplete


def _error(value):
    if value:
        return ValueError('unexpected token in plural form: %s' % value)
    return None('unexpected end of plural form')

_binary_ops = (('||',), ('&&',), ('==', '!='), ('<', '>', '<=', '>='), ('+', '-'), ('*', '/', '%'))
_binary_ops = enumerate(_binary_ops, 1)()
_c2py_ops = {
    '||': 'or',
    '&&': 'and',
    '/': '//' }

def _parse(tokens, priority = (-1,)):
    result = ''
    nexttok = next(tokens)
# WARNING: Decompyle incomplete


def _as_int(n):
    
    try:
        round(n)
    except TypeError:
        raise TypeError(f'''Plural value must be an integer, got {n.__class__.__name__!s}'''), None

    import warnings
    frame = sys._getframe(1)
    stacklevel = 2
# WARNING: Decompyle incomplete


def c2py(plural):
    '''Gets a C expression as used in PO files for plural forms and returns a
    Python function that implements an equivalent expression.
    '''
    if len(plural) > 1000:
        raise ValueError('plural form expression is too long')
    
    try:
        (result, nexttok) = _parse(_tokenize(plural))
        if nexttok:
            raise _error(nexttok)
        depth = 0
        for c in result:
            if c == '(':
                depth += 1
                if depth > 20:
                    raise ValueError('plural form expression is too complex')
                continue
            if c == ')':
                depth -= 1
            ns = {
                '_as_int': _as_int,
                '__name__': __name__ }
            exec('if True:\n            def func(n):\n                if not isinstance(n, int):\n                    n = _as_int(n)\n                return int(%s)\n            ' % result, ns)
            return ns['func']
            except RecursionError:
                raise ValueError('plural form expression is too complex')



def _expand_lang(loc):
    import locale
    loc = locale.normalize(loc)
    COMPONENT_CODESET = 1
    COMPONENT_TERRITORY = 2
    COMPONENT_MODIFIER = 4
    mask = 0
    pos = loc.find('@')
    if pos >= 0:
        modifier = loc[pos:]
        loc = loc[:pos]
        mask |= COMPONENT_MODIFIER
    else:
        modifier = ''
    pos = loc.find('.')
    if pos >= 0:
        codeset = loc[pos:]
        loc = loc[:pos]
        mask |= COMPONENT_CODESET
    else:
        codeset = ''
    pos = loc.find('_')
    if pos >= 0:
        territory = loc[pos:]
        loc = loc[:pos]
        mask |= COMPONENT_TERRITORY
    else:
        territory = ''
    language = loc
    ret = []
    for i in range(mask + 1):
        if not i & ~mask:
            val = language
            if i & COMPONENT_TERRITORY:
                val += territory
            if i & COMPONENT_CODESET:
                val += codeset
            if i & COMPONENT_MODIFIER:
                val += modifier
            ret.append(val)
        ret.reverse()
        return ret


class NullTranslations:
    
    def __init__(self, fp = (None,)):
        self._info = { }
        self._charset = None
        self._fallback = None
    # WARNING: Decompyle incomplete

    
    def _parse(self, fp):
        pass

    
    def add_fallback(self, fallback):
        if self._fallback:
            self._fallback.add_fallback(fallback)
            return None
        self._fallback = None

    
    def gettext(self, message):
        if self._fallback:
            return self._fallback.gettext(message)

    
    def ngettext(self, msgid1, msgid2, n):
        if self._fallback:
            return self._fallback.ngettext(msgid1, msgid2, n)
        if None == 1:
            return msgid1

    
    def pgettext(self, context, message):
        if self._fallback:
            return self._fallback.pgettext(context, message)

    
    def npgettext(self, context, msgid1, msgid2, n):
        if self._fallback:
            return self._fallback.npgettext(context, msgid1, msgid2, n)
        if None == 1:
            return msgid1

    
    def info(self):
        return self._info

    
    def charset(self):
        return self._charset

    
    def install(self, names = (None,)):
        import builtins
        builtins.__dict__['_'] = self.gettext
    # WARNING: Decompyle incomplete



class GNUTranslations(NullTranslations):
    LE_MAGIC = 0x950412DE
    BE_MAGIC = 0xDE120495
    CONTEXT = '%s\x04%s'
    VERSIONS = (0, 1)
    
    def _get_versions(self, version):
        '''Returns a tuple of major version, minor version'''
        return (version >> 16, version & 65535)

    
    def _parse(self, fp):
        '''Override this method to support alternative .mo formats.'''
        unpack = unpack
        import struct
        filename = getattr(fp, 'name', '')
        self._catalog = { }
        catalog = { }
        
        self.plural = lambda n: int(n != 1)
        buf = fp.read()
        buflen = len(buf)
        magic = unpack('<I', buf[:4])[0]
        if magic == self.LE_MAGIC:
            (version, msgcount, masteridx, transidx) = unpack('<4I', buf[4:20])
            ii = '<II'
        elif magic == self.BE_MAGIC:
            (version, msgcount, masteridx, transidx) = unpack('>4I', buf[4:20])
            ii = '>II'
        else:
            raise OSError(0, 'Bad magic number', filename)
        (major_version, minor_version) = self._get_versions(version)
        if major_version not in self.VERSIONS:
            raise OSError(0, 'Bad version number ' + str(major_version), filename)
        for i in range(0, msgcount):
            (mlen, moff) = unpack(ii, buf[masteridx:masteridx + 8])
            mend = moff + mlen
            (tlen, toff) = unpack(ii, buf[transidx:transidx + 8])
            tend = toff + tlen
            if mend < buflen and tend < buflen:
                msg = buf[moff:mend]
                tmsg = buf[toff:tend]
            else:
                raise OSError(0, 'File is corrupt', filename)
            if mlen == 0:
                lastk = None
                for b_item in tmsg.split(b'\n'):
                    item = b_item.decode().strip()
                    if not item:
                        continue
                    if item.startswith('#-#-#-#-#') and item.endswith('#-#-#-#-#'):
                        continue
                    k = None
                    v = None
                    if ':' in item:
                        (k, v) = item.split(':', 1)
                        k = k.strip().lower()
                        v = v.strip()
                        self._info[k] = v
                        lastk = k
                    elif lastk:
                        pass
                    if k == 'content-type':
                        v.split('charset=')[1] = None
                        continue
                    if k == 'plural-forms':
                        v = v.split(';')
                        plural = v[1].split('plural=')[1]
                        self.plural = c2py(plural)
                    if not self._charset:
                        charset = 'ascii'
                        if b'\x00' in msg:
                            (msgid1, msgid2) = msg.split(b'\x00')
                            tmsg = tmsg.split(b'\x00')
                            msgid1 = str(msgid1, charset)
                            for i, x in enumerate(tmsg):
                                catalog[(msgid1, i)] = str(x, charset)
            catalog[str(msg, charset)] = str(tmsg, charset)
            masteridx += 8
            transidx += 8
            return None

    
    def gettext(self, message):
        missing = object()
        tmsg = self._catalog.get(message, missing)
        if tmsg is missing:
            tmsg = self._catalog.get((message, self.plural(1)), missing)
        if tmsg is not missing:
            return tmsg
        if None._fallback:
            return self._fallback.gettext(message)

    
    def ngettext(self, msgid1, msgid2, n):
        
        try:
            tmsg = self._catalog[(msgid1, self.plural(n))]
        except KeyError:
            if self._fallback:
                return 
            if None == 1:
                pass
            else:
                msgid2 = msgid1

        return tmsg

    
    def pgettext(self, context, message):
        ctxt_msg_id = self.CONTEXT % (context, message)
        missing = object()
        tmsg = self._catalog.get(ctxt_msg_id, missing)
        if tmsg is missing:
            tmsg = self._catalog.get((ctxt_msg_id, self.plural(1)), missing)
        if tmsg is not missing:
            return tmsg
        if None._fallback:
            return self._fallback.pgettext(context, message)

    
    def npgettext(self, context, msgid1, msgid2, n):
        ctxt_msg_id = self.CONTEXT % (context, msgid1)
        
        try:
            tmsg = self._catalog[(ctxt_msg_id, self.plural(n))]
        except KeyError:
            if self._fallback:
                return 
            if None == 1:
                pass
            else:
                msgid2 = msgid1

        return tmsg



def find(domain, localedir, languages, all = (None, None, False)):
    pass
# WARNING: Decompyle incomplete

_translations = { }

def translation(domain, localedir, languages, class_, fallback = (None, None, None, False)):
    pass
# WARNING: Decompyle incomplete


def install(domain = None, localedir = (None,), *, names):
    t = translation(domain, localedir, fallback = True)
    t.install(names)

_localedirs = { }
_current_domain = 'messages'

def textdomain(domain = (None,)):
    pass
# WARNING: Decompyle incomplete


def bindtextdomain(domain, localedir = (None,)):
    pass
# WARNING: Decompyle incomplete


def dgettext(domain, message):
    
    try:
        t = translation(domain, _localedirs.get(domain, None))
    except OSError:
        return 

    return t.gettext(message)


def dngettext(domain, msgid1, msgid2, n):
    
    try:
        t = translation(domain, _localedirs.get(domain, None))
    except OSError:
        if n == 1:
            return 
        return 

    return t.ngettext(msgid1, msgid2, n)


def dpgettext(domain, context, message):
    
    try:
        t = translation(domain, _localedirs.get(domain, None))
    except OSError:
        return 

    return t.pgettext(context, message)


def dnpgettext(domain, context, msgid1, msgid2, n):
    
    try:
        t = translation(domain, _localedirs.get(domain, None))
    except OSError:
        if n == 1:
            return 
        return 

    return t.npgettext(context, msgid1, msgid2, n)


def gettext(message):
    return dgettext(_current_domain, message)


def ngettext(msgid1, msgid2, n):
    return dngettext(_current_domain, msgid1, msgid2, n)


def pgettext(context, message):
    return dpgettext(_current_domain, context, message)


def npgettext(context, msgid1, msgid2, n):
    return dnpgettext(_current_domain, context, msgid1, msgid2, n)

Catalog = translation
