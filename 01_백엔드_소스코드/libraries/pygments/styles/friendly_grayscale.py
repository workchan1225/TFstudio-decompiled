# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: friendly_grayscale.pyc (Python 3.11)

'''
    pygments.styles.friendly_grayscale
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A style based on friendly style.
    The color values of the friendly style have been converted to grayscale
    using the luminosity value calculated by
    http://www.workwithcolor.com/color-converter-01.htm

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Whitespace
__all__ = [
    'FriendlyGrayscaleStyle']

class FriendlyGrayscaleStyle(Style):
    __module__ = __name__
    __qualname__ = 'FriendlyGrayscaleStyle'
    __doc__ = '\n    A modern grayscale style based on the friendly style.\n\n    .. versionadded:: 2.11\n    '
    name = 'friendly_grayscale'
    background_color = '#f0f0f0'
# WARNING: Decompyle incomplete
