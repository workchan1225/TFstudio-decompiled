# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: deprecation.pyc (Python 3.11)

'''
Support for deprecation warnings when importing names from old locations.

When software evolves, things tend to move around. This is usually detrimental
to backwards compatibility (in Python this primarily manifests itself as
:exc:`~exceptions.ImportError` exceptions).

While backwards compatibility is very important, it should not get in the way
of progress. It would be great to have the agility to move things around
without breaking backwards compatibility.

This is where the :mod:`humanfriendly.deprecation` module comes in: It enables
the definition of backwards compatible aliases that emit a deprecation warning
when they are accessed.

The way it works is that it wraps the original module in an :class:`DeprecationProxy`
object that defines a :func:`~DeprecationProxy.__getattr__()` special method to
override attribute access of the module.
'''
import collections
import functools
import importlib
import inspect
import sys
import types
import warnings
from humanfriendly.text import format
REGISTRY = collections.defaultdict(dict)
__all__ = ('DeprecationProxy', 'define_aliases', 'deprecated_args', 'get_aliases', 'is_method')

def define_aliases(module_name, **aliases):
    '''
    Update a module with backwards compatible aliases.

    :param module_name: The ``__name__`` of the module (a string).
    :param aliases: Each keyword argument defines an alias. The values
                    are expected to be "dotted paths" (strings).

    The behavior of this function depends on whether the Sphinx documentation
    generator is active, because the use of :class:`DeprecationProxy` to shadow the
    real module in :data:`sys.modules` has the unintended side effect of
    breaking autodoc support for ``:data:`` members (module variables).

    To avoid breaking Sphinx the proxy object is omitted and instead the
    aliased names are injected into the original module namespace, to make sure
    that imports can be satisfied when the documentation is being rendered.

    If you run into cyclic dependencies caused by :func:`define_aliases()` when
    running Sphinx, you can try moving the call to :func:`define_aliases()` to
    the bottom of the Python module you\'re working on.
    '''
    module = sys.modules[module_name]
    proxy = DeprecationProxy(module, aliases)
    for name, target in aliases.items():
        REGISTRY[module.__name__][name] = target
        if 'sphinx' in sys.modules:
            for name, target in aliases.items():
                setattr(module, name, proxy.resolve(target))
                return None
                sys.modules[module_name] = proxy
                return None


def get_aliases(module_name):
    """
    Get the aliases defined by a module.

    :param module_name: The ``__name__`` of the module (a string).
    :returns: A dictionary with string keys and values:

              1. Each key gives the name of an alias
                 created for backwards compatibility.

              2. Each value gives the dotted path of
                 the proper location of the identifier.

              An empty dictionary is returned for modules that
              don't define any backwards compatible aliases.
    """
    return REGISTRY.get(module_name, { })


def deprecated_args(*names):
    """
    Deprecate positional arguments without dropping backwards compatibility.

    :param names:

      The positional arguments to :func:`deprecated_args()` give the names of
      the positional arguments that the to-be-decorated function should warn
      about being deprecated and translate to keyword arguments.

    :returns: A decorator function specialized to `names`.

    The :func:`deprecated_args()` decorator function was created to make it
    easy to switch from positional arguments to keyword arguments [#]_ while
    preserving backwards compatibility [#]_ and informing call sites
    about the change.

    .. [#] Increased flexibility is the main reason why I find myself switching
           from positional arguments to (optional) keyword arguments as my code
           evolves to support more use cases.

    .. [#] In my experience positional argument order implicitly becomes part
           of API compatibility whether intended or not. While this makes sense
           for functions that over time adopt more and more optional arguments,
           at a certain point it becomes an inconvenience to code maintenance.

    Here's an example of how to use the decorator::

      @deprecated_args('text')
      def report_choice(**options):
          print(options['text'])

    When the decorated function is called with positional arguments
    a deprecation warning is given::

      >>> report_choice('this will give a deprecation warning')
      DeprecationWarning: report_choice has deprecated positional arguments, please switch to keyword arguments
      this will give a deprecation warning

    But when the function is called with keyword arguments no deprecation
    warning is emitted::

      >>> report_choice(text='this will not give a deprecation warning')
      this will not give a deprecation warning
    """
    pass
# WARNING: Decompyle incomplete


def is_method(function):
    '''Check if the expected usage of the given function is as an instance method.'''
    
    try:
        signature = inspect.signature(function)
        return 'self' in signature.parameters
    except AttributeError:
        metadata = inspect.getargspec(function)
        return 



class DeprecationProxy(types.ModuleType):
    pass
# WARNING: Decompyle incomplete
