# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rrt.pyc (Python 3.11)

'''
    pygments.styles.rrt
    ~~~~~~~~~~~~~~~~~~~

    pygments "rrt" theme, based on Zap and Emacs defaults.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, String, Number, Operator
__all__ = [
    'RrtStyle']

class RrtStyle(Style):
    '''
    Minimalistic "rrt" theme, based on Zap and Emacs defaults.
    '''
    name = 'rrt'
    background_color = '#000000'
    highlight_color = '#0000ff'
    styles = {
        Number: '#ff00ff',
        Keyword.Type: '#ee82ee',
        String: '#87ceeb',
        Comment.Preproc: '#e5e5e5',
        Operator.Word: '#ff0000',
        Keyword: '#ff0000',
        Name.Constant: '#7fffd4',
        Name.Variable: '#eedd82',
        Name.Function: '#ffff00',
        Comment: '#00ff00',
        Token: '#dddddd' }
