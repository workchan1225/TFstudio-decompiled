# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parsing.pyc (Python 3.11)

'''
:func:`~pandas.eval` source string parsing functions
'''
from __future__ import annotations
from enum import Enum
from io import StringIO
from keyword import iskeyword
import token
import tokenize
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Hashable, Iterator
BACKTICK_QUOTED_STRING = 100

def create_valid_python_identifier(name = None):
    '''
    Create valid Python identifiers from any string.

    Check if name contains any special characters. If it contains any
    special characters, the special characters will be replaced by
    a special string and a prefix is added.

    Raises
    ------
    SyntaxError
        If the returned name is not a Python valid identifier, raise an exception.
    '''
    pass
# WARNING: Decompyle incomplete


def clean_backtick_quoted_toks(tok = None):
    '''
    Clean up a column name if surrounded by backticks.

    Backtick quoted string are indicated by a certain tokval value. If a string
    is a backtick quoted token it will processed by
    :func:`_create_valid_python_identifier` so that the parser can find this
    string when the query is executed.
    In this case the tok will get the NAME tokval.

    Parameters
    ----------
    tok : tuple of int, str
        ints correspond to the all caps constants in the tokenize module

    Returns
    -------
    tok : Tuple[int, str]
        Either the input or token or the replacement values
    '''
    (toknum, tokval) = tok
    if toknum == BACKTICK_QUOTED_STRING:
        return (tokenize.NAME, create_valid_python_identifier(tokval))
    return (None, tokval)


def clean_column_name(name = None):
    '''
    Function to emulate the cleaning of a backtick quoted name.

    The purpose for this function is to see what happens to the name of
    identifier if it goes to the process of being parsed a Python code
    inside a backtick quoted string and than being cleaned
    (removed of any special characters).

    Parameters
    ----------
    name : hashable
        Name to be cleaned.

    Returns
    -------
    name : hashable
        Returns the name after tokenizing and cleaning.
    '''
    
    try:
        name = name.replace('`', '``') if isinstance(name, str) else name
        tokenized = tokenize_string(f'''`{name}`''')
        tokval = next(tokenized)[1]
        return create_valid_python_identifier(tokval)
    except SyntaxError:
        return 



class ParseState(Enum):
    DEFAULT = 0
    IN_BACKTICK = 1
    IN_SINGLE_QUOTE = 2
    IN_DOUBLE_QUOTE = 3


def _split_by_backtick(s = None):
    '''
    Splits a str into substrings along backtick characters (`).

    Disregards backticks inside quotes.

    Parameters
    ----------
    s : str
        The Python source code string.

    Returns
    -------
    substrings: list[tuple[bool, str]]
        List of tuples, where each tuple has two elements:
        The first is a boolean indicating if the substring is backtick-quoted.
        The second is the actual substring.
    '''
    substrings = []
    substr = []
    i = 0
    parse_state = ParseState.DEFAULT
# WARNING: Decompyle incomplete


def tokenize_string(source = None):
    '''
    Tokenize a Python source code string.

    Parameters
    ----------
    source : str
        The Python source code string.

    Returns
    -------
    tok_generator : Iterator[Tuple[int, str]]
        An iterator yielding all tokens with only toknum and tokval (Tuple[ing, str]).
    '''
    pass
# WARNING: Decompyle incomplete
