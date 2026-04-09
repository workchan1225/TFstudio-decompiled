# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vengine_gen.pyc (Python 3.11)

import sys
import os
import types
from  import model
from error import VerificationError

class VGenericEngine(object):
    _class_key = 'g'
    _gen_python_module = False
    
    def __init__(self, verifier):
        self.verifier = verifier
        self.ffi = verifier.ffi
        self.export_symbols = []
        self._struct_pending_verification = { }

    
    def patch_extension_kwds(self, kwds):
        kwds.setdefault('export_symbols', self.export_symbols)

    
    def find_module(self, module_name, path, so_suffixes):
        pass
    # WARNING: Decompyle incomplete

    
    def collect_types(self):
        pass

    
    def _prnt(self, what = ('',)):
        self._f.write(what + '\n')

    
    def write_source_to_f(self):
        prnt = self._prnt
        prnt(cffimod_header)
        prnt(self.verifier.preamble)
        self._generate('decl')
        if sys.platform == 'win32':
            if sys.version_info >= (3,):
                prefix = 'PyInit_'
            else:
                prefix = 'init'
            modname = self.verifier.get_module_name()
            prnt(f'''void {prefix!s}{modname!s}(void) {{ }}\n''')
            return None

    
    def load_library(self, flags = (0,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_declarations(self):
        lst = self.ffi._parser._declarations.items()()
        lst.sort()
        return lst

    
    def _generate(self, step_name):
        for name, tp in self._get_declarations():
            (kind, realname) = name.split(' ', 1)
            method = getattr(self, f'''_generate_gen_{kind!s}_{step_name!s}''')
        except AttributeError:
            raise VerificationError('not implemented in verify(): %r' % name)
        method(tp, realname)
        continue
        except Exception:
            e = None
            model.attach_exception_info(e, name)
            raise 
            e = None
            del e

    
    def _load(self, module, step_name, **kwds):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_nothing(self, tp, name):
        pass

    
    def _loaded_noop(self, tp, name, module, **kwds):
        pass

    _generate_gen_typedef_decl = _generate_nothing
    _loading_gen_typedef = _loaded_noop
    _loaded_gen_typedef = _loaded_noop
    
    def _generate_gen_function_decl(self, tp, name):
        pass
    # WARNING: Decompyle incomplete

    _loading_gen_function = _loaded_noop
    
    def _loaded_gen_function(self, tp, name, module, library):
        pass
    # WARNING: Decompyle incomplete

    
    def _make_struct_wrapper(self, oldfunc, i, tp, base_tp):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_gen_struct_decl(self, tp, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _loading_gen_struct(self, tp, name, module):
        self._loading_struct_or_union(tp, 'struct', name, module)

    
    def _loaded_gen_struct(self, tp, name, module, **kwds):
        self._loaded_struct_or_union(tp)

    
    def _generate_gen_union_decl(self, tp, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _loading_gen_union(self, tp, name, module):
        self._loading_struct_or_union(tp, 'union', name, module)

    
    def _loaded_gen_union(self, tp, name, module, **kwds):
        self._loaded_struct_or_union(tp)

    
    def _generate_struct_or_union_decl(self, tp, prefix, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _loading_struct_or_union(self, tp, prefix, name, module):
        pass
    # WARNING: Decompyle incomplete

    
    def _loaded_struct_or_union(self, tp):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_gen_anonymous_decl(self, tp, name):
        if isinstance(tp, model.EnumType):
            self._generate_gen_enum_decl(tp, name, '')
            return None
        None._generate_struct_or_union_decl(tp, '', name)

    
    def _loading_gen_anonymous(self, tp, name, module):
        if isinstance(tp, model.EnumType):
            self._loading_gen_enum(tp, name, module, '')
            return None
        None._loading_struct_or_union(tp, '', name, module)

    
    def _loaded_gen_anonymous(self, tp, name, module, **kwds):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_gen_const(self, is_int, name, tp, category, check_value = (None, 'const', None)):
        prnt = self._prnt
        funcname = f'''_cffi_{category!s}_{name!s}'''
        self.export_symbols.append(funcname)
    # WARNING: Decompyle incomplete

    
    def _generate_gen_constant_decl(self, tp, name):
