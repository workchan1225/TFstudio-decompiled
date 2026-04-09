# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageFont.pyc (Python 3.11)

from __future__ import annotations
import base64
import os
import sys
import warnings
from enum import IntEnum
from io import BytesIO
from types import ModuleType
from typing import IO, Any, BinaryIO, TypedDict, cast
from  import Image
from _typing import StrOrBytesPath
from _util import DeferredError, is_path
TYPE_CHECKING = False
if TYPE_CHECKING:
    from  import ImageFile
    from _imaging import ImagingFont
    from _imagingft import Font

class Axis(TypedDict):
    name: 'bytes | None' = 'Axis'


class Layout(IntEnum):
    BASIC = 0
    RAQM = 1

core: 'ModuleType | DeferredError' = 1000000

try:
    from  import _imagingft as core
except ImportError:
    ex = None
    core = DeferredError.new(ex)
    ex = None
    del ex
except:
    ex = None
    del ex


def _string_length_check(text = None):
    pass
# WARNING: Decompyle incomplete


class ImageFont:
    font: 'ImagingFont' = 'PIL font wrapper'
    
    def _load_pilfont(self = None, filename = None):
        fp = open(filename, 'rb')
        image = None
        root = os.path.splitext(filename)[0]
        for ext in ('.png', '.gif', '.pbm'):
            if image:
                image.close()
            fullname = root + ext
            image = Image.open(fullname)
            if image and image.mode in ('1', 'L'):
                pass
            
            except Exception:
                continue
            if image:
                image.close()
        msg = f'''cannot find glyph data file {root}.{{gif|pbm|png}}'''
        raise OSError(msg)
        self.file = fullname
        self._load_pilfont_data(fp, image)
        image.close()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _load_pilfont_data(self = None, file = None, image = None):
        if image.mode not in ('1', 'L'):
            msg = 'invalid font image mode'
            raise TypeError(msg)
        if file.read(8) != b'PILfont\n':
            msg = 'Not a PILfont file'
            raise SyntaxError(msg)
        file.readline()
        self.info = []
        s = file.readline()
        if s or s == b'DATA\n':
            pass
        else:
            self.info.append(s)
        data = file.read(5120)
        image.load()
        self.font = Image.core.font(image.im, data)

    
    def getmask(self = None, text = None, mode = None, *args, **kwargs):
        '''
        Create a bitmap for the text.

        If the font uses antialiasing, the bitmap should have mode ``L`` and use a
        maximum value of 255. Otherwise, it should have mode ``1``.

        :param text: Text to render.
        :param mode: Used by some graphics drivers to indicate what mode the
                     driver prefers; if empty, the renderer may return either
                     mode. Note that the mode is always a string, to simplify
                     C-level implementations.

                     .. versionadded:: 1.1.5

        :return: An internal PIL storage memory instance as defined by the
                 :py:mod:`PIL.Image.core` interface module.
        '''
        _string_length_check(text)
        Image._decompression_bomb_check(self.font.getsize(text))
        return self.font.getmask(text, mode)

    
    def getbbox(self = None, text = None, *args, **kwargs):
        '''
        Returns bounding box (in pixels) of given text.

        .. versionadded:: 9.2.0

        :param text: Text to render.

        :return: ``(left, top, right, bottom)`` bounding box
        '''
        _string_length_check(text)
        (width, height) = self.font.getsize(text)
        return (0, 0, width, height)

    
    def getlength(self = None, text = None, *args, **kwargs):
        '''
        Returns length (in pixels) of given text.
        This is the amount by which following text should be offset.

        .. versionadded:: 9.2.0
        '''
        _string_length_check(text)
        (width, height) = self.font.getsize(text)
        return width



