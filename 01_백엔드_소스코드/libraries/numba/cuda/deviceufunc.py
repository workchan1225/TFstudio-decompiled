# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: deviceufunc.pyc (Python 3.11)

'''
Implements custom ufunc dispatch mechanism for non-CPU devices.
'''
from abc import ABCMeta, abstractmethod
from collections import OrderedDict
import operator
import warnings
from functools import reduce
import numpy as np
from numba.np.ufunc.ufuncbuilder import _BaseUFuncBuilder, parse_identity
from numba.core import types, sigutils
from numba.core.typing import signature
from numba.np.ufunc.sigparse import parse_signature

def _broadcast_axis(a, b):
    '''
    Raises
    ------
    ValueError if broadcast fails
    '''
    if a == b:
        return a
    if None == 1:
        return b
    if None == 1:
        return a
    raise None('failed to broadcast {0} and {1}'.format(a, b))


def _pairwise_broadcast(shape1, shape2):
    '''
    Raises
    ------
    ValueError if broadcast fails
    '''
    (shape1, shape2) = map(tuple, [
        shape1,
        shape2])
# WARNING: Decompyle incomplete


def _multi_broadcast(*shapelist):
    '''
    Raises
    ------
    ValueError if broadcast fails
    '''
    pass
# WARNING: Decompyle incomplete


class UFuncMechanism(object):
    '''
    Prepare ufunc arguments for vectorize.
    '''
    DEFAULT_STREAM = None
    SUPPORT_DEVICE_SLICING = False
    
    def __init__(self, typemap, args):
        '''Never used directly by user. Invoke by UFuncMechanism.call().
        '''
        self.typemap = typemap
        self.args = args
        nargs = len(self.args)
        self.argtypes = [
            None] * nargs
        self.scalarpos = []
        self.signature = None
        self.arrays = [
            None] * nargs

    
    def _fill_arrays(self):
        '''
        Get all arguments in array form
        '''
        for i, arg in enumerate(self.args):
            if self.is_device_array(arg):
                self.arrays[i] = self.as_device_array(arg)
                continue
            if isinstance(arg, (int, float, complex, np.number)):
                self.scalarpos.append(i)
                continue
            self.arrays[i] = np.asarray(arg)
            return None

    
    def _fill_argtypes(self):
        '''
        Get dtypes
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _resolve_signature(self):
        '''Resolve signature.
        May have ambiguous case.
        '''
        matches = []
    # WARNING: Decompyle incomplete

    
    def _get_actual_args(self):
        '''Return the actual arguments
        Casts scalar arguments to np.array.
        '''
        for i in self.scalarpos:
            self.arrays[i] = np.array([
                self.args[i]], dtype = self.argtypes[i])
            return self.arrays

    
    def _broadcast(self, arys):
        '''Perform numpy ufunc broadcasting
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_arguments(self):
        '''Prepare and return the arguments for the ufunc.
        Does not call to_device().
        '''
        self._fill_arrays()
        self._fill_argtypes()
        self._resolve_signature()
        arys = self._get_actual_args()
        return self._broadcast(arys)

    
    def get_function(self):
        '''Returns (result_dtype, function)
        '''
        return self.typemap[self.argtypes]

    
    def is_device_array(self, obj):
        '''Is the `obj` a device array?
        Override in subclass
        '''
        return False

    
    def as_device_array(self, obj):
        '''Convert the `obj` to a device array
        Override in subclass

        Default implementation is an identity function
        '''
        return obj

    
    def broadcast_device(self, ary, shape):
        '''Handles ondevice broadcasting

        Override in subclass to add support.
        '''
        raise NotImplementedError('broadcasting on device is not supported')

    
    def force_array_layout(self, ary):
        '''Ensures array layout met device requirement.

        Override in sublcass
        '''
        return ary

    call = (lambda cls, typemap, args, kws: pass# WARNING: Decompyle incomplete
)()
    
    def to_device(self, hostary, stream):
        '''Implement to device transfer
        Override in subclass
        '''
        raise NotImplementedError

    
    def to_host(self, devary, stream):
        '''Implement to host transfer
        Override in subclass
        '''
        raise NotImplementedError

    
    def allocate_device_array(self, shape, dtype, stream):
        '''Implements device allocation
        Override in subclass
        '''
        raise NotImplementedError

    
    def launch(self, func, count, stream, args):
        '''Implements device function invocation
        Override in subclass
        '''
        raise NotImplementedError



def to_dtype(ty):
    if isinstance(ty, types.EnumMember):
        ty = ty.dtype
    return np.dtype(str(ty))


