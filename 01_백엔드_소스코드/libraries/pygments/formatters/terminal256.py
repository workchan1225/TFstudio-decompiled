# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: terminal256.pyc (Python 3.11)

'''
    pygments.formatters.terminal256
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for 256-color terminal output with ANSI sequences.

    RGB-to-XTERM color conversion routines adapted from xterm256-conv
    tool (http://frexx.de/xterm-256-notes/data/xterm256-conv2.tar.bz2)
    by Wolfgang Frisch.

    Formatter version 1.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.formatter import Formatter
from pygments.console import codes
from pygments.style import ansicolors
__all__ = [
    'Terminal256Formatter',
    'TerminalTrueColorFormatter']

class EscapeSequence:
    
    def __init__(self, fg, bg, bold, underline, italic = (None, None, False, False, False)):
        self.fg = fg
        self.bg = bg
        self.bold = bold
        self.underline = underline
        self.italic = italic

    
    def escape(self, attrs):
        if len(attrs):
            return '\x1b[' + ';'.join(attrs) + 'm'

    
    def color_string(self):
        attrs = []
    # WARNING: Decompyle incomplete

    
    def true_color_string(self):
        attrs = []
        if self.fg:
            attrs.extend(('38', '2', str(self.fg[0]), str(self.fg[1]), str(self.fg[2])))
        if self.bg:
            attrs.extend(('48', '2', str(self.bg[0]), str(self.bg[1]), str(self.bg[2])))
        if self.bold:
            attrs.append('01')
        if self.underline:
            attrs.append('04')
        if self.italic:
            attrs.append('03')
        return self.escape(attrs)

    
    def reset_string(self):
        attrs = []
    # WARNING: Decompyle incomplete



class Terminal256Formatter(Formatter):
    """
    Format tokens with ANSI color sequences, for output in a 256-color
    terminal or console.  Like in `TerminalFormatter` color sequences
    are terminated at newlines, so that paging the output works correctly.

    The formatter takes colors from a style defined by the `style` option
    and converts them to nearest ANSI 256-color escape sequences. Bold and
    underline attributes from the style are preserved (and displayed).

    .. versionadded:: 0.9

    .. versionchanged:: 2.2
       If the used style defines foreground colors in the form ``#ansi*``, then
       `Terminal256Formatter` will map these to non extended foreground color.
       See :ref:`AnsiTerminalStyle` for more information.

    .. versionchanged:: 2.4
       The ANSI color names have been updated with names that are easier to
       understand and align with colornames of other projects and terminals.
       See :ref:`this table <new-ansi-color-names>` for more information.


    Options accepted:

    `style`
        The style to use, can be a string or a Style subclass (default:
        ``'default'``).

    `linenos`
        Set to ``True`` to have line numbers on the terminal output as well
        (default: ``False`` = no line numbers).
    """
    name = 'Terminal256'
    aliases = [
        'terminal256',
        'console256',
        '256']
    filenames = []
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def _build_color_table(self):
        self.xterm_colors.append((0, 0, 0))
        self.xterm_colors.append((205, 0, 0))
        self.xterm_colors.append((0, 205, 0))
        self.xterm_colors.append((205, 205, 0))
        self.xterm_colors.append((0, 0, 238))
        self.xterm_colors.append((205, 0, 205))
        self.xterm_colors.append((0, 205, 205))
        self.xterm_colors.append((229, 229, 229))
        self.xterm_colors.append((127, 127, 127))
        self.xterm_colors.append((255, 0, 0))
        self.xterm_colors.append((0, 255, 0))
        self.xterm_colors.append((255, 255, 0))
        self.xterm_colors.append((92, 92, 255))
        self.xterm_colors.append((255, 0, 255))
        self.xterm_colors.append((0, 255, 255))
        self.xterm_colors.append((255, 255, 255))
        valuerange = (0, 95, 135, 175, 215, 255)
        for i in range(217):
            r = valuerange[i // 36 % 6]
            g = valuerange[i // 6 % 6]
            b = valuerange[i % 6]
            self.xterm_colors.append((r, g, b))
            for i in range(1, 22):
                v = 8 + i * 10
                self.xterm_colors.append((v, v, v))
                return None

    
    def _closest_color(self, r, g, b):
        distance = 198147
        match = 0
        for i in range(0, 254):
            values = self.xterm_colors[i]
            rd = r - values[0]
            gd = g - values[1]
            bd = b - values[2]
            d = rd * rd + gd * gd + bd * bd
            if d < distance:
                match = i
                distance = d
            return match

    
    def _color_index(self, color):
        index = self.best_match.get(color, None)
        if color in ansicolors:
            index = color
            self.best_match[color] = index
    # WARNING: Decompyle incomplete

    
    def _setup_styles(self):
        for ttype, ndef in self.style:
            escape = EscapeSequence()
            if ndef['ansicolor']:
                escape.fg = self._color_index(ndef['ansicolor'])
            elif ndef['color']:
                escape.fg = self._color_index(ndef['color'])
            if ndef['bgansicolor']:
                escape.bg = self._color_index(ndef['bgansicolor'])
            elif ndef['bgcolor']:
                escape.bg = self._color_index(ndef['bgcolor'])
            if self.usebold and ndef['bold']:
                escape.bold = True
            if self.useunderline and ndef['underline']:
                escape.underline = True
            if self.useitalic and ndef['italic']:
                escape.italic = True
            self.style_string[str(ttype)] = (escape.color_string(), escape.reset_string())
            return None

    
    def _write_lineno(self, outfile):
