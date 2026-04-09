# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pangomarkup.pyc (Python 3.11)

'''
    pygments.formatters.pangomarkup
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for Pango markup output.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.formatter import Formatter
__all__ = [
    'PangoMarkupFormatter']
_escape_table = {
    ord('<'): '&lt;',
    ord('&'): '&amp;' }

def escape_special_chars(text, table = (_escape_table,)):
    '''Escape & and < for Pango Markup.'''
    return text.translate(table)


class PangoMarkupFormatter(Formatter):
    '''
    Format tokens as Pango Markup code. It can then be rendered to an SVG.

    .. versionadded:: 2.9
    '''
    name = 'Pango Markup'
    aliases = [
        'pango',
        'pangomarkup']
    filenames = []
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def format_unencoded(self, tokensource, outfile):
        lastval = ''
        lasttype = None
        outfile.write('<tt>')
    # WARNING: Decompyle incomplete
