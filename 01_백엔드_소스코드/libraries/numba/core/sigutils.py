# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sigutils.pyc (Python 3.11)

from numba.core import types, typing

def is_signature(sig):
    '''
    Return whether *sig* is a potentially valid signature
    specification (for user-facing APIs).
    '''
    return isinstance(sig, (str, tuple, typing.Signature))


def _parse_signature_string(signature_str):
    '''
    Parameters
    ----------
    signature_str : str
    '''
    return eval(signature_str, { }, types.__dict__)


def normalize_signature(sig):
    '''
    From *sig* (a signature specification), return a ``(args, return_type)``
    tuple, where ``args`` itself is a tuple of types, and ``return_type``
    can be None if not specified.
    '''
    if isinstance(sig, str):
        parsed = _parse_signature_string(sig)
    else:
        parsed = sig
    if isinstance(parsed, tuple):
        return_type = None
        args = parsed
    elif isinstance(parsed, typing.Signature):
        return_type = parsed.return_type
        args = parsed.args
    else:
        raise TypeError(f'''invalid signature: {sig!r} (type: {sig.__class__.__name__!r}) evaluates to {parsed.__class__.__name__!r} instead of tuple or Signature''')
    
    def check_type(ty):
        if not isinstance(ty, types.Type):
            raise TypeError(f'''invalid type in signature: expected a type instance, got {ty!r}''')

# WARNING: Decompyle incomplete
