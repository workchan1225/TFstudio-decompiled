# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lightbulb.pyc (Python 3.11)

'''
    pygments.styles.lightbulb
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A minimal dark theme based on the Lightbulb theme for VSCode.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.style import Style
from pygments.token import Comment, Error, Generic, Keyword, Literal, Name, Number, Operator, Punctuation, String, Token
__all__ = [
    'LightbulbStyle']
COLORS = {
    'bg': '#1d2331',
    'blue_1': '#73D0FF',
    'gray_1': '#7e8aa1',
    'gray_2': '#3c4354',
    'gray_3': '#6e7681',
    'red_1': '#f88f7f',
    'red_2': '#3d1e20',
    'orange_1': '#FFAD66',
    'orange_2': '#F29E74',
    'yellow_1': '#FFD173',
    'white': '#d4d2c8',
    'magenta_1': '#DFBFFF',
    'green_1': '#D5FF80',
    'green_2': '#19362c',
    'cyan_1': '#95E6CB' }

class LightbulbStyle(Style):
    __module__ = __name__
    __qualname__ = 'LightbulbStyle'
    __doc__ = '\n    A minimal dark theme based on the Lightbulb theme for VSCode.\n    '
    name = 'lightbulb'
    background_color = COLORS['bg']
    highlight_color = COLORS['gray_3']
    line_number_color = COLORS['gray_2']
    line_number_special_color = COLORS['gray_2']
# WARNING: Decompyle incomplete
