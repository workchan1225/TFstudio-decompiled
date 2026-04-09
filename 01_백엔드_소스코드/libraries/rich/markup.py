# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: markup.pyc (Python 3.11)

import re
from ast import literal_eval
from operator import attrgetter
from typing import Callable, Iterable, List, Match, NamedTuple, Optional, Tuple, Union
from _emoji_replace import _emoji_replace
from emoji import EmojiVariant
from errors import MarkupError
from style import Style
from text import Span, Text
RE_TAGS = re.compile('((\\\\*)\\[([a-z#/@][^[]*?)])', re.VERBOSE)
RE_HANDLER = re.compile('^([\\w.]*?)(\\(.*?\\))?$')

class Tag(NamedTuple):
    parameters: Optional[str] = 'A tag in console markup.'
    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete

    markup = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

_ReStringMatch = Match[str]
_ReSubCallable = Callable[([
    _ReStringMatch], str)]
_EscapeSubMethod = Callable[([
    _ReSubCallable,
    str], str)]

def escape(markup = None, _escape = None):
    """Escapes text so that it won't be interpreted as markup.

    Args:
        markup (str): Content to be inserted in to markup.

    Returns:
        str: Markup with square brackets escaped.
    """
    
    def escape_backslashes(match = None):
        '''Called by re.sub replace matches.'''
        (backslashes, text) = match.groups()
        return f'''{backslashes}{backslashes}\\{text}'''

    markup = _escape(escape_backslashes, markup)
    if not markup.endswith('\\') and markup.endswith('\\\\'):
        return markup + '\\'


def _parse(markup = None):
    '''Parse markup in to an iterable of tuples of (position, text, tag).

    Args:
        markup (str): A string containing console markup

    '''
    pass
# WARNING: Decompyle incomplete


def render(markup = None, style = None, emoji = None, emoji_variant = ('', True, None)):
    '''Render console markup in to a Text instance.

    Args:
        markup (str): A string containing console markup.
        style: (Union[str, Style]): The style to use.
        emoji (bool, optional): Also render emoji code. Defaults to True.
        emoji_variant (str, optional): Optional emoji variant, either "text" or "emoji". Defaults to None.


    Raises:
        MarkupError: If there is a syntax error in the markup.

    Returns:
        Text: A test instance.
    '''
    pass
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    MARKUP = [
        '[red]Hello World[/red]',
        '[magenta]Hello [b]World[/b]',
        '[bold]Bold[italic] bold and italic [/bold]italic[/italic]',
        'Click [link=https://www.willmcgugan.com]here[/link] to visit my Blog',
        ':warning-emoji: [bold red blink] DANGER![/]']
    from rich import print
    from rich.table import Table
    grid = Table('Markup', 'Result', padding = (0, 1))
    for markup in MARKUP:
        grid.add_row(Text(markup), markup)
        print(grid)
        return None
        return None
