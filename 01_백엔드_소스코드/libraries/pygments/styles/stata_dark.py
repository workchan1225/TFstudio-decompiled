# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stata_dark.pyc (Python 3.11)

"""
    pygments.styles.stata_dark
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Dark style inspired by Stata's do-file editor. Note this is not
    meant to be a complete style, just for Stata's file formats.


    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
from pygments.style import Style
from pygments.token import Token, Keyword, Name, Comment, String, Error, Number, Operator, Whitespace, Generic
__all__ = [
    'StataDarkStyle']

class StataDarkStyle(Style):
    name = 'stata-dark'
    background_color = '#232629'
    highlight_color = '#49483e'
    styles = {
        Generic.Prompt: '#ffffff',
        Name.Variable.Global: 'bold #BE646C',
        Name.Variable: 'bold #7AB4DB',
        Comment: 'italic #777777',
        Keyword.Constant: '',
        Keyword: 'bold #7686bb',
        Name.Other: '#e2828e',
        Name.Function: '#6a6aff',
        Operator: '',
        Number: '#4FB8CC',
        String: '#51cc99',
        Error: 'bg:#e3d2d2 #a61717',
        Whitespace: '#bbbbbb',
        Token: '#cccccc' }
