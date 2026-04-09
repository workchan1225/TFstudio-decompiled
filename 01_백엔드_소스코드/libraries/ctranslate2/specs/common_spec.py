# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common_spec.pyc (Python 3.11)

import enum
from ctranslate2.specs import model_spec

class Activation(enum.IntEnum):
    '''Activation type.'''
    RELU = 0
    GELUTanh = 1
    SWISH = 2
    GELU = 3
    GELUSigmoid = 4
    Tanh = 5
    Sigmoid = 6


class EmbeddingsMerge(enum.IntEnum):
    '''Merge strategy for factors embeddings.'''
    CONCAT = 0
    ADD = 1


class Quantization(enum.IntEnum):
    '''Activation type.'''
    CT2 = 0
    AWQ_GEMM = 1
    AWQ_GEMV = 2


class LayerNormSpec(model_spec.LayerSpec):
    
    def __init__(self, rms_norm = (False,)):
        self.gamma = None
        if not rms_norm:
            self.beta = None
            return None
        self.layer_norm_use_residual = None.OPTIONAL



class LinearSpec(model_spec.LayerSpec):
    
    def __init__(self):
        self.weight = None
        self.weight_scale = model_spec.OPTIONAL
        self.weight_zero = model_spec.OPTIONAL
        self.bias = model_spec.OPTIONAL

    
    def has_bias(self):
        return not isinstance(self.bias, str)



class Conv1DSpec(model_spec.LayerSpec):
    
    def __init__(self):
        self.weight = None
        self.weight_scale = model_spec.OPTIONAL
        self.bias = model_spec.OPTIONAL



class EmbeddingsSpec(model_spec.LayerSpec):
    
    def __init__(self):
        self.weight = None
        self.weight_scale = model_spec.OPTIONAL
        self.multiply_by_sqrt_depth = model_spec.OPTIONAL
