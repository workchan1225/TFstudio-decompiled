# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rtf.pyc (Python 3.11)

'''
    pygments.formatters.rtf
    ~~~~~~~~~~~~~~~~~~~~~~~

    A formatter that generates RTF files.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from collections import OrderedDict
from pygments.formatter import Formatter
from pygments.style import _ansimap
from pygments.util import get_bool_opt, get_int_opt, get_list_opt, surrogatepair
__all__ = [
    'RtfFormatter']

class RtfFormatter(Formatter):
    """
    Format tokens as RTF markup. This formatter automatically outputs full RTF
    documents with color information and other useful stuff. Perfect for Copy and
    Paste into Microsoft(R) Word(R) documents.

    Please note that ``encoding`` and ``outencoding`` options are ignored.
    The RTF format is ASCII natively, but handles unicode characters correctly
    thanks to escape sequences.

    .. versionadded:: 0.6

    Additional options accepted:

    `style`
        The style to use, can be a string or a Style subclass (default:
        ``'default'``).

    `fontface`
        The used font family, for example ``Bitstream Vera Sans``. Defaults to
        some generic font which is supposed to have fixed width.

    `fontsize`
        Size of the font used. Size is specified in half points. The
        default is 24 half-points, giving a size 12 font.

        .. versionadded:: 2.0

    `linenos`
        Turn on line numbering (default: ``False``).

        .. versionadded:: 2.18

    `lineno_fontsize`
        Font size for line numbers. Size is specified in half points
        (default: `fontsize`). 

        .. versionadded:: 2.18

    `lineno_padding`
        Number of spaces between the (inline) line numbers and the
        source code (default: ``2``).

        .. versionadded:: 2.18

    `linenostart`
        The line number for the first line (default: ``1``).

        .. versionadded:: 2.18

    `linenostep`
        If set to a number n > 1, only every nth line number is printed.

        .. versionadded:: 2.18

    `lineno_color`
        Color for line numbers specified as a hex triplet, e.g. ``'5e5e5e'``. 
        Defaults to the style's line number color if it is a hex triplet, 
        otherwise ansi bright black.

        .. versionadded:: 2.18

    `hl_lines`
        Specify a list of lines to be highlighted, as line numbers separated by
        spaces, e.g. ``'3 7 8'``. The line numbers are relative to the input 
        (i.e. the first line is line 1) unless `hl_linenostart` is set.

        .. versionadded:: 2.18

    `hl_color`
        Color for highlighting the lines specified in `hl_lines`, specified as 
        a hex triplet (default: style's `highlight_color`).

        .. versionadded:: 2.18

    `hl_linenostart`
        If set to ``True`` line numbers in `hl_lines` are specified
        relative to `linenostart` (default ``False``).

        .. versionadded:: 2.18
    """
    name = 'RTF'
    aliases = [
        'rtf']
    filenames = [
        '*.rtf']
    
    def __init__(self, **options):
        '''
        Additional options accepted:

        ``fontface``
            Name of the font used. Could for example be ``\'Courier New\'``
            to further specify the default which is ``\'\\fmodern\'``. The RTF
            specification claims that ``\\fmodern`` are "Fixed-pitch serif
            and sans serif fonts". Hope every RTF implementation thinks
            the same about modern...

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _escape(self, text):
        return text.replace('\\', '\\\\').replace('{', '\\{').replace('}', '\\}')

    
    def _escape_text(self, text):
        if not text:
            return ''
        text = None._escape(text)
        buf = []
        for c in text:
            cn = ord(c)
            if cn < 128:
                buf.append(str(c))
                continue
            if  <= 128, cn or 128, cn < 65536:
                pass
            
        buf.append('{\\u%d}' % cn)
        continue
        if 65536 <= cn:
            buf.append('{\\u%d}{\\u%d}' % surrogatepair(cn))
        continue
        return ''.join(buf).replace('\n', '\\par')

    hex_to_rtf_color = (lambda hex_color: if hex_color[0] == '#':
hex_color = hex_color[1:]'\\red%d\\green%d\\blue%d;' % (int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)))()
    
    def _split_tokens_on_newlines(self, tokensource):
        '''
        Split tokens containing newline characters into multiple token
        each representing a line of the input file. Needed for numbering
        lines of e.g. multiline comments.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _create_color_mapping(self):
        '''
        Create a mapping of style hex colors to index/offset in
        the RTF color table.
        '''
        color_mapping = OrderedDict()
        offset = 1
        if self.linenos:
            color_mapping[self.lineno_color] = offset
            offset += 1
        if self.hl_lines:
            color_mapping[self.hl_color] = offset
            offset += 1
        for _, style in self.style:
            for color in (style['color'], style['bgcolor'], style['border']):
                if color and color not in color_mapping:
                    color_mapping[color] = offset
                    offset += 1
                return color_mapping

    _lineno_template = (lambda self: if self.lineno_fontsize != self.fontsize:
'{{\\fs{} \\cf{} %s{}}}'.format(self.lineno_fontsize, self.color_mapping[self.lineno_color], ' ' * self.lineno_padding)None.format(self.color_mapping[self.lineno_color], ' ' * self.lineno_padding))()
    _hl_open_str = (lambda self: f'''{{\\highlight{self.color_mapping[self.hl_color]} ''')()
    _rtf_header = (lambda self: lines = []if self.fontface:
if not ' ' + self._escape(self.fontface):
lines.append('{\\rtf1\\ansi\\uc0\\deff0{\\fonttbl{\\f0\\fmodern\\fprq1\\fcharset0%s;}}' % '')lines.append('{\\colortbl;')for color, _ in self.color_mapping.items():
lines.append(self.hex_to_rtf_color(color))lines.append('}')lines.append('\\f0\\sa0')if self.fontsize:
lines.append('\\fs%d' % self.fontsize)lines.append('\\dntblnsbdb')lines)()
    
    def format_unencoded(self, tokensource, outfile):
        pass
    # WARNING: Decompyle incomplete
