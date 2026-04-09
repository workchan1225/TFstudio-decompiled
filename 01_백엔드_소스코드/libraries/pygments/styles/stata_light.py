# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stata_light.pyc (Python 3.11)

"""
    pygments.styles.stata_light
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Light Style inspired by Stata's do-file editor. Note this is not
    meant to be a complete style, just for Stata's file formats.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Whitespace, Text
__all__ = [
    'StataLightStyle']

class StataLightStyle(Style):
    """
    Light mode style inspired by Stata's do-file editor. This is not
    meant to be a complete style, just for use with Stata.
    """
    name = 'stata-light'
    styles = {
        Name.Variable.Global: 'bold #b5565e',
        Name.Variable: 'bold #35baba',
        Comment: 'italic #008800',
        Keyword.Constant: '',
        Keyword: 'bold #353580',
        Name.Other: '#be646c',
        Name.Function: '#2c2cff',
        Operator: '',
        Number: '#2c2cff',
        String: '#7a2424',
        Error: 'bg:#e3d2d2 #a61717',
        Whitespace: '#bbbbbb',
        Text: '#111111' }
