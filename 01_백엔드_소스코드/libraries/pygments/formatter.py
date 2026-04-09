# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: formatter.pyc (Python 3.11)

'''
    pygments.formatter
    ~~~~~~~~~~~~~~~~~~

    Base formatter class.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import codecs
from pygments.util import get_bool_opt
from pygments.styles import get_style_by_name
__all__ = [
    'Formatter']

def _lookup_style(style):
    if isinstance(style, str):
        return get_style_by_name(style)


class Formatter:
    '''
    Converts a token stream to text.

    Formatters should have attributes to help selecting them. These
    are similar to the corresponding :class:`~pygments.lexer.Lexer`
    attributes.

    .. autoattribute:: name
       :no-value:

    .. autoattribute:: aliases
       :no-value:

    .. autoattribute:: filenames
       :no-value:

    You can pass options as keyword arguments to the constructor.
    All formatters accept these basic options:

    ``style``
        The style to use, can be a string or a Style subclass
        (default: "default"). Not used by e.g. the
        TerminalFormatter.
    ``full``
        Tells the formatter to output a "full" document, i.e.
        a complete self-contained document. This doesn\'t have
        any effect for some formatters (default: false).
    ``title``
        If ``full`` is true, the title that should be used to
        caption the document (default: \'\').
    ``encoding``
        If given, must be an encoding name. This will be used to
        convert the Unicode token strings to byte strings in the
        output. If it is "" or None, Unicode strings will be written
        to the output file, which most file-like objects do not
        support (default: None).
    ``outencoding``
        Overrides ``encoding`` if given.

    '''
    name = None
    aliases = []
    filenames = []
    unicodeoutput = True
    
    def __init__(self, **options):
