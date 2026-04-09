# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: formatting.pyc (Python 3.11)

import typing as t
from contextlib import contextmanager
from gettext import gettext as _
from _compat import term_len
from parser import split_opt
FORCED_WIDTH: t.Optional[int] = None

def measure_table(rows = None):
    widths = { }
    for row in rows:
        for idx, col in enumerate(row):
            widths[idx] = max(widths.get(idx, 0), term_len(col))
            return (lambda .0: pass# WARNING: Decompyle incomplete
)(sorted(widths.items())())


def iter_rows(rows = None, col_count = None):
    pass
# WARNING: Decompyle incomplete


def wrap_text(text = None, width = None, initial_indent = None, subsequent_indent = (78, '', '', False), preserve_paragraphs = ('text', str, 'width', int, 'initial_indent', str, 'subsequent_indent', str, 'preserve_paragraphs', bool, 'return', str)):
    '''A helper function that intelligently wraps text.  By default, it
    assumes that it operates on a single paragraph of text but if the
    `preserve_paragraphs` parameter is provided it will intelligently
    handle paragraphs (defined by two empty lines).

    If paragraphs are handled, a paragraph can be prefixed with an empty
    line containing the ``\\b`` character (``\\x08``) to indicate that
    no rewrapping should happen in that block.

    :param text: the text that should be rewrapped.
    :param width: the maximum width for the text.
    :param initial_indent: the initial indent that should be placed on the
                           first line as a string.
    :param subsequent_indent: the indent string that should be placed on
                              each consecutive line.
    :param preserve_paragraphs: if this flag is set then the wrapping will
                                intelligently handle paragraphs.
    '''
    pass
# WARNING: Decompyle incomplete


class HelpFormatter:
    """This class helps with formatting text-based help pages.  It's
    usually just needed for very special internal cases, but it's also
    exposed so that developers can write their own fancy outputs.

    At present, it always writes into memory.

    :param indent_increment: the additional increment for each level.
    :param width: the width for the text.  This defaults to the terminal
                  width clamped to a maximum of 78.
    """
    
    def __init__(self = None, indent_increment = None, width = None, max_width = (2, None, None)):
        import shutil
        self.indent_increment = indent_increment
    # WARNING: Decompyle incomplete

    
    def write(self = None, string = None):
        '''Writes a unicode string into the internal buffer.'''
        self.buffer.append(string)

    
    def indent(self = None):
        '''Increases the indentation.'''
        pass

    
    def dedent(self = None):
        '''Decreases the indentation.'''
        pass

    
    def write_usage(self = None, prog = None, args = None, prefix = ('', None)):
        '''Writes a usage line into the buffer.

        :param prog: the program name.
        :param args: whitespace separated list of arguments.
        :param prefix: The prefix for the first line. Defaults to
            ``"Usage: "``.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def write_heading(self = None, heading = None):
        '''Writes a heading into the buffer.'''
        self.write(f'''{'':
