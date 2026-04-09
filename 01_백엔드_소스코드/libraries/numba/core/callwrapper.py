# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: callwrapper.pyc (Python 3.11)

from llvmlite.ir import Constant, IRBuilder
import llvmlite.ir as llvmlite
from numba.core import types, config, cgutils

class _ArgManager(object):
    '''
    A utility class to handle argument unboxing and cleanup
    '''
    
    def __init__(self, context, builder, api, env_manager, endblk, nargs):
        self.context = context
        self.builder = builder
        self.api = api
        self.env_manager = env_manager
        self.arg_count = 0
        self.cleanups = []
        self.nextblk = endblk

    
    def add_arg(self, obj, ty):
        '''
        Unbox argument and emit code that handles any error during unboxing.
        Args are cleaned up in reverse order of the parameter list, and
        cleanup begins as soon as unboxing of any argument fails. E.g. failure
        on arg2 will result in control flow going through:

            arg2.err -> arg1.err -> arg0.err -> arg.end (returns)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def emit_cleanup(self):
        '''
        Emit the cleanup code after returning from the wrapped function.
        '''
        for dtor in self.cleanups:
            dtor()
            return None



class _GilManager(object):
    '''
    A utility class to handle releasing the GIL and then re-acquiring it
    again.
    '''
    
    def __init__(self, builder, api, argman):
        self.builder = builder
        self.api = api
        self.argman = argman
        self.thread_state = api.save_thread()

    
    def emit_cleanup(self):
        self.api.restore_thread(self.thread_state)
        self.argman.emit_cleanup()



class PyCallWrapper(object):
    
    def __init__(self, context, module, func, fndesc, env, call_helper, release_gil):
        self.context = context
        self.module = module
        self.func = func
        self.fndesc = fndesc
        self.env = env
        self.release_gil = release_gil

    
    def build(self):
        wrapname = self.fndesc.llvm_cpython_wrapper_name
        pyobj = self.context.get_argument_type(types.pyobject)
        wrapty = llvmlite.ir.FunctionType(pyobj, [
            pyobj,
            pyobj,
            pyobj])
        wrapper = llvmlite.ir.Function(self.module, wrapty, name = wrapname)
        builder = IRBuilder(wrapper.append_basic_block('entry'))
        (closure, args, kws) = wrapper.args
        closure.name = 'py_closure'
        args.name = 'py_args'
        kws.name = 'py_kws'
        api = self.context.get_python_api(builder)
        self.build_wrapper(api, builder, closure, args, kws)
        return (wrapper, api)

    
    def build_wrapper(self, api, builder, closure, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def get_env(self, api, builder):
        '''Get the Environment object which is declared as a global
        in the module of the wrapped function.
        '''
        envname = self.context.get_env_name(self.fndesc)
        gvptr = self.context.declare_env_global(builder.module, envname)
        envptr = builder.load(gvptr)
        env_body = self.context.get_env_body(builder, envptr)
        api.emit_environment_sentry(envptr, return_pyobject = True, debug_msg = self.fndesc.env_name)
        env_manager = api.get_env_manager(self.env, env_body, envptr)
        return env_manager

    
    def _simplified_return_type(self):
        '''
        The NPM callconv has already converted simplified optional types.
        We can simply use the value type from it.
        '''
        restype = self.fndesc.restype
        if isinstance(restype, types.Optional):
            return restype.type

    
    def debug_print(self, builder, msg):
        if config.DEBUG_JIT:
            self.context.debug_print(builder, 'DEBUGJIT: {0}'.format(msg))
            return None
