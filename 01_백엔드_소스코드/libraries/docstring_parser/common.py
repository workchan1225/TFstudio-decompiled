# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''Common methods for parsing.'''
import enum
import typing as T
PARAM_KEYWORDS = {
    'arg',
    'key',
    'param',
    'keyword',
    'argument',
    'attribute',
    'parameter'}
RAISES_KEYWORDS = {
    'raise',
    'except',
    'raises',
    'exception'}
DEPRECATION_KEYWORDS = {
    'deprecation',
    'deprecated'}
RETURNS_KEYWORDS = {
    'return',
    'returns'}
YIELDS_KEYWORDS = {
    'yield',
    'yields'}
EXAMPLES_KEYWORDS = {
    'example',
    'examples'}

class ParseError(RuntimeError):
    '''Base class for all parsing related errors.'''
    pass


class DocstringStyle(enum.Enum):
    '''Docstring style.'''
    REST = 1
    GOOGLE = 2
    NUMPYDOC = 3
    EPYDOC = 4
    AUTO = 255


class RenderingStyle(enum.Enum):
    '''Rendering style when unparsing parsed docstrings.'''
    COMPACT = 1
    CLEAN = 2
    EXPANDED = 3


class DocstringMeta:
    '''Docstring meta information.

    Symbolizes lines in form of

        :param arg: description
        :raises ValueError: if something happens
    '''
    
    def __init__(self = None, args = None, description = None):
        """Initialize self.

        :param args: list of arguments. The exact content of this variable is
            dependent on the kind of docstring; it's used to distinguish
            between custom docstring meta information items.
        :param description: associated docstring description.
        """
        self.args = args
        self.description = description



class DocstringParam(DocstringMeta):
    pass
# WARNING: Decompyle incomplete


class DocstringReturns(DocstringMeta):
    pass
# WARNING: Decompyle incomplete


class DocstringRaises(DocstringMeta):
    pass
# WARNING: Decompyle incomplete


class DocstringDeprecated(DocstringMeta):
    pass
# WARNING: Decompyle incomplete


class DocstringExample(DocstringMeta):
    pass
# WARNING: Decompyle incomplete


class Docstring:
    '''Docstring object representation.'''
    
    def __init__(self = None, style = None):
        '''Initialize self.'''
        self.short_description = None
        self.long_description = None
        self.blank_after_short_description = False
        self.blank_after_long_description = False
        self.meta = []
        self.style = style

    description = (lambda self = None: ret = []if self.short_description:
ret.append(self.short_description)if self.blank_after_short_description:
ret.append('')if self.long_description:
ret.append(self.long_description)if not ret:
NoneNone.join(ret))()
    params = (lambda self = None: self.meta())()
    raises = (lambda self = None: self.meta())()
    returns = (lambda self = None: for item in self.meta:
if isinstance(item, DocstringReturns):
None, itemNone)()
    many_returns = (lambda self = None: self.meta())()
    deprecation = (lambda self = None: for item in self.meta:
if isinstance(item, DocstringDeprecated):
None, itemNone)()
    examples = (lambda self = None: self.meta())()
