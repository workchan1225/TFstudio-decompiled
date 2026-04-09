# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: igor.pyc (Python 3.11)

'''
    pygments.styles.igor
    ~~~~~~~~~~~~~~~~~~~~

    Igor Pro default style.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String
__all__ = [
    'IgorStyle']

class IgorStyle(Style):
    '''
    Pygments version of the official colors for Igor Pro procedures.
    '''
    name = 'igor'
    styles = {
        String: '#009C00',
        Name.Class: '#007575',
        Name.Decorator: '#CC00A3',
        Name.Function: '#C34E00',
        Keyword: '#0000FF',
        Comment: 'italic #FF0000' }
