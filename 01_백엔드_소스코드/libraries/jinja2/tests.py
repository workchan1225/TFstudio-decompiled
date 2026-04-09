# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tests.pyc (Python 3.11)

__doc__ = 'Built-in template tests used with the ``is`` operator.'
import operator
import typing as t
from collections import abc
from numbers import Number
from runtime import Undefined
from utils import pass_environment
if t.TYPE_CHECKING:
    from environment import Environment

def test_odd(value = None):
    '''Return true if the variable is odd.'''
    return value % 2 == 1


def test_even(value = None):
    '''Return true if the variable is even.'''
    return value % 2 == 0


def test_divisibleby(value = None, num = None):
    '''Check if a variable is divisible by a number.'''
    return value % num == 0


def test_defined(value = None):
    '''Return true if the variable is defined:

    .. sourcecode:: jinja

        {% if variable is defined %}
            value of variable: {{ variable }}
        {% else %}
            variable is not defined
        {% endif %}

    See the :func:`default` filter for a simple way to set undefined
    variables.
    '''
    return not isinstance(value, Undefined)


def test_undefined(value = None):
    '''Like :func:`defined` but the other way round.'''
    return isinstance(value, Undefined)

test_filter = (lambda env = None, value = None: value in env.filters)()
test_test = (lambda env = None, value = None: value in env.tests)()

def test_none(value = None):
    '''Return true if the variable is none.'''
    return value is None


def test_boolean(value = None):
