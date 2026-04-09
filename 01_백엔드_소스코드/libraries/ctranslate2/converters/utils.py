# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import numpy as np

def fuse_linear(spec, layers):
    pass
# WARNING: Decompyle incomplete


def fuse_linear_prequant(spec, layers, axis):
    pass
# WARNING: Decompyle incomplete


def permute_for_sliced_rotary(weight, num_heads, rotary_dim = (None,)):
    '''Permutes the weight to use the sliced rotary implementation.'''
    pass
# WARNING: Decompyle incomplete


def smooth_activation(layer_norm, linear, activation_scales):
    '''Applies the activation smoothing technique described in
    https://github.com/mit-han-lab/smoothquant.
    '''
    if not isinstance(linear.weight, np.ndarray):
        linear_weight = linear.weight.numpy()
        activation_scales = activation_scales.numpy()
    else:
        linear_weight = linear.weight
    weight_scales = np.amax(np.absolute(linear_weight), axis = 0)
    weight_scales = np.maximum(weight_scales, 1e-05)
    activation_scales = activation_scales.astype(weight_scales.dtype)
    scales = np.sqrt(activation_scales / weight_scales)
    scales = np.maximum(scales, 1e-05)
    if not isinstance(linear.weight, np.ndarray):
        import torch
        scales = torch.from_numpy(scales)


def raise_unsupported(reasons):
    message = 'The model you are trying to convert is not supported by CTranslate2. We identified the following reasons:\n'
    for reason in reasons:
        message += '\n- ' + reason
        raise ValueError(message)


class ConfigurationChecker:
    
    def __init__(self):
        self._unsupported_reasons = []

    
    def __call__(self, assert_condition, error_message):
        if not assert_condition:
            self._unsupported_reasons.append(error_message)
            return None

    
    def validate(self):
        if self._unsupported_reasons:
            raise_unsupported(self._unsupported_reasons)
            return None
