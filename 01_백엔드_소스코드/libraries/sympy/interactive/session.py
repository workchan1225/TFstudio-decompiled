# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session.pyc (Python 3.11)

'''Tools for setting up interactive sessions. '''
from sympy.external.gmpy import GROUND_TYPES
from sympy.external.importtools import version_tuple
from sympy.interactive.printing import init_printing
from sympy.utilities.misc import ARCH
preexec_source = "from sympy import *\nx, y, z, t = symbols('x y z t')\nk, m, n = symbols('k m n', integer=True)\nf, g, h = symbols('f g h', cls=Function)\ninit_printing()\n"
verbose_message = 'These commands were executed:\n%(source)s\nDocumentation can be found at https://docs.sympy.org/%(version)s\n'
no_ipython = "Could not locate IPython. Having IPython installed is greatly recommended.\nSee http://ipython.scipy.org for more details. If you use Debian/Ubuntu,\njust install the 'ipython' package and start isympy again.\n"

def _make_message(ipython, quiet, source = (True, False, None)):
    '''Create a banner for an interactive session. '''
    sympy_version = __version__
    import sympy
    SYMPY_DEBUG = SYMPY_DEBUG
    import sympy
    import sys
    import os
    if quiet:
        return ''
    python_version = None % sys.version_info[:3]
    if ipython:
        shell_name = 'IPython'
    else:
        shell_name = 'Python'
    info = [
        'ground types: %s' % GROUND_TYPES]
    cache = os.getenv('SYMPY_USE_CACHE')
# WARNING: Decompyle incomplete


def int_to_Integer(s):
    """
    Wrap integer literals with Integer.

    This is based on the decistmt example from
    https://docs.python.org/3/library/tokenize.html.

    Only integer literals are converted.  Float literals are left alone.

    Examples
    ========

    >>> from sympy import Integer # noqa: F401
    >>> from sympy.interactive.session import int_to_Integer
    >>> s = '1.2 + 1/2 - 0x12 + a1'
    >>> int_to_Integer(s)
    '1.2 +Integer (1 )/Integer (2 )-Integer (0x12 )+a1 '
    >>> s = 'print (1/2)'
    >>> int_to_Integer(s)
    'print (Integer (1 )/Integer (2 ))'
    >>> exec(s)
    0.5
    >>> exec(int_to_Integer(s))
    1/2
    """
    generate_tokens = generate_tokens
    untokenize = untokenize
    NUMBER = NUMBER
    NAME = NAME
    OP = OP
    import tokenize
    StringIO = StringIO
    import io
    
    def _is_int(num):
        '''
        Returns true if string value num (with token NUMBER) represents an integer.
        '''
        if '.' in num and 'j' in num.lower() or 'e' in num.lower():
            return False

    result = []
    g = generate_tokens(StringIO(s).readline)
    for toknum, tokval, _, _, _ in g:
        if toknum == NUMBER and _is_int(tokval):
            result.extend([
                (NAME, 'Integer'),
                (OP, '('),
                (NUMBER, tokval),
                (OP, ')')])
            continue
        result.append((toknum, tokval))
        return untokenize(result)


def enable_automatic_int_sympification(shell):
    '''
    Allow IPython to automatically convert integer literals to Integer.
    '''
    pass
# WARNING: Decompyle incomplete


def enable_automatic_symbols(shell):
    '''Allow IPython to automatically create symbols (``isympy -a``). '''
    pass
# WARNING: Decompyle incomplete


def init_ipython_session(shell, argv, auto_symbols, auto_int_to_Integer = (None, [], False, False)):
    '''Construct new IPython session. '''
    import IPython
    if version_tuple(IPython.__version__) >= version_tuple('0.11'):
        if not shell:
            if version_tuple(IPython.__version__) >= version_tuple('1.0'):
                ipapp = ipapp
                import IPython.terminal
            else:
                ipapp = ipapp
                import IPython.frontend.terminal
            app = ipapp.TerminalIPythonApp()
            app.display_banner = False
            app.initialize(argv)
            shell = app.shell
        if auto_symbols:
            enable_automatic_symbols(shell)
        if auto_int_to_Integer:
            enable_automatic_int_sympification(shell)
        return shell
    make_IPython = make_IPython
    import IPython.Shell
    return make_IPython(argv)


