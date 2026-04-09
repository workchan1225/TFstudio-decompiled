# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message.pyc (Python 3.11)


class MessageRule:
    '''A marshal for converting between a descriptor and proto.Message.'''
    
    def __init__(self = None, descriptor = None, wrapper = None):
        self._descriptor = descriptor
        self._wrapper = wrapper

    
    def to_python(self = None, value = None, *, absent):
        if isinstance(value, self._descriptor):
            return self._wrapper.wrap(value)

    
    def to_proto(self, value):
        if isinstance(value, self._wrapper):
            return self._wrapper.pb(value)
    # WARNING: Decompyle incomplete

    is_map = (lambda self: desc = self._descriptor.DESCRIPTORif desc.has_options:
passdesc.GetOptions().map_entry)()
