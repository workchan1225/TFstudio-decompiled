# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: logic.pyc (Python 3.11)

'''Logic expressions handling

NOTE
----

at present this is mainly needed for facts.py, feel free however to improve
this stuff for general purpose.
'''
from __future__ import annotations
from typing import Optional
FuzzyBool = Optional[bool]

def _torf(args):
    '''Return True if all args are True, False if they
    are all False, else None.

    >>> from sympy.core.logic import _torf
    >>> _torf((True, True))
    True
    >>> _torf((False, False))
    False
    >>> _torf((True, False))
    '''
    sawT = False
    sawF = False
    for a in args:
        if a is True:
            if sawF:
                return None
            sawT = None
            continue
        if a is False:
            if sawT:
                return None
            sawF = None
            continue
        return None
        return sawT


def _fuzzy_group(args, quick_exit = (False,)):
    '''Return True if all args are True, None if there is any None else False
    unless ``quick_exit`` is True (then return None as soon as a second False
    is seen.

     ``_fuzzy_group`` is like ``fuzzy_and`` except that it is more
    conservative in returning a False, waiting to make sure that all
    arguments are True or False and returning None if any arguments are
    None. It also has the capability of permiting only a single False and
    returning None if more than one is seen. For example, the presence of a
    single transcendental amongst rationals would indicate that the group is
    no longer rational; but a second transcendental in the group would make the
    determination impossible.


    Examples
    ========

    >>> from sympy.core.logic import _fuzzy_group

    By default, multiple Falses mean the group is broken:

    >>> _fuzzy_group([False, False, True])
    False

    If multiple Falses mean the group status is unknown then set
    `quick_exit` to True so None can be returned when the 2nd False is seen:

    >>> _fuzzy_group([False, False, True], quick_exit=True)

    But if only a single False is seen then the group is known to
    be broken:

    >>> _fuzzy_group([False, True, True], quick_exit=True)
    False

    '''
    saw_other = False
# WARNING: Decompyle incomplete


def fuzzy_bool(x):
    '''Return True, False or None according to x.

    Whereas bool(x) returns True or False, fuzzy_bool allows
    for the None value and non-false values (which become None), too.

    Examples
    ========

    >>> from sympy.core.logic import fuzzy_bool
    >>> from sympy.abc import x
    >>> fuzzy_bool(x), fuzzy_bool(None)
    (None, None)
    >>> bool(x), bool(None)
    (True, False)

    '''
    pass
# WARNING: Decompyle incomplete


def fuzzy_and(args):
    '''Return True (all True), False (any False) or None.

    Examples
    ========

    >>> from sympy.core.logic import fuzzy_and
    >>> from sympy import Dummy

    If you had a list of objects to test the commutivity of
    and you want the fuzzy_and logic applied, passing an
    iterator will allow the commutativity to only be computed
    as many times as necessary. With this list, False can be
    returned after analyzing the first symbol:

    >>> syms = [Dummy(commutative=False), Dummy()]
    >>> fuzzy_and(s.is_commutative for s in syms)
    False

    That False would require less work than if a list of pre-computed
    items was sent:

    >>> fuzzy_and([s.is_commutative for s in syms])
    False
    '''
    rv = True
    for ai in args:
        ai = fuzzy_bool(ai)
        if ai is False:
            return False
        if None:
            rv = ai
        return rv


def fuzzy_not(v):
    '''
    Not in fuzzy logic

    Return None if `v` is None else `not v`.

    Examples
    ========

    >>> from sympy.core.logic import fuzzy_not
    >>> fuzzy_not(True)
    False
    >>> fuzzy_not(None)
    >>> fuzzy_not(False)
    True

    '''
    pass
# WARNING: Decompyle incomplete


def fuzzy_or(args):
    """
    Or in fuzzy logic. Returns True (any True), False (all False), or None

    See the docstrings of fuzzy_and and fuzzy_not for more info.  fuzzy_or is
    related to the two by the standard De Morgan's law.

    >>> from sympy.core.logic import fuzzy_or
    >>> fuzzy_or([True, False])
    True
    >>> fuzzy_or([True, None])
    True
    >>> fuzzy_or([False, False])
    False
    >>> print(fuzzy_or([False, None]))
    None

    """
    rv = False
    for ai in args:
        ai = fuzzy_bool(ai)
        if ai is True:
            return True
        if None is False:
            rv = ai
        return rv


def fuzzy_xor(args):
    '''Return None if any element of args is not True or False, else
    True (if there are an odd number of True elements), else False.'''
    t = 0
    f = 0
    for a in args:
        ai = fuzzy_bool(a)
        if ai:
            t += 1
            continue
        if ai is False:
            f += 1
            continue
        return None
        return t % 2 == 1


def fuzzy_nand(args):
    '''Return False if all args are True, True if they are all False,
    else None.'''
    return fuzzy_not(fuzzy_and(args))


class Logic:
    '''Logical expression'''
    op_2class: 'dict[str, type[Logic]]' = { }
    
    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj.args = args
        return obj

    
    def __getnewargs__(self):
        return self.args

    
    def __hash__(self):
        return hash((type(self).__name__,) + tuple(self.args))

    
    def __eq__(a, b):
        if not isinstance(b, type(a)):
            return False
        return None.args == b.args

    
    def __ne__(a, b):
        if not isinstance(b, type(a)):
            return True
        return None.args != b.args

    
    def __lt__(self, other):
        if self.__cmp__(other) == -1:
            return True

    
    def __cmp__(self, other):
        if type(self) is not type(other):
            a = str(type(self))
            b = str(type(other))
        else:
            a = self.args
            b = other.args
        return (a > b) - (a < b)

    
    def __str__(self):
        return f'''({(lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())!s})'''

    __repr__ = __str__
    fromstring = (lambda text: lexpr = Noneschedop = None# WARNING: Decompyle incomplete
)()


class AndOr_Base(Logic):
    
    def __new__(cls, *args):
        bargs = []
    # WARNING: Decompyle incomplete

    flatten = (lambda cls, args: args_queue = list(args)res = []try:
arg = args_queue.pop(0)except IndexError:
passexcept:
if isinstance(arg, Logic) and isinstance(arg, cls):
args_queue.extend(arg.args)continueres.append(arg)continueargs = tuple(res)args)()


class And(AndOr_Base):
    op_x_notx = False
    
    def _eval_propagate_not(self):
        pass
    # WARNING: Decompyle incomplete

    
    def expand(self):
        pass
    # WARNING: Decompyle incomplete



class Or(AndOr_Base):
    op_x_notx = True
    
    def _eval_propagate_not(self):
        pass
    # WARNING: Decompyle incomplete



class Not(Logic):
    
    def __new__(cls, arg):
        if isinstance(arg, str):
            return Logic.__new__(cls, arg)
        if None(arg, bool):
            return not arg
        if None(arg, Not):
            return arg.args[0]
        if None(arg, Logic):
            arg = arg._eval_propagate_not()
            return arg
        raise None(f'''Not: unknown argument {arg!r}''')

    arg = (lambda self: self.args[0])()

Logic.op_2class['&'] = And
Logic.op_2class['|'] = Or
Logic.op_2class['!'] = Not
