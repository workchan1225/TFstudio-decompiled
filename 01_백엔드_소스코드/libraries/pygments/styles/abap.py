# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abap.pyc (Python 3.11)

'''
    pygments.styles.abap
    ~~~~~~~~~~~~~~~~~~~~

    ABAP workbench like style.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator
__all__ = [
    'AbapStyle']

class AbapStyle(Style):
    name = 'abap'
    styles = {
        Error: '#F00',
        String: '#5a2',
        Number: '#3af',
        Name: '#000',
        Operator.Word: '#00f',
        Keyword: '#00f',
        Comment.Special: '#888',
        Comment: 'italic #888' }
