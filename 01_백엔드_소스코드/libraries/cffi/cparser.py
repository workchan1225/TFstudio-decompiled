# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cparser.pyc (Python 3.11)

from  import model
from commontypes import COMMON_TYPES, resolve_common_type
from error import FFIError, CDefError

try:
    from  import _pycparser as pycparser
except ImportError:
    import pycparser

import weakref
import re
import sys

try:
    if sys.version_info < (3,):
        import thread as _thread
    else:
        import _thread
    lock = _thread.allocate_lock()
except ImportError:
    lock = None


def _workaround_for_static_import_finders():
    import pycparser.yacctab as pycparser
    import pycparser.lextab as pycparser

CDEF_SOURCE_STRING = '<cdef source string>'
_r_comment = re.compile('/\\*.*?\\*/|//([^\\n\\\\]|\\\\.)*?$', re.DOTALL | re.MULTILINE)
_r_define = re.compile('^\\s*#\\s*define\\s+([A-Za-z_][A-Za-z_0-9]*)\\b((?:[^\\n\\\\]|\\\\.)*?)$', re.DOTALL | re.MULTILINE)
_r_line_directive = re.compile('^[ \\t]*#[ \\t]*(?:line|\\d+)\\b.*$', re.MULTILINE)
_r_partial_enum = re.compile('=\\s*\\.\\.\\.\\s*[,}]|\\.\\.\\.\\s*\\}')
_r_enum_dotdotdot = re.compile('__dotdotdot\\d+__$')
_r_partial_array = re.compile('\\[\\s*\\.\\.\\.\\s*\\]')
_r_words = re.compile('\\w+|\\S')
_parser_cache = None
_r_int_literal = re.compile('-?0?x?[0-9a-f]+[lu]*$', re.IGNORECASE)
_r_stdcall1 = re.compile('\\b(__stdcall|WINAPI)\\b')
_r_stdcall2 = re.compile('[(]\\s*(__stdcall|WINAPI)\\b')
_r_cdecl = re.compile('\\b__cdecl\\b')
_r_extern_python = re.compile('\\bextern\\s*"(Python|Python\\s*\\+\\s*C|C\\s*\\+\\s*Python)"\\s*.')
_r_star_const_space = re.compile('[*]\\s*((const|volatile|restrict)\\b\\s*)+')
_r_int_dotdotdot = re.compile('(\\b(int|long|short|signed|unsigned|char)\\s*)+\\.\\.\\.')
_r_float_dotdotdot = re.compile('\\b(double|float)\\s*\\.\\.\\.')

def _get_parser():
    pass
# WARNING: Decompyle incomplete


def _workaround_for_old_pycparser(csource):
    parts = []
    match = _r_star_const_space.search(csource)
    if not match:
        pass
# WARNING: Decompyle incomplete


def _preprocess_extern_python(csource):
    parts = []
    match = _r_extern_python.search(csource)
    if not match:
        pass
    else:
        endpos = match.end() - 1
        None(parts.append[csource:match.start()])
        if 'C' in match.group(1):
            parts.append('void __cffi_extern_python_plus_c_start; ')
        else:
            parts.append('void __cffi_extern_python_start; ')
        if csource[endpos] == '{':
            closing = csource.find('}', endpos)
            if closing < 0:
                raise CDefError('\'extern "Python" {\': no \'}\' found')
            if csource.find('{', endpos + 1, closing) >= 0:
                raise NotImplementedError('cannot use { } inside a block \'extern "Python" { ... }\'')
            parts.append(csource[endpos + 1:closing])
            csource = csource[closing + 1:]
        else:
            semicolon = csource.find(';', endpos)
            if semicolon < 0:
                raise CDefError('\'extern "Python": no \';\' found')
            parts.append(csource[endpos:semicolon + 1])
            csource = csource[semicolon + 1:]
        parts.append(' void __cffi_extern_python_stop;')
    parts.append(csource)
    return ''.join(parts)


def _warn_for_string_literal(csource):
    if '"' not in csource:
        return None
    for line in None.splitlines():
        if not '"' in line and line.lstrip().startswith('#'):
            import warnings
            warnings.warn('String literal found in cdef() or type source. String literals are ignored here, but you should remove them anyway because some character sequences confuse pre-parsing.')
            return None
        return None


