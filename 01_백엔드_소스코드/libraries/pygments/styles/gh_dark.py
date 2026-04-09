# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gh_dark.pyc (Python 3.11)

"""
    pygments.styles.gh_dark
    ~~~~~~~~~~~~~~~~~~~~~~~

    Github's Dark-Colorscheme based theme for Pygments
    Colors extracted from https://github.com/primer/primitives

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, Error, Number, Operator, Generic, Text, Literal, String, Token
__all__ = [
    'GhDarkStyle']
RED_2 = '#ffa198'
RED_3 = '#ff7b72'
RED_9 = '#490202'
ORANGE_2 = '#ffa657'
ORANGE_3 = '#f0883e'
GREEN_1 = '#7ee787'
GREEN_2 = '#56d364'
GREEN_7 = '#0f5323'
BLUE_1 = '#a5d6ff'
BLUE_2 = '#79c0ff'
PURPLE_2 = '#d2a8ff'
GRAY_3 = '#8b949e'
GRAY_4 = '#6e7681'
FG_SUBTLE = '#6e7681'
FG_DEFAULT = '#e6edf3'
BG_DEFAULT = '#0d1117'
DANGER_FG = '#f85149'

class GhDarkStyle(Style):
    __module__ = __name__
    __qualname__ = 'GhDarkStyle'
    __doc__ = "\n    Github's Dark-Colorscheme based theme for Pygments\n    "
    name = 'github-dark'
    background_color = BG_DEFAULT
    highlight_color = GRAY_4
    line_number_special_color = FG_DEFAULT
    line_number_special_background_color = FG_SUBTLE
    line_number_color = GRAY_4
    line_number_background_color = BG_DEFAULT
# WARNING: Decompyle incomplete
