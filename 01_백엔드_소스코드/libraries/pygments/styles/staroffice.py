# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: staroffice.pyc (Python 3.11)

'''
    pygments.styles.staroffice
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Style similar to StarOffice style, also in OpenOffice and LibreOffice.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.style import Style
from pygments.token import Comment, Error, Literal, Name, Token
__all__ = [
    'StarofficeStyle']

class StarofficeStyle(Style):
    '''
    Style similar to StarOffice style, also in OpenOffice and LibreOffice.
    '''
    name = 'staroffice'
    styles = {
        Name: '#008000',
        Literal: '#EE0000',
        Error: '#800000',
        Comment: '#696969',
        Token: '#000080' }