def _warn_for_non_extern_non_static_global_variable(decl):
    if not decl.storage:
        import warnings
        warnings.warn(f'''Global variable \'{decl.name!s}\' in cdef(): for consistency with C it should have a storage class specifier (usually \'extern\')''')
        return None


def _remove_line_directives(csource):
    pass
# WARNING: Decompyle incomplete


def _put_back_line_directives(csource, line_directives):
    pass
# WARNING: Decompyle incomplete


def _preprocess(csource):
    (csource, line_directives) = _remove_line_directives(csource)
    
    def replace_keeping_newlines(m):
        return ' ' + m.group().count('\n') * '\n'

    csource = _r_comment.sub(replace_keeping_newlines, csource)
    macros = { }
    for match in _r_define.finditer(csource):
        (macroname, macrovalue) = match.groups()
        macrovalue = macrovalue.replace('\\\n', '').strip()
        macros[macroname] = macrovalue
        csource = _r_define.sub('', csource)
        if pycparser.__version__ < '2.14':
            csource = _workaround_for_old_pycparser(csource)
    csource = _r_stdcall2.sub(' volatile volatile const(', csource)
    csource = _r_stdcall1.sub(' volatile volatile const ', csource)
    csource = _r_cdecl.sub(' ', csource)
    csource = _preprocess_extern_python(csource)
    _warn_for_string_literal(csource)
    csource = _r_partial_array.sub('[__dotdotdotarray__]', csource)
    matches = list(_r_partial_enum.finditer(csource))
# WARNING: Decompyle incomplete


def _common_type_names(csource):
    look_for_words = set(COMMON_TYPES)
    look_for_words.add(';')
    look_for_words.add(',')
    look_for_words.add('(')
    look_for_words.add(')')
    look_for_words.add('typedef')
    words_used = set()
    is_typedef = False
    paren = 0
    previous_word = ''
    for word in _r_words.findall(csource):
        if word in look_for_words:
            if word == ';':
                if is_typedef:
                    words_used.discard(previous_word)
                    look_for_words.discard(previous_word)
                    is_typedef = False
                elif word == 'typedef':
                    is_typedef = True
                    paren = 0
                elif word == '(':
                    paren += 1
                elif word == ')':
                    paren -= 1
                elif word == ',':
                    if is_typedef and paren == 0:
                        words_used.discard(previous_word)
                        look_for_words.discard(previous_word)
                    else:
                        words_used.add(word)
        previous_word = word
        return words_used


