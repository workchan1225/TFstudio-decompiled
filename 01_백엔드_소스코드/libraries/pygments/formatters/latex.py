# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: latex.pyc (Python 3.11)

'''
    pygments.formatters.latex
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for LaTeX fancyvrb output.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from io import StringIO
from pygments.formatter import Formatter
from pygments.lexer import Lexer, do_insertions
from pygments.token import Token, STANDARD_TYPES
from pygments.util import get_bool_opt, get_int_opt
__all__ = [
    'LatexFormatter']

def escape_tex(text, commandprefix):
    return text.replace('\\', '\x00').replace('{', '\x01').replace('}', '\x02').replace('\x00', f'''\\{commandprefix}Zbs{{}}''').replace('\x01', f'''\\{commandprefix}Zob{{}}''').replace('\x02', f'''\\{commandprefix}Zcb{{}}''').replace('^', f'''\\{commandprefix}Zca{{}}''').replace('_', f'''\\{commandprefix}Zus{{}}''').replace('&', f'''\\{commandprefix}Zam{{}}''').replace('<', f'''\\{commandprefix}Zlt{{}}''').replace('>', f'''\\{commandprefix}Zgt{{}}''').replace('#', f'''\\{commandprefix}Zsh{{}}''').replace('%', f'''\\{commandprefix}Zpc{{}}''').replace('$', f'''\\{commandprefix}Zdl{{}}''').replace('-', f'''\\{commandprefix}Zhy{{}}''').replace("'", f'''\\{commandprefix}Zsq{{}}''').replace('"', f'''\\{commandprefix}Zdq{{}}''').replace('~', f'''\\{commandprefix}Zti{{}}''')

DOC_TEMPLATE = '\n\\documentclass{%(docclass)s}\n\\usepackage{fancyvrb}\n\\usepackage{color}\n\\usepackage[%(encoding)s]{inputenc}\n%(preamble)s\n\n%(styledefs)s\n\n\\begin{document}\n\n\\section*{%(title)s}\n\n%(code)s\n\\end{document}\n'
STYLE_TEMPLATE = '\n\\makeatletter\n\\def\\%(cp)s@reset{\\let\\%(cp)s@it=\\relax \\let\\%(cp)s@bf=\\relax%%\n    \\let\\%(cp)s@ul=\\relax \\let\\%(cp)s@tc=\\relax%%\n    \\let\\%(cp)s@bc=\\relax \\let\\%(cp)s@ff=\\relax}\n\\def\\%(cp)s@tok#1{\\csname %(cp)s@tok@#1\\endcsname}\n\\def\\%(cp)s@toks#1+{\\ifx\\relax#1\\empty\\else%%\n    \\%(cp)s@tok{#1}\\expandafter\\%(cp)s@toks\\fi}\n\\def\\%(cp)s@do#1{\\%(cp)s@bc{\\%(cp)s@tc{\\%(cp)s@ul{%%\n    \\%(cp)s@it{\\%(cp)s@bf{\\%(cp)s@ff{#1}}}}}}}\n\\def\\%(cp)s#1#2{\\%(cp)s@reset\\%(cp)s@toks#1+\\relax+\\%(cp)s@do{#2}}\n\n%(styles)s\n\n\\def\\%(cp)sZbs{\\char`\\\\}\n\\def\\%(cp)sZus{\\char`\\_}\n\\def\\%(cp)sZob{\\char`\\{}\n\\def\\%(cp)sZcb{\\char`\\}}\n\\def\\%(cp)sZca{\\char`\\^}\n\\def\\%(cp)sZam{\\char`\\&}\n\\def\\%(cp)sZlt{\\char`\\<}\n\\def\\%(cp)sZgt{\\char`\\>}\n\\def\\%(cp)sZsh{\\char`\\#}\n\\def\\%(cp)sZpc{\\char`\\%%}\n\\def\\%(cp)sZdl{\\char`\\$}\n\\def\\%(cp)sZhy{\\char`\\-}\n\\def\\%(cp)sZsq{\\char`\\\'}\n\\def\\%(cp)sZdq{\\char`\\"}\n\\def\\%(cp)sZti{\\char`\\~}\n%% for compatibility with earlier versions\n\\def\\%(cp)sZat{@}\n\\def\\%(cp)sZlb{[}\n\\def\\%(cp)sZrb{]}\n\\makeatother\n'

def _get_ttype_name(ttype):
    fname = STANDARD_TYPES.get(ttype)
    if fname:
        return fname
    aname = None
# WARNING: Decompyle incomplete


class LatexFormatter(Formatter):
    '''
    Format tokens as LaTeX code. This needs the `fancyvrb` and `color`
    standard packages.

    Without the `full` option, code is formatted as one ``Verbatim``
    environment, like this:

    .. sourcecode:: latex

        \\begin{Verbatim}[commandchars=\\\\\\{\\}]
        \\PY{k}{def }\\PY{n+nf}{foo}(\\PY{n}{bar}):
            \\PY{k}{pass}
        \\end{Verbatim}

    Wrapping can be disabled using the `nowrap` option.

    The special command used here (``\\PY``) and all the other macros it needs
    are output by the `get_style_defs` method.

    With the `full` option, a complete LaTeX document is output, including
    the command definitions in the preamble.

    The `get_style_defs()` method of a `LatexFormatter` returns a string
    containing ``\\def`` commands defining the macros needed inside the
    ``Verbatim`` environments.

    Additional options accepted:

    `nowrap`
        If set to ``True``, don\'t wrap the tokens at all, not even inside a
        ``\\begin{Verbatim}`` environment. This disables most other options
        (default: ``False``).

    `style`
        The style to use, can be a string or a Style subclass (default:
        ``\'default\'``).

    `full`
        Tells the formatter to output a "full" document, i.e. a complete
        self-contained document (default: ``False``).

    `title`
        If `full` is true, the title that should be used to caption the
        document (default: ``\'\'``).

    `docclass`
        If the `full` option is enabled, this is the document class to use
        (default: ``\'article\'``).

    `preamble`
        If the `full` option is enabled, this can be further preamble commands,
        e.g. ``\\usepackage`` (default: ``\'\'``).

    `linenos`
        If set to ``True``, output line numbers (default: ``False``).

    `linenostart`
        The line number for the first line (default: ``1``).

    `linenostep`
        If set to a number n > 1, only every nth line number is printed.

    `verboptions`
        Additional options given to the Verbatim environment (see the *fancyvrb*
        docs for possible values) (default: ``\'\'``).

    `commandprefix`
        The LaTeX commands used to produce colored output are constructed
        using this prefix and some letters (default: ``\'PY\'``).

        .. versionadded:: 0.7
        .. versionchanged:: 0.10
           The default is now ``\'PY\'`` instead of ``\'C\'``.

    `texcomments`
        If set to ``True``, enables LaTeX comment lines.  That is, LaTex markup
        in comment tokens is not escaped so that LaTeX can render it (default:
        ``False``).

        .. versionadded:: 1.2

    `mathescape`
        If set to ``True``, enables LaTeX math mode escape in comments. That
        is, ``\'$...$\'`` inside a comment will trigger math mode (default:
        ``False``).

        .. versionadded:: 1.2

    `escapeinside`
        If set to a string of length 2, enables escaping to LaTeX. Text
        delimited by these 2 characters is read as LaTeX code and
        typeset accordingly. It has no effect in string literals. It has
        no effect in comments if `texcomments` or `mathescape` is
        set. (default: ``\'\'``).

        .. versionadded:: 2.0

    `envname`
        Allows you to pick an alternative environment name replacing Verbatim.
        The alternate environment still has to support Verbatim\'s option syntax.
        (default: ``\'Verbatim\'``).

        .. versionadded:: 2.0
    '''
    name = 'LaTeX'
    aliases = [
        'latex',
        'tex']
    filenames = [
        '*.tex']
    
    def __init__(self, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def _create_stylesheet(self):
        t2n = {
            Token: '' }
        self.ttype2name = {
            Token: '' }
        c2d = { }
        self.cmd2def = { }
        cp = self.commandprefix
        
        def rgbcolor(col):
            pass
        # WARNING: Decompyle incomplete

        for ttype, ndef in self.style:
            name = _get_ttype_name(ttype)
            cmndef = ''
            if ndef['bold']:
                cmndef += '\\let\\$$@bf=\\textbf'
            if ndef['italic']:
                cmndef += '\\let\\$$@it=\\textit'
            if ndef['underline']:
                cmndef += '\\let\\$$@ul=\\underline'
            if ndef['roman']:
                cmndef += '\\let\\$$@ff=\\textrm'
            if ndef['sans']:
                cmndef += '\\let\\$$@ff=\\textsf'
            if ndef['mono']:
                cmndef += '\\let\\$$@ff=\\textsf'
            if ndef['color']:
                cmndef += '\\def\\$$@tc##1{{\\textcolor[rgb]{{{}}}{{##1}}}}'.format(rgbcolor(ndef['color']))
            if ndef['border']:
                cmndef += '\\def\\$$@bc##1{{{{\\setlength{{\\fboxsep}}{{\\string -\\fboxrule}}\\fcolorbox[rgb]{{{}}}{{{}}}{{\\strut ##1}}}}}}'.format(rgbcolor(ndef['border']), rgbcolor(ndef['bgcolor']))
            elif ndef['bgcolor']:
                cmndef += '\\def\\$$@bc##1{{{{\\setlength{{\\fboxsep}}{{0pt}}\\colorbox[rgb]{{{}}}{{\\strut ##1}}}}}}'.format(rgbcolor(ndef['bgcolor']))
            if cmndef == '':
                continue
            cmndef = cmndef.replace('$$', cp)
            t2n[ttype] = name
            c2d[name] = cmndef
            return None

    
    def get_style_defs(self, arg = ('',)):
        '''
        Return the command sequences needed to define the commands
        used to format text in the verbatim environment. ``arg`` is ignored.
        '''
        cp = self.commandprefix
        styles = []
        for name, definition in self.cmd2def.items():
            styles.append(f'''\\@namedef{{{cp}@tok@{name}}}{{{definition}}}''')
            return STYLE_TEMPLATE % {
                'cp': self.commandprefix,
                'styles': '\n'.join(styles) }

    
    def format_unencoded(self, tokensource, outfile):
        t2n = self.ttype2name
        cp = self.commandprefix
        if self.full:
            realoutfile = outfile
            outfile = StringIO()
        if not self.nowrap:
            outfile.write('\\begin{' + self.envname + '}[commandchars=\\\\\\{\\}')
            if self.linenos:
                step = self.linenostep
                start = self.linenostart
                if start:
                    if ',firstnumber=%d' % start or step:
                        if not ',stepnumber=%d' % step:
                            outfile.write(',numbers=left' + '' + '')
                            if self.mathescape and self.texcomments or self.escapeinside:
                                outfile.write(',codes={\\catcode`\\$=3\\catcode`\\^=7\\catcode`\\_=8\\relax}')
            if self.verboptions:
                outfile.write(',' + self.verboptions)
            outfile.write(']\n')
    # WARNING: Decompyle incomplete



class LatexEmbeddedLexer(Lexer):
    '''
    This lexer takes one lexer as argument, the lexer for the language
    being formatted, and the left and right delimiters for escaped text.

    First everything is scanned using the language lexer to obtain
    strings and comments. All other consecutive tokens are merged and
    the resulting text is scanned for escaped segments, which are given
    the Token.Escape type. Finally text that is not escaped is scanned
    again with the language lexer.
    '''
    
    def __init__(self, left, right, lang, **options):
        self.left = left
        self.right = right
        self.lang = lang
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        buffered = ''
        insertions = []
        insertion_buf = []
    # WARNING: Decompyle incomplete

    
    def _find_safe_escape_tokens(self, text):
        ''' find escape tokens that are not in strings or comments '''
        pass
    # WARNING: Decompyle incomplete

    
    def _filter_to(self, it, pred):
        ''' Keep only the tokens that match `pred`, merge the others together '''
        pass
    # WARNING: Decompyle incomplete

    
    def _find_escape_tokens(self, text):
        ''' Find escape tokens within text, give token=None otherwise '''
        pass
    # WARNING: Decompyle incomplete
