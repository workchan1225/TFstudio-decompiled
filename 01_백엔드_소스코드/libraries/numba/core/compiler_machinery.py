# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compiler_machinery.pyc (Python 3.11)

import timeit
from abc import abstractmethod, ABCMeta
from collections import namedtuple, OrderedDict
import inspect
from numba.core.compiler_lock import global_compiler_lock
from numba.core import errors, config, transforms, utils
from numba.core.tracing import event
from numba.core.postproc import PostProcessor
from numba.core.ir_utils import enforce_no_dels, legalize_single_scope

event
errors.termcolor() = import numba.core.event, core

class SimpleTimer(object):
    '''
    A simple context managed timer
    '''
    
    def __enter__(self):
        self.ts = timeit.default_timer()
        return self

    
    def __exit__(self, *exc):
        self.elapsed = timeit.default_timer() - self.ts



def CompilerPass():
    '''CompilerPass'''
    __doc__ = ' The base class for all compiler passes.\n    '
    __init__ = (lambda self: self._analysis = Noneself._pass_id = None)()
    name = (lambda cls: cls._name)()
    pass_id = (lambda self: self._pass_id)()
    pass_id = (lambda self, val: self._pass_id = val)()
    analysis = (lambda self: self._analysis)()
    analysis = (lambda self, val: self._analysis = val)()
    
    def run_initialization(self, *args, **kwargs):
        '''
        Runs the initialization sequence for the pass, will run before
        `run_pass`.
        '''
        return False

    run_pass = (lambda self: pass)()
    
    def run_finalizer(self, *args, **kwargs):
        '''
        Runs the initialization sequence for the pass, will run before
        `run_pass`.
        '''
        return False

    
    def get_analysis_usage(self, AU):
        ''' Override to set analysis usage
        '''
        pass

    
    def get_analysis(self, pass_name):
        '''
        Gets the analysis from a given pass
        '''
        return self._analysis[pass_name]


CompilerPass = <NODE:27>(CompilerPass, 'CompilerPass', metaclass = ABCMeta)

class SSACompliantMixin(object):
    ''' Mixin to indicate a pass is SSA form compliant. Nothing is asserted
    about this condition at present.
    '''
    pass


class FunctionPass(CompilerPass):
    ''' Base class for function passes
    '''
    pass


class AnalysisPass(CompilerPass):
    ''' Base class for analysis passes (no modification made to state)
    '''
    pass


class LoweringPass(CompilerPass):
    ''' Base class for lowering passes
    '''
    pass


class AnalysisUsage(object):
    """This looks and behaves like LLVM's AnalysisUsage because its like that.
    """
    
    def __init__(self):
        self._required = set()
        self._preserved = set()

    
    def get_required_set(self):
        return self._required

    
    def get_preserved_set(self):
        return self._preserved

    
    def add_required(self, pss):
        self._required.add(pss)

    
    def add_preserved(self, pss):
        self._preserved.add(pss)

    
    def __str__(self):
        return 'required: %s\n' % self._required


_DEBUG = False