class DeviceVectorize(_BaseUFuncBuilder):
    
    def __init__(self, func, identity, cache, targetoptions = (None, False, None)):
        pass
    # WARNING: Decompyle incomplete

    pyfunc = (lambda self: self.py_func)()
    
    def add(self, sig = (None,)):
        (args, return_type) = sigutils.normalize_signature(sig)
    # WARNING: Decompyle incomplete

    
    def build_ufunc(self):
        raise NotImplementedError

    
    def _get_kernel_source(self, template, sig, funcname):
        args = range(len(sig.args))()
        fmts = funcname(name = ', '.join(args), args = ', '.join, argitems = (lambda .0: pass# WARNING: Decompyle incomplete
)(args()))
    # WARNING: Decompyle incomplete

    
    def _compile_core(self, sig):
        raise NotImplementedError

    
    def _get_globals(self, corefn):
        raise NotImplementedError

    
    def _compile_kernel(self, fnobj, sig):
        raise NotImplementedError



class DeviceGUFuncVectorize(_BaseUFuncBuilder):
    
    def __init__(self, func, sig, identity, cache, targetoptions, writable_args = (None, False, None, ())):
        pass
    # WARNING: Decompyle incomplete

    pyfunc = (lambda self: self.py_func)()
    
    def add(self, sig = (None,)):
        indims = self.inputsig()
        outdims = self.outputsig()
        (args, return_type) = sigutils.normalize_signature(sig)
        valid_return_type = return_type in (types.none, None)
        if not valid_return_type:
            raise TypeError(f'''guvectorized functions cannot return values: signature {sig} specifies {return_type} return type''')
        funcname = self.py_func.__name__
        src = expand_gufunc_template(self._kernel_template, indims, outdims, funcname, args)
        glbls = self._get_globals(sig)
        exec(src, glbls)
        fnobj = glbls['__gufunc_{name}'.format(name = funcname)]
        outertys = list(_determine_gufunc_outer_types(args, indims + outdims))
        kernel = self._compile_kernel(fnobj, sig = tuple(outertys))
        nout = len(outdims)
        dtypes = outertys()
        indtypes = tuple(dtypes[:-nout])
        outdtypes = tuple(dtypes[-nout:])
        self.kernelmap[indtypes] = (outdtypes, kernel)

    
    def _compile_kernel(self, fnobj, sig):
        raise NotImplementedError

    
    def _get_globals(self, sig):
        raise NotImplementedError



def _determine_gufunc_outer_types(argtys, dims):
    pass
# WARNING: Decompyle incomplete


def expand_gufunc_template(template, indims, outdims, funcname, argtypes):
    '''Expand gufunc source template
    '''
    argdims = indims + outdims
    argnames = range(len(argdims))()
    checkedarg = ', '.join((lambda .0: [ '{0}.shape[0]'.format(a) for a in .0 ])(argnames()))
    inputs = zip(argnames, indims, argtypes)()
    outputs = zip(argnames[len(indims):], outdims, argtypes[len(indims):])()
    argitems = inputs + outputs
    src = template.format(name = funcname, args = ', '.join(argnames), checkedarg = checkedarg, argitems = ', '.join(argitems))
    return src


def _gen_src_for_indexing(aref, adims, atype):
    return '{aref}[{sliced}]'.format(aref = aref, sliced = _gen_src_index(adims, atype))


def _gen_src_index(adims, atype):
    if adims > 0:
        return ','.join([
            '__tid__'] + [
            ':'] * adims)
    if None(atype, types.Array) and atype.ndim - 1 == adims:
        return '__tid__:(__tid__ + 1)'


class GUFuncEngine(object):
    '''Determine how to broadcast and execute a gufunc
    base on input shape and signature
    '''
    from_signature = (lambda cls, signature: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self, inputsig, outputsig):
        self.sin = inputsig
        self.sout = outputsig
        self.nin = len(self.sin)
        self.nout = len(self.sout)

    
    def schedule(self, ishapes):
        if len(ishapes) != self.nin:
            raise TypeError('invalid number of input argument')
        symbolmap = { }
        outer_shapes = []
        inner_shapes = []
        for shape, symbols in enumerate(zip(ishapes, self.sin)):
            argn += 1
            inner_ndim = len(symbols)
            if len(shape) < inner_ndim:
                fmt = 'arg #%d: insufficient inner dimension'
                raise ValueError(fmt % (argn,))
            for dim, sym in enumerate(zip(inner_shape, symbols)):
                axis += len(outer_shape)
                if sym in symbolmap and symbolmap[sym] != dim:
                    fmt = 'arg #%d: shape[%d] mismatch argument'
                    raise ValueError(fmt % (argn, axis))
                symbolmap[sym] = dim
                outer_shapes.append(outer_shape)
                inner_shapes.append(inner_shape)
                oshapes = []
                for outsig in self.sout:
                    oshape = []
                    for sym in outsig:
                        oshape.append(symbolmap[sym])
                        oshapes.append(tuple(oshape))
                        sizes = outer_shapes()
                        largest_i = np.argmax(sizes)
                        loopdims = outer_shapes[largest_i]
                        pinned = [
                            False] * self.nin
                        for i, d in enumerate(outer_shapes):
                            if d != loopdims:
                                if d == (1,) or d == ():
                                    pinned[i] = True
                                    continue
                                fmt = 'arg #%d: outer dimension mismatch'
                                raise ValueError(fmt % (i + 1,))
                            return GUFuncSchedule(self, inner_shapes, oshapes, loopdims, pinned)



