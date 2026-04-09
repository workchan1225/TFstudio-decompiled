# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: setters.pyc (Python 3.11)

'''
Commonly used hooks for on_setattr.
'''
from  import _config
from exceptions import FrozenAttributeError

def pipe(*setters):
    '''
    Run all *setters* and return the return value of the last one.

    .. versionadded:: 20.1.0
    '''
    pass
# WARNING: Decompyle incomplete


def frozen(_, __, ___):
    '''
    Prevent an attribute to be modified.

    .. versionadded:: 20.1.0
    '''
    raise FrozenAttributeError


def validate(instance, attrib, new_value):
    """
    Run *attrib*'s validator on *new_value* if it has one.

    .. versionadded:: 20.1.0
    """
    if _config._run_validators is False:
        return new_value
    v = None.validator
    if not v:
        return new_value
    v(instance, attrib, new_value)
    return new_value


def convert(instance, attrib, new_value):
    """
    Run *attrib*'s converter -- if it has one -- on *new_value* and return the
    result.

    .. versionadded:: 20.1.0
    """
    c = attrib.converter
    if c:
        Converter = Converter
        import _make
        if not isinstance(c, Converter):
            return c(new_value)
        return c(new_value, instance, attrib)

NO_OP = object()
