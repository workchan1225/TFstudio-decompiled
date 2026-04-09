# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: globals.pyc (Python 3.11)

import typing as t
from threading import local
if t.TYPE_CHECKING:
    import typing_extensions as te
    from core import Context
_local = local()
get_current_context = (lambda silent = None: pass)()
get_current_context = (lambda silent = None: pass)()

def get_current_context(silent = None):
    '''Returns the current click context.  This can be used as a way to
    access the current context object from anywhere.  This is a more implicit
    alternative to the :func:`pass_context` decorator.  This function is
    primarily useful for helpers such as :func:`echo` which might be
    interested in changing its behavior based on the current context.

    To push the current context, :meth:`Context.scope` can be used.

    .. versionadded:: 5.0

    :param silent: if set to `True` the return value is `None` if no context
                   is available.  The default behavior is to raise a
                   :exc:`RuntimeError`.
    '''
    
    try:
        return t.cast('Context', _local.stack[-1])
    except (AttributeError, IndexError):
        e = None
        if not silent:
            raise RuntimeError('There is no active click context.'), e
        e = None
        del e
    except:
        e = None
        del e



def push_context(ctx = None):
    '''Pushes a new context to the current stack.'''
    _local.__dict__.setdefault('stack', []).append(ctx)


def pop_context():
    '''Removes the top level from the stack.'''
    _local.stack.pop()


def resolve_color_default(color = None):
    """Internal helper to get the default value of the color flag.  If a
    value is passed it's returned unchanged, otherwise it's looked up from
    the current context.
    """
    pass
# WARNING: Decompyle incomplete