class Parser(object):
    
    def __init__(self):
        self._declarations = { }
        self._included_declarations = set()
        self._anonymous_counter = 0
        self._structnode2type = weakref.WeakKeyDictionary()
        self._options = { }
        self._int_constants = { }
        self._recomplete = []
        self._uses_new_feature = None

    
    def _parse(self, csource):
        (csource, macros) = _preprocess(csource)
        ctn = _common_type_names(csource)
        typenames = []
    # WARNING: Decompyle incomplete

    
    def _convert_pycparser_error(self, e, csource):
        line = None
        msg = str(e)
        match = re.match(f'''{CDEF_SOURCE_STRING!s}:(\\d+):''', msg)
        return line

    
    def convert_pycparser_error(self, e, csource):
        line = self._convert_pycparser_error(e, csource)
        msg = str(e)
        if line:
            msg = f'''cannot parse "{line.strip()!s}"\n{msg!s}'''
        else:
            msg = f'''parse error\n{msg!s}'''
        raise CDefError(msg)

    
    def parse(self, csource, override, packed, pack, dllexport = (False, False, None, False)):
        if packed:
            if packed != True:
                raise ValueError("'packed' should be False or True; use 'pack' to give another value")
            if pack:
                raise ValueError("cannot give both 'pack' and 'packed'")
            pack = 1
        elif pack:
            if pack & pack - 1:
                raise ValueError(f'''\'pack\' must be a power of two, not {pack!r}''')
        else:
            pack = 0
        prev_options = self._options
        
        try:
            self._options = {
                'override': override,
                'packed': pack,
                'dllexport': dllexport }
            self._internal_parse(csource)
            self._options = prev_options
            return None
        except:
            self._options = prev_options


    
    def _internal_parse(self, csource):
        (ast, macros, csource) = self._parse(csource)
        self._process_macros(macros)
        iterator = iter(ast.ext)
    # WARNING: Decompyle incomplete

    
    def _add_constants(self, key, val):
        if key in self._int_constants:
            if self._int_constants[key] == val:
                return None
            raise None(f'''multiple declarations of constant: {key!s}''')
        self._int_constants[key] = val

    
    def _add_integer_constant(self, name, int_str):
        int_str = int_str.lower().rstrip('ul')
        neg = int_str.startswith('-')
        if neg:
            int_str = int_str[1:]
        if not int_str.startswith('0') and int_str != '0' and int_str.startswith('0x'):
            int_str = '0o' + int_str[1:]
        pyvalue = int(int_str, 0)
        if neg:
            pyvalue = -pyvalue
        self._add_constants(name, pyvalue)
        self._declare('macro ' + name, pyvalue)

    
    def _process_macros(self, macros):
        for key, value in macros.items():
            value = value.strip()
            if _r_int_literal.match(value):
                self._add_integer_constant(key, value)
                continue
            if value == '...':
                self._declare('macro ' + key, value)
                continue
            raise CDefError(f'''only supports one of the following syntax:\n  #define {key!s} ...     (literally dot-dot-dot)\n  #define {key!s} NUMBER  (with NUMBER an integer constant, decimal/hex/octal)\ngot:\n  #define {key!s} {value!s}''')
            return None

    
    def _declare_function(self, tp, quals, decl):
        tp = self._get_type_pointer(tp, quals)
        if self._options.get('dllexport'):
            tag = 'dllexport_python '
        elif self._inside_extern_python == '__cffi_extern_python_start':
            tag = 'extern_python '
        elif self._inside_extern_python == '__cffi_extern_python_plus_c_start':
            tag = 'extern_python_plus_c '
        else:
            tag = 'function '
        self._declare(tag + decl.name, tp)

    
    def _parse_decl(self, decl):
        node = decl.type
    # WARNING: Decompyle incomplete

    
    def parse_type(self, cdecl):
        return self.parse_type_and_quals(cdecl)[0]

    
    def parse_type_and_quals(self, cdecl):
        (ast, macros) = self._parse('void __dummy(\n%s\n);' % cdecl)[:2]
    # WARNING: Decompyle incomplete

    
    def _declare(self, name, obj, included, quals = (False, 0)):
        if name in self._declarations:
            (prevobj, prevquals) = self._declarations[name]
            if prevobj is obj and prevquals == quals:
                return None
            if not None._options.get('override'):
                raise FFIError(f'''multiple declarations of {name!s} (for interactive usage, try cdef(xx, override=True))''')
    # WARNING: Decompyle incomplete

    
    def _extract_quals(self, type):
        quals = 0
        if isinstance(type, (pycparser.c_ast.TypeDecl, pycparser.c_ast.PtrDecl)):
            if 'const' in type.quals:
                quals |= model.Q_CONST
            if 'volatile' in type.quals:
                quals |= model.Q_VOLATILE
            if 'restrict' in type.quals:
                quals |= model.Q_RESTRICT
        return quals

    
    def _get_type_pointer(self, type, quals, declname = (None,)):
        if isinstance(type, model.RawFunctionType):
            return type.as_function_pointer()
    # WARNING: Decompyle incomplete

    
    def _get_type_and_quals(self, typenode, name, partial_length_ok, typedef_example = (None, False, None)):
        if isinstance(typenode, pycparser.c_ast.TypeDecl) and isinstance(typenode.type, pycparser.c_ast.IdentifierType) and len(typenode.type.names) == 1 and 'typedef ' + typenode.type.names[0] in self._declarations:
            (tp, quals) = self._declarations['typedef ' + typenode.type.names[0]]
            quals |= self._extract_quals(typenode)
            return (tp, quals)
    # WARNING: Decompyle incomplete

    
    def _parse_function_type(self, typenode, funcname = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _as_func_arg(self, type, quals):
        if isinstance(type, model.ArrayType):
            return model.PointerType(type.item, quals)
        if None(type, model.RawFunctionType):
            return type.as_function_pointer()

    
    def _get_struct_union_enum_type(self, kind, type, name, nested = (None, False)):
        
        try:
            return self._structnode2type[type]
        except KeyError:
            pass

        force_name = name
        name = type.name
    # WARNING: Decompyle incomplete

    
    def _make_partial(self, tp, nested):
        if not isinstance(tp, model.StructOrUnion):
            raise CDefError(f'''{tp!s} cannot be partial''')
        if not tp.has_c_name() and nested:
            raise NotImplementedError(f'''{tp!s} is partial but has no C name''')
        tp.partial = True

    
    def _parse_constant(self, exprnode, partial_length_ok = (False,)):
        if isinstance(exprnode, pycparser.c_ast.Constant):
            s = exprnode.value
            if  <= '0', s[0] or '0', s[0] <= '9':
                pass
            
        else:
            
            try:
                if s.startswith('0'):
                    return int(s, 8)
                return s.rstrip('uUlL')(s, 10)
            except ValueError:
                raise CDefError(f'''invalid constant {s!r}''')
                if s[0] == "'" and s[-1] == "'":
                    if (len(s) == 3 or len(s) == 4) and s[1] == '\\':
                        return ord(s[-2])
                    raise None if len(s) > 1 else None(f'''invalid constant {s!r}''')
                if isinstance(exprnode, pycparser.c_ast.UnaryOp) and exprnode.op == '+':
                    return self._parse_constant(exprnode.expr)
                if None if len(s) > 1 else None(exprnode, pycparser.c_ast.UnaryOp) and exprnode.op == '-':
                    return -self._parse_constant(exprnode.expr)
                if None(exprnode, pycparser.c_ast.ID) and exprnode.name in self._int_constants:
                    return self._int_constants[exprnode.name]
                if None(exprnode, pycparser.c_ast.ID) and exprnode.name == '__dotdotdotarray__':
                    if partial_length_ok:
                        return '...'
                    raise None(":%d: unsupported '[...]' here, cannot derive the actual array length in this context" % exprnode.coord.line)
                if isinstance(exprnode, pycparser.c_ast.BinaryOp):
                    self._parse_constant(exprnode.left) = None
                    right = self._parse_constant(exprnode.right)
                    if exprnode.op == '+':
                        return left + right
                    if None.op == '-':
                        return left - right
                    if None.op == '*':
                        return left * right
                    if None.op == '/':
                        return self._c_div(left, right)
                    if None.op == '%':
                        return left - self._c_div(left, right) * right
                    if None.op == '<<':
                        return left << right
                    if None.op == '>>':
                        return left >> right
                    if None.op == '&':
                        return left & right
                    if None.op == '|':
                        return left | right
                    if None.op == '^':
                        return left ^ right
                    raise None(':%d: unsupported expression: expected a simple numeric constant' % exprnode.coord.line)


    
    def _c_div(self, a, b):
        result = a // b
        if (a < 0) ^ (b < 0) and a % b != 0:
            result += 1
        return result

    
    def _build_enum_type(self, explicit_name, decls):
        pass
    # WARNING: Decompyle incomplete

    
    def include(self, other):
        for tp, quals in other._declarations.items():
            if name.startswith('anonymous $enum_$'):
                continue
            kind = name.split(' ', 1)[0]
            if kind in ('struct', 'union', 'enum', 'anonymous', 'typedef'):
                self._declare(name, tp, included = True, quals = quals)
            for k, v in other._int_constants.items():
                self._add_constants(k, v)
                return None

    
    def _get_unknown_type(self, decl):
        typenames = decl.type.type.names
        if typenames == [
            '__dotdotdot__']:
            return model.unknown_type(decl.name)
    # WARNING: Decompyle incomplete

    
    def _get_unknown_ptr_type(self, decl):
        if decl.type.type.type.names == [
            '__dotdotdot__']:
            return model.unknown_ptr_type(decl.name)
        raise None(':%d: unsupported usage of "..." in typedef' % decl.coord.line)