def debug_print(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete

pass_timings = namedtuple('pass_timings', 'init run finalize')

class PassManager(object):
    '''
    The PassManager is a named instance of a particular compilation pipeline
    '''
    _ENFORCING = False
    
    def __init__(self, pipeline_name):
        '''
        Create a new pipeline with name "pipeline_name"
        '''
        self.passes = []
        self.exec_times = OrderedDict()
        self._finalized = False
        self._analysis = None
        self._print_after = None
        self.pipeline_name = pipeline_name

    
    def _validate_pass(self, pass_cls):
        if not isinstance(pass_cls, str):
            if not inspect.isclass(pass_cls) or issubclass(pass_cls, CompilerPass):
                msg = 'Pass must be referenced by name or be a subclass of a CompilerPass. Have %s' % pass_cls
                raise TypeError(msg)
        if isinstance(pass_cls, str):
            pass_cls = _pass_registry.find_by_name(pass_cls)
            return None
        if not None.is_registered(pass_cls):
            raise ValueError('Pass %s is not registered' % pass_cls)

    
    def add_pass(self, pss, description = ('',)):
        """
        Append a pass to the PassManager's compilation pipeline
        """
        self._validate_pass(pss)
        func_desc_tuple = (pss, description)
        self.passes.append(func_desc_tuple)
        self._finalized = False

    
    def add_pass_after(self, pass_cls, location):
        """
        Add a pass `pass_cls` to the PassManager's compilation pipeline after
        the pass `location`.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _debug_init(self):
        pass
    # WARNING: Decompyle incomplete

    
    def finalize(self):
        '''
        Finalize the PassManager, after which no more passes may be added
        without re-finalization.
        '''
        self._analysis = self.dependency_analysis()
        (self._print_after, self._print_before, self._print_wrap) = self._debug_init()
        self._finalized = True

    finalized = (lambda self: self._finalized)()
    
    def _patch_error(self, desc, exc):
        '''
        Patches the error to show the stage that it arose in.
        '''
        newmsg = '{desc}\n{exc}'.format(desc = desc, exc = exc)
        exc.args = (newmsg,)
        return exc

    _runPass = (lambda self, index, pss, internal_state: pass# WARNING: Decompyle incomplete
)()
    
    def run(self, state):
        '''
        Run the defined pipelines on the state.
        '''
        _EarlyPipelineCompletion = _EarlyPipelineCompletion
        import numba.core.compiler
        if not self.finalized:
            raise RuntimeError('Cannot run non-finalised pipeline')
        for pss, pass_desc in enumerate(self.passes):
            event('-- %s' % pass_desc)
            pass_inst = _pass_registry.get(pss).pass_inst
            if isinstance(pass_inst, CompilerPass):
                self._runPass(idx, pass_inst, state)
            else:
                raise BaseException('Legacy pass in use')
            except _EarlyPipelineCompletion:
                e = None
                raise e
                e = None
                del e
            except Exception:
                e = None
                if not isinstance(e, errors.NumbaError):
                    raise e
                msg = f'''Failed in {self.pipeline_name!s} mode pipeline (step: {pass_desc!s})'''
                patched_exception = self._patch_error(msg, e)
                raise patched_exception
                e = None
                del e
            return None

    
    def dependency_analysis(self):
        '''
        Computes dependency analysis
        '''
        deps = dict()
        for pss, _ in self.passes:
            x = _pass_registry.get(pss).pass_inst
            au = AnalysisUsage()
            x.get_analysis_usage(au)
            deps[type(x)] = au
            requires_map = dict()
            for k, v in deps.items():
                requires_map[k] = v.get_required_set()
                
                def resolve_requires(key, rmap):
                    pass
                # WARNING: Decompyle incomplete

                dep_chain = dict()
                for k, v in requires_map.items():
                    dep_chain[k] = set(v) | resolve_requires(v, requires_map)
                    return dep_chain


pass_info = namedtuple('pass_info', 'pass_inst mutates_CFG analysis_only')

class PassRegistry(object):
    '''
    Pass registry singleton class.
    '''
    _id = 0
    _registry = dict()
    
    def register(self, mutates_CFG, analysis_only):
        pass
    # WARNING: Decompyle incomplete

    
    def is_registered(self, clazz):
        return clazz in self._registry.keys()

    
    def get(self, clazz):
        pass
    # WARNING: Decompyle incomplete

    
    def _does_pass_name_alias(self, check):
        for k, v in self._registry.items():
            if v.pass_inst.name == check:
                return True
            return False

    
    def find_by_name(self, class_name):
        pass
    # WARNING: Decompyle incomplete

    
    def dump(self):
        for k, v in self._registry.items():
            print(f'''{k!s}: {v!s}''')


_pass_registry = PassRegistry()
del PassRegistry
register_pass = _pass_registry.register
