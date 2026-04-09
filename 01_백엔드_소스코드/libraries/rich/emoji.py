# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: emoji.pyc (Python 3.11)

import sys
from typing import TYPE_CHECKING, Optional, Union, Literal
from jupyter import JupyterMixin
from segment import Segment
from style import Style
from _emoji_codes import EMOJI
from _emoji_replace import _emoji_replace
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderResult
EmojiVariant = Literal[('emoji', 'text')]

class NoEmoji(Exception):
    '''No emoji by that name.'''
    pass


class Emoji(JupyterMixin):
    __slots__ = [
        'name',
        'style',
        '_char',
        'variant']
    VARIANTS = {
        'text': '︎',
        'emoji': '️' }
    
    def __init__(self = None, name = None, style = None, variant = ('none', None)):
        """A single emoji character.

        Args:
            name (str): Name of emoji.
            style (Union[str, Style], optional): Optional style. Defaults to None.

        Raises:
            NoEmoji: If the emoji doesn't exist.
        """
        self.name = name
        self.style = style
        self.variant = variant
        
        try:
            self._char = EMOJI[name]
        except KeyError:
            raise NoEmoji(f'''No emoji called {name!r}''')

    # WARNING: Decompyle incomplete

    replace = (lambda cls = None, text = None: _emoji_replace(text))()
    
    def __repr__(self = None):
        return f'''<emoji {self.name!r}>'''

    
    def __str__(self = None):
        return self._char

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete


if __name__ == '__main__':
    import sys
    from rich.columns import Columns
    from rich.console import Console
    console = Console(record = True)
    columns = (lambda .0: pass# WARNING: Decompyle incomplete
)(sorted(EMOJI.keys())(), column_first = True)
    console.print(columns)
    if len(sys.argv) > 1:
        console.save_html(sys.argv[1])
        return None
    return Columns