class FreeTypeFont:
    font_bytes: 'bytes' = 'FreeType font wrapper (requires _imagingft service)'
    
    def __init__(self, font = None, size = None, index = None, encoding = (10, 0, '', None), layout_engine = ('font', 'StrOrBytesPath | BinaryIO', 'size', 'float', 'index', 'int', 'encoding', 'str', 'layout_engine', 'Layout | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self = None):
        return [
            self.path,
            self.size,
            self.index,
            self.encoding,
            self.layout_engine]

    
    def __setstate__(self = None, state = None):
        (path, size, index, encoding, layout_engine) = state
        FreeTypeFont.__init__(self, path, size, index, encoding, layout_engine)

    
    def getname(self = None):
        '''
        :return: A tuple of the font family (e.g. Helvetica) and the font style
            (e.g. Bold)
        '''
        return (self.font.family, self.font.style)

    
    def getmetrics(self = None):
        '''
        :return: A tuple of the font ascent (the distance from the baseline to
            the highest outline point) and descent (the distance from the
            baseline to the lowest outline point, a negative value)
        '''
        return (self.font.ascent, self.font.descent)

    
    def getlength(self, text = None, mode = None, direction = None, features = ('', None, None, None), language = ('text', 'str | bytes', 'mode', 'str', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'return', 'float')):
        '''
        Returns length (in pixels with 1/64 precision) of given text when rendered
        in font with provided direction, features, and language.

        This is the amount by which following text should be offset.
        Text bounding box may extend past the length in some fonts,
        e.g. when using italics or accents.

        The result is returned as a float; it is a whole number if using basic layout.

        Note that the sum of two lengths may not equal the length of a concatenated
        string due to kerning. If you need to adjust for kerning, include the following
        character and subtract its length.

        For example, instead of ::

          hello = font.getlength("Hello")
          world = font.getlength("World")
          hello_world = hello + world  # not adjusted for kerning
          assert hello_world == font.getlength("HelloWorld")  # may fail

        use ::

          hello = font.getlength("HelloW") - font.getlength("W")  # adjusted for kerning
          world = font.getlength("World")
          hello_world = hello + world  # adjusted for kerning
          assert hello_world == font.getlength("HelloWorld")  # True

        or disable kerning with (requires libraqm) ::

          hello = draw.textlength("Hello", font, features=["-kern"])
          world = draw.textlength("World", font, features=["-kern"])
          hello_world = hello + world  # kerning is disabled, no need to adjust
          assert hello_world == draw.textlength("HelloWorld", font, features=["-kern"])

        .. versionadded:: 8.0.0

        :param text: Text to measure.
        :param mode: Used by some graphics drivers to indicate what mode the
                     driver prefers; if empty, the renderer may return either
                     mode. Note that the mode is always a string, to simplify
                     C-level implementations.

        :param direction: Direction of the text. It can be \'rtl\' (right to
                          left), \'ltr\' (left to right) or \'ttb\' (top to bottom).
                          Requires libraqm.

        :param features: A list of OpenType font features to be used during text
                         layout. This is usually used to turn on optional
                         font features that are not enabled by default,
                         for example \'dlig\' or \'ss01\', but can be also
                         used to turn off default font features for
                         example \'-liga\' to disable ligatures or \'-kern\'
                         to disable kerning.  To get all supported
                         features, see
                         https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist
                         Requires libraqm.

        :param language: Language of the text. Different languages may use
                         different glyph shapes or ligatures. This parameter tells
                         the font which language the text is in, and to apply the
                         correct substitutions as appropriate, if available.
                         It should be a `BCP 47 language code
                         <https://www.w3.org/International/articles/language-tags/>`_
                         Requires libraqm.

        :return: Either width for horizontal text, or height for vertical text.
        '''
        _string_length_check(text)
        return self.font.getlength(text, mode, direction, features, language) / 64

    
    def getbbox(self, text, mode, direction = None, features = None, language = None, stroke_width = ('', None, None, None, 0, None), anchor = ('text', 'str | bytes', 'mode', 'str', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'stroke_width', 'float', 'anchor', 'str | None', 'return', 'tuple[float, float, float, float]')):
        """
        Returns bounding box (in pixels) of given text relative to given anchor
        when rendered in font with provided direction, features, and language.

        Use :py:meth:`getlength()` to get the offset of following text with
        1/64 pixel precision. The bounding box includes extra margins for
        some fonts, e.g. italics or accents.

        .. versionadded:: 8.0.0

        :param text: Text to render.
        :param mode: Used by some graphics drivers to indicate what mode the
                     driver prefers; if empty, the renderer may return either
                     mode. Note that the mode is always a string, to simplify
                     C-level implementations.

        :param direction: Direction of the text. It can be 'rtl' (right to
                          left), 'ltr' (left to right) or 'ttb' (top to bottom).
                          Requires libraqm.

        :param features: A list of OpenType font features to be used during text
                         layout. This is usually used to turn on optional
                         font features that are not enabled by default,
                         for example 'dlig' or 'ss01', but can be also
                         used to turn off default font features for
                         example '-liga' to disable ligatures or '-kern'
                         to disable kerning.  To get all supported
                         features, see
                         https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist
                         Requires libraqm.

        :param language: Language of the text. Different languages may use
                         different glyph shapes or ligatures. This parameter tells
                         the font which language the text is in, and to apply the
                         correct substitutions as appropriate, if available.
                         It should be a `BCP 47 language code
                         <https://www.w3.org/International/articles/language-tags/>`_
                         Requires libraqm.

        :param stroke_width: The width of the text stroke.

        :param anchor:  The text anchor alignment. Determines the relative location of
                        the anchor to the text. The default alignment is top left,
                        specifically ``la`` for horizontal text and ``lt`` for
                        vertical text. See :ref:`text-anchors` for details.

        :return: ``(left, top, right, bottom)`` bounding box
        """
        _string_length_check(text)
        (size, offset) = self.font.getsize(text, mode, direction, features, language, anchor)
        top = offset[1] - stroke_width
        left = offset[0] - stroke_width
        height = size[1] + 2 * stroke_width
        width = size[0] + 2 * stroke_width
        return (left, top, left + width, top + height)

    
    def getmask(self, text, mode, direction, features, language = None, stroke_width = None, anchor = None, ink = ('', None, None, None, 0, None, 0, None), start = ('text', 'str | bytes', 'mode', 'str', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'stroke_width', 'float', 'anchor', 'str | None', 'ink', 'int', 'start', 'tuple[float, float] | None', 'return', 'Image.core.ImagingCore')):
        """
        Create a bitmap for the text.

        If the font uses antialiasing, the bitmap should have mode ``L`` and use a
        maximum value of 255. If the font has embedded color data, the bitmap
        should have mode ``RGBA``. Otherwise, it should have mode ``1``.

        :param text: Text to render.
        :param mode: Used by some graphics drivers to indicate what mode the
                     driver prefers; if empty, the renderer may return either
                     mode. Note that the mode is always a string, to simplify
                     C-level implementations.

                     .. versionadded:: 1.1.5

        :param direction: Direction of the text. It can be 'rtl' (right to
                          left), 'ltr' (left to right) or 'ttb' (top to bottom).
                          Requires libraqm.

                          .. versionadded:: 4.2.0

        :param features: A list of OpenType font features to be used during text
                         layout. This is usually used to turn on optional
                         font features that are not enabled by default,
                         for example 'dlig' or 'ss01', but can be also
                         used to turn off default font features for
                         example '-liga' to disable ligatures or '-kern'
                         to disable kerning.  To get all supported
                         features, see
                         https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist
                         Requires libraqm.

                         .. versionadded:: 4.2.0

        :param language: Language of the text. Different languages may use
                         different glyph shapes or ligatures. This parameter tells
                         the font which language the text is in, and to apply the
                         correct substitutions as appropriate, if available.
                         It should be a `BCP 47 language code
                         <https://www.w3.org/International/articles/language-tags/>`_
                         Requires libraqm.

                         .. versionadded:: 6.0.0

        :param stroke_width: The width of the text stroke.

                         .. versionadded:: 6.2.0

        :param anchor:  The text anchor alignment. Determines the relative location of
                        the anchor to the text. The default alignment is top left,
                        specifically ``la`` for horizontal text and ``lt`` for
                        vertical text. See :ref:`text-anchors` for details.

                         .. versionadded:: 8.0.0

        :param ink: Foreground ink for rendering in RGBA mode.

                         .. versionadded:: 8.0.0

        :param start: Tuple of horizontal and vertical offset, as text may render
                      differently when starting at fractional coordinates.

                         .. versionadded:: 9.4.0

        :return: An internal PIL storage memory instance as defined by the
                 :py:mod:`PIL.Image.core` interface module.
        """
        return self.getmask2(text, mode, direction = direction, features = features, language = language, stroke_width = stroke_width, anchor = anchor, ink = ink, start = start)[0]

    
    def getmask2(self, text, mode, direction, features, language = None, stroke_width = None, anchor = None, ink = ('', None, None, None, 0, None, 0, None), start = ('text', 'str | bytes', 'mode', 'str', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'stroke_width', 'float', 'anchor', 'str | None', 'ink', 'int', 'start', 'tuple[float, float] | None', 'args', 'Any', 'kwargs', 'Any', 'return', 'tuple[Image.core.ImagingCore, tuple[int, int]]'), *args, **kwargs):
        """
        Create a bitmap for the text.

        If the font uses antialiasing, the bitmap should have mode ``L`` and use a
        maximum value of 255. If the font has embedded color data, the bitmap
        should have mode ``RGBA``. Otherwise, it should have mode ``1``.

        :param text: Text to render.
        :param mode: Used by some graphics drivers to indicate what mode the
                     driver prefers; if empty, the renderer may return either
                     mode. Note that the mode is always a string, to simplify
                     C-level implementations.

                     .. versionadded:: 1.1.5

        :param direction: Direction of the text. It can be 'rtl' (right to
                          left), 'ltr' (left to right) or 'ttb' (top to bottom).
                          Requires libraqm.

                          .. versionadded:: 4.2.0

        :param features: A list of OpenType font features to be used during text
                         layout. This is usually used to turn on optional
                         font features that are not enabled by default,
                         for example 'dlig' or 'ss01', but can be also
                         used to turn off default font features for
                         example '-liga' to disable ligatures or '-kern'
                         to disable kerning.  To get all supported
                         features, see
                         https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist
                         Requires libraqm.

                         .. versionadded:: 4.2.0

        :param language: Language of the text. Different languages may use
                         different glyph shapes or ligatures. This parameter tells
                         the font which language the text is in, and to apply the
                         correct substitutions as appropriate, if available.
                         It should be a `BCP 47 language code
                         <https://www.w3.org/International/articles/language-tags/>`_
                         Requires libraqm.

                         .. versionadded:: 6.0.0

        :param stroke_width: The width of the text stroke.

                         .. versionadded:: 6.2.0

        :param anchor:  The text anchor alignment. Determines the relative location of
                        the anchor to the text. The default alignment is top left,
                        specifically ``la`` for horizontal text and ``lt`` for
                        vertical text. See :ref:`text-anchors` for details.

                         .. versionadded:: 8.0.0

        :param ink: Foreground ink for rendering in RGBA mode.

                         .. versionadded:: 8.0.0

        :param start: Tuple of horizontal and vertical offset, as text may render
                      differently when starting at fractional coordinates.

                         .. versionadded:: 9.4.0

        :return: A tuple of an internal PIL storage memory instance as defined by the
                 :py:mod:`PIL.Image.core` interface module, and the text offset, the
                 gap between the starting coordinate and the first marking
        """
        pass
    # WARNING: Decompyle incomplete

    
    def font_variant(self, font = None, size = None, index = None, encoding = (None, None, None, None, None), layout_engine = ('font', 'StrOrBytesPath | BinaryIO | None', 'size', 'float | None', 'index', 'int | None', 'encoding', 'str | None', 'layout_engine', 'Layout | None', 'return', 'FreeTypeFont')):
        '''
        Create a copy of this FreeTypeFont object,
        using any specified arguments to override the settings.

        Parameters are identical to the parameters used to initialize this
        object.

        :return: A FreeTypeFont object.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_variation_names(self = None):
        '''
        :returns: A list of the named styles in a variation font.
        :exception OSError: If the font is not a variation font.
        '''
        names = self.font.getvarnames()
        return names()

    
    def set_variation_by_name(self = None, name = None):
        '''
        :param name: The name of the style.
        :exception OSError: If the font is not a variation font.
        '''
        names = self.get_variation_names()
        if not isinstance(name, bytes):
            name = name.encode()
        index = names.index(name) + 1
        if index == getattr(self, '_last_variation_index', None):
            return None
        self._last_variation_index = None
        self.font.setvarname(index)

    
    def get_variation_axes(self = None):
        '''
        :returns: A list of the axes in a variation font.
        :exception OSError: If the font is not a variation font.
        '''
        axes = self.font.getvaraxes()
        for axis in axes:
            if axis['name']:
                axis['name'] = axis['name'].replace(b'\x00', b'')
            return axes

    
    def set_variation_by_axes(self = None, axes = None):
        '''
        :param axes: A list of values for each axis.
        :exception OSError: If the font is not a variation font.
        '''
        self.font.setvaraxes(axes)



class TransposedFont:
    '''Wrapper for writing rotated or mirrored text'''
    
    def __init__(self = None, font = None, orientation = None):
        '''
        Wrapper that creates a transposed font from any existing font
        object.

        :param font: A font object.
        :param orientation: An optional orientation.  If given, this should
            be one of Image.Transpose.FLIP_LEFT_RIGHT, Image.Transpose.FLIP_TOP_BOTTOM,
            Image.Transpose.ROTATE_90, Image.Transpose.ROTATE_180, or
            Image.Transpose.ROTATE_270.
        '''
        self.font = font
        self.orientation = orientation

    
    def getmask(self = None, text = None, mode = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def getbbox(self = None, text = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def getlength(self = None, text = None, *args, **kwargs):
        if self.orientation in (Image.Transpose.ROTATE_90, Image.Transpose.ROTATE_270):
            msg = 'text length is undefined for text rotated by 90 or 270 degrees'
            raise ValueError(msg)
    # WARNING: Decompyle incomplete



def load(filename = None):
    '''
    Load a font file. This function loads a font object from the given
    bitmap font file, and returns the corresponding font object. For loading TrueType
    or OpenType fonts instead, see :py:func:`~PIL.ImageFont.truetype`.

    :param filename: Name of font file.
    :return: A font object.
    :exception OSError: If the file could not be read.
    '''
    f = ImageFont()
    f._load_pilfont(filename)
    return f


def truetype(font = None, size = None, index = None, encoding = (10, 0, '', None), layout_engine = ('font', 'StrOrBytesPath | BinaryIO', 'size', 'float', 'index', 'int', 'encoding', 'str', 'layout_engine', 'Layout | None', 'return', 'FreeTypeFont')):
    '''
    Load a TrueType or OpenType font from a file or file-like object,
    and create a font object. This function loads a font object from the given
    file or file-like object, and creates a font object for a font of the given
    size. For loading bitmap fonts instead, see :py:func:`~PIL.ImageFont.load`
    and :py:func:`~PIL.ImageFont.load_path`.

    Pillow uses FreeType to open font files. On Windows, be aware that FreeType
    will keep the file open as long as the FreeTypeFont object exists. Windows
    limits the number of files that can be open in C at once to 512, so if many
    fonts are opened simultaneously and that limit is approached, an
    ``OSError`` may be thrown, reporting that FreeType "cannot open resource".
    A workaround would be to copy the file(s) into memory, and open that instead.

    This function requires the _imagingft service.

    :param font: A filename or file-like object containing a TrueType font.
                 If the file is not found in this filename, the loader may also
                 search in other directories, such as:

                 * The :file:`fonts/` directory on Windows,
                 * :file:`/Library/Fonts/`, :file:`/System/Library/Fonts/`
                   and :file:`~/Library/Fonts/` on macOS.
                 * :file:`~/.local/share/fonts`, :file:`/usr/local/share/fonts`,
                   and :file:`/usr/share/fonts` on Linux; or those specified by
                   the ``XDG_DATA_HOME`` and ``XDG_DATA_DIRS`` environment variables
                   for user-installed and system-wide fonts, respectively.

    :param size: The requested size, in pixels.
    :param index: Which font face to load (default is first available face).
    :param encoding: Which font encoding to use (default is Unicode). Possible
                     encodings include (see the FreeType documentation for more
                     information):

                     * "unic" (Unicode)
                     * "symb" (Microsoft Symbol)
                     * "ADOB" (Adobe Standard)
                     * "ADBE" (Adobe Expert)
                     * "ADBC" (Adobe Custom)
                     * "armn" (Apple Roman)
                     * "sjis" (Shift JIS)
                     * "gb  " (PRC)
                     * "big5"
                     * "wans" (Extended Wansung)
                     * "joha" (Johab)
                     * "lat1" (Latin-1)

                     This specifies the character set to use. It does not alter the
                     encoding of any text provided in subsequent operations.
    :param layout_engine: Which layout engine to use, if available:
                     :attr:`.ImageFont.Layout.BASIC` or :attr:`.ImageFont.Layout.RAQM`.
                     If it is available, Raqm layout will be used by default.
                     Otherwise, basic layout will be used.

                     Raqm layout is recommended for all non-English text. If Raqm layout
                     is not required, basic layout will have better performance.

                     You can check support for Raqm layout using
                     :py:func:`PIL.features.check_feature` with ``feature="raqm"``.

                     .. versionadded:: 4.2.0
    :return: A font object.
    :exception OSError: If the file could not be read.
    :exception ValueError: If the font size is not greater than zero.
    '''
    pass
# WARNING: Decompyle incomplete


def load_path(filename = None):
    '''
    Load font file. Same as :py:func:`~PIL.ImageFont.load`, but searches for a
    bitmap font along the Python path.

    :param filename: Name of font file.
    :return: A font object.
    :exception OSError: If the file could not be read.
    '''
    if not isinstance(filename, str):
        filename = filename.decode('utf-8')
    for directory in sys.path:
        
        return None, load(os.path.join(directory, filename))
        except OSError:
            continue
        if os.path.exists(filename):
            msg += f''', did you mean ImageFont.load("{filename}") instead?''' = f'''cannot find font file "{filename}" in sys.path'''
    raise OSError(msg)


def load_default_imagefont():
    f = ImageFont()
    f._load_pilfont_data(BytesIO(base64.b64decode(b'\nUElMZm9udAo7Ozs7OzsxMDsKREFUQQoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAA//8AAQAAAAAAAAABAAEA\nBgAAAAH/+gADAAAAAQAAAAMABgAGAAAAAf/6AAT//QADAAAABgADAAYAAAAA//kABQABAAYAAAAL\nAAgABgAAAAD/+AAFAAEACwAAABAACQAGAAAAAP/5AAUAAAAQAAAAFQAHAAYAAP////oABQAAABUA\nAAAbAAYABgAAAAH/+QAE//wAGwAAAB4AAwAGAAAAAf/5AAQAAQAeAAAAIQAIAAYAAAAB//kABAAB\nACEAAAAkAAgABgAAAAD/+QAE//0AJAAAACgABAAGAAAAAP/6AAX//wAoAAAALQAFAAYAAAAB//8A\nBAACAC0AAAAwAAMABgAAAAD//AAF//0AMAAAADUAAQAGAAAAAf//AAMAAAA1AAAANwABAAYAAAAB\n//kABQABADcAAAA7AAgABgAAAAD/+QAFAAAAOwAAAEAABwAGAAAAAP/5AAYAAABAAAAARgAHAAYA\nAAAA//kABQAAAEYAAABLAAcABgAAAAD/+QAFAAAASwAAAFAABwAGAAAAAP/5AAYAAABQAAAAVgAH\nAAYAAAAA//kABQAAAFYAAABbAAcABgAAAAD/+QAFAAAAWwAAAGAABwAGAAAAAP/5AAUAAABgAAAA\nZQAHAAYAAAAA//kABQAAAGUAAABqAAcABgAAAAD/+QAFAAAAagAAAG8ABwAGAAAAAf/8AAMAAABv\nAAAAcQAEAAYAAAAA//wAAwACAHEAAAB0AAYABgAAAAD/+gAE//8AdAAAAHgABQAGAAAAAP/7AAT/\n/gB4AAAAfAADAAYAAAAB//oABf//AHwAAACAAAUABgAAAAD/+gAFAAAAgAAAAIUABgAGAAAAAP/5\nAAYAAQCFAAAAiwAIAAYAAP////oABgAAAIsAAACSAAYABgAA////+gAFAAAAkgAAAJgABgAGAAAA\nAP/6AAUAAACYAAAAnQAGAAYAAP////oABQAAAJ0AAACjAAYABgAA////+gAFAAAAowAAAKkABgAG\nAAD////6AAUAAACpAAAArwAGAAYAAAAA//oABQAAAK8AAAC0AAYABgAA////+gAGAAAAtAAAALsA\nBgAGAAAAAP/6AAQAAAC7AAAAvwAGAAYAAP////oABQAAAL8AAADFAAYABgAA////+gAGAAAAxQAA\nAMwABgAGAAD////6AAUAAADMAAAA0gAGAAYAAP////oABQAAANIAAADYAAYABgAA////+gAGAAAA\n2AAAAN8ABgAGAAAAAP/6AAUAAADfAAAA5AAGAAYAAP////oABQAAAOQAAADqAAYABgAAAAD/+gAF\nAAEA6gAAAO8ABwAGAAD////6AAYAAADvAAAA9gAGAAYAAAAA//oABQAAAPYAAAD7AAYABgAA////\n+gAFAAAA+wAAAQEABgAGAAD////6AAYAAAEBAAABCAAGAAYAAP////oABgAAAQgAAAEPAAYABgAA\n////+gAGAAABDwAAARYABgAGAAAAAP/6AAYAAAEWAAABHAAGAAYAAP////oABgAAARwAAAEjAAYA\nBgAAAAD/+gAFAAABIwAAASgABgAGAAAAAf/5AAQAAQEoAAABKwAIAAYAAAAA//kABAABASsAAAEv\nAAgABgAAAAH/+QAEAAEBLwAAATIACAAGAAAAAP/5AAX//AEyAAABNwADAAYAAAAAAAEABgACATcA\nAAE9AAEABgAAAAH/+QAE//wBPQAAAUAAAwAGAAAAAP/7AAYAAAFAAAABRgAFAAYAAP////kABQAA\nAUYAAAFMAAcABgAAAAD/+wAFAAABTAAAAVEABQAGAAAAAP/5AAYAAAFRAAABVwAHAAYAAAAA//sA\nBQAAAVcAAAFcAAUABgAAAAD/+QAFAAABXAAAAWEABwAGAAAAAP/7AAYAAgFhAAABZwAHAAYAAP//\n//kABQAAAWcAAAFtAAcABgAAAAD/+QAGAAABbQAAAXMABwAGAAAAAP/5AAQAAgFzAAABdwAJAAYA\nAP////kABgAAAXcAAAF+AAcABgAAAAD/+QAGAAABfgAAAYQABwAGAAD////7AAUAAAGEAAABigAF\nAAYAAP////sABQAAAYoAAAGQAAUABgAAAAD/+wAFAAABkAAAAZUABQAGAAD////7AAUAAgGVAAAB\nmwAHAAYAAAAA//sABgACAZsAAAGhAAcABgAAAAD/+wAGAAABoQAAAacABQAGAAAAAP/7AAYAAAGn\nAAABrQAFAAYAAAAA//kABgAAAa0AAAGzAAcABgAA////+wAGAAABswAAAboABQAGAAD////7AAUA\nAAG6AAABwAAFAAYAAP////sABgAAAcAAAAHHAAUABgAAAAD/+wAGAAABxwAAAc0ABQAGAAD////7\nAAYAAgHNAAAB1AAHAAYAAAAA//sABQAAAdQAAAHZAAUABgAAAAH/+QAFAAEB2QAAAd0ACAAGAAAA\nAv/6AAMAAQHdAAAB3gAHAAYAAAAA//kABAABAd4AAAHiAAgABgAAAAD/+wAF//0B4gAAAecAAgAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAB\n//sAAwACAecAAAHpAAcABgAAAAD/+QAFAAEB6QAAAe4ACAAGAAAAAP/5AAYAAAHuAAAB9AAHAAYA\nAAAA//oABf//AfQAAAH5AAUABgAAAAD/+QAGAAAB+QAAAf8ABwAGAAAAAv/5AAMAAgH/AAACAAAJ\nAAYAAAAA//kABQABAgAAAAIFAAgABgAAAAH/+gAE//sCBQAAAggAAQAGAAAAAP/5AAYAAAIIAAAC\nDgAHAAYAAAAB//kABf/+Ag4AAAISAAUABgAA////+wAGAAACEgAAAhkABQAGAAAAAP/7AAX//gIZ\nAAACHgADAAYAAAAA//wABf/9Ah4AAAIjAAEABgAAAAD/+QAHAAACIwAAAioABwAGAAAAAP/6AAT/\n+wIqAAACLgABAAYAAAAA//kABP/8Ai4AAAIyAAMABgAAAAD/+gAFAAACMgAAAjcABgAGAAAAAf/5\nAAT//QI3AAACOgAEAAYAAAAB//kABP/9AjoAAAI9AAQABgAAAAL/+QAE//sCPQAAAj8AAgAGAAD/\n///7AAYAAgI/AAACRgAHAAYAAAAA//kABgABAkYAAAJMAAgABgAAAAH//AAD//0CTAAAAk4AAQAG\nAAAAAf//AAQAAgJOAAACUQADAAYAAAAB//kABP/9AlEAAAJUAAQABgAAAAH/+QAF//4CVAAAAlgA\nBQAGAAD////7AAYAAAJYAAACXwAFAAYAAP////kABgAAAl8AAAJmAAcABgAA////+QAGAAACZgAA\nAm0ABwAGAAD////5AAYAAAJtAAACdAAHAAYAAAAA//sABQACAnQAAAJ5AAcABgAA////9wAGAAAC\neQAAAoAACQAGAAD////3AAYAAAKAAAAChwAJAAYAAP////cABgAAAocAAAKOAAkABgAA////9wAG\nAAACjgAAApUACQAGAAD////4AAYAAAKVAAACnAAIAAYAAP////cABgAAApwAAAKjAAkABgAA////\n+gAGAAACowAAAqoABgAGAAAAAP/6AAUAAgKqAAACrwAIAAYAAP////cABQAAAq8AAAK1AAkABgAA\n////9wAFAAACtQAAArsACQAGAAD////3AAUAAAK7AAACwQAJAAYAAP////gABQAAAsEAAALHAAgA\nBgAAAAD/9wAEAAACxwAAAssACQAGAAAAAP/3AAQAAALLAAACzwAJAAYAAAAA//cABAAAAs8AAALT\nAAkABgAAAAD/+AAEAAAC0wAAAtcACAAGAAD////6AAUAAALXAAAC3QAGAAYAAP////cABgAAAt0A\nAALkAAkABgAAAAD/9wAFAAAC5AAAAukACQAGAAAAAP/3AAUAAALpAAAC7gAJAAYAAAAA//cABQAA\nAu4AAALzAAkABgAAAAD/9wAFAAAC8wAAAvgACQAGAAAAAP/4AAUAAAL4AAAC/QAIAAYAAAAA//oA\nBf//Av0AAAMCAAUABgAA////+gAGAAADAgAAAwkABgAGAAD////3AAYAAAMJAAADEAAJAAYAAP//\n//cABgAAAxAAAAMXAAkABgAA////9wAGAAADFwAAAx4ACQAGAAD////4AAYAAAAAAAoABwASAAYA\nAP////cABgAAAAcACgAOABMABgAA////+gAFAAAADgAKABQAEAAGAAD////6AAYAAAAUAAoAGwAQ\nAAYAAAAA//gABgAAABsACgAhABIABgAAAAD/+AAGAAAAIQAKACcAEgAGAAAAAP/4AAYAAAAnAAoA\nLQASAAYAAAAA//gABgAAAC0ACgAzABIABgAAAAD/+QAGAAAAMwAKADkAEQAGAAAAAP/3AAYAAAA5\nAAoAPwATAAYAAP////sABQAAAD8ACgBFAA8ABgAAAAD/+wAFAAIARQAKAEoAEQAGAAAAAP/4AAUA\nAABKAAoATwASAAYAAAAA//gABQAAAE8ACgBUABIABgAAAAD/+AAFAAAAVAAKAFkAEgAGAAAAAP/5\nAAUAAABZAAoAXgARAAYAAAAA//gABgAAAF4ACgBkABIABgAAAAD/+AAGAAAAZAAKAGoAEgAGAAAA\nAP/4AAYAAABqAAoAcAASAAYAAAAA//kABgAAAHAACgB2ABEABgAAAAD/+AAFAAAAdgAKAHsAEgAG\nAAD////4AAYAAAB7AAoAggASAAYAAAAA//gABQAAAIIACgCHABIABgAAAAD/+AAFAAAAhwAKAIwA\nEgAGAAAAAP/4AAUAAACMAAoAkQASAAYAAAAA//gABQAAAJEACgCWABIABgAAAAD/+QAFAAAAlgAK\nAJsAEQAGAAAAAP/6AAX//wCbAAoAoAAPAAYAAAAA//oABQABAKAACgClABEABgAA////+AAGAAAA\npQAKAKwAEgAGAAD////4AAYAAACsAAoAswASAAYAAP////gABgAAALMACgC6ABIABgAA////+QAG\nAAAAugAKAMEAEQAGAAD////4AAYAAgDBAAoAyAAUAAYAAP////kABQACAMgACgDOABMABgAA////\n+QAGAAIAzgAKANUAEw==\n')), Image.open(BytesIO(base64.b64decode(b'\niVBORw0KGgoAAAANSUhEUgAAAx4AAAAUAQAAAAArMtZoAAAEwElEQVR4nABlAJr/AHVE4czCI/4u\nMc4b7vuds/xzjz5/3/7u/n9vMe7vnfH/9++vPn/xyf5zhxzjt8GHw8+2d83u8x27199/nxuQ6Od9\nM43/5z2I+9n9ZtmDBwMQECDRQw/eQIQohJXxpBCNVE6QCCAAAAD//wBlAJr/AgALyj1t/wINwq0g\nLeNZUworuN1cjTPIzrTX6ofHWeo3v336qPzfEwRmBnHTtf95/fglZK5N0PDgfRTslpGBvz7LFc4F\nIUXBWQGjQ5MGCx34EDFPwXiY4YbYxavpnhHFrk14CDAAAAD//wBlAJr/AgKqRooH2gAgPeggvUAA\nBu2WfgPoAwzRAABAAAAAAACQgLz/3Uv4Gv+gX7BJgDeeGP6AAAD1NMDzKHD7ANWr3loYbxsAD791\nNAADfcoIDyP44K/jv4Y63/Z+t98Ovt+ub4T48LAAAAD//wBlAJr/AuplMlADJAAAAGuAphWpqhMx\nin0A/fRvAYBABPgBwBUgABBQ/sYAyv9g0bCHgOLoGAAAAAAAREAAwI7nr0ArYpow7aX8//9LaP/9\nSjdavWA8ePHeBIKB//81/83ndznOaXx379wAAAD//wBlAJr/AqDxW+D3AABAAbUh/QMnbQag/gAY\nAYDAAACgtgD/gOqAAAB5IA/8AAAk+n9w0AAA8AAAmFRJuPo27ciC0cD5oeW4E7KA/wD3ECMAn2tt\ny8PgwH8AfAxFzC0JzeAMtratAsC/ffwAAAD//wBlAJr/BGKAyCAA4AAAAvgeYTAwHd1kmQF5chkG\nABoMIHcL5xVpTfQbUqzlAAAErwAQBgAAEOClA5D9il08AEh/tUzdCBsXkbgACED+woQg8Si9VeqY\nlODCn7lmF6NhnAEYgAAA/NMIAAAAAAD//2JgjLZgVGBg5Pv/Tvpc8hwGBjYGJADjHDrAwPzAjv/H\n/Wf3PzCwtzcwHmBgYGcwbZz8wHaCAQMDOwMDQ8MCBgYOC3W7mp+f0w+wHOYxO3OG+e376hsMZjk3\nAAAAAP//YmCMY2A4wMAIN5e5gQETPD6AZisDAwMDgzSDAAPjByiHcQMDAwMDg1nOze1lByRu5/47\nc4859311AYNZzg0AAAAA//9iYGDBYihOIIMuwIjGL39/fwffA8b//xv/P2BPtzzHwCBjUQAAAAD/\n/yLFBrIBAAAA//9i1HhcwdhizX7u8NZNzyLbvT97bfrMf/QHI8evOwcSqGUJAAAA//9iYBB81iSw\npEE170Qrg5MIYydHqwdDQRMrAwcVrQAAAAD//2J4x7j9AAMDn8Q/BgYLBoaiAwwMjPdvMDBYM1Tv\noJodAAAAAP//Yqo/83+dxePWlxl3npsel9lvLfPcqlE9725C+acfVLMEAAAA//9i+s9gwCoaaGMR\nevta/58PTEWzr21hufPjA8N+qlnBwAAAAAD//2JiWLci5v1+HmFXDqcnULE/MxgYGBj+f6CaJQAA\nAAD//2Ji2FrkY3iYpYC5qDeGgeEMAwPDvwQBBoYvcTwOVLMEAAAA//9isDBgkP///0EOg9z35v//\nGc/eeW7BwPj5+QGZhANUswMAAAD//2JgqGBgYGBgqEMXlvhMPUsAAAAA//8iYDd1AAAAAP//AwDR\nw7IkEbzhVQAAAABJRU5ErkJggg==\n'))))
    return f


def load_default(size = None):
    '''If FreeType support is available, load a version of Aileron Regular,
    https://dotcolon.net/fonts/aileron, with a more limited character set.

    Otherwise, load a "better than nothing" font.

    .. versionadded:: 1.1.4

    :param size: The font size of Aileron Regular.

        .. versionadded:: 10.1.0

    :return: A font object.
    '''
    pass
# WARNING: Decompyle incomplete
