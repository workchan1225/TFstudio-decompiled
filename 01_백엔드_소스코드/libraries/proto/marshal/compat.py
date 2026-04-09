# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compat.pyc (Python 3.11)

from google.protobuf.internal import containers

try:
    from google._upb import _message as _message_upb
except ImportError:
    _message_upb = None


try:
    from google.protobuf.pyext import _message as _message_pyext
except ImportError:
    _message_pyext = None

repeated_composite_types = (containers.RepeatedCompositeFieldContainer,)
repeated_scalar_types = (containers.RepeatedScalarFieldContainer,)
map_composite_types = (containers.MessageMap,)
map_composite_type_names = ('MessageMapContainer',)
for message in (_message_upb, _message_pyext):
    if message:
        repeated_composite_types += (message.RepeatedCompositeContainer,)
        repeated_scalar_types += (message.RepeatedScalarContainer,)
        map_composite_types += (message.MessageMapContainer,)
        continue
        except AttributeError:
            continue
    __all__ = ('repeated_composite_types', 'repeated_scalar_types', 'map_composite_types', 'map_composite_type_names')
    return None
