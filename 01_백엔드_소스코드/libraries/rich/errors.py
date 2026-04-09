# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)


class ConsoleError(Exception):
    '''An error in console operation.'''
    pass


class StyleError(Exception):
    '''An error in styles.'''
    pass


class StyleSyntaxError(ConsoleError):
    '''Style was badly formatted.'''
    pass


class MissingStyle(StyleError):
    '''No such style.'''
    pass


class StyleStackError(ConsoleError):
    '''Style stack is invalid.'''
    pass


class NotRenderableError(ConsoleError):
    '''Object is not renderable.'''
    pass


class MarkupError(ConsoleError):
    '''Markup was badly formatted.'''
    pass


class LiveError(ConsoleError):
    '''Error related to Live display.'''
    pass


class NoAltScreen(ConsoleError):
    '''Alt screen mode was required.'''
    pass
