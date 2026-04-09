# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import annotations
import copy
import re
import sys
import typing
from functools import cached_property
from unicode import pyparsing_unicode as ppu
from util import _collapse_string_to_ranges, col, line, lineno, replaced_by_pep8

class _ExceptionWordUnicodeSet(ppu.Cyrillic, ppu.Greek, ppu.LatinB, ppu.LatinA, ppu.Latin1):
    pass

_extract_alphanums = _collapse_string_to_ranges(_ExceptionWordUnicodeSet.alphanums)
_exception_word_extractor = re.compile('([' + _extract_alphanums + ']{1,16})|.')

class ParseBaseException(Exception):
    args: 'tuple[str, int, typing.Optional[str]]' = 'base exception class for all parsing runtime exceptions'
    __slots__ = ('loc', 'msg', 'pstr', 'parser_element', 'args')
    
    def __init__(self = None, pstr = None, loc = None, msg = (0, None, None), elem = ('pstr', 'str', 'loc', 'int', 'msg', 'typing.Optional[str]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    explain_exception = (lambda exc = None, depth = None: import inspectParserElement = ParserElementimport core# WARNING: Decompyle incomplete
)()
    _from_exception = (lambda cls = None, pe = None: cls(pe.pstr, pe.loc, pe.msg, pe.parser_element))()
    line = (lambda self = None: line(self.loc, self.pstr))()
    lineno = (lambda self = None: lineno(self.loc, self.pstr))()
    col = (lambda self = None: col(self.loc, self.pstr))()
    column = (lambda self = None: col(self.loc, self.pstr))()
    found = (lambda self = None: if not self.pstr:
''if None.loc >= len(self.pstr):
'end of text'found_match = None.match(self.pstr, self.loc)# WARNING: Decompyle incomplete
)()
    parserElement = (lambda self: self.parser_element)()
    parserElement = (lambda self, elem: self.parser_element = elem)()
    
    def copy(self):
        return copy.copy(self)

    
    def formatted_message(self = None):
        '''
        Output the formatted exception message.
        Can be overridden to customize the message formatting or contents.

        .. versionadded:: 3.2.0
        '''
        found_phrase = f''', found {self.found}''' if self.found else ''
        return f'''{self.msg}{found_phrase}  (at char {self.loc}), (line:{self.lineno}, col:{self.column})'''

    
    def __str__(self = None):
        '''
        .. versionchanged:: 3.2.0
           Now uses :meth:`formatted_message` to format message.
        '''
        return self.formatted_message()

    
    def __repr__(self):
        return str(self)

    
    def mark_input_line(self = None, marker_string = None, *, markerString):
        '''
        Extracts the exception line from the input string, and marks
        the location of the exception with a special symbol.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def explain(self = None, depth = None):
        '''
        Method to translate the Python internal traceback into a list
        of the pyparsing expressions that caused the exception to be raised.

        Parameters:

        - depth (default=16) - number of levels back in the stack trace to list expression
          and function names; if None, the full stack trace names will be listed; if 0, only
          the failing input line, marker, and exception string will be shown

        Returns a multi-line string listing the ParserElements and/or function names in the
        exception\'s stack trace.

        Example:

        .. testcode::

            # an expression to parse 3 integers
            expr = pp.Word(pp.nums) * 3
            try:
                # a failing parse - the third integer is prefixed with "A"
                expr.parse_string("123 456 A789")
            except pp.ParseException as pe:
                print(pe.explain(depth=0))

        prints:

        .. testoutput::

            123 456 A789
                    ^
            ParseException: Expected W:(0-9), found \'A789\'  (at char 8), (line:1, col:9)

        Note: the diagnostic output will include string representations of the expressions
        that failed to parse. These representations will be more helpful if you use `set_name` to
        give identifiable names to your expressions. Otherwise they will use the default string
        forms, which may be cryptic to read.

        Note: pyparsing\'s default truncation of exception tracebacks may also truncate the
        stack of expressions that are displayed in the ``explain`` output. To get the full listing
        of parser expressions, you may have to set ``ParserElement.verbose_stacktrace = True``
        '''
        return self.explain_exception(self, depth)

    markInputline = replaced_by_pep8('markInputline', mark_input_line)


class ParseException(ParseBaseException):
    '''
    Exception thrown when a parse expression doesn\'t match the input string

    Example:

    .. testcode::

        integer = Word(nums).set_name("integer")
        try:
            integer.parse_string("ABC")
        except ParseException as pe:
            print(pe, f"column: {pe.column}")

    prints:

    .. testoutput::

       Expected integer, found \'ABC\'  (at char 0), (line:1, col:1) column: 1

    '''
    pass


class ParseFatalException(ParseBaseException):
    '''
    User-throwable exception thrown when inconsistent parse content
    is found; stops all parsing immediately
    '''
    pass


class ParseSyntaxException(ParseFatalException):
    """
    Just like :class:`ParseFatalException`, but thrown internally
    when an :class:`ErrorStop<And._ErrorStop>` ('-' operator) indicates
    that parsing is to stop immediately because an unbacktrackable
    syntax error has been found.
    """
    pass


class RecursiveGrammarException(Exception):
    '''
    .. deprecated:: 3.0.0
       Only used by the deprecated :meth:`ParserElement.validate`.

    Exception thrown by :class:`ParserElement.validate` if the
    grammar could be left-recursive; parser may need to enable
    left recursion using :class:`ParserElement.enable_left_recursion<ParserElement.enable_left_recursion>`
    '''
    
    def __init__(self = None, parseElementList = None):
        self.parseElementTrace = parseElementList

    
    def __str__(self = None):
        return f'''RecursiveGrammarException: {self.parseElementTrace}'''
