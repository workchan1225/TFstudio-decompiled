# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: traceback.pyc (Python 3.11)

'''Extract, format and print information about Python stack traces.'''
import collections.abc as collections
import itertools
import linecache
import sys
import textwrap
from contextlib import suppress
__all__ = [
    'extract_stack',
    'extract_tb',
    'format_exception',
    'format_exception_only',
    'format_list',
    'format_stack',
    'format_tb',
    'print_exc',
    'format_exc',
    'print_exception',
    'print_last',
    'print_stack',
    'print_tb',
    'clear_frames',
    'FrameSummary',
    'StackSummary',
    'TracebackException',
    'walk_stack',
    'walk_tb']

def print_list(extracted_list, file = (None,)):
    '''Print the list of tuples as returned by extract_tb() or
    extract_stack() as a formatted stack trace to the given file.'''
    pass
# WARNING: Decompyle incomplete


def format_list(extracted_list):
    '''Format a list of tuples or FrameSummary objects for printing.

    Given a list of tuples or FrameSummary objects as returned by
    extract_tb() or extract_stack(), return a list of strings ready
    for printing.

    Each string in the resulting list corresponds to the item with the
    same index in the argument list.  Each string ends in a newline;
    the strings may contain internal newlines as well, for those items
    whose source text line is not None.
    '''
    return StackSummary.from_list(extracted_list).format()


def print_tb(tb, limit, file = (None, None)):
    """Print up to 'limit' stack trace entries from the traceback 'tb'.

    If 'limit' is omitted or None, all entries are printed.  If 'file'
    is omitted or None, the output goes to sys.stderr; otherwise
    'file' should be an open file or file-like object with a write()
    method.
    """
    print_list(extract_tb(tb, limit = limit), file = file)


def format_tb(tb, limit = (None,)):
    """A shorthand for 'format_list(extract_tb(tb, limit))'."""
    return extract_tb(tb, limit = limit).format()


def extract_tb(tb, limit = (None,)):
    """
    Return a StackSummary object representing a list of
    pre-processed entries from traceback.

    This is useful for alternate formatting of stack traces.  If
    'limit' is omitted or None, all entries are extracted.  A
    pre-processed stack trace entry is a FrameSummary object
    containing attributes filename, lineno, name, and line
    representing the information that is usually printed for a stack
    trace.  The line is a string with leading and trailing
    whitespace stripped; if the source is not available it is None.
    """
    return StackSummary._extract_from_extended_frame_gen(_walk_tb_with_full_positions(tb), limit = limit)

_cause_message = '\nThe above exception was the direct cause of the following exception:\n\n'
_context_message = '\nDuring handling of the above exception, another exception occurred:\n\n'

class _Sentinel:
    
    def __repr__(self):
        return '<implicit>'


_sentinel = _Sentinel()

def _parse_value_tb(exc, value, tb):
    if (value is _sentinel) != (tb is _sentinel):
        raise ValueError('Both or neither of value and tb must be given')
    if  is value, tb or value, tb is _sentinel:
        pass
    
# WARNING: Decompyle incomplete


def print_exception(exc, value, tb, limit, file, chain = (_sentinel, _sentinel, None, None, True)):
    '''Print exception up to \'limit\' stack trace entries from \'tb\' to \'file\'.

    This differs from print_tb() in the following ways: (1) if
    traceback is not None, it prints a header "Traceback (most recent
    call last):"; (2) it prints the exception type and value after the
    stack trace; (3) if type is SyntaxError and value has the
    appropriate format, it prints the line where the syntax error
    occurred with a caret on the next line indicating the approximate
    position of the error.
    '''
    (value, tb) = _parse_value_tb(exc, value, tb)
    te = TracebackException(type(value), value, tb, limit = limit, compact = True)
    te.print(file = file, chain = chain)


def format_exception(exc, value, tb, limit, chain = (_sentinel, _sentinel, None, True)):
    '''Format a stack trace and the exception information.

    The arguments have the same meaning as the corresponding arguments
    to print_exception().  The return value is a list of strings, each
    ending in a newline and some containing internal newlines.  When
    these lines are concatenated and printed, exactly the same text is
    printed as does print_exception().
    '''
    (value, tb) = _parse_value_tb(exc, value, tb)
    te = TracebackException(type(value), value, tb, limit = limit, compact = True)
    return list(te.format(chain = chain))


