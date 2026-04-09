# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abc.pyc (Python 3.11)

from abc import ABC

class RichRenderable(ABC):
    '''An abstract base class for Rich renderables.

    Note that there is no need to extend this class, the intended use is to check if an
    object supports the Rich renderable protocol. For example::

        if isinstance(my_object, RichRenderable):
            console.print(my_object)

    '''
    __subclasshook__ = (lambda cls = None, other = None:
