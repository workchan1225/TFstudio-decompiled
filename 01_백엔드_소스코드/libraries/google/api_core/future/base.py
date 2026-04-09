# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Abstract and helper bases for Future implementations.'''
import abc

def Future():
    '''Future'''
    __doc__ = 'Future interface.\n\n    This interface is based on :class:`concurrent.futures.Future`.\n    '
    cancel = (lambda self: raise NotImplementedError())()
    cancelled = (lambda self: raise NotImplementedError())()
    running = (lambda self: raise NotImplementedError())()
    done = (lambda self: raise NotImplementedError())()
    result = (lambda self, timeout = (None,): raise NotImplementedError())()
    exception = (lambda self, timeout = (None,): raise NotImplementedError())()
    add_done_callback = (lambda self, fn: raise NotImplementedError())()
    set_result = (lambda self, result: raise NotImplementedError())()
    set_exception = (lambda self, exception: raise NotImplementedError())()

Future = <NODE:27>(Future, 'Future', object, metaclass = abc.ABCMeta)
