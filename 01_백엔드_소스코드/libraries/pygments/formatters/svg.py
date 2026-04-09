# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: svg.pyc (Python 3.11)

'''
    pygments.formatters.svg
    ~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for SVG output.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.formatter import Formatter
from pygments.token import Comment
from pygments.util import get_bool_opt, get_int_opt
__all__ = [
    'SvgFormatter']

def escape_html(text):
    '''Escape &, <, > as well as single and double quotes for HTML.'''
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')

class2style = { }

class SvgFormatter(Formatter):
    '''
    Format tokens as an SVG graphics file.  This formatter is still experimental.
    Each line of code is a ``<text>`` element with explicit ``x`` and ``y``
    coordinates containing ``<tspan>`` elements with the individual token styles.

    By default, this formatter outputs a full SVG document including doctype
    declaration and the ``<svg>`` root element.

    .. versionadded:: 0.9

    Additional options accepted:

    `nowrap`
        Don\'t wrap the SVG ``<text>`` elements in ``<svg><g>`` elements and
        don\'t add a XML declaration and a doctype.  If true, the `fontfamily`
        and `fontsize` options are ignored.  Defaults to ``False``.

    `fontfamily`
        The value to give the wrapping ``<g>`` element\'s ``font-family``
        attribute, defaults to ``"monospace"``.

    `fontsize`
        The value to give the wrapping ``<g>`` element\'s ``font-size``
        attribute, defaults to ``"14px"``.

    `linenos`
        If ``True``, add line numbers (default: ``False``).

    `linenostart`
        The line number for the first line (default: ``1``).

    `linenostep`
        If set to a number n > 1, only every nth line number is printed.

    `linenowidth`
        Maximum width devoted to line numbers (default: ``3*ystep``, sufficient
        for up to 4-digit line numbers. Increase width for longer code blocks).

    `xoffset`
        Starting offset in X direction, defaults to ``0``.

    `yoffset`
        Starting offset in Y direction, defaults to the font size if it is given
        in pixels, or ``20`` else.  (This is necessary since text coordinates
        refer to the text baseline, not the top edge.)

    `ystep`
        Offset to add to the Y coordinate for each subsequent line.  This should
        roughly be the text size plus 5.  It defaults to that value if the text
        size is given in pixels, or ``25`` else.

    `spacehack`
        Convert spaces in the source to ``&#160;``, which are non-breaking
        spaces.  SVG provides the ``xml:space`` attribute to control how
        whitespace inside tags is handled, in theory, the ``preserve`` value
        could be used to keep all whitespace as-is.  However, many current SVG
        viewers don\'t obey that rule, so this option is provided as a workaround
        and defaults to ``True``.
    '''
    name = 'SVG'
    aliases = [
        'svg']
    filenames = [
        '*.svg']
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def format_unencoded(self, tokensource, outfile):
        """
        Format ``tokensource``, an iterable of ``(tokentype, tokenstring)``
        tuples and write it into ``outfile``.

        For our implementation we put all lines in their own 'line group'.
        """
        x = self.xoffset
        y = self.yoffset
        if not self.nowrap:
            if self.encoding:
                outfile.write(f'''<?xml version="1.0" encoding="{self.encoding}"?>\n''')
            else:
                outfile.write('<?xml version="1.0"?>\n')
            outfile.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.0//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">\n')
            outfile.write('<svg xmlns="http://www.w3.org/2000/svg">\n')
            outfile.write(f'''<g font-family="{self.fontfamily}" font-size="{self.fontsize}">\n''')
        counter = self.linenostart
        counter_step = self.linenostep
        counter_style = self._get_style(Comment)
        line_x = x
        if self.linenos:
            if counter % counter_step == 0:
                outfile.write(f'''<text x="{x + self.linenowidth}" y="{y}" {counter_style} text-anchor="end">{counter}</text>''')
            line_x += self.linenowidth + self.ystep
            counter += 1
        outfile.write(f'''<text x="{line_x}" y="{y}" xml:space="preserve">''')
        for ttype, value in tokensource:
            style = self._get_style(ttype)
            if style:
                if not '<tspan' + style + '>':
                    tspan = ''
                    if tspan:
                        if not '</tspan>':
                            tspanend = ''
                            value = escape_html(value)
                            if self.spacehack:
                                value = value.expandtabs().replace(' ', '&#160;')
            parts = value.split('\n')
            for part in parts[:-1]:
                outfile.write(tspan + part + tspanend)
                y += self.ystep
                outfile.write('</text>\n')
                if self.linenos and counter % counter_step == 0:
                    outfile.write(f'''<text x="{x + self.linenowidth}" y="{y}" text-anchor="end" {counter_style}>{counter}</text>''')
                counter += 1
                outfile.write(f'''<text x="{line_x}" y="{y}" xml:space="preserve">''')
                outfile.write(tspan + parts[-1] + tspanend)
                outfile.write('</text>')
                if not self.nowrap:
                    outfile.write('</g></svg>\n')
                    return None
                return None

    
    def _get_style(self, tokentype):
        if tokentype in self._stylecache:
            return self._stylecache[tokentype]
        otokentype = None
    # WARNING: Decompyle incomplete
