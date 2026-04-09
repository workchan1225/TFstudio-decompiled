# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wav2vec2_spec.pyc (Python 3.11)

from typing import List, Optional, Tuple
import numpy as np
from ctranslate2.specs import common_spec, model_spec, transformer_spec

class Wav2Vec2Config(model_spec.ModelConfig):
    '''Configuration for the Wav2Vec2 model.'''
    
    def __init__(self):
        pass



class Wav2Vec2Spec(model_spec.LanguageModelSpec):
    pass
# WARNING: Decompyle incomplete


class Wav2Vec2LayerNormConvLayer(model_spec.LayerSpec):
    
    def __init__(self):
        self.conv = common_spec.Conv1DSpec()
        self.layer_norm = common_spec.LayerNormSpec()



class Wav2Vec2PosEmbedConvLayer(model_spec.LayerSpec):
    
    def __init__(self):
        self.conv = common_spec.Conv1DSpec()



class Wav2Vec2EncoderSpec(model_spec.LayerSpec):
    
    def __init__(self, feat_layers, num_layers, num_heads, return_hidden):
        self.num_heads = np.dtype('int16').type(num_heads)
        self.feat_layer0 = Wav2Vec2LayerNormConvLayer()
        self.feat_layer = range(feat_layers - 1)()
        self.fp_layer_norm = common_spec.LayerNormSpec()
        self.fp_projection = common_spec.LinearSpec()
        self.pos_conv_embed = Wav2Vec2PosEmbedConvLayer()
        self.layer_norm = common_spec.LayerNormSpec()
        self.layer = range(num_layers)()
        if not return_hidden:
            self.lm_head = common_spec.LinearSpec()
            return None
        return (lambda .0: [ transformer_spec.TransformerEncoderLayerSpec() for _ in .0 ])
