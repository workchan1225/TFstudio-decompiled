# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: attention_spec.pyc (Python 3.11)

import enum
import numpy as np
from ctranslate2.specs import common_spec, model_spec

class RotaryScalingType(enum.IntEnum):
    '''RoPE scaling type.'''
    Linear = 0
    Su = 1
    Llama3 = 2


class MultiHeadAttentionSpec(model_spec.LayerSpec):
    
    def __init__(self, self_attention, relative_position, relative_asymmetric_position, relative_attention_bias, rms_norm, rotary_dim, rotary_interleave, rotary_scaling_type, rotary_scaling_factor, rotary_base, original_max_position_embeddings, max_position_embeddings, num_heads_kv, head_dim, sliding_window, qk_norm, qk_norm_rms = (False, False, False, False, False, None, True, None, 1, 10000, 0, 0, None, None, None, False, True)):
        self.queries_scale = model_spec.OPTIONAL
        self.layer_norm = common_spec.LayerNormSpec(rms_norm = rms_norm)
        self.linear = range(2 if self_attention else 3)()
        if qk_norm:
            self.q_norm = common_spec.LayerNormSpec(rms_norm = qk_norm_rms)
            self.k_norm = common_spec.LayerNormSpec(rms_norm = qk_norm_rms)
        if relative_position:
            self.relative_position_keys = None
            self.relative_position_values = None
        if relative_attention_bias:
            self.relative_attention_bias = None
            self.relative_attention_max_distance = None
        if relative_asymmetric_position:
            self.relative_asymmetric_position_keys = None
            self.relative_left_max_position = None
            self.relative_right_max_position = None
        if original_max_position_embeddings != 0:
            self.original_max_position_embeddings = np.dtype('int32').type(original_max_position_embeddings)
        if max_position_embeddings != 0:
            self.max_position_embeddings = np.dtype('int32').type(max_position_embeddings)
    # WARNING: Decompyle incomplete