def format_exception_only(exc, value = (_sentinel,)):
    """Format the exception part of a traceback.

    The return value is a list of strings, each ending in a newline.

    The list contains the exception's message, which is
    normally a single string; however, for :exc:`SyntaxError` exceptions, it
    contains several lines that (when printed) display detailed information
    about where the syntax error occurred. Following the message, the list
    contains the exception's ``__notes__``.
    """
    if value is _sentinel:
        value = exc
    te = TracebackException(type(value), value, None, compact = True)
    return list(te.format_exception_only())


def _format_final_exc_line(etype, value):
    valuestr = _safe_string(value, 'exception')
# WARNING: Decompyle incomplete


def _safe_string(value, what, func = (str,)):
    
    try:
        return func(value)
    except:
        return 



def print_exc(limit, file, chain = (None, None, True)):
    """Shorthand for 'print_exception(*sys.exc_info(), limit, file)'."""
    pass
# WARNING: Decompyle incomplete


def format_exc(limit, chain = (None, True)):
    '''Like print_exc() but return a string.'''
    pass
# WARNING: Decompyle incomplete


def print_last(limit, file, chain = (None, None, True)):
    """This is a shorthand for 'print_exception(sys.last_type,
    sys.last_value, sys.last_traceback, limit, file)'."""
    if not hasattr(sys, 'last_type'):
        raise ValueError('no last exception')
    print_exception(sys.last_type, sys.last_value, sys.last_traceback, limit, file, chain)


def print_stack(f, limit, file = (None, None, None)):
    """Print a stack trace from its invocation point.

    The optional 'f' argument can be used to specify an alternate
    stack frame at which to start. The optional 'limit' and 'file'
    arguments have the same meaning as for print_exception().
    """
    pass
# WARNING: Decompyle incomplete


def format_stack(f, limit = (None, None)):
    """Shorthand for 'format_list(extract_stack(f, limit))'."""
    pass
# WARNING: Decompyle incomplete


def extract_stack(f, limit = (None, None)):
    """Extract the raw traceback from the current stack frame.

    The return value has the same format as for extract_tb().  The
    optional 'f' and 'limit' arguments have the same meaning as for
    print_stack().  Each item in the list is a quadruple (filename,
    line number, function name, text), and the entries are in order
    from oldest to newest stack frame.
    """
    pass
# WARNING: Decompyle incomplete


def clear_frames(tb):
    '''Clear all references to local variables in the frames of a traceback.'''
    pass
# WARNING: Decompyle incomplete


class FrameSummary:
    '''Information about a single frame from a traceback.

    - :attr:`filename` The filename for the frame.
    - :attr:`lineno` The line within filename for the frame that was
      active when the frame was captured.
    - :attr:`name` The name of the function or method that was executing
      when the frame was captured.
    - :attr:`line` The text from the linecache module for the
      of code that was running when the frame was captured.
    - :attr:`locals` Either None if locals were not supplied, or a dict
      mapping the name to the repr() of the variable.
    '''
    __slots__ = ('filename', 'lineno', 'end_lineno', 'colno', 'end_colno', 'name', '_line', 'locals')
    
    def __init__(self, filename, lineno = None, name = {
        'lookup_line': True,
        'locals': None,
        'line': None,
        'end_lineno': None,
        'colno': None,
        'end_colno': None }, *, lookup_line, locals, line, end_lineno, colno, end_colno):
        '''Construct a FrameSummary.

        :param lookup_line: If True, `linecache` is consulted for the source
            code line. Otherwise, the line will be looked up when first needed.
        :param locals: If supplied the frame locals, which will be captured as
            object representations.
        :param line: If provided, use this instead of looking up the line in
            the linecache.
        '''
        self.filename = filename
        self.lineno = lineno
        self.name = name
        self._line = line
        if lookup_line:
            self.line
        self.locals = locals.items()() if locals else None
        self.end_lineno = end_lineno
        self.colno = colno
        self.end_colno = end_colno

    
    def __eq__(self, other):
