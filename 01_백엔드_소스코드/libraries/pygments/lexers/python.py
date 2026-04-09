# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: python.pyc (Python 3.11)

'''
    pygments.lexers.python
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Python and related languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import keyword
from pygments.lexer import DelegatingLexer, RegexLexer, include, bygroups, using, default, words, combined, this
from pygments.util import get_bool_opt, shebang_matches
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Generic, Other, Error, Whitespace
from pygments import unistring as uni
__all__ = [
    'PythonLexer',
    'PythonConsoleLexer',
    'PythonTracebackLexer',
    'Python2Lexer',
    'Python2TracebackLexer',
    'CythonLexer',
    'DgLexer',
    'NumPyLexer']

class PythonLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'PythonLexer'
    __doc__ = '\n    For Python source code (version 3.x).\n\n    .. versionchanged:: 2.5\n       This is now the default ``PythonLexer``.  It is still available as the\n       alias ``Python3Lexer``.\n    '
    name = 'Python'
    url = 'https://www.python.org'
    aliases = [
        'python',
        'py',
        'sage',
        'python3',
        'py3',
        'bazel',
        'starlark',
        'pyi']
    filenames = [
        '*.py',
        '*.pyw',
        '*.pyi',
        '*.jy',
        '*.sage',
        '*.sc',
        'SConstruct',
        'SConscript',
        '*.bzl',
        'BUCK',
        'BUILD',
        'BUILD.bazel',
        'WORKSPACE',
        '*.tac']
    mimetypes = [
        'text/x-python',
        'application/x-python',
        'text/x-python3',
        'application/x-python3']
    version_added = '0.10'
    uni_name = f'''[{uni.xid_start}][{uni.xid_continue}]*'''
    
    def innerstring_rules(ttype):
        return [
            ('%(\\(\\w+\\))?[-#0 +]*([0-9]+|[*])?(\\.([0-9]+|[*]))?[hlL]?[E-GXc-giorsaux%]', String.Interpol),
            ('\\{((\\w+)((\\.\\w+)|(\\[[^\\]]+\\]))*)?(\\![sra])?(\\:(.?[<>=\\^])?[-+ ]?#?0?(\\d+)?,?(\\.\\d+)?[E-GXb-gnosx%]?)?\\}', String.Interpol),
            ('[^\\\\\\\'"%{\\n]+', ttype),
            ('[\\\'"\\\\]', ttype),
            ('%|(\\{{1,2})', ttype)]

    
    def fstring_rules(ttype):
        return [
            ('\\}', String.Interpol),
            ('\\{', String.Interpol, 'expr-inside-fstring'),
            ('[^\\\\\\\'"{}\\n]+', ttype),
            ('[\\\'"\\\\]', ttype)]

# WARNING: Decompyle incomplete

Python3Lexer = PythonLexer

class Python2Lexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'Python2Lexer'
    __doc__ = '\n    For Python 2.x source code.\n\n    .. versionchanged:: 2.5\n       This class has been renamed from ``PythonLexer``.  ``PythonLexer`` now\n       refers to the Python 3 variant.  File name patterns like ``*.py`` have\n       been moved to Python 3 as well.\n    '
    name = 'Python 2.x'
    url = 'https://www.python.org'
    aliases = [
        'python2',
        'py2']
    filenames = []
    mimetypes = [
        'text/x-python2',
        'application/x-python2']
    version_added = ''
    
    def innerstring_rules(ttype):
        return [
            ('%(\\(\\w+\\))?[-#0 +]*([0-9]+|[*])?(\\.([0-9]+|[*]))?[hlL]?[E-GXc-giorsux%]', String.Interpol),
            ('[^\\\\\\\'"%\\n]+', ttype),
            ('[\\\'"\\\\]', ttype),
            ('%', ttype)]

# WARNING: Decompyle incomplete


class _PythonConsoleLexerBase(RegexLexer):
    name = 'Python console session'
    aliases = [
        'pycon',
        'python-console']
    mimetypes = [
        'text/x-python-doctest']
    tokens = {
        'root': [
            ('(>>> )(.*\\n)', bygroups(Generic.Prompt, Other.Code), 'continuations'),
            ('(>>>)(\\n)', bygroups(Generic.Prompt, Whitespace)),
            ('(\\^C)?Traceback \\(most recent call last\\):\\n', Other.Traceback, 'traceback'),
            ('  File "[^"]+", line \\d+', Other.Traceback, 'traceback'),
            ('.*\\n', Generic.Output)],
        'continuations': [
            ('(\\.\\.\\. )(.*\\n)', bygroups(Generic.Prompt, Other.Code)),
            ('(\\.\\.\\.)(\\n)', bygroups(Generic.Prompt, Whitespace)),
            default('#pop')],
        'traceback': [
            ('(?=>>>( |$))', Text, '#pop'),
            ('(KeyboardInterrupt)(\\n)', bygroups(Name.Class, Whitespace)),
            ('.*\\n', Other.Traceback)] }


class PythonConsoleLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class PythonTracebackLexer(RegexLexer):
    '''
    For Python 3.x tracebacks, with support for chained exceptions.

    .. versionchanged:: 2.5
       This is now the default ``PythonTracebackLexer``.  It is still available
       as the alias ``Python3TracebackLexer``.
    '''
    name = 'Python Traceback'
    aliases = [
        'pytb',
        'py3tb']
    filenames = [
        '*.pytb',
        '*.py3tb']
    mimetypes = [
        'text/x-python-traceback',
        'text/x-python3-traceback']
    url = 'https://python.org'
    version_added = '1.0'
    tokens = {
        'root': [
            ('\\n', Whitespace),
            ('^(\\^C)?Traceback \\(most recent call last\\):\\n', Generic.Traceback, 'intb'),
            ('^During handling of the above exception, another exception occurred:\\n\\n', Generic.Traceback),
            ('^The above exception was the direct cause of the following exception:\\n\\n', Generic.Traceback),
            ('^(?=  File "[^"]+", line \\d+)', Generic.Traceback, 'intb'),
            ('^.*\\n', Other)],
        'intb': [
            ('^(  File )("[^"]+")(, line )(\\d+)(, in )(.+)(\\n)', bygroups(Text, Name.Builtin, Text, Number, Text, Name, Whitespace)),
            ('^(  File )("[^"]+")(, line )(\\d+)(\\n)', bygroups(Text, Name.Builtin, Text, Number, Whitespace)),
            ('^(    )(.+)(\\n)', bygroups(Whitespace, using(PythonLexer), Whitespace), 'markers'),
            ('^([ \\t]*)(\\.\\.\\.)(\\n)', bygroups(Whitespace, Comment, Whitespace)),
            ('^([^:]+)(: )(.+)(\\n)', bygroups(Generic.Error, Text, Name, Whitespace), '#pop'),
            ('^([a-zA-Z_][\\w.]*)(:?\\n)', bygroups(Generic.Error, Whitespace), '#pop'),
            default('#pop')],
        'markers': [
            ('^( {4,})([~^]+)(\\n)', bygroups(Whitespace, Punctuation.Marker, Whitespace), '#pop'),
            default('#pop')] }

Python3TracebackLexer = PythonTracebackLexer

class Python2TracebackLexer(RegexLexer):
    '''
    For Python tracebacks.

    .. versionchanged:: 2.5
       This class has been renamed from ``PythonTracebackLexer``.
       ``PythonTracebackLexer`` now refers to the Python 3 variant.
    '''
    name = 'Python 2.x Traceback'
    aliases = [
        'py2tb']
    filenames = [
        '*.py2tb']
    mimetypes = [
        'text/x-python2-traceback']
    url = 'https://python.org'
    version_added = '0.7'
    tokens = {
        'root': [
            ('^(\\^C)?(Traceback.*\\n)', bygroups(Text, Generic.Traceback), 'intb'),
            ('^(?=  File "[^"]+", line \\d+)', Generic.Traceback, 'intb'),
            ('^.*\\n', Other)],
        'intb': [
            ('^(  File )("[^"]+")(, line )(\\d+)(, in )(.+)(\\n)', bygroups(Text, Name.Builtin, Text, Number, Text, Name, Whitespace)),
            ('^(  File )("[^"]+")(, line )(\\d+)(\\n)', bygroups(Text, Name.Builtin, Text, Number, Whitespace)),
            ('^(    )(.+)(\\n)', bygroups(Text, using(Python2Lexer), Whitespace), 'marker'),
            ('^([ \\t]*)(\\.\\.\\.)(\\n)', bygroups(Text, Comment, Whitespace)),
            ('^([^:]+)(: )(.+)(\\n)', bygroups(Generic.Error, Text, Name, Whitespace), '#pop'),
            ('^([a-zA-Z_]\\w*)(:?\\n)', bygroups(Generic.Error, Whitespace), '#pop')],
        'marker': [
            ('( {4,})(\\^)', bygroups(Text, Punctuation.Marker), '#pop'),
            default('#pop')] }


class CythonLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'CythonLexer'
    __doc__ = '\n    For Pyrex and Cython source code.\n    '
    name = 'Cython'
    url = 'https://cython.org'
    aliases = [
        'cython',
        'pyx',
        'pyrex']
    filenames = [
        '*.pyx',
        '*.pxd',
        '*.pxi']
    mimetypes = [
        'text/x-cython',
        'application/x-cython']
    version_added = '1.1'
# WARNING: Decompyle incomplete


class DgLexer(RegexLexer):
    '''
    Lexer for dg,
    a functional and object-oriented programming language
    running on the CPython 3 VM.
    '''
    name = 'dg'
    aliases = [
        'dg']
    filenames = [
        '*.dg']
    mimetypes = [
        'text/x-dg']
    url = 'http://pyos.github.io/dg'
    version_added = '1.6'
    tokens = {
        'root': [
            ('\\s+', Text),
            ('#.*?$', Comment.Single),
            ('(?i)0b[01]+', Number.Bin),
            ('(?i)0o[0-7]+', Number.Oct),
            ('(?i)0x[0-9a-f]+', Number.Hex),
            ('(?i)[+-]?[0-9]+\\.[0-9]+(e[+-]?[0-9]+)?j?', Number.Float),
            ('(?i)[+-]?[0-9]+e[+-]?\\d+j?', Number.Float),
            ('(?i)[+-]?[0-9]+j?', Number.Integer),
            ("(?i)(br|r?b?)'''", String, combined('stringescape', 'tsqs', 'string')),
            ('(?i)(br|r?b?)"""', String, combined('stringescape', 'tdqs', 'string')),
            ("(?i)(br|r?b?)'", String, combined('stringescape', 'sqs', 'string')),
            ('(?i)(br|r?b?)"', String, combined('stringescape', 'dqs', 'string')),
            ("`\\w+'*`", Operator),
            ('\\b(and|in|is|or|where)\\b', Operator.Word),
            ('[!$%&*+\\-./:<-@\\\\^|~;,]+', Operator),
            (words(('bool', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', "dict'", 'float', 'frozenset', 'int', 'list', "list'", 'memoryview', 'object', 'property', 'range', 'set', "set'", 'slice', 'staticmethod', 'str', 'super', 'tuple', "tuple'", 'type'), prefix = '(?<!\\.)', suffix = "(?![\\'\\w])"), Name.Builtin),
            (words(('__import__', 'abs', 'all', 'any', 'bin', 'bind', 'chr', 'cmp', 'compile', 'complex', 'delattr', 'dir', 'divmod', 'drop', 'dropwhile', 'enumerate', 'eval', 'exhaust', 'filter', 'flip', 'foldl1?', 'format', 'fst', 'getattr', 'globals', 'hasattr', 'hash', 'head', 'hex', 'id', 'init', 'input', 'isinstance', 'issubclass', 'iter', 'iterate', 'last', 'len', 'locals', 'map', 'max', 'min', 'next', 'oct', 'open', 'ord', 'pow', 'print', 'repr', 'reversed', 'round', 'setattr', 'scanl1?', 'snd', 'sorted', 'sum', 'tail', 'take', 'takewhile', 'vars', 'zip'), prefix = '(?<!\\.)', suffix = "(?![\\'\\w])"), Name.Builtin),
            ("(?<!\\.)(self|Ellipsis|NotImplemented|None|True|False)(?!['\\w])", Name.Builtin.Pseudo),
            ("(?<!\\.)[A-Z]\\w*(Error|Exception|Warning)'*(?!['\\w])", Name.Exception),
            ("(?<!\\.)(Exception|GeneratorExit|KeyboardInterrupt|StopIteration|SystemExit)(?!['\\w])", Name.Exception),
            ("(?<![\\w.])(except|finally|for|if|import|not|otherwise|raise|subclass|while|with|yield)(?!['\\w])", Keyword.Reserved),
            ("[A-Z_]+'*(?!['\\w])", Name),
            ("[A-Z]\\w+'*(?!['\\w])", Keyword.Type),
            ("\\w+'*", Name),
            ('[()]', Punctuation),
            ('.', Error)],
        'stringescape': [
            ('\\\\([\\\\abfnrtv"\\\']|\\n|N\\{.*?\\}|u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})', String.Escape)],
        'string': [
            ('%(\\(\\w+\\))?[-#0 +]*([0-9]+|[*])?(\\.([0-9]+|[*]))?[hlL]?[E-GXc-giorsux%]', String.Interpol),
            ('[^\\\\\\\'"%\\n]+', String),
            ('[\\\'"\\\\]', String),
            ('%', String),
            ('\\n', String)],
        'dqs': [
            ('"', String, '#pop')],
        'sqs': [
            ("'", String, '#pop')],
        'tdqs': [
            ('"""', String, '#pop')],
        'tsqs': [
            ("'''", String, '#pop')] }


