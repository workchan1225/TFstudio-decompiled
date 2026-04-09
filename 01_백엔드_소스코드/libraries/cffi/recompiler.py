# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: recompiler.pyc (Python 3.11)

import io
import os
import sys
import sysconfig
from  import ffiplatform, model
from error import VerificationError
from cffi_opcode import *
VERSION_BASE = 9729
VERSION_EMBEDDED = 9985
VERSION_CHAR16CHAR32 = 10241
if not sys.platform != 'win32' and sys.version_info < (3, 0):
    if sys.version_info >= (3, 5):
        USE_LIMITED_API = not sysconfig.get_config_var('Py_GIL_DISABLED')
        
        class GlobalExpr:
            
            def __init__(self, name, address, type_op, size, check_value = (0, 0)):
                self.name = name
                self.address = address
                self.type_op = type_op
                self.size = size
                self.check_value = check_value

            
            def as_c_expr(self):
                return f'''  {{ "{self.name!s}", (void *){self.address!s}, {self.type_op.as_c_expr()!s}, (void *){self.size!s} }},'''

            
            def as_python_expr(self):
                return "b'%s%s',%d" % (self.type_op.as_python_bytes(), self.name, self.check_value)


        
        class FieldExpr:
            
            def __init__(self, name, field_offset, field_size, fbitsize, field_type_op):
                self.name = name
                self.field_offset = field_offset
                self.field_size = field_size
                self.fbitsize = fbitsize
                self.field_type_op = field_type_op

            
            def as_c_expr(self):
                spaces = ' ' * len(self.name)
                return f'''  {{ "{self.name!s}", {self.field_offset!s},\n''' + f'''     {spaces!s}   {self.field_size!s},\n''' + f'''     {spaces!s}   {self.field_type_op.as_c_expr()!s} }},'''

            
            def as_python_expr(self):
                raise NotImplementedError

            
            def as_field_python_expr(self):
                if self.field_type_op.op == OP_NOOP:
                    size_expr = ''
                elif self.field_type_op.op == OP_BITFIELD:
                    size_expr = format_four_bytes(self.fbitsize)
                else:
                    raise NotImplementedError
                return f'''b\'{self.field_type_op.as_python_bytes()!s}{size_expr!s}{self.name!s}\''''


        
        class StructUnionExpr:
            
            def __init__(self, name, type_index, flags, size, alignment, comment, first_field_index, c_fields):
                self.name = name
                self.type_index = type_index
                self.flags = flags
                self.size = size
                self.alignment = alignment
                self.comment = comment
                self.first_field_index = first_field_index
                self.c_fields = c_fields

            
            def as_c_expr(self):
                return '  { "%s", %d, %s,' % (self.name, self.type_index, self.flags) + f'''\n    {self.size!s}, {self.alignment!s}, ''' + '%d, %d ' % (self.first_field_index, len(self.c_fields)) + '/* %s */ ' % self.comment if self.comment else '' + '},'

            
            def as_python_expr(self):
                flags = eval(self.flags, G_FLAGS)
                fields_expr = self.c_fields()
                return f'''(b\'{format_four_bytes(self.type_index)!s}{format_four_bytes(flags)!s}{self.name!s}\',{','.join(fields_expr)!s})'''


        
        class EnumExpr:
            
            def __init__(self, name, type_index, size, signed, allenums):
                self.name = name
                self.type_index = type_index
                self.size = size
                self.signed = signed
                self.allenums = allenums

            
            def as_c_expr(self):
                return '  { "%s", %d, _cffi_prim_int(%s, %s),\n    "%s" },' % (self.name, self.type_index, self.size, self.signed, self.allenums)

            
            def as_python_expr(self):
                prim_index = {
                    (1, 0): PRIM_UINT8,
                    (1, 1): PRIM_INT8,
                    (2, 0): PRIM_UINT16,
                    (2, 1): PRIM_INT16,
                    (4, 0): PRIM_UINT32,
                    (4, 1): PRIM_INT32,
                    (8, 0): PRIM_UINT64,
                    (8, 1): PRIM_INT64 }[(self.size, self.signed)]
                return f'''b\'{format_four_bytes(self.type_index)!s}{format_four_bytes(prim_index)!s}{self.name!s}\\x00{self.allenums!s}\''''


        
        class TypenameExpr:
            
            def __init__(self, name, type_index):
                self.name = name
                self.type_index = type_index

            
            def as_c_expr(self):
                return '  { "%s", %d },' % (self.name, self.type_index)

            
            def as_python_expr(self):
                return f'''b\'{format_four_bytes(self.type_index)!s}{self.name!s}\''''


        
        class Recompiler:
            _num_externpy = 0
            
            def __init__(self, ffi, module_name, target_is_python = (False,)):
                self.ffi = ffi
                self.module_name = module_name
                self.target_is_python = target_is_python
                self._version = VERSION_BASE

            
            def needs_version(self, ver):
                self._version = max(self._version, ver)

            
            def collect_type_table(self):
                self._typesdict = { }
                self._generate('collecttype')
                all_decls = sorted(self._typesdict, key = str)
                self.cffi_types = []
            # WARNING: Decompyle incomplete

            
            def _enum_fields(self, tp):
                expand_anonymous_struct_union = not (self.target_is_python)
                return tp.enumfields(expand_anonymous_struct_union)

            
            def _do_collect_type(self, tp):
                pass
            # WARNING: Decompyle incomplete

            
            def _generate(self, step_name):
                lst = self.ffi._parser._declarations.items()
                for tp, quals in sorted(lst):
                    (kind, realname) = name.split(' ', 1)
                    method = getattr(self, f'''_generate_cpy_{kind!s}_{step_name!s}''')
                except AttributeError:
                    raise VerificationError('not implemented in recompile(): %r' % name)
                self._current_quals = quals
                method(tp, realname)
                continue
                except Exception:
                    e = None
                    model.attach_exception_info(e, name)
                    raise 
                    e = None
                    del e

            ALL_STEPS = [
                'global',
                'field',
                'struct_union',
                'enum',
                'typename']
            
            def collect_step_tables(self):
                self._lsts = { }
            # WARNING: Decompyle incomplete

            
            def _prnt(self, what = ('',)):
                self._f.write(what + '\n')

            
            def write_source_to_f(self, f, preamble):
                pass
            # WARNING: Decompyle incomplete

            
            def _rel_readlines(self, filename):
                g = open(os.path.join(os.path.dirname(__file__), filename), 'r')
                lines = g.readlines()
                g.close()
                return lines

            
            def write_c_source_to_f(self, f, preamble):
                self._f = f
                prnt = self._prnt
            # WARNING: Decompyle incomplete

            
            def _to_py(self, x):
                pass
            # WARNING: Decompyle incomplete

            
            def write_py_source_to_f(self, f):
                self._f = f
                prnt = self._prnt
                prnt('# auto-generated file')
                prnt('import _cffi_backend')
            # WARNING: Decompyle incomplete

            
            def _gettypenum(self, type):
                return self._typesdict[type]

            
            def _convert_funcarg_to_c(self, tp, fromvar, tovar, errcode):
                extraarg = ''
                if not isinstance(tp, model.BasePrimitiveType) and tp.is_complex_type():
                    if tp.is_integer_type() and tp.name != '_Bool':
                        converter = '_cffi_to_c_int'
                        extraarg = ', %s' % tp.name
                    elif isinstance(tp, model.UnknownFloatType):
                        converter = f'''({tp.get_c_name('')!s})_cffi_to_c_double'''
                    else:
                        cname = tp.get_c_name('')
                        converter = f'''({cname!s})_cffi_to_c_{tp.name.replace(' ', '_')!s}'''
                        if cname in ('char16_t', 'char32_t'):
                            self.needs_version(VERSION_CHAR16CHAR32)
                    errvalue = '-1'
                elif isinstance(tp, model.PointerType):
                    self._convert_funcarg_to_c_ptr_or_array(tp, fromvar, tovar, errcode)
                    return None
                if isinstance(tp, model.StructOrUnionOrEnum) or isinstance(tp, model.BasePrimitiveType):
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
                self._prnt(f'''    {tovar!s} = ((size_t)datasize) <= 640 ? ({tp.get_c_name('')!s})alloca((size_t)datasize) : NULL;''')
                self._prnt('    if (_cffi_convert_array_argument(_cffi_type(%d), %s, (char **)&%s,' % (self._gettypenum(tp), fromvar, tovar))
                self._prnt('            datasize, &large_args_free) < 0)')
                self._prnt('      %s;' % errcode)
                self._prnt('  }')

            
            def _convert_expr_from_c(self, tp, var, context):
                if isinstance(tp, model.BasePrimitiveType):
                    if tp.is_integer_type() and tp.name != '_Bool':
                        return f'''_cffi_from_c_int({var!s}, {tp.name!s})'''
                    if None(tp, model.UnknownFloatType):
                        return f'''_cffi_from_c_double({var!s})'''
                    if not None.name != 'long double' and tp.is_complex_type():
                        cname = tp.name.replace(' ', '_')
                        if cname in ('char16_t', 'char32_t'):
                            self.needs_version(VERSION_CHAR16CHAR32)
                        return f'''_cffi_from_c_{cname!s}({var!s})'''
                    return None % (var, self._gettypenum(tp))
                if None(tp, (model.PointerType, model.FunctionPtrType)):
                    return '_cffi_from_c_pointer((char *)%s, _cffi_type(%d))' % (var, self._gettypenum(tp))
                if None(tp, model.ArrayType):
                    return '_cffi_from_c_pointer((char *)%s, _cffi_type(%d))' % (var, self._gettypenum(model.PointerType(tp.item)))
            # WARNING: Decompyle incomplete

            
            def _typedef_type(self, tp, name):
                return self._global_type(tp, f'''(*({name!s} *)0)''')

            
            def _generate_cpy_typedef_collecttype(self, tp, name):
                self._do_collect_type(self._typedef_type(tp, name))

            
            def _generate_cpy_typedef_decl(self, tp, name):
                pass

            
            def _typedef_ctx(self, tp, name):
                type_index = self._typesdict[tp]
                self._lsts['typename'].append(TypenameExpr(name, type_index))

            
            def _generate_cpy_typedef_ctx(self, tp, name):
                tp = self._typedef_type(tp, name)
                self._typedef_ctx(tp, name)
                if getattr(tp, 'origin', None) == 'unknown_type':
                    self._struct_ctx(tp, tp.name, approxname = None)
                    return None
                if None(tp, model.NamedPointerType):
                    self._struct_ctx(tp.totype, tp.totype.name, approxname = tp.name, named_ptr = tp)
                    return None

            
            def _generate_cpy_function_collecttype(self, tp, name):
                self._do_collect_type(tp.as_raw_function())
                if not tp.ellipsis or self.target_is_python:
                    self._do_collect_type(tp)
                    return None
                return None

            
            def _generate_cpy_function_decl(self, tp, name):
                pass
            # WARNING: Decompyle incomplete

            
            def _generate_cpy_function_ctx(self, tp, name):
                if not tp.ellipsis and self.target_is_python:
                    self._generate_cpy_constant_ctx(tp, name)
                    return None
                type_index = None._typesdict[tp.as_raw_function()]
                numargs = len(tp.args)
                if self.target_is_python:
                    meth_kind = OP_DLOPEN_FUNC
                elif numargs == 0:
                    meth_kind = OP_CPYTHON_BLTN_N
                elif numargs == 1:
                    meth_kind = OP_CPYTHON_BLTN_O
                else:
                    meth_kind = OP_CPYTHON_BLTN_V
                self._lsts['global'].append(GlobalExpr(name, '_cffi_f_%s' % name, CffiOp(meth_kind, type_index), size = '_cffi_d_%s' % name))

            
            def _field_type(self, tp_struct, field_name, tp_field):
                if isinstance(tp_field, model.ArrayType):
                    actual_length = tp_field.length
                    if actual_length == '...':
                        ptr_struct_name = tp_struct.get_c_name('*')
                        actual_length = f'''_cffi_array_len((({ptr_struct_name!s})0)->{field_name!s})'''
                    tp_item = self._field_type(tp_struct, '%s[0]' % field_name, tp_field.item)
                    tp_field = model.ArrayType(tp_item, actual_length)
                return tp_field

            
            def _struct_collecttype(self, tp):
                self._do_collect_type(tp)
                if self.target_is_python:
                    for fldtype in tp.anonymous_struct_fields():
                        self._struct_collecttype(fldtype)
                        return None
                        return None

            
            def _struct_decl(self, tp, cname, approxname):
                pass
            # WARNING: Decompyle incomplete

            
            def _struct_ctx(self, tp, cname, approxname, named_ptr = (None,)):
                type_index = self._typesdict[tp]
                reason_for_not_expanding = None
                flags = []
                if isinstance(tp, model.UnionType):
                    flags.append('_CFFI_F_UNION')
            # WARNING: Decompyle incomplete

            
            def _check_not_opaque(self, tp, location):
                pass
            # WARNING: Decompyle incomplete

            
            def _add_missing_struct_unions(self):
                lst = list(self._struct_unions.items())
                lst.sort(key = (lambda tp_order: tp_order[1]))
                for tp, order in lst:
                    if tp not in self._seen_struct_unions:
                        if tp.partial:
                            raise NotImplementedError(f'''internal inconsistency: {tp!r} is partial but was not seen at this point''')
                        if tp.name.startswith('$') and tp.name[1:].isdigit():
                            approxname = tp.name[1:]
                        elif tp.name == '_IO_FILE' and tp.forcename == 'FILE':
                            approxname = 'FILE'
                            self._typedef_ctx(tp, 'FILE')
                        else:
                            raise NotImplementedError(f'''internal inconsistency: {tp!r}''')
                        self._struct_ctx(tp, None, approxname)
                    return None

            
            def _generate_cpy_struct_collecttype(self, tp, name):
                self._struct_collecttype(tp)

            _generate_cpy_union_collecttype = _generate_cpy_struct_collecttype
            
            def _struct_names(self, tp):
                cname = tp.get_c_name('')
                if ' ' in cname:
                    return (cname, cname.replace(' ', '_'))
                return (None, '_' + cname)

            
            def _generate_cpy_struct_decl(self, tp, name):
                pass
            # WARNING: Decompyle incomplete

            _generate_cpy_union_decl = _generate_cpy_struct_decl
            
            def _generate_cpy_struct_ctx(self, tp, name):
                pass
            # WARNING: Decompyle incomplete

            _generate_cpy_union_ctx = _generate_cpy_struct_ctx
            
            def _generate_cpy_anonymous_collecttype(self, tp, name):
                if isinstance(tp, model.EnumType):
                    self._generate_cpy_enum_collecttype(tp, name)
                    return None
                None._struct_collecttype(tp)

            
            def _generate_cpy_anonymous_decl(self, tp, name):
                if isinstance(tp, model.EnumType):
                    self._generate_cpy_enum_decl(tp)
                    return None
                None._struct_decl(tp, name, 'typedef_' + name)

            
            def _generate_cpy_anonymous_ctx(self, tp, name):
                if isinstance(tp, model.EnumType):
                    self._enum_ctx(tp, name)
                    return None
                None._struct_ctx(tp, name, 'typedef_' + name)

            
            def _generate_cpy_const(self, is_int, name, tp, category, check_value = (None, 'const', None)):
                if (category, name) in self._seen_constants:
                    raise VerificationError(f'''duplicate declaration of {category!s} \'{name!s}\'''')
                self._seen_constants.add((category, name))
                prnt = self._prnt
                funcname = f'''_cffi_{category!s}_{name!s}'''
            # WARNING: Decompyle incomplete

            
            def _generate_cpy_constant_collecttype(self, tp, name):
                is_int = tp.is_integer_type()
                if is_int or self.target_is_python:
                    self._do_collect_type(tp)
                    return None

            
            def _generate_cpy_constant_decl(self, tp, name):
                is_int = tp.is_integer_type()
                self._generate_cpy_const(is_int, name, tp)

            
            def _generate_cpy_constant_ctx(self, tp, name):
                if self.target_is_python and tp.is_integer_type():
                    type_op = CffiOp(OP_CONSTANT_INT, -1)
                elif self.target_is_python:
                    const_kind = OP_DLOPEN_CONST
                else:
                    const_kind = OP_CONSTANT
                type_index = self._typesdict[tp]
                type_op = CffiOp(const_kind, type_index)
                self._lsts['global'].append(GlobalExpr(name, '_cffi_const_%s' % name, type_op))

            
            def _generate_cpy_enum_collecttype(self, tp, name):
                self._do_collect_type(tp)

            
            def _generate_cpy_enum_decl(self, tp, name = (None,)):
                for enumerator in tp.enumerators:
                    self._generate_cpy_const(True, enumerator)
                    return None

            
            def _enum_ctx(self, tp, cname):
                type_index = self._typesdict[tp]
                type_op = CffiOp(OP_ENUM, -1)
                if self.target_is_python:
                    tp.check_not_partial()
            # WARNING: Decompyle incomplete

            
            def _generate_cpy_enum_ctx(self, tp, name):
                self._enum_ctx(tp, tp._get_c_name())

            
            def _generate_cpy_macro_collecttype(self, tp, name):
                pass

            
            def _generate_cpy_macro_decl(self, tp, name):
                if tp == '...':
                    check_value = None
                else:
                    check_value = tp
                self._generate_cpy_const(True, name, check_value = check_value)

            
            def _generate_cpy_macro_ctx(self, tp, name):
                if tp == '...':
                    if self.target_is_python:
                        raise VerificationError(f'''cannot use the syntax \'...\' in \'#define {name!s} ...\' when using the ABI mode''')
                    check_value = None
                else:
                    check_value = tp
                type_op = CffiOp(OP_CONSTANT_INT, -1)
                self._lsts['global'].append(GlobalExpr(name, '_cffi_const_%s' % name, type_op, check_value = check_value))

            
            def _global_type(self, tp, global_name):
                if isinstance(tp, model.ArrayType):
                    actual_length = tp.length
                    if actual_length == '...':
                        actual_length = f'''_cffi_array_len({global_name!s})'''
                    tp_item = self._global_type(tp.item, '%s[0]' % global_name)
                    tp = model.ArrayType(tp_item, actual_length)
                return tp

            
            def _generate_cpy_variable_collecttype(self, tp, name):
                self._do_collect_type(self._global_type(tp, name))

            
            def _generate_cpy_variable_decl(self, tp, name):
                prnt = self._prnt
                tp = self._global_type(tp, name)
            # WARNING: Decompyle incomplete

            
            def _generate_cpy_variable_ctx(self, tp, name):
                tp = self._global_type(tp, name)
                type_index = self._typesdict[tp]
                if self.target_is_python:
                    op = OP_GLOBAL_VAR
                else:
                    op = OP_GLOBAL_VAR_F
                self._lsts['global'].append(GlobalExpr(name, '_cffi_var_%s' % name, CffiOp(op, type_index)))

            
            def _generate_cpy_extern_python_collecttype(self, tp, name):
                pass
            # WARNING: Decompyle incomplete

            _generate_cpy_dllexport_python_collecttype = _generate_cpy_extern_python_collecttype
            _generate_cpy_extern_python_plus_c_collecttype = _generate_cpy_extern_python_collecttype
            
            def _extern_python_decl(self, tp, name, tag_and_space):
                prnt = self._prnt
                if isinstance(tp.result, model.VoidType):
                    size_of_result = '0'
                else:
                    context = 'result of %s' % name
                    size_of_result = f'''(int)sizeof({tp.result.get_c_name('', context)!s})'''
                prnt('static struct _cffi_externpy_s _cffi_externpy__%s =' % name)
                prnt(f'''  {{ "{self.module_name!s}.{name!s}", {size_of_result!s}, 0, 0 }};''')
                prnt()
                arguments = []
                context = 'argument of %s' % name
                for i, type in enumerate(tp.args):
                    arg = type.get_c_name(' a%d' % i, context)
                    arguments.append(arg)
                    repr_arguments = ', '.join(arguments)
                    if not repr_arguments:
                        repr_arguments = 'void'
                        name_and_arguments = f'''{name!s}({repr_arguments!s})'''
                        if tp.abi == '__stdcall':
                            name_and_arguments = '_cffi_stdcall ' + name_and_arguments
                
                def may_need_128_bits(tp):