def init_python_session():
    '''Construct new Python session. '''
    pass
# WARNING: Decompyle incomplete


def init_session(ipython, pretty_print, order, use_unicode, use_latex, quiet, auto_symbols, auto_int_to_Integer, str_printer, pretty_printer, latex_printer, argv = (None, True, None, None, None, False, False, False, None, None, None, [])):
    """
    Initialize an embedded IPython or Python session. The IPython session is
    initiated with the --pylab option, without the numpy imports, so that
    matplotlib plotting can be interactive.

    Parameters
    ==========

    pretty_print: boolean
        If True, use pretty_print to stringify;
        if False, use sstrrepr to stringify.
    order: string or None
        There are a few different settings for this parameter:
        lex (default), which is lexographic order;
        grlex, which is graded lexographic order;
        grevlex, which is reversed graded lexographic order;
        old, which is used for compatibility reasons and for long expressions;
        None, which sets it to lex.
    use_unicode: boolean or None
        If True, use unicode characters;
        if False, do not use unicode characters.
    use_latex: boolean or None
        If True, use latex rendering if IPython GUI's;
        if False, do not use latex rendering.
    quiet: boolean
        If True, init_session will not print messages regarding its status;
        if False, init_session will print messages regarding its status.
    auto_symbols: boolean
        If True, IPython will automatically create symbols for you.
        If False, it will not.
        The default is False.
    auto_int_to_Integer: boolean
        If True, IPython will automatically wrap int literals with Integer, so
        that things like 1/2 give Rational(1, 2).
        If False, it will not.
        The default is False.
    ipython: boolean or None
        If True, printing will initialize for an IPython console;
        if False, printing will initialize for a normal console;
        The default is None, which automatically determines whether we are in
        an ipython instance or not.
    str_printer: function, optional, default=None
        A custom string printer function. This should mimic
        sympy.printing.sstrrepr().
    pretty_printer: function, optional, default=None
        A custom pretty printer. This should mimic sympy.printing.pretty().
    latex_printer: function, optional, default=None
        A custom LaTeX printer. This should mimic sympy.printing.latex()
        This should mimic sympy.printing.latex().
    argv: list of arguments for IPython
        See sympy.bin.isympy for options that can be used to initialize IPython.

    See Also
    ========

    sympy.interactive.printing.init_printing: for examples and the rest of the parameters.


    Examples
    ========

    >>> from sympy import init_session, Symbol, sin, sqrt
    >>> sin(x) #doctest: +SKIP
    NameError: name 'x' is not defined
    >>> init_session() #doctest: +SKIP
    >>> sin(x) #doctest: +SKIP
    sin(x)
    >>> sqrt(5) #doctest: +SKIP
      ___
    \\/ 5
    >>> init_session(pretty_print=False) #doctest: +SKIP
    >>> sqrt(5) #doctest: +SKIP
    sqrt(5)
    >>> y + x + y**2 + x**2 #doctest: +SKIP
    x**2 + x + y**2 + y
    >>> init_session(order='grlex') #doctest: +SKIP
    >>> y + x + y**2 + x**2 #doctest: +SKIP
    x**2 + y**2 + x + y
    >>> init_session(order='grevlex') #doctest: +SKIP
    >>> y * x**2 + x * y**2 #doctest: +SKIP
    x**2*y + x*y**2
    >>> init_session(order='old') #doctest: +SKIP
    >>> x**2 + y**2 + x + y #doctest: +SKIP
    x + y + x**2 + y**2
    >>> theta = Symbol('theta') #doctest: +SKIP
    >>> theta #doctest: +SKIP
    theta
    >>> init_session(use_unicode=True) #doctest: +SKIP
    >>> theta # doctest: +SKIP
    θ
    """
    pass
# WARNING: Decompyle incomplete
