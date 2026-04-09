# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vengine_cpy.pyc (Python 3.11)

import sys
from  import model
from error import VerificationError
from  import _imp_emulation as imp

class VCPythonEngine(object):
    _class_key = 'x'
    _gen_python_module = True
    
    def __init__(self, verifier):
        self.verifier = verifier
        self.ffi = verifier.ffi
        self._struct_pending_verification = { }
        self._types_of_builtin_functions = { }

    
    def patch_extension_kwds(self, kwds):
        pass

    
    def find_module(self, module_name, path, so_suffixes):
        
        try:
            (f, filename, descr) = imp.find_module(module_name, path)
        except ImportError:
            return None

    # WARNING: Decompyle incomplete

    
    def collect_types(self):
        self._typesdict = { }
        self._generate('collecttype')

    
    def _prnt(self, what = ('',)):
        self._f.write(what + '\n')

    
    def _gettypenum(self, type):
        return self._typesdict[type]

    
    def _do_collect_type(self, tp):
        if isinstance(tp, model.PrimitiveType) or tp.name == 'long double':
            if tp not in self._typesdict:
                num = len(self._typesdict)
                self._typesdict[tp] = num
                return None
            return None

    
    def write_source_to_f(self):
        self.collect_types()
        self._chained_list_constants = [
            '((void)lib,0)',
            '((void)lib,0)']
        prnt = self._prnt
        prnt(cffimod_header)
        prnt()
        prnt(self.verifier.preamble)
        prnt()
        self._generate('decl')
        self._generate_setup_custom()
        prnt()
        prnt('static PyMethodDef _cffi_methods[] = {')
        self._generate('method')
        prnt('  {"_cffi_setup", _cffi_setup, METH_VARARGS, NULL},')
        prnt('  {NULL, NULL, 0, NULL}    /* Sentinel */')
        prnt('};')
        prnt()
        modname = self.verifier.get_module_name()
        constants = self._chained_list_constants[False]
        prnt('#if PY_MAJOR_VERSION >= 3')
        prnt()
        prnt('static struct PyModuleDef _cffi_module_def = {')
        prnt('  PyModuleDef_HEAD_INIT,')
        prnt('  "%s",' % modname)
        prnt('  NULL,')
        prnt('  -1,')
        prnt('  _cffi_methods,')
        prnt('  NULL, NULL, NULL, NULL')
        prnt('};')
        prnt()
        prnt('PyMODINIT_FUNC')
        prnt('PyInit_%s(void)' % modname)
        prnt('{')
        prnt('  PyObject *lib;')
        prnt('  lib = PyModule_Create(&_cffi_module_def);')
        prnt('  if (lib == NULL)')
        prnt('    return NULL;')
        prnt(f'''  if ({constants!s} < 0 || _cffi_init() < 0) {{''')
        prnt('    Py_DECREF(lib);')
        prnt('    return NULL;')
        prnt('  }')
        prnt('#if Py_GIL_DISABLED')
        prnt('  PyUnstable_Module_SetGIL(lib, Py_MOD_GIL_NOT_USED);')
        prnt('#endif')
        prnt('  return lib;')
        prnt('}')
        prnt()
        prnt('#else')
        prnt()
        prnt('PyMODINIT_FUNC')
        prnt('init%s(void)' % modname)
        prnt('{')
        prnt('  PyObject *lib;')
        prnt('  lib = Py_InitModule("%s", _cffi_methods);' % modname)
        prnt('  if (lib == NULL)')
        prnt('    return;')
        prnt(f'''  if ({constants!s} < 0 || _cffi_init() < 0)''')
        prnt('    return;')
        prnt('  return;')
        prnt('}')
        prnt()
        prnt('#endif')

    
    def load_library(self, flags = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_declarations(self):
        lst = self.ffi._parser._declarations.items()()
        lst.sort()
        return lst

    
    def _generate(self, step_name):
        for name, tp in self._get_declarations():
            (kind, realname) = name.split(' ', 1)
            method = getattr(self, f'''_generate_cpy_{kind!s}_{step_name!s}''')
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

    
    def _convert_funcarg_to_c(self, tp, fromvar, tovar, errcode):
        extraarg = ''
        if isinstance(tp, model.PrimitiveType):
            if tp.is_integer_type() and tp.name != '_Bool':
                converter = '_cffi_to_c_int'
                extraarg = ', %s' % tp.name
            elif tp.is_complex_type():
                raise VerificationError('not implemented in verify(): complex types')
            converter = f'''({tp.get_c_name('')!s})_cffi_to_c_{tp.name.replace(' ', '_')!s}'''
            errvalue = '-1'
        elif isinstance(tp, model.PointerType):
            self._convert_funcarg_to_c_ptr_or_array(tp, fromvar, tovar, errcode)
            return None
        if isinstance(tp, (model.StructOrUnion, model.EnumType)):
            self._prnt('  if (_cffi_to_c((char *)&%s, _cffi_type(%d), %s) < 0)' % (tovar, self._gettypenum(tp), fromvar))
            self._prnt('    %s;' % errcode)
            return None
        if None(tp, model.FunctionPtrType):
            converter = '(%s)_cffi_to_c_pointer' % tp.get_c_name('')
            extraarg = ', _cffi_type(%d)' % self._gettypenum(tp)
            errvalue = 'NULL'
        else:
            raise NotImplementedError(tp)
        self._prnt(f'''  {tovar!s} = {converter!s}({fromvar!s}{extraarg!s});''')
        self._prnt(f'''  if ({tovar!s} == ({tp.get_c_name('')!s}){errvalue!s} && PyErr_Occurred())''')
        self._prnt('    %s;' % errcode)

    
    def _extra_local_variables(self, tp, localvars, freelines):
        if isinstance(tp, model.PointerType):
            localvars.add('Py_ssize_t datasize')
            localvars.add('struct _cffi_freeme_s *large_args_free = NULL')
            freelines.add('if (large_args_free != NULL) _cffi_free_array_arguments(large_args_free);')
            return None

    
    def _convert_funcarg_to_c_ptr_or_array(self, tp, fromvar, tovar, errcode):
        self._prnt('  datasize = _cffi_prepare_pointer_call_argument(')
        self._prnt('      _cffi_type(%d), %s, (char **)&%s);' % (self._gettypenum(tp), fromvar, tovar))
        self._prnt('  if (datasize != 0) {')
        self._prnt(f'''    {tovar!s} = ((size_t)datasize) <= 640 ? alloca((size_t)datasize) : NULL;''')
        self._prnt('    if (_cffi_convert_array_argument(_cffi_type(%d), %s, (char **)&%s,' % (self._gettypenum(tp), fromvar, tovar))
        self._prnt('            datasize, &large_args_free) < 0)')
        self._prnt('      %s;' % errcode)
        self._prnt('  }')

    
    def _convert_expr_from_c(self, tp, var, context):
        if isinstance(tp, model.PrimitiveType):
            if tp.is_integer_type() and tp.name != '_Bool':
                return f'''_cffi_from_c_int({var!s}, {tp.name!s})'''
            if None.name != 'long double':
                return f'''_cffi_from_c_{tp.name.replace(' ', '_')!s}({var!s})'''
            return None % (var, self._gettypenum(tp))
        if None(tp, (model.PointerType, model.FunctionPtrType)):
            return '_cffi_from_c_pointer((char *)%s, _cffi_type(%d))' % (var, self._gettypenum(tp))
        if None(tp, model.ArrayType):
            return '_cffi_from_c_pointer((char *)%s, _cffi_type(%d))' % (var, self._gettypenum(model.PointerType(tp.item)))
    # WARNING: Decompyle incomplete

    _generate_cpy_typedef_collecttype = _generate_nothing
    _generate_cpy_typedef_decl = _generate_nothing
    _generate_cpy_typedef_method = _generate_nothing
    _loading_cpy_typedef = _loaded_noop
    _loaded_cpy_typedef = _loaded_noop
    
    def _generate_cpy_function_collecttype(self, tp, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_cpy_function_decl(self, tp, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_cpy_function_method(self, tp, name):
        if tp.ellipsis:
            return None
        numargs = None(tp.args)
        if numargs == 0:
            meth = 'METH_NOARGS'
        elif numargs == 1:
            meth = 'METH_O'
        else:
            meth = 'METH_VARARGS'
        self._prnt(f'''  {{"{name!s}", _cffi_f_{name!s}, {meth!s}, NULL}},''')

    _loading_cpy_function = _loaded_noop
    
    def _loaded_cpy_function(self, tp, name, module, library):
        if tp.ellipsis:
            return None
        func = None(module, name)
        setattr(library, name, func)
        self._types_of_builtin_functions[func] = tp

    _generate_cpy_struct_collecttype = _generate_nothing
    
    def _generate_cpy_struct_decl(self, tp, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_cpy_struct_method(self, tp, name):
        self._generate_struct_or_union_method(tp, 'struct', name)

    
    def _loading_cpy_struct(self, tp, name, module):
        self._loading_struct_or_union(tp, 'struct', name, module)

    
    def _loaded_cpy_struct(self, tp, name, module, **kwds):
        self._loaded_struct_or_union(tp)

    _generate_cpy_union_collecttype = _generate_nothing
    
    def _generate_cpy_union_decl(self, tp, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_cpy_union_method(self, tp, name):
        self._generate_struct_or_union_method(tp, 'union', name)

    
    def _loading_cpy_union(self, tp, name, module):
        self._loading_struct_or_union(tp, 'union', name, module)

    
    def _loaded_cpy_union(self, tp, name, module, **kwds):
        self._loaded_struct_or_union(tp)

    
    def _generate_struct_or_union_decl(self, tp, prefix, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_struct_or_union_method(self, tp, prefix, name):
        pass
    # WARNING: Decompyle incomplete

    
    def _loading_struct_or_union(self, tp, prefix, name, module):
        pass
    # WARNING: Decompyle incomplete

    
    def _loaded_struct_or_union(self, tp):
        pass
    # WARNING: Decompyle incomplete

    _generate_cpy_anonymous_collecttype = _generate_nothing
    
    def _generate_cpy_anonymous_decl(self, tp, name):
        if isinstance(tp, model.EnumType):
            self._generate_cpy_enum_decl(tp, name, '')
            return None
        None._generate_struct_or_union_decl(tp, '', name)

    
    def _generate_cpy_anonymous_method(self, tp, name):
        if not isinstance(tp, model.EnumType):
            self._generate_struct_or_union_method(tp, '', name)
            return None

    
    def _loading_cpy_anonymous(self, tp, name, module):
        if isinstance(tp, model.EnumType):
            self._loading_cpy_enum(tp, name, module)
            return None
        None._loading_struct_or_union(tp, '', name, module)

    
    def _loaded_cpy_anonymous(self, tp, name, module, **kwds):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_cpy_const(self, is_int, name, tp, category, vartp, delayed, size_too, check_value = (None, 'const', None, True, False, None)):
        prnt = self._prnt
        funcname = f'''_cffi_{category!s}_{name!s}'''
        prnt('static int %s(PyObject *lib)' % funcname)
        prnt('{')
        prnt('  PyObject *o;')
        prnt('  int res;')
    # WARNING: Decompyle incomplete

    
    def _generate_cpy_constant_collecttype(self, tp, name):
