# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error.pyc (Python 3.11)


class CudaDriverError(Exception):
    pass


class CudaRuntimeError(Exception):
    pass


class CudaSupportError(ImportError):
    pass


class NvvmError(Exception):
    
    def __str__(self):
        return '\n'.join(map(str, self.args))



class NvvmSupportError(ImportError):
    pass


class NvvmWarning(Warning):
    pass


class NvrtcError(Exception):
    
    def __str__(self):
        return '\n'.join(map(str, self.args))



class NvrtcCompilationError(NvrtcError):
    pass


class NvrtcSupportError(ImportError):
    pass
