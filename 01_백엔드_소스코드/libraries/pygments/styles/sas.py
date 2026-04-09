# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sas.pyc (Python 3.11)

"""
    pygments.styles.sas
    ~~~~~~~~~~~~~~~~~~~

    Style inspired by SAS' enhanced program editor. Note This is not
    meant to be a complete style. It's merely meant to mimic SAS'
    program editor syntax highlighting.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Other, Whitespace, Generic
__all__ = [
    'SasStyle']

class SasStyle(Style):
    """
    Style inspired by SAS' enhanced program editor. Note This is not
    meant to be a complete style. It's merely meant to mimic SAS'
    program editor syntax highlighting.
    """
    name = 'sas'
    styles = {
        Error: 'bg:#e3d2d2 #a61717',
        Generic.Error: '#d30202',
        Generic.Emph: '#008800',
        Generic: '#2c2cff',
        Name.Variable: 'bold #2c2cff',
        Name.Function: 'bold italic',
        Name.Builtin: '#2c2cff',
        Keyword.Constant: 'bold',
        Keyword.Reserved: 'bold #353580',
        Keyword: '#2c2cff',
        Other: 'bg:#ffffe0',
        Number: 'bold #2c8553',
        String: '#800080',
        Comment: 'italic #008800',
        Whitespace: '#bbbbbb' }
