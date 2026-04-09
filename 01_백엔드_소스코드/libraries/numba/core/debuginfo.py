# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: debuginfo.pyc (Python 3.11)

'''
Implements helpers to build LLVM debuginfo.
'''
import abc
import os.path as os
from contextlib import contextmanager
from llvmlite import ir
from numba.core import cgutils, types
from numba.core.datamodel.models import ComplexModel, UniTupleModel
from numba.core import config
suspend_emission = (lambda builder: pass# WARNING: Decompyle incomplete
)()

def AbstractDIBuilder():
    '''AbstractDIBuilder'''
    mark_variable = (lambda self, builder, allocavalue, name, lltype, size, line, datamodel, argidx = (None, None): pass)()
    mark_location = (lambda self, builder, line: pass)()
    mark_subprogram = (lambda self, function, qualname, argnames, argtypes, line: pass)()
    initialize = (lambda self: pass)()
    finalize = (lambda self: pass)()

AbstractDIBuilder = <NODE:27>(AbstractDIBuilder, 'AbstractDIBuilder', metaclass = abc.ABCMeta)

class DummyDIBuilder(AbstractDIBuilder):
    
    def __init__(self, module, filepath, cgctx, directives_only):
        pass

    
    def mark_variable(self, builder, allocavalue, name, lltype, size, line, datamodel, argidx = (None, None)):
        pass

    
    def mark_location(self, builder, line):
        pass

    
    def mark_subprogram(self, function, qualname, argnames, argtypes, line):
        pass

    
    def initialize(self):
        pass

    
    def finalize(self):
        pass


_BYTE_SIZE = 8

class DIBuilder(AbstractDIBuilder):
    DWARF_VERSION = 4
    DEBUG_INFO_VERSION = 3
    DBG_CU_NAME = 'llvm.dbg.cu'
    _DEBUG = False
    
    def __init__(self, module, filepath, cgctx, directives_only):
        self.module = module
        self.filepath = os.path.abspath(filepath)
        self.difile = self._di_file()
        self.subprograms = []
        self.cgctx = cgctx
        if directives_only:
            self.emission_kind = 'DebugDirectivesOnly'
        else:
            self.emission_kind = 'FullDebug'
        self.initialize()

    
    def initialize(self):
        self.dicompileunit = self._di_compile_unit()

    
    def _var_type(self, lltype, size, datamodel = (None,)):
        if self._DEBUG:
            print('-->', lltype, size, datamodel, getattr(datamodel, 'fe_type', 'NO FE TYPE'))
        m = self.module
        bitsize = _BYTE_SIZE * size
        int_type = (ir.IntType,)
        real_type = (ir.FloatType, ir.DoubleType)
    # WARNING: Decompyle incomplete

    
    def mark_variable(self, builder, allocavalue, name, lltype, size, line, datamodel, argidx = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def mark_location(self, builder, line):
        builder.debug_metadata = self._add_location(line)

    
    def mark_subprogram(self, function, qualname, argnames, argtypes, line):
        name = qualname
        argmap = dict(zip(argnames, argtypes))
        di_subp = self._add_subprogram(name = name, linkagename = function.name, line = line, function = function, argmap = argmap)
        function.set_metadata('dbg', di_subp)

    
    def finalize(self):
        dbgcu = cgutils.get_or_insert_named_metadata(self.module, self.DBG_CU_NAME)
        dbgcu.add(self.dicompileunit)
        self._set_module_flags()

    
    def _set_module_flags(self):
        '''Set the module flags metadata
        '''
        module = self.module
        mflags = cgutils.get_or_insert_named_metadata(module, 'llvm.module.flags')
        require_warning_behavior = self._const_int(2)
    # WARNING: Decompyle incomplete

    
    def _add_subprogram(self, name, linkagename, line, function, argmap):
        '''Emit subprogram metadata
        '''
        subp = self._di_subprogram(name, linkagename, line, function, argmap)
        self.subprograms.append(subp)
        return subp

    
    def _add_location(self, line):
        '''Emit location metatdaa
        '''
        loc = self._di_location(line)
        return loc

    _const_int = (lambda cls, num, bits = (32,): ir.IntType(bits)(num))()
    _const_bool = (lambda cls, boolean: ir.IntType(1)(boolean))()
    
    def _di_file(self):
        return self.module.add_debug_info('DIFile', {
            'directory': os.path.dirname(self.filepath),
            'filename': os.path.basename(self.filepath) })

    
    def _di_compile_unit(self):
        return self.module.add_debug_info('DICompileUnit', {
            'language': ir.DIToken('DW_LANG_C_plus_plus'),
            'file': self.difile,
            'producer': 'clang (Numba)',
            'runtimeVersion': 0,
            'isOptimized': config.OPT != 0,
            'emissionKind': ir.DIToken(self.emission_kind) }, is_distinct = True)

    
    def _di_subroutine_type(self, line, function, argmap):
        llfunc = function
        md = []
        for idx, llarg in enumerate(llfunc.args):
            if not llarg.name.startswith('arg.'):
                name = llarg.name.replace('.', '$')
                lltype = llarg.type
                size = self.cgctx.get_abi_sizeof(lltype)
                mdtype = self._var_type(lltype, size, datamodel = None)
                md.append(mdtype)
            for name, nbtype in enumerate(argmap.items()):
                name = name.replace('.', '$')
                datamodel = self.cgctx.data_model_manager[nbtype]
                lltype = self.cgctx.get_value_type(nbtype)
                size = self.cgctx.get_abi_sizeof(lltype)
                mdtype = self._var_type(lltype, size, datamodel = datamodel)
                md.append(mdtype)
                return self.module.add_debug_info('DISubroutineType', {
                    'types': self.module.add_metadata(md) })

    
    def _di_subprogram(self, name, linkagename, line, function, argmap):
        return self.module.add_debug_info('DISubprogram', {
            'name': name,
            'linkageName': linkagename,
            'scope': self.difile,
            'file': self.difile,
            'line': line,
            'type': self._di_subroutine_type(line, function, argmap),
            'isLocal': False,
            'isDefinition': True,
            'scopeLine': line,
            'isOptimized': config.OPT != 0,
            'unit': self.dicompileunit }, is_distinct = True)

    
    def _di_location(self, line):
        return self.module.add_debug_info('DILocation', {
            'line': line,
            'column': 1,
            'scope': self.subprograms[-1] })