class GUFuncSchedule(object):
    
    def __init__(self, parent, ishapes, oshapes, loopdims, pinned):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        pass
    # WARNING: Decompyle incomplete



class GeneralizedUFunc(object):
    
    def __init__(self, kernelmap, engine):
        self.kernelmap = kernelmap
        self.engine = engine
        self.max_blocksize = 1073741824

    
    def __call__(self, *args, **kws):
        callsteps = self._call_steps(self.engine.nin, self.engine.nout, args, kws)
        (indtypes, schedule, outdtypes, kernel) = self._schedule(callsteps.inputs, callsteps.outputs)
        callsteps.adjust_input_types(indtypes)
        outputs = callsteps.prepare_outputs(schedule, outdtypes)
        inputs = callsteps.prepare_inputs()
        parameters = self._broadcast(schedule, inputs, outputs)
        callsteps.launch_kernel(kernel, schedule.loopn, parameters)
        return callsteps.post_process_outputs(outputs)

    
    def _schedule(self, inputs, outs):
        input_shapes = inputs()
        schedule = self.engine.schedule(input_shapes)
        indtypes = (lambda .0: pass# WARNING: Decompyle incomplete
)(inputs())
        
        try:
            (outdtypes, kernel) = self.kernelmap[indtypes]
        except KeyError:
            indtypes = self._search_matching_signature(indtypes)
            (outdtypes, kernel) = self.kernelmap[indtypes]

    # WARNING: Decompyle incomplete

    
    def _search_matching_signature(self, idtypes):
        '''
        Given the input types in `idtypes`, return a compatible sequence of
        types that is defined in `kernelmap`.

        Note: Ordering is guaranteed by `kernelmap` being a OrderedDict
        '''
        for sig in self.kernelmap.keys():
            if (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(sig, idtypes)()):
                
                return all, sig
            raise TypeError('no matching signature')

    
    def _broadcast(self, schedule, params, retvals):
        pass
    # WARNING: Decompyle incomplete

    
    def _broadcast_array(self, ary, newdim, innerdim):
        newshape = (newdim,) + innerdim
        if ary.shape == newshape:
            return ary
    # WARNING: Decompyle incomplete

    
    def _broadcast_add_axis(self, ary, newshape):
        raise NotImplementedError('cannot add new axis')

    
    def _broadcast_scalar_input(self, ary, shape):
        raise NotImplementedError



def GUFuncCallSteps():
    '''GUFuncCallSteps'''
    __doc__ = '\n    Implements memory management and kernel launch operations for GUFunc calls.\n\n    One instance of this class is instantiated for each call, and the instance\n    is specific to the arguments given to the GUFunc call.\n\n    The base class implements the overall logic; subclasses provide\n    target-specific implementations of individual functions.\n    '
    __slots__ = [
        'outputs',
        'inputs',
        '_copy_result_to_host']
    launch_kernel = (lambda self, kernel, nelem, args: pass)()
    is_device_array = (lambda self, obj: pass)()
    as_device_array = (lambda self, obj: pass)()
    to_device = (lambda self, hostary: pass)()
    allocate_device_array = (lambda self, shape, dtype: pass)()
    
    def __init__(self, nin, nout, args, kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def adjust_input_types(self, indtypes):
        '''
        Attempt to cast the inputs to the required types if necessary
        and if they are not device arrays.

        Side effect: Only affects the elements of `inputs` that require
        a type cast.
        '''
        for ity, val in enumerate(zip(indtypes, self.inputs)):
            if ity != val.dtype:
                if not hasattr(val, 'astype'):
                    msg = 'compatible signature is possible by casting but {0} does not support .astype()'.format(type(val))
                    raise TypeError(msg)
                self.inputs[i] = val.astype(ity)
            return None

    
    def prepare_outputs(self, schedule, outdtypes):
        '''
        Returns a list of output parameters that all reside on the target
        device.

        Outputs that were passed-in to the GUFunc are used if they reside on the
        device; other outputs are allocated as necessary.
        '''
        outputs = []
    # WARNING: Decompyle incomplete

    
    def prepare_inputs(self):
        '''
        Returns a list of input parameters that all reside on the target device.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def post_process_outputs(self, outputs):
        '''
        Moves the given output(s) to the host if necessary.

        Returns a single value (e.g. an array) if there was one output, or a
        tuple of arrays if there were multiple. Although this feels a little
        jarring, it is consistent with the behavior of GUFuncs in general.
        '''
        pass
    # WARNING: Decompyle incomplete


GUFuncCallSteps = <NODE:27>(GUFuncCallSteps, 'GUFuncCallSteps', metaclass = ABCMeta)
