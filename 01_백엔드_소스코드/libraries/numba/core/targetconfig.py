# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: targetconfig.pyc (Python 3.11)

'''
This module contains utils for manipulating target configurations such as
compiler flags.
'''
import re
import zlib
import base64
from types import MappingProxyType
from numba.core import utils

class Option:
    '''An option to be used in ``TargetConfig``.
    '''
    __slots__ = ('_type', '_default', '_doc')
    
    def __init__(self, type, *, default, doc):
        '''
        Parameters
        ----------
        type :
            Type of the option value. It can be a callable.
            The setter always calls ``self._type(value)``.
        default :
            The default value for the option.
        doc : str
            Docstring for the option.
        '''
        self._type = type
        self._default = default
        self._doc = doc

    type = (lambda self: self._type)()
    default = (lambda self: self._default)()
    doc = (lambda self: self._doc)()


def _FlagsStack():
    '''_FlagsStack'''
    pass

_FlagsStack = <NODE:27>(_FlagsStack, '_FlagsStack', utils.ThreadLocalStack, stack_name = 'flags')

class ConfigStack:
    '''A stack for tracking target configurations in the compiler.

    It stores the stack in a thread-local class attribute. All instances in the
    same thread will see the same stack.
    '''
    top_or_none = (lambda cls: self = cls()if self:
flags = self.top()else:
flags = Noneflags)()
    
    def __init__(self):
        self._stk = _FlagsStack()

    
    def top(self):
        return self._stk.top()

    
    def __len__(self):
        return len(self._stk)

    
    def enter(self, flags):
        '''Returns a contextmanager that performs ``push(flags)`` on enter and
        ``pop()`` on exit.
        '''
        return self._stk.enter(flags)



class _MetaTargetConfig(type):
    '''Metaclass for ``TargetConfig``.

    When a subclass of ``TargetConfig`` is created, all ``Option`` defined
    as class members will be parsed and corresponding getters, setters, and
    delters will be inserted.
    '''
    
    def __init__(cls, name, bases, dct):
        '''Invoked when subclass is created.

        Insert properties for each ``Option`` that are class members.
        All the options will be grouped inside the ``.options`` class
        attribute.
        '''
        opts = { }
        for base_cls in reversed(bases):
            opts.update(base_cls.options)
            opts.update(cls.find_options(dct))
            cls.options = MappingProxyType(opts)
            
            def make_prop(name, option):
                pass
            # WARNING: Decompyle incomplete

            for name, option in cls.options.items():
                setattr(cls, name, make_prop(name, option))
                return None

    
    def find_options(cls, dct):
        '''Returns a new dict with all the items that are a mapping to an
        ``Option``.
        '''
        return dct.items()()



class _NotSetType:
    
    def __repr__(self):
        return '<NotSet>'


_NotSet = _NotSetType()

def TargetConfig():
    '''TargetConfig'''
    __doc__ = 'Base class for ``TargetConfig``.\n\n    Subclass should fill class members with ``Option``. For example:\n\n    >>> class MyTargetConfig(TargetConfig):\n    >>>     a_bool_option = Option(type=bool, default=False, doc="a bool")\n    >>>     an_int_option = Option(type=int, default=0, doc="an int")\n\n    The metaclass will insert properties for each ``Option``. For example:\n\n    >>> tc = MyTargetConfig()\n    >>> tc.a_bool_option = True  # invokes the setter\n    >>> print(tc.an_int_option)  # print the default\n    '
    __slots__ = [
        '_values']
    _ZLIB_CONFIG = {
        'wbits': -15 }
    
    def __init__(self, copy_from = (None,)):
        '''
        Parameters
        ----------
        copy_from : TargetConfig or None
            if None, creates an empty ``TargetConfig``.
            Otherwise, creates a copy.
        '''
        self._values = { }
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        args = []
        defs = []
        for k in self.options:
            msg = f'''{k}={getattr(self, k)}'''
            if not self.is_set(k):
                defs.append(msg)
                continue
            args.append(msg)
            clsname = self.__class__.__name__
            return f'''{clsname}({', '.join(args)}, [{', '.join(defs)}])'''

    
    def __hash__(self):
        return hash(tuple(sorted(self.values())))

    
    def __eq__(self, other):
        if isinstance(other, TargetConfig):
            return self.values() == other.values()

    
    def values(self):
        '''Returns a dict of all the values
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def is_set(self, name):
        '''Is the option set?
        '''
        self._guard_option(name)
        return name in self._values

    
    def discard(self, name):
        '''Remove the option by name if it is defined.

        After this, the value for the option will be set to its default value.
        '''
        self._guard_option(name)
        self._values.pop(name, None)

    
    def inherit_if_not_set(self, name, default = (_NotSet,)):
        '''Inherit flag from ``ConfigStack``.

        Parameters
        ----------
        name : str
            Option name.
        default : optional
            When given, it overrides the default value.
            It is only used when the flag is not defined locally and there is
            no entry in the ``ConfigStack``.
        '''
        self._guard_option(name)
        if not self.is_set(name):
            cstk = ConfigStack()
            if cstk:
                top = cstk.top()
                setattr(self, name, getattr(top, name))
                return None
            if None is not _NotSet:
                setattr(self, name, default)
                return None
            return None

    
    def copy(self):
        '''Clone this instance.
        '''
        return type(self)(self)

    
    def summary(self = None):
        '''Returns a ``str`` that summarizes this instance.

        In contrast to ``__repr__``, only options that are explicitly set will
        be shown.
        '''
        args = self._summary_args()()
        clsname = self.__class__.__name__
        return f'''{clsname}({', '.join(args)})'''

    
    def _guard_option(self, name):
        if name not in self.options:
            msg = f'''{name!r} is not a valid option for {type(self)}'''
            raise ValueError(msg)

    
    def _summary_args(self):
        '''returns a sorted sequence of 2-tuple containing the
        ``(flag_name, flag_value)`` for flag that are set with a non-default
        value.
        '''
        args = []
        for k in sorted(self.options):
            opt = self.options[k]
            if self.is_set(k):
                flagval = getattr(self, k)
                if opt.default != flagval:
                    v = (k, flagval)
                    args.append(v)
            return args

    _make_compression_dictionary = (lambda cls = None: buf = []buf.append('numba')buf.append(cls.__class__.__name__)buf.extend([
'True',
'False'])for k, opt in cls.options.items():
buf.append(k)buf.append(str(opt.default))''.join(buf).encode())()
    
    def get_mangle_string(self = None):
        '''Return a string suitable for symbol mangling.
        '''
        zdict = self._make_compression_dictionary()
    # WARNING: Decompyle incomplete

    demangle = (lambda cls = None, mangled = None: 
def repl(x):
chr(int('0x' + x.group(0)[1:], 16))unescaped = re.sub('_[a-zA-Z0-9][a-zA-Z0-9]', repl, mangled)raw = base64.b64decode(unescaped)zdict = cls._make_compression_dictionary()# WARNING: Decompyle incomplete
)()

TargetConfig = <NODE:27>(TargetConfig, 'TargetConfig', metaclass = _MetaTargetConfig)
