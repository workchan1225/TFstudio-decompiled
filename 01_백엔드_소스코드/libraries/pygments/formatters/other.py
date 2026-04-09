# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: other.pyc (Python 3.11)

'''
    pygments.formatters.other
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Other formatters: NullFormatter, RawTokenFormatter.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.formatter import Formatter
from pygments.util import get_choice_opt
from pygments.token import Token
from pygments.console import colorize
__all__ = [
    'NullFormatter',
    'RawTokenFormatter',
    'TestcaseFormatter']

class NullFormatter(Formatter):
    '''
    Output the text unchanged without any formatting.
    '''
    name = 'Text only'
    aliases = [
        'text',
        'null']
    filenames = [
        '*.txt']
    
    def format(self, tokensource, outfile):
        enc = self.encoding
        for ttype, value in tokensource:
            if enc:
                outfile.write(value.encode(enc))
                continue
            outfile.write(value)
            return None



class RawTokenFormatter(Formatter):
    """
    Format tokens as a raw representation for storing token streams.

    The format is ``tokentype<TAB>repr(tokenstring)\\n``. The output can later
    be converted to a token stream with the `RawTokenLexer`, described in the
    :doc:`lexer list <lexers>`.

    Only two options are accepted:

    `compress`
        If set to ``'gz'`` or ``'bz2'``, compress the output with the given
        compression algorithm after encoding (default: ``''``).
    `error_color`
        If set to a color name, highlight error tokens using that color.  If
        set but with no value, defaults to ``'red'``.

        .. versionadded:: 0.11

    """
    name = 'Raw tokens'
    aliases = [
        'raw',
        'tokens']
    filenames = [
        '*.raw']
    unicodeoutput = False
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def format(self, tokensource, outfile):
        pass
    # WARNING: Decompyle incomplete


TESTCASE_BEFORE = '    def testNeedsName(lexer):\n        fragment = %r\n        tokens = [\n'
TESTCASE_AFTER = '        ]\n        assert list(lexer.get_tokens(fragment)) == tokens\n'

class TestcaseFormatter(Formatter):
    '''
    Format tokens as appropriate for a new testcase.

    .. versionadded:: 2.0
    '''
    name = 'Testcase'
    aliases = [
        'testcase']
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def format(self, tokensource, outfile):
        indentation = '            '
        rawbuf = []
        outbuf = []
    # WARNING: Decompyle incomplete
