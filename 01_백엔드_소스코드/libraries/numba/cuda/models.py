# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

import functools
from llvmlite import ir
from numba.core.datamodel.registry import DataModelManager, register
from numba.core.extending import models
from numba.core import types
from numba.cuda.types import Dim3, GridGroup, CUDADispatcher
cuda_data_manager = DataModelManager()
register_model = functools.partial(register, cuda_data_manager)
Dim3Model = <NODE:12>()
GridGroupModel = <NODE:12>()
FloatModel = <NODE:12>()
register_model(CUDADispatcher)(models.OpaqueModel)
