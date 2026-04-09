# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImageText.pyc (Python 3.11)

from __future__ import annotations
from  import ImageFont
from _typing import _Ink

class Text:
    
    def __init__(self, text, font, mode = None, spacing = None, direction = None, features = (None, 'RGB', 4, None, None, None), language = ('text', 'str | bytes', 'font', 'ImageFont.ImageFont | ImageFont.FreeTypeFont | ImageFont.TransposedFont | None', 'mode', 'str', 'spacing', 'float', 'direction', 'str | None', 'features', 'list[str] | None', 'language', 'str | None', 'return', 'None')):
        '''
        :param text: String to be drawn.
        :param font: Either an :py:class:`~PIL.ImageFont.ImageFont` instance,
                     :py:class:`~PIL.ImageFont.FreeTypeFont` instance,
                     :py:class:`~PIL.ImageFont.TransposedFont` instance or ``None``. If
                     ``None``, the default font from :py:meth:`.ImageFont.load_default`
                     will be used.
        :param mode: The image mode this will be used with.
        :param spacing: The number of pixels between lines.
        :param direction: Direction of the text. It can be ``"rtl"`` (right to left),
                          ``"ltr"`` (left to right) or ``"ttb"`` (top to bottom).
                          Requires libraqm.
        :param features: A list of OpenType font features to be used during text
                         layout. This is usually used to turn on optional font features
                         that are not enabled by default, for example ``"dlig"`` or
                         ``"ss01"``, but can be also used to turn off default font
                         features, for example ``"-liga"`` to disable ligatures or
                         ``"-kern"`` to disable kerning.  To get all supported
                         features, see `OpenType docs`_.
                         Requires libraqm.
        :param language: Language of the text. Different languages may use
                         different glyph shapes or ligatures. This parameter tells
                         the font which language the text is in, and to apply the
                         correct substitutions as appropriate, if available.
                         It should be a `BCP 47 language code`_.
                         Requires libraqm.
        '''
        self.text = text
        if not font:
            pass
        self.font = ImageFont.load_default()
        self.mode = mode
        self.spacing = spacing
        self.direction = direction
        self.features = features
        self.language = language
        self.embedded_color = False
        self.stroke_width = 0
        self.stroke_fill = None

    
    def embed_color(self = None):
        '''
        Use embedded color glyphs (COLR, CBDT, SBIX).
        '''
        if self.mode not in ('RGB', 'RGBA'):
            msg = 'Embedded color supported only in RGB and RGBA modes'
            raise ValueError(msg)
        self.embedded_color = True

    
    def stroke(self = None, width = None, fill = None):
        '''
        :param width: The width of the text stroke.
        :param fill: Color to use for the text stroke when drawing. If not given, will
                     default to the ``fill`` parameter from
                     :py:meth:`.ImageDraw.ImageDraw.text`.
        '''
        self.stroke_width = width
        self.stroke_fill = fill

    
    def _get_fontmode(self = None):
        if self.mode in ('1', 'P', 'I', 'F'):
            return '1'
        if None.embedded_color:
            return 'RGBA'

    
    def get_length(self):
        '''
        Returns length (in pixels with 1/64 precision) of text.

        This is the amount by which following text should be offset.
        Text bounding box may extend past the length in some fonts,
        e.g. when using italics or accents.

        The result is returned as a float; it is a whole number if using basic layout.

        Note that the sum of two lengths may not equal the length of a concatenated
        string due to kerning. If you need to adjust for kerning, include the following
        character and subtract its length.

        For example, instead of::

            hello = ImageText.Text("Hello", font).get_length()
            world = ImageText.Text("World", font).get_length()
            helloworld = ImageText.Text("HelloWorld", font).get_length()
            assert hello + world == helloworld

        use::

            hello = (
                ImageText.Text("HelloW", font).get_length() -
                ImageText.Text("W", font).get_length()
            )  # adjusted for kerning
            world = ImageText.Text("World", font).get_length()
            helloworld = ImageText.Text("HelloWorld", font).get_length()
            assert hello + world == helloworld

        or disable kerning with (requires libraqm)::

            hello = ImageText.Text("Hello", font, features=["-kern"]).get_length()
            world = ImageText.Text("World", font, features=["-kern"]).get_length()
            helloworld = ImageText.Text(
                "HelloWorld", font, features=["-kern"]
            ).get_length()
            assert hello + world == helloworld

        :return: Either width for horizontal text, or height for vertical text.
        '''
        split_character = '\n' if isinstance(self.text, str) else b'\n'
        if split_character in self.text:
            msg = "can't measure length of multiline text"
            raise ValueError(msg)
        return self.font.getlength(self.text, self._get_fontmode(), self.direction, self.features, self.language)

    
    def _split(self = None, xy = None, anchor = None, align = ('xy', 'tuple[float, float]', 'anchor', 'str | None', 'align', 'str', 'return', 'list[tuple[tuple[float, float], str, str | bytes]]')):
        pass
    # WARNING: Decompyle incomplete

    
    def get_bbox(self = None, xy = None, anchor = None, align = ((0, 0), None, 'left')):
        '''
        Returns bounding box (in pixels) of text.

        Use :py:meth:`get_length` to get the offset of following text with 1/64 pixel
        precision. The bounding box includes extra margins for some fonts, e.g. italics
        or accents.

        :param xy: The anchor coordinates of the text.
        :param anchor: The text anchor alignment. Determines the relative location of
                       the anchor to the text. The default alignment is top left,
                       specifically ``la`` for horizontal text and ``lt`` for
                       vertical text. See :ref:`text-anchors` for details.
        :param align: For multiline text, ``"left"``, ``"center"``, ``"right"`` or
                      ``"justify"`` determines the relative alignment of lines. Use the
                      ``anchor`` parameter to specify the alignment to ``xy``.

        :return: ``(left, top, right, bottom)`` bounding box
        '''
        bbox = None
        fontmode = self._get_fontmode()
    # WARNING: Decompyle incomplete
