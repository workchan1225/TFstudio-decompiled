# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lovelace.pyc (Python 3.11)

'''
    pygments.styles.lovelace
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lovelace by Miikka Salminen

    Pygments style by Miikka Salminen (https://github.com/miikkas)
    A desaturated, somewhat subdued style created for the Lovelace interactive
    learning environment.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Punctuation, Generic, Whitespace
__all__ = [
    'LovelaceStyle']

class LovelaceStyle(Style):
    __module__ = __name__
    __qualname__ = 'LovelaceStyle'
    __doc__ = '\n    The style used in Lovelace interactive learning environment. Tries to avoid\n    the "angry fruit salad" effect with desaturated and dim colours.\n    '
    name = 'lovelace'
    _KW_BLUE = '#2838b0'
    _NAME_GREEN = '#388038'
    _DOC_ORANGE = '#b85820'
    _OW_PURPLE = '#a848a8'
    _FUN_BROWN = '#785840'
    _STR_RED = '#b83838'
    _CLS_CYAN = '#287088'
    _ESCAPE_LIME = '#709030'
    _LABEL_CYAN = '#289870'
    _EXCEPT_YELLOW = '#908828'
# WARNING: Decompyle incomplete
