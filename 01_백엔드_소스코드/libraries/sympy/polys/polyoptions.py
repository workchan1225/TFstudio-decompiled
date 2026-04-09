# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polyoptions.pyc (Python 3.11)

'''Options manager for :class:`~.Poly` and public API functions. '''
from __future__ import annotations
__all__ = [
    'Options']
from sympy.core import Basic, sympify
from sympy.polys.polyerrors import GeneratorsError, OptionError, FlagError
from sympy.utilities import numbered_symbols, topological_sort, public
from sympy.utilities.iterables import has_dups, is_sequence
import sympy.polys as sympy
import re

class Option:
    '''Base class for all kinds of options. '''
    option: 'str | None' = None
    is_Flag = False
    requires: 'list[str]' = []
    excludes: 'list[str]' = []
    after: 'list[str]' = []
    before: 'list[str]' = []
    default = (lambda cls: pass)()
    preprocess = (lambda cls, option: pass)()
    postprocess = (lambda cls, options: pass)()


class Flag(Option):
    '''Base class for all kinds of flags. '''
    is_Flag = True


class BooleanOption(Option):
    '''An option that must have a boolean value or equivalent assigned. '''
    preprocess = (lambda cls, value: if value in (True, False):
bool(value)raise None(f'''\'{cls.option!s}\' must have a boolean value assigned, got {value!s}'''))()


