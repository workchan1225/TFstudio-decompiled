# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: groff.pyc (Python 3.11)

'''
    pygments.formatters.groff
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for groff output.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import math
from pygments.formatter import Formatter
from pygments.util import get_bool_opt, get_int_opt
__all__ = [
    'GroffFormatter']

class GroffFormatter(Formatter):
    """
    Format tokens with groff escapes to change their color and font style.

    .. versionadded:: 2.11

    Additional options accepted:

    `style`
        The style to use, can be a string or a Style subclass (default:
        ``'default'``).

    `monospaced`
        If set to true, monospace font will be used (default: ``true``).

    `linenos`
        If set to true, print the line numbers (default: ``false``).

    `wrap`
        Wrap lines to the specified number of characters. Disabled if set to 0
        (default: ``0``).
    """
    name = 'groff'
    aliases = [
        'groff',
        'troff',
        'roff']
    filenames = []
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def _make_styles(self):
        regular = '\\f[CR]' if self.monospaced else '\\f[R]'
        bold = '\\f[CB]' if self.monospaced else '\\f[B]'
        italic = '\\f[CI]' if self.monospaced else '\\f[I]'
        for ttype, ndef in self.style:
            start = ''
            end = ''
            if ndef['color']:
                start += '\\m[{}]'.format(ndef['color'])
                end = '\\m[]' + end
            if ndef['bold']:
                start += bold
                end = regular + end
            if ndef['italic']:
                start += italic
                end = regular + end
            if ndef['bgcolor']:
                start += '\\M[{}]'.format(ndef['bgcolor'])
                end = '\\M[]' + end
            self.styles[ttype] = (start, end)
            return None

    
    def _define_colors(self, outfile):
        colors = set()
    # WARNING: Decompyle incomplete

    
    def _write_lineno(self, outfile):