class NumPyLexer(PythonLexer):
    '''
    A Python lexer recognizing Numerical Python builtins.
    '''
    name = 'NumPy'
    url = 'https://numpy.org/'
    aliases = [
        'numpy']
    version_added = '0.10'
    mimetypes = []
    filenames = []
    EXTRA_KEYWORDS = {
        'c_',
        'i0',
        'r_',
        's_',
        'abs',
        'add',
        'all',
        'any',
        'cos',
        'cov',
        'dot',
        'exp',
        'eye',
        'fft',
        'fix',
        'inf',
        'inv',
        'ix_',
        'log',
        'mat',
        'max',
        'min',
        'mod',
        'nan',
        'ptp',
        'put',
        'sin',
        'std',
        'sum',
        'svd',
        'tan',
        'tri',
        'var',
        'who',
        'alen',
        'amax',
        'amin',
        'beta',
        'bmat',
        'ceil',
        'clip',
        'conj',
        'copy',
        'cosh',
        'diag',
        'diff',
        'disp',
        'dump',
        'fabs',
        'fill',
        'flat',
        'fmod',
        'ifft',
        'imag',
        'info',
        'item',
        'kron',
        'less',
        'load',
        'log2',
        'mean',
        'modf',
        'ndim',
        'ones',
        'pinv',
        'poly',
        'prod',
        'ranf',
        'rank',
        'real',
        'rint',
        'roll',
        'seed',
        'sign',
        'sinc',
        'sinh',
        'size',
        'sort',
        'sqrt',
        'take',
        'tanh',
        'test',
        'tile',
        'tril',
        'triu',
        'vdot',
        'view',
        'angle',
        'array',
        'bytes',
        'cross',
        'dtype',
        'dumps',
        'empty',
        'equal',
        'expm1',
        'finfo',
        'floor',
        'frexp',
        'hypot',
        'inner',
        'isinf',
        'isnan',
        'ldexp',
        'loads',
        'log10',
        'log1p',
        'lstsq',
        'mgrid',
        'msort',
        'ogrid',
        'outer',
        'place',
        'power',
        'ravel',
        'roots',
        'rot90',
        'round',
        'shape',
        'slice',
        'solve',
        'split',
        'trace',
        'trapz',
        'where',
        'zeros',
        'append',
        'arange',
        'arccos',
        'arcsin',
        'arctan',
        'argmax',
        'argmin',
        'around',
        'astype',
        'choose',
        'cumsum',
        'delete',
        'divide',
        'dsplit',
        'dstack',
        'fliplr',
        'flipud',
        'geterr',
        'gumbel',
        'hsplit',
        'hstack',
        'insert',
        'interp',
        'invert',
        'isreal',
        'kaiser',
        'matrix',
        'median',
        'nanmax',
        'nanmin',
        'nansum',
        'poly1d',
        'reduce',
        'repeat',
        'resize',
        'round_',
        'sample',
        'select',
        'seterr',
        'source',
        'square',
        'tofile',
        'tolist',
        'unique',
        'unwrap',
        'vander',
        'vsplit',
        'vstack',
        'alltrue',
        'arccosh',
        'arcsinh',
        'arctan2',
        'arctanh',
        'argsort',
        'asarray',
        'average',
        'cumprod',
        'ediff1d',
        'extract',
        'fftfreq',
        'flatten',
        'generic',
        'greater',
        'hamming',
        'hanning',
        'indices',
        'itemset',
        'lexsort',
        'loadtxt',
        'maximum',
        'minimum',
        'ndindex',
        'newaxis',
        'nonzero',
        'pkgload',
        'poisson',
        'polyadd',
        'polyder',
        'polydiv',
        'polyfit',
        'polyint',
        'polymul',
        'polysub',
        'polyval',
        'product',
        'putmask',
        'randint',
        'require',
        'reshape',
        'savetxt',
        'shuffle',
        'signbit',
        'squeeze',
        'uniform',
        'union1d',
        'weibull',
        'absolute',
        'allclose',
        'alterdot',
        'argwhere',
        'asfarray',
        'asmatrix',
        'asscalar',
        'bartlett',
        'bincount',
        'binomial',
        'blackman',
        'byteswap',
        'can_cast',
        'compress',
        'convolve',
        'corrcoef',
        'diagflat',
        'diagonal',
        'digitize',
        'fftshift',
        'fromfile',
        'fromiter',
        'getfield',
        'gradient',
        'identity',
        'isfinite',
        'isneginf',
        'isposinf',
        'isscalar',
        'issctype',
        'iterable',
        'linspace',
        'logspace',
        'meshgrid',
        'multiply',
        'negative',
        'recarray',
        'rollaxis',
        'setfield',
        'setflags',
        'setxor1d',
        'sometrue',
        'subtract',
        'swapaxes',
        'tostring',
        'typeDict',
        'typename',
        'unique1d',
        'vonmises',
        'array_str',
        'base_repr',
        'broadcast',
        'conjugate',
        'correlate',
        'deprecate',
        'getbuffer',
        'geterrobj',
        'histogram',
        'index_exp',
        'iscomplex',
        'isfortran',
        'isrealobj',
        'nanargmax',
        'nanargmin',
        'newbuffer',
        'not_equal',
        'ones_like',
        'piecewise',
        'remainder',
        'row_stack',
        'setdiff1d',
        'seterrobj',
        'tensordot',
        'transpose',
        'vectorize',
        'accumulate',
        'array_repr',
        'arrayrange',
        'asanyarray',
        'atleast_1d',
        'atleast_2d',
        'atleast_3d',
        'bitwise_or',
        'cumproduct',
        'empty_like',
        'fromarrays',
        'frombuffer',
        'frompyfunc',
        'fromstring',
        'getbufsize',
        'geterrcall',
        'issubdtype',
        'left_shift',
        'less_equal',
        'logical_or',
        'nan_to_num',
        'obj2sctype',
        'reciprocal',
        'restoredot',
        'setbufsize',
        'seterrcall',
        'trim_zeros',
        'zeros_like',
        'array_equal',
        'array_equiv',
        'array_split',
        'binary_repr',
        'bitwise_and',
        'bitwise_not',
        'bitwise_xor',
        'byte_bounds',
        'common_type',
        'concatenate',
        'expand_dims',
        'flatnonzero',
        'get_include',
        'histogram2d',
        'histogramdd',
        'intersect1d',
        'issubclass_',
        'issubsctype',
        'logical_and',
        'logical_not',
        'logical_xor',
        'mintypecode',
        'ndenumerate',
        'permutation',
        'right_shift',
        'sctype2char',
        'setmember1d',
        'show_config',
        'true_divide',
        'array2string',
        'column_stack',
        'floor_divide',
        'fromfunction',
        'int_asbuffer',
        'iscomplexobj',
        'newbyteorder',
        'searchsorted',
        'sort_complex',
        'greater_equal',
        'random_sample',
        'real_if_close',
        'unravel_index',
        'asfortranarray',
        'get_array_wrap',
        'intersect1d_nu',
        'maximum_sctype',
        'apply_over_axes',
        'random_integers',
        'set_numeric_ops',
        'standard_normal',
        'apply_along_axis',
        'get_printoptions',
        'may_share_memory',
        'set_printoptions',
        'asarray_chkfinite',
        'ascontiguousarray',
        'get_numpy_include',
        'compare_chararrays',
        'set_string_function',
        'fastCopyAndTranspose',
        'get_numarray_include'}
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete

    
    def analyse_text(text):