class OptionType(type):
    '''Base type for all options that does registers options. '''
    
    def __init__(cls, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete


Options = <NODE:12>()

def Expand():
    '''Expand'''
    __doc__ = '``expand`` option to polynomial manipulation functions. '
    option = 'expand'
    requires: 'list[str]' = []
    excludes: 'list[str]' = []
    default = (lambda cls: True)()

Expand = <NODE:27>(Expand, 'Expand', BooleanOption, metaclass = OptionType)

def Gens():
    '''Gens'''
    __doc__ = '``gens`` option to polynomial manipulation functions. '
    option = 'gens'
    requires: 'list[str]' = []
    excludes: 'list[str]' = []
    default = (lambda cls: ())()
    preprocess = (lambda cls, gens: if isinstance(gens, Basic):
gens = (gens,)elif len(gens) == 1 and is_sequence(gens[0]):
gens = gens[0]if gens == (None,):
gens = ()elif has_dups(gens):
raise GeneratorsError('duplicated generators: %s' % str(gens))if (lambda .0: pass# WARNING: Decompyle incomplete
)(gens()):
            raise GeneratorsError('non-commutative generators: %s' % str(gens))
        return tuple(gens)
)()

Gens = <NODE:27>(Gens, 'Gens', Option, metaclass = OptionType)

def Wrt():
    '''Wrt'''
    __doc__ = '``wrt`` option to polynomial manipulation functions. '
    option = 'wrt'
    requires: 'list[str]' = []
    excludes: 'list[str]' = []
    _re_split = re.compile('\\s*,\\s*|\\s+')
    preprocess = (lambda cls, wrt: if isinstance(wrt, Basic):
[
str(wrt)]if None(wrt, str):
wrt = wrt.strip()if wrt.endswith(','):
raise OptionError('Bad input: missing parameter.')if not wrt:
[]None(cls._re_split.split(wrt))if None(wrt, '__getitem__'):
list(map(str, wrt))raise None("invalid argument for 'wrt' option"))()

Wrt = <NODE:27>(Wrt, 'Wrt', Option, metaclass = OptionType)

def Sort():
    '''Sort'''
    __doc__ = '``sort`` option to polynomial manipulation functions. '
    option = 'sort'
    requires: 'list[str]' = []
    excludes: 'list[str]' = []
    default = (lambda cls: [])()
    preprocess = (lambda cls, sort: if isinstance(sort, str):
sort.split('>')()if None(sort, '__getitem__'):
list(map(str, sort))raise None("invalid argument for 'sort' option"))()

Sort = <NODE:27>(Sort, 'Sort', Option, metaclass = OptionType)

def Order():
    '''Order'''
    __doc__ = '``order`` option to polynomial manipulation functions. '
    option = 'order'
    requires: 'list[str]' = []
    excludes: 'list[str]' = []
    default = (lambda cls: sympy.polys.orderings.lex)()
    preprocess = (lambda cls, order: sympy.polys.orderings.monomial_key(order))()

Order = <NODE:27>(Order, 'Order', Option, metaclass = OptionType)

def Field():
    '''Field'''
    __doc__ = '``field`` option to polynomial manipulation functions. '
    option = 'field'
    requires: 'list[str]' = []
    excludes = [
        'domain',
        'split',
        'gaussian']

Field = <NODE:27>(Field, 'Field', BooleanOption, metaclass = OptionType)

def Greedy():
    '''Greedy'''
    __doc__ = '``greedy`` option to polynomial manipulation functions. '
    option = 'greedy'
    requires: 'list[str]' = []
    excludes = [
        'domain',
        'split',
        'gaussian',
        'extension',
        'modulus',
        'symmetric']

Greedy = <NODE:27>(Greedy, 'Greedy', BooleanOption, metaclass = OptionType)

def Composite():
    '''Composite'''
    __doc__ = '``composite`` option to polynomial manipulation functions. '
    option = 'composite'
    default = (lambda cls: pass)()
    requires: 'list[str]' = []
    excludes = [
        'domain',
        'split',
        'gaussian',
        'extension',
        'modulus',
        'symmetric']

Composite = <NODE:27>(Composite, 'Composite', BooleanOption, metaclass = OptionType)

def Domain():
    '''Domain'''
    __doc__ = '``domain`` option to polynomial manipulation functions. '
    option = 'domain'
    requires: 'list[str]' = []
    excludes = [
        'field',
        'greedy',
        'split',
        'gaussian',
        'extension']
    after = [
        'gens']
    _re_realfield = re.compile('^(R|RR)(_(\\d+))?$')
    _re_complexfield = re.compile('^(C|CC)(_(\\d+))?$')
    _re_finitefield = re.compile('^(FF|GF)\\((\\d+)\\)$')
    _re_polynomial = re.compile('^(Z|ZZ|Q|QQ|ZZ_I|QQ_I|R|RR|C|CC)\\[(.+)\\]$')
    _re_fraction = re.compile('^(Z|ZZ|Q|QQ)\\((.+)\\)$')
    _re_algebraic = re.compile('^(Q|QQ)\\<(.+)\\>$')
    preprocess = (lambda cls, domain: if isinstance(domain, sympy.polys.domains.Domain):
domainif None(domain, 'to_domain'):
domain.to_domain()# WARNING: Decompyle incomplete
)()
    postprocess = (lambda cls, options: if 'gens' in options and 'domain' in options and options['domain'].is_Composite and set(options['domain'].symbols) & set(options['gens']):
raise GeneratorsError('ground domain and generators interfere together')if not 'gens' not in options or options['gens']:
if 'domain' in options or options['domain'] == sympy.polys.domains.EX:
raise GeneratorsError('you have to provide generators because EX domain was requested')NoneNone)()

Domain = <NODE:27>(Domain, 'Domain', Option, metaclass = OptionType)

def Split():
    '''Split'''
    __doc__ = '``split`` option to polynomial manipulation functions. '
    option = 'split'
    requires: 'list[str]' = []
    excludes = [
        'field',
        'greedy',
        'domain',
        'gaussian',
        'extension',
        'modulus',
        'symmetric']
    postprocess = (lambda cls, options: if 'split' in options:
raise NotImplementedError("'split' option is not implemented yet"))()

Split = <NODE:27>(Split, 'Split', BooleanOption, metaclass = OptionType)

def Gaussian():
    '''Gaussian'''
    __doc__ = '``gaussian`` option to polynomial manipulation functions. '
    option = 'gaussian'
    requires: 'list[str]' = []
    excludes = [
        'field',
        'greedy',
        'domain',
        'split',
        'extension',
        'modulus',
        'symmetric']
    postprocess = (lambda cls, options: if 'gaussian' in options or options['gaussian'] is True:
options['domain'] = sympy.polys.domains.QQ_IExtension.postprocess(options)NoneNone)()

Gaussian = <NODE:27>(Gaussian, 'Gaussian', BooleanOption, metaclass = OptionType)

def Extension():
    '''Extension'''
    __doc__ = '``extension`` option to polynomial manipulation functions. '
    option = 'extension'
    requires: 'list[str]' = []
    excludes = [
        'greedy',
        'domain',
        'split',
        'gaussian',
        'modulus',
        'symmetric']
    preprocess = (lambda cls, extension: if extension == 1:
bool(extension)if None == 0:
raise OptionError("'False' is an invalid argument for 'extension'")if not hasattr(extension, '__iter__'):
extension = {
extension}elif not extension:
extension = Noneelse:
extension = set(extension)extension)()
    postprocess = (lambda cls, options: pass# WARNING: Decompyle incomplete
)()

Extension = <NODE:27>(Extension, 'Extension', Option, metaclass = OptionType)

def Modulus():
    '''Modulus'''
    __doc__ = '``modulus`` option to polynomial manipulation functions. '
    option = 'modulus'
    requires: 'list[str]' = []
    excludes = [
        'greedy',
        'split',
        'domain',
        'gaussian',
        'extension']
    preprocess = (lambda cls, modulus: modulus = sympify(modulus)if modulus.is_Integer and modulus > 0:
int(modulus)raise None("'modulus' must a positive integer, got %s" % modulus))()
    postprocess = (lambda cls, options: if 'modulus' in options:
modulus = options['modulus']symmetric = options.get('symmetric', True)options['domain'] = sympy.polys.domains.FF(modulus, symmetric)None)()

Modulus = <NODE:27>(Modulus, 'Modulus', Option, metaclass = OptionType)

def Symmetric():
    '''Symmetric'''
    __doc__ = '``symmetric`` option to polynomial manipulation functions. '
    option = 'symmetric'
    requires = [
        'modulus']
    excludes = [
        'greedy',
        'domain',
        'split',
        'gaussian',
        'extension']

Symmetric = <NODE:27>(Symmetric, 'Symmetric', BooleanOption, metaclass = OptionType)

def Strict():
    '''Strict'''
    __doc__ = '``strict`` option to polynomial manipulation functions. '
    option = 'strict'
    default = (lambda cls: True)()

Strict = <NODE:27>(Strict, 'Strict', BooleanOption, metaclass = OptionType)

def Auto():
    '''Auto'''
    __doc__ = '``auto`` flag to polynomial manipulation functions. '
    option = 'auto'
    after = [
        'field',
        'domain',
        'extension',
        'gaussian']
    default = (lambda cls: True)()
    postprocess = (lambda cls, options: if 'domain' in options or 'field' in options:
if 'auto' not in options:
options['auto'] = FalseNoneNone)()

Auto = <NODE:27>(Auto, 'Auto', BooleanOption, Flag, metaclass = OptionType)

def Frac():
    '''Frac'''
    __doc__ = '``auto`` option to polynomial manipulation functions. '
    option = 'frac'
    default = (lambda cls: False)()

Frac = <NODE:27>(Frac, 'Frac', BooleanOption, Flag, metaclass = OptionType)

def Formal():
    '''Formal'''
    __doc__ = '``formal`` flag to polynomial manipulation functions. '
    option = 'formal'
    default = (lambda cls: False)()

Formal = <NODE:27>(Formal, 'Formal', BooleanOption, Flag, metaclass = OptionType)

def Polys():
    '''Polys'''
    __doc__ = '``polys`` flag to polynomial manipulation functions. '
    option = 'polys'

Polys = <NODE:27>(Polys, 'Polys', BooleanOption, Flag, metaclass = OptionType)

def Include():
    '''Include'''
    __doc__ = '``include`` flag to polynomial manipulation functions. '
    option = 'include'
    default = (lambda cls: False)()

Include = <NODE:27>(Include, 'Include', BooleanOption, Flag, metaclass = OptionType)

def All():
    '''All'''
    __doc__ = '``all`` flag to polynomial manipulation functions. '
    option = 'all'
    default = (lambda cls: False)()

All = <NODE:27>(All, 'All', BooleanOption, Flag, metaclass = OptionType)

def Gen():
    '''Gen'''
    __doc__ = '``gen`` flag to polynomial manipulation functions. '
    option = 'gen'
    default = (lambda cls: 0)()
    preprocess = (lambda cls, gen: if isinstance(gen, (Basic, int)):
genraise None("invalid argument for 'gen' option"))()

Gen = <NODE:27>(Gen, 'Gen', Flag, metaclass = OptionType)

def Series():
    '''Series'''
    __doc__ = '``series`` flag to polynomial manipulation functions. '
    option = 'series'
    default = (lambda cls: False)()

Series = <NODE:27>(Series, 'Series', BooleanOption, Flag, metaclass = OptionType)

def Symbols():
    '''Symbols'''
    __doc__ = '``symbols`` flag to polynomial manipulation functions. '
    option = 'symbols'
    default = (lambda cls: numbered_symbols('s', start = 1))()
    preprocess = (lambda cls, symbols: if hasattr(symbols, '__iter__'):
iter(symbols)raise None('expected an iterator or iterable container, got %s' % symbols))()

Symbols = <NODE:27>(Symbols, 'Symbols', Flag, metaclass = OptionType)

def Method():
    '''Method'''
    __doc__ = '``method`` flag to polynomial manipulation functions. '
    option = 'method'
    preprocess = (lambda cls, method: if isinstance(method, str):
method.lower()raise None('expected a string, got %s' % method))()

Method = <NODE:27>(Method, 'Method', Flag, metaclass = OptionType)

def build_options(gens, args = (None,)):
    '''Construct options from keyword arguments or ... options. '''
    pass
# WARNING: Decompyle incomplete


def allowed_flags(args, flags):
    """
    Allow specified flags to be used in the given context.

    Examples
    ========

    >>> from sympy.polys.polyoptions import allowed_flags
    >>> from sympy.polys.domains import ZZ

    >>> allowed_flags({'domain': ZZ}, [])

    >>> allowed_flags({'domain': ZZ, 'frac': True}, [])
    Traceback (most recent call last):
    ...
    FlagError: 'frac' flag is not allowed in this context

    >>> allowed_flags({'domain': ZZ, 'frac': True}, ['frac'])

    """
    flags = set(flags)
    for arg in args.keys():
        if Options.__options__[arg].is_Flag and arg not in flags:
            raise FlagError("'%s' flag is not allowed in this context" % arg)
        except KeyError:
            raise OptionError("'%s' is not a valid option" % arg)
        return None


def set_defaults(options, **defaults):
    '''Update options with default values. '''
    if 'defaults' not in options:
        options = dict(options)
        options['defaults'] = defaults
    return options

Options._init_dependencies_order()
