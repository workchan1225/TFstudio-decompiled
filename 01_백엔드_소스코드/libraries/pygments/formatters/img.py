# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: img.pyc (Python 3.11)

'''
    pygments.formatters.img
    ~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for Pixmap output.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import os
import sys
from pygments.formatter import Formatter
from pygments.util import get_bool_opt, get_int_opt, get_list_opt, get_choice_opt
import subprocess

try:
    from PIL import Image, ImageDraw, ImageFont
    pil_available = True
except ImportError:
    pil_available = False


try:
    import _winreg
except ImportError:
    import winreg as _winreg
except ImportError:
    _winreg = None

__all__ = [
    'ImageFormatter',
    'GifImageFormatter',
    'JpgImageFormatter',
    'BmpImageFormatter']
STYLES = {
    'NORMAL': [
        '',
        'Roman',
        'Book',
        'Normal',
        'Regular',
        'Medium'],
    'ITALIC': [
        'Oblique',
        'Italic'],
    'BOLD': [
        'Bold'],
    'BOLDITALIC': [
        'Bold Oblique',
        'Bold Italic'] }
DEFAULT_FONT_NAME_NIX = 'DejaVu Sans Mono'
DEFAULT_FONT_NAME_WIN = 'Courier New'
DEFAULT_FONT_NAME_MAC = 'Menlo'

class PilNotAvailable(ImportError):
    '''When Python imaging library is not available'''
    pass


class FontNotFound(Exception):
    '''When there are no usable fonts specified'''
    pass


class FontManager:
    '''
    Manages a set of fonts: normal, italic, bold, etc...
    '''
    
    def __init__(self, font_name, font_size = (14,)):
        self.font_name = font_name
        self.font_size = font_size
        self.fonts = { }
        self.encoding = None
        self.variable = False
        if hasattr(font_name, 'read') or os.path.isfile(font_name):
            font = ImageFont.truetype(font_name, self.font_size)
            self.variable = True
            for style in STYLES:
                self.fonts[style] = font
                return None
                if sys.platform.startswith('win'):
                    if not font_name:
                        self.font_name = DEFAULT_FONT_NAME_WIN
                    self._create_win()
                    return None
                if None.platform.startswith('darwin'):
                    if not font_name:
                        self.font_name = DEFAULT_FONT_NAME_MAC
                    self._create_mac()
                    return None
                if not None:
                    self.font_name = DEFAULT_FONT_NAME_NIX
        self._create_nix()

    
    def _get_nix_font_path(self, name, style):
        proc = subprocess.Popen([
            'fc-list',
            f'''{name}:style={style}''',
            'file'], stdout = subprocess.PIPE, stderr = None)
        (stdout, _) = proc.communicate()
        if proc.returncode == 0:
            lines = stdout.splitlines()
            for line in lines:
                if line.startswith(b'Fontconfig warning:'):
                    continue
                path = line.decode().strip().strip(':')
                if path:
                    
                    return None, path
                return None
                return None

    
    def _create_nix(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_mac_font_path(self, font_map, name, style):
        return font_map.get((name + ' ' + style).strip().lower())

    
    def _create_mac(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _lookup_win(self, key, basename, styles, fail = (False,)):
        for suffix in ('', ' (TrueType)'):
            for style in styles:
                if style:
                    valname = '{}{}{}'.format(basename, ' ' + style, suffix)
                    (val, _) = _winreg.QueryValueEx(key, valname)
                    
                    
                    return None, None, val
                except OSError:
                    basename
                    continue
                if fail:
                    raise FontNotFound(f'''Font {basename} ({styles[0]}) not found in registry''')
                return None

    
    def _create_win(self):
        lookuperror = None
        keynames = [
            (_winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\Fonts'),
            (_winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Fonts'),
            (_winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\Fonts'),
            (_winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\Windows\\CurrentVersion\\Fonts')]
    # WARNING: Decompyle incomplete

    
    def get_char_size(self):
        '''
        Get the character size.
        '''
        return self.get_text_size('M')

    
    def get_text_size(self, text):
        '''
        Get the text size (width, height).
        '''
        font = self.fonts['NORMAL']
        if hasattr(font, 'getbbox'):
            return font.getbbox(text)[2:4]
        return None.getsize(text)

    
    def get_font(self, bold, oblique):
        '''
        Get the font based on bold and italic flags.
        '''
        if bold and oblique:
            if self.variable:
                return self.get_style('BOLDITALIC')
            return None.fonts['BOLDITALIC']
        if None:
            if self.variable:
                return self.get_style('BOLD')
            return None.fonts['BOLD']
        if None:
            if self.variable:
                return self.get_style('ITALIC')
            return None.fonts['ITALIC']
        if None.variable:
            return self.get_style('NORMAL')
        return None.fonts['NORMAL']

    
    def get_style(self, style):
        '''
        Get the specified style of the font if it is a variable font.
        If not found, return the normal font.
        '''
        font = self.fonts[style]
        for style_name in STYLES[style]:
            font.set_variation_by_name(style_name)
            
            return None, font
            except ValueError:
                continue
            except OSError:
                
                return None, font, 
            return font



class ImageFormatter(Formatter):
    '''
    Create a PNG image from source code. This uses the Python Imaging Library to
    generate a pixmap from the source code.

    .. versionadded:: 0.10

    Additional options accepted:

    `image_format`
        An image format to output to that is recognised by PIL, these include:

        * "PNG" (default)
        * "JPEG"
        * "BMP"
        * "GIF"

    `line_pad`
        The extra spacing (in pixels) between each line of text.

        Default: 2

    `font_name`
        The font name to be used as the base font from which others, such as
        bold and italic fonts will be generated.  This really should be a
        monospace font to look sane.
        If a filename or a file-like object is specified, the user must
        provide different styles of the font.

        Default: "Courier New" on Windows, "Menlo" on Mac OS, and
                 "DejaVu Sans Mono" on \\*nix

    `font_size`
        The font size in points to be used.

        Default: 14

    `image_pad`
        The padding, in pixels to be used at each edge of the resulting image.

        Default: 10

    `line_numbers`
        Whether line numbers should be shown: True/False

        Default: True

    `line_number_start`
        The line number of the first line.

        Default: 1

    `line_number_step`
        The step used when printing line numbers.

        Default: 1

    `line_number_bg`
        The background colour (in "#123456" format) of the line number bar, or
        None to use the style background color.

        Default: "#eed"

    `line_number_fg`
        The text color of the line numbers (in "#123456"-like format).

        Default: "#886"

    `line_number_chars`
        The number of columns of line numbers allowable in the line number
        margin.

        Default: 2

    `line_number_bold`
        Whether line numbers will be bold: True/False

        Default: False

    `line_number_italic`
        Whether line numbers will be italicized: True/False

        Default: False

    `line_number_separator`
        Whether a line will be drawn between the line number area and the
        source code area: True/False

        Default: True

    `line_number_pad`
        The horizontal padding (in pixels) between the line number margin, and
        the source code area.

        Default: 6

    `hl_lines`
        Specify a list of lines to be highlighted.

        .. versionadded:: 1.2

        Default: empty list

    `hl_color`
        Specify the color for highlighting lines.

        .. versionadded:: 1.2

        Default: highlight color of the selected style
    '''
    name = 'img'
    aliases = [
        'img',
        'IMG',
        'png']
    filenames = [
        '*.png']
    unicodeoutput = False
    default_image_format = 'png'
    
    def __init__(self, **options):
        '''
        See the class docstring for explanation of options.
        '''
        if not pil_available:
            raise PilNotAvailable('Python Imaging Library is required for this formatter')
    # WARNING: Decompyle incomplete

    
    def get_style_defs(self, arg = ('',)):
        raise NotImplementedError('The -S option is meaningless for the image formatter. Use -O style=<stylename> instead.')

    
    def _get_line_height(self):
        '''
        Get the height of a line.
        '''
        return self.fonth + self.line_pad

    
    def _get_line_y(self, lineno):
        '''
        Get the Y coordinate of a line number.
        '''
        return lineno * self._get_line_height() + self.image_pad

    
    def _get_char_width(self):
        '''
        Get the width of a character.
        '''
        return self.fontw

    
    def _get_char_x(self, linelength):
        '''
        Get the X coordinate of a character position.
        '''
        return linelength + self.image_pad + self.line_number_width

    
    def _get_text_pos(self, linelength, lineno):
        '''
        Get the actual position for a character and line position.
        '''
        return (self._get_char_x(linelength), self._get_line_y(lineno))

    
    def _get_linenumber_pos(self, lineno):
        '''
        Get the actual position for the start of a line number.
        '''
        return (self.image_pad, self._get_line_y(lineno))

    
    def _get_text_color(self, style):
        '''
        Get the correct color for the token from the style.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_text_bg_color(self, style):
        '''
        Get the correct background color for the token from the style.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_style_font(self, style):
        '''
        Get the correct font for the style.
        '''
        return self.fonts.get_font(style['bold'], style['italic'])

    
    def _get_image_size(self, maxlinelength, maxlineno):
        '''
        Get the required image size.
        '''
        return (self._get_char_x(maxlinelength) + self.image_pad, self._get_line_y(maxlineno + 0) + self.image_pad)

    
    def _draw_linenumber(self, posno, lineno):
        '''
        Remember a line number drawable to paint later.
        '''
        self._draw_text(self._get_linenumber_pos(posno), str(lineno).rjust(self.line_number_chars), font = self.fonts.get_font(self.line_number_bold, self.line_number_italic), text_fg = self.line_number_fg, text_bg = None)

    
    def _draw_text(self, pos, text, font, text_fg, text_bg):
        '''
        Remember a single drawable tuple to paint later.
        '''
        self.drawables.append((pos, text, font, text_fg, text_bg))

    
    def _create_drawables(self, tokensource):
        '''
        Create drawables for the token content.
        '''
        lineno = 0
        charno = 0
        maxcharno = 0
        maxlinelength = 0
        linelength = 0
    # WARNING: Decompyle incomplete

    
    def _draw_line_numbers(self):
        '''
        Create drawables for the line numbers.
        '''
        if not self.line_numbers:
            return None
        for p in None(self.maxlineno):
            n = p + self.line_number_start
            if n % self.line_number_step == 0:
                self._draw_linenumber(p, n)
            return None

    
    def _paint_line_number_bg(self, im):
        '''
        Paint the line number background on the image.
        '''
        if not self.line_numbers:
            return None
    # WARNING: Decompyle incomplete

    
    def format(self, tokensource, outfile):
        '''
        Format ``tokensource``, an iterable of ``(tokentype, tokenstring)``
        tuples and write it into ``outfile``.

        This implementation calculates where it should draw each token on the
        pixmap, then calculates the required pixmap size and draws the items.
        '''
        self._create_drawables(tokensource)
        self._draw_line_numbers()
        im = Image.new('RGB', self._get_image_size(self.maxlinelength, self.maxlineno), self.background_color)
        self._paint_line_number_bg(im)
        draw = ImageDraw.Draw(im)
        if self.hl_lines:
            x = (self.image_pad + self.line_number_width - self.line_number_pad) + 1
            recth = self._get_line_height()
            rectw = im.size[0] - x
            for linenumber in self.hl_lines:
                y = self._get_line_y(linenumber - 1)
                draw.rectangle([
                    (x, y),
                    (x + rectw, y + recth)], fill = self.hl_color)
                for pos, value, font, text_fg, text_bg in self.drawables:
                    if text_bg:
                        if hasattr(draw, 'textsize'):
                            text_size = draw.textsize(text = value, font = font)
                        else:
                            text_size = font.getbbox(value)[2:]
                        draw.rectangle([
                            pos[0],
                            pos[1],
                            pos[0] + text_size[0],
                            pos[1] + text_size[1]], fill = text_bg)
                    draw.text(pos, value, font = font, fill = text_fg)
                    im.save(outfile, self.image_format.upper())
                    return None



class GifImageFormatter(ImageFormatter):
    '''
    Create a GIF image from source code. This uses the Python Imaging Library to
    generate a pixmap from the source code.

    .. versionadded:: 1.0
    '''
    name = 'img_gif'
    aliases = [
        'gif']
    filenames = [
        '*.gif']
    default_image_format = 'gif'


class JpgImageFormatter(ImageFormatter):
    '''
    Create a JPEG image from source code. This uses the Python Imaging Library to
    generate a pixmap from the source code.

    .. versionadded:: 1.0
    '''
    name = 'img_jpg'
    aliases = [
        'jpg',
        'jpeg']
    filenames = [
        '*.jpg']
    default_image_format = 'jpeg'


class BmpImageFormatter(ImageFormatter):
    '''
    Create a bitmap image from source code. This uses the Python Imaging Library to
    generate a pixmap from the source code.

    .. versionadded:: 1.0
    '''
    name = 'img_bmp'
    aliases = [
        'bmp',
        'bitmap']
    filenames = [
        '*.bmp']
    default_image_format = 'bmp'
