# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: google.pyc (Python 3.11)

'''Google-style docstring parsing.'''
import inspect
import re
import typing as T
from collections import OrderedDict, namedtuple
from enum import IntEnum
from common import EXAMPLES_KEYWORDS, PARAM_KEYWORDS, RAISES_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, Docstring, DocstringExample, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns, DocstringStyle, ParseError, RenderingStyle

class SectionType(IntEnum):
    '''Types of sections.'''
    SINGULAR = 0
    MULTIPLE = 1
    SINGULAR_OR_MULTIPLE = 2


def Section():
    '''Section'''
    __doc__ = 'A docstring section.'

Section = <NODE:27>(Section, 'Section', namedtuple('SectionBase', 'title key type'))
GOOGLE_TYPED_ARG_REGEX = re.compile('\\s*(.+?)\\s*\\(\\s*(.*[^\\s]+)\\s*\\)')
GOOGLE_ARG_DESC_REGEX = re.compile('.*\\. Defaults to (.+)\\.')
MULTIPLE_PATTERN = re.compile('(\\s*[^:\\s]+:)|([^:]*\\]:.*)')
DEFAULT_SECTIONS = [
    Section('Arguments', 'param', SectionType.MULTIPLE),
    Section('Args', 'param', SectionType.MULTIPLE),
    Section('Parameters', 'param', SectionType.MULTIPLE),
    Section('Params', 'param', SectionType.MULTIPLE),
    Section('Raises', 'raises', SectionType.MULTIPLE),
    Section('Exceptions', 'raises', SectionType.MULTIPLE),
    Section('Except', 'raises', SectionType.MULTIPLE),
    Section('Attributes', 'attribute', SectionType.MULTIPLE),
    Section('Example', 'examples', SectionType.SINGULAR),
    Section('Examples', 'examples', SectionType.SINGULAR),
    Section('Returns', 'returns', SectionType.SINGULAR_OR_MULTIPLE),
    Section('Yields', 'yields', SectionType.SINGULAR_OR_MULTIPLE)]

class GoogleParser:
    '''Parser for Google-style docstrings.'''
    
    def __init__(self = None, sections = None, title_colon = None):
        '''Setup sections.

        :param sections: Recognized sections or None to defaults.
        :param title_colon: require colon after section title.
        '''
        if not sections:
            sections = DEFAULT_SECTIONS
        self.sections = sections()
        self.title_colon = title_colon
        self._setup()

    
    def _setup(self):
        if self.title_colon:
            colon = ':'
        else:
            colon = ''
        self.titles_re = '^('('|'.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(self.sections()) + ')' + colon + '[ \t\r\x0c\x0b]*$', flags = re.M)

    
    def _build_meta(self = None, text = None, title = None):
        '''Build docstring element.

        :param text: docstring element text
        :param title: title of section containing element
        :return:
        '''
        section = self.sections[title]
        if section.type == SectionType.SINGULAR_OR_MULTIPLE or MULTIPLE_PATTERN.match(text) or section.type == SectionType.SINGULAR:
            return self._build_single_meta(section, text)
        if None not in text:
            raise ParseError(f'''Expected a colon in {text!r}.''')
        (before, desc) = text.split(':', 1)
        if before and '\n' in before:
            (first_line, rest) = before.split('\n', 1)
            before = first_line + inspect.cleandoc(rest)
        if desc:
            desc = desc[1:] if desc[0] == ' ' else desc
            if '\n' in desc:
                (first_line, rest) = desc.split('\n', 1)
                desc = first_line + '\n' + inspect.cleandoc(rest)
            desc = desc.strip('\n')
        return self._build_multi_meta(section, before, desc)

    _build_single_meta = (lambda section = None, desc = None: if section.key in RETURNS_KEYWORDS | YIELDS_KEYWORDS:
DocstringReturns(args = [
section.key], description = desc, type_name = None, is_generator = section.key in YIELDS_KEYWORDS)if None.key in RAISES_KEYWORDS:
DocstringRaises(args = [
section.key], description = desc, type_name = None)if None.key in EXAMPLES_KEYWORDS:
DocstringExample(args = [
section.key], snippet = None, description = desc)if None.key in PARAM_KEYWORDS:
raise ParseError('Expected paramenter name.')DocstringMeta(args = [
section.key], description = desc))()
    _build_multi_meta = (lambda section = None, before = None, desc = staticmethod: if section.key in PARAM_KEYWORDS:
match = GOOGLE_TYPED_ARG_REGEX.match(before)if match:
(arg_name, type_name) = match.group(1, 2)if type_name.endswith(', optional'):
is_optional = Truetype_name = type_name[:-10]elif type_name.endswith('?'):
is_optional = Truetype_name = type_name[:-1]else:
is_optional = Falseelse:
type_name = Nonearg_name = beforeis_optional = Nonematch = GOOGLE_ARG_DESC_REGEX.match(desc)default = match.group(1) if match else NoneDocstringParam(args = [
section.key,
before], description = desc, arg_name = arg_name, type_name = type_name, is_optional = is_optional, default = default)if None.key in RETURNS_KEYWORDS | YIELDS_KEYWORDS:
DocstringReturns(args = [
section.key,
before], description = desc, type_name = before, is_generator = section.key in YIELDS_KEYWORDS)if None.key in RAISES_KEYWORDS:
DocstringRaises(args = [
section.key,
before], description = desc, type_name = before)None(args = [
section.key,
before], description = desc))()
    
    def add_section(self = None, section = None):
        '''Add or replace a section.

        :param section: The new section.
        '''
        self.sections[section.title] = section
        self._setup()

    
    def parse(self = None, text = None):
        '''Parse the Google-style docstring into its components.

        :returns: parsed docstring
        '''
        ret = Docstring(style = DocstringStyle.GOOGLE)
        if not text:
            return ret
        text = None.cleandoc(text)
        match = self.titles_re.search(text)
        if match:
            desc_chunk = None[text:match.start()]
            meta_chunk = text[match.start():]
        else:
            desc_chunk = text
            meta_chunk = ''
        parts = desc_chunk.split('\n', 1)
    # WARNING: Decompyle incomplete



def parse(text = None):
    '''Parse the Google-style docstring into its components.

    :returns: parsed docstring
    '''
    return GoogleParser().parse(text)


def compose(docstring = None, rendering_style = None, indent = None):
    '''Render a parsed docstring into docstring text.

    :param docstring: parsed docstring representation
    :param rendering_style: the style to render docstrings
    :param indent: the characters used as indentation in the docstring string
    :returns: docstring text
    '''
    pass
# WARNING: Decompyle incomplete
