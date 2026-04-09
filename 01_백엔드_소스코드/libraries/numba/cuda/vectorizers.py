# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vectorizers.pyc (Python 3.11)

from numba import cuda
from numpy import array as np_array
from numba.cuda import deviceufunc
from numba.cuda.deviceufunc import UFuncMechanism, GeneralizedUFunc, GUFuncCallSteps

class CUDAUFuncDispatcher(object):
    '''
    Invoke the CUDA ufunc specialization for the given inputs.
    '''
    
    def __init__(self, types_to_retty_kernels, pyfunc):
        self.functions = types_to_retty_kernels
        self.__name__ = pyfunc.__name__

    
    def __call__(self, *args, **kws):
        '''
        *args: numpy arrays or DeviceArrayBase (created by cuda.to_device).
               Cannot mix the two types in one call.

        **kws:
            stream -- cuda stream; when defined, asynchronous mode is used.
            out    -- output array. Can be a numpy array or DeviceArrayBase
                      depending on the input arguments.  Type must match
                      the input arguments.
        '''
        return CUDAUFuncMechanism.call(self.functions, args, kws)

    
    def reduce(self, arg, stream = (0,)):
        pass
    # WARNING: Decompyle incomplete

    
    def __reduce(self, mem, gpu_mems, stream):
        n = mem.shape[0]
        if n % 2 != 0:
            (fatcut, thincut) = mem.split(n - 1)
            gpu_mems.append(fatcut)
            gpu_mems.append(thincut)
            out = self.__reduce(fatcut, gpu_mems, stream)
            gpu_mems.append(out)
            return self(out, thincut, out = out, stream = stream)
        (left, right) = None.split(n // 2)
        gpu_mems.append(left)
        gpu_mems.append(right)
        self(left, right, out = left, stream = stream)
        if n // 2 > 1:
            return self.__reduce(left, gpu_mems, stream)



class _CUDAGUFuncCallSteps(GUFuncCallSteps):
    pass
# WARNING: Decompyle incomplete


class CUDAGeneralizedUFunc(GeneralizedUFunc):
    pass
# WARNING: Decompyle incomplete


class CUDAUFuncMechanism(UFuncMechanism):
    '''
    Provide CUDA specialization
    '''
    DEFAULT_STREAM = 0
    
    def launch(self, func, count, stream, args):
        pass
    # WARNING: Decompyle incomplete

    
    def is_device_array(self, obj):
        return cuda.is_cuda_array(obj)

    
    def as_device_array(self, obj):
        if cuda.cudadrv.devicearray.is_cuda_ndarray(obj):
            return obj
        return None.as_cuda_array(obj)

    
    def to_device(self, hostary, stream):
        return cuda.to_device(hostary, stream = stream)

    
    def to_host(self, devary, stream):
        return devary.copy_to_host(stream = stream)

    
    def allocate_device_array(self, shape, dtype, stream):
        return cuda.device_array(shape = shape, dtype = dtype, stream = stream)

    
    def broadcast_device(self, ary, shape):
        pass
    # WARNING: Decompyle incomplete


vectorizer_stager_source = '\ndef __vectorized_{name}({args}, __out__):\n    __tid__ = __cuda__.grid(1)\n    if __tid__ < __out__.shape[0]:\n        __out__[__tid__] = __core__({argitems})\n'

class CUDAVectorize(deviceufunc.DeviceVectorize):
    
    def _compile_core(self, sig):
        cudevfn = cuda.jit(sig, device = True, inline = True)(self.pyfunc)
        return (cudevfn, cudevfn.overloads[sig.args].signature.return_type)

    
    def _get_globals(self, corefn):
        glbl = self.pyfunc.__globals__.copy()
        glbl.update({
            '__cuda__': cuda,
            '__core__': corefn })
        return glbl

    
    def _compile_kernel(self, fnobj, sig):
        return cuda.jit(fnobj)

    
    def build_ufunc(self):
        return CUDAUFuncDispatcher(self.kernelmap, self.pyfunc)

    _kernel_template = (lambda self: vectorizer_stager_source)()

_gufunc_stager_source = '\ndef __gufunc_{name}({args}):\n    __tid__ = __cuda__.grid(1)\n    if __tid__ < {checkedarg}:\n        __core__({argitems})\n'

class CUDAGUFuncVectorize(deviceufunc.DeviceGUFuncVectorize):
    
    def build_ufunc(self):
        engine = deviceufunc.GUFuncEngine(self.inputsig, self.outputsig)
        return CUDAGeneralizedUFunc(kernelmap = self.kernelmap, engine = engine, pyfunc = self.pyfunc)

    
    def _compile_kernel(self, fnobj, sig):
        return cuda.jit(sig)(fnobj)

    _kernel_template = (lambda self: _gufunc_stager_source)()
    
    def _get_globals(self, sig):
        corefn = cuda.jit(sig, device = True)(self.pyfunc)
        glbls = self.py_func.__globals__.copy()
        glbls.update({
            '__cuda__': cuda,
            '__core__': corefn })
        return glbls
