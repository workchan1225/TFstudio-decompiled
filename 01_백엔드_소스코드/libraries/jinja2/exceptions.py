# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

import typing as t
if t.TYPE_CHECKING:
    from runtime import Undefined

class TemplateError(Exception):
    pass
# WARNING: Decompyle incomplete


class TemplateNotFound(TemplateError, LookupError, IOError):
    '''Raised if a template does not exist.

    .. versionchanged:: 2.11
        If the given name is :class:`Undefined` and no message was
        provided, an :exc:`UndefinedError` is raised.
    '''
    message: t.Optional[str] = None
    
    def __init__(self = None, name = None, message = None):
        IOError.__init__(self, name)
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        return str(self.message)



class TemplatesNotFound(TemplateNotFound):
    pass
# WARNING: Decompyle incomplete


class TemplateSyntaxError(TemplateError):
    pass
# WARNING: Decompyle incomplete


class TemplateAssertionError(TemplateSyntaxError):
    """Like a template syntax error, but covers cases where something in the
    template caused an error at compile time that wasn't necessarily caused
    by a syntax error.  However it's a direct subclass of
    :exc:`TemplateSyntaxError` and has the same attributes.
    """
    pass


class TemplateRuntimeError(TemplateError):
    '''A generic runtime error in the template engine.  Under some situations
    Jinja may raise this exception.
    '''
    pass


class UndefinedError(TemplateRuntimeError):
    '''Raised if a template tries to operate on :class:`Undefined`.'''
    pass


class SecurityError(TemplateRuntimeError):
    '''Raised if a template tries to do something insecure if the
    sandbox is enabled.
    '''
    pass


class FilterArgumentError(TemplateRuntimeError):
    '''This error is raised if a filter was called with inappropriate
    arguments
    '''
    pass
