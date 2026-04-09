# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: builtins.pyc (Python 3.11)

import itertools
import numpy as np
import operator
from numba.core import types, errors
from numba import prange
from numba.parfors.parfor import internal_prange
from numba.core.typing.templates import AttributeTemplate, ConcreteTemplate, AbstractTemplate, infer_global, infer, infer_getattr, signature, bound_function, make_callable_template
from numba.core.extending import typeof_impl, type_callable, models, register_model, make_attribute_wrapper
Print = <NODE:12>()
PrintItem = <NODE:12>()
Abs = <NODE:12>()
Slice = <NODE:12>()
Range = <NODE:12>()()()
GetIter = <NODE:12>()
IterNext = <NODE:12>()
PairFirst = <NODE:12>()
PairSecond = <NODE:12>()

def choose_result_bitwidth(*inputs):
