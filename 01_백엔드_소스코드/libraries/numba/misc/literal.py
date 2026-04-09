# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: literal.pyc (Python 3.11)

from numba.core.extending import overload
from numba.core import types
from numba.misc.special import literally, literal_unroll
from numba.core.errors import TypingError
_ov_literally = (lambda obj: if isinstance(obj, (types.Literal, types.InitialValue)):
(lambda obj: obj)
    m = None.format(obj)
    raise TypingError(m)
)()
literal_unroll_impl = (lambda container: if isinstance(container, types.Poison):
m = f'''Invalid use of non-Literal type in literal_unroll({container})'''raise TypingError(m)
def impl(container):
containerimpl)()
