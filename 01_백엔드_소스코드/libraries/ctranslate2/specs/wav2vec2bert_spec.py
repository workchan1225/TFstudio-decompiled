# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wav2vec2bert_spec.pyc (Python 3.11)

import numpy as np
from ctranslate2.specs import attention_spec, common_spec, model_spec

class Wav2Vec2BertConfig(model_spec.ModelConfig):
    '''Configuration for the Wav2Vec2Bert model.'''
    
    def __init__(self):
        pass



class Wav2Vec2BertSpec(model_spec.LanguageModelSpec):
    pass
# WARNING: Decompyle incomplete


class Wav2Vec2BertFeedForwardSpec(model_spec.LayerSpec):
    
    def __init__(self, glu, rms_norm = (False, False)):
        self.linear_0 = common_spec.LinearSpec()
        self.linear_1 = common_spec.LinearSpec()
        if glu:
            self.linear_0_noact = common_spec.LinearSpec()
            return None



class EncoderSpec(model_spec.LayerSpec):
    
    def __init__(self):
        self.enc_ffn1_layer_norm = common_spec.LayerNormSpec()
        self.enc_ffn1 = Wav2Vec2BertFeedForwardSpec()
        self.enc_attn_layer_norm = common_spec.LayerNormSpec()
        self.enc_attn = attention_spec.MultiHeadAttentionSpec(self_attention = True, relative_asymmetric_position = True)
        del self.enc_attn.layer_norm
        self.enc_conv_layer_norm = common_spec.LayerNormSpec()
        self.enc_conv_pointwise_conv1 = common_spec.Conv1DSpec()
        del self.enc_conv_pointwise_conv1.bias
        self.enc_conv_depthwise_conv = common_spec.Conv1DSpec()
        del self.enc_conv_depthwise_conv.bias
        self.enc_conv_depthwise_layer_norm = common_spec.LayerNormSpec()
        self.enc_conv_pointwise_conv2 = common_spec.Conv1DSpec()
        del self.enc_conv_pointwise_conv2.bias
        self.enc_ffn2_layer_norm = common_spec.LayerNormSpec()
        self.enc_ffn2 = Wav2Vec2BertFeedForwardSpec()
        self.enc_final_layer_norm = common_spec.LayerNormSpec()



class AdapterSpec(model_spec.LayerSpec):
    
    def __init__(self):
        self.adpt_residual_layer_norm = common_spec.LayerNormSpec()
        self.adpt_residual_conv = common_spec.Conv1DSpec()
        self.adpt_attn_layer_norm = common_spec.LayerNormSpec()
        self.adpt_attn_conv = common_spec.Conv1DSpec()
        self.adpt_attn_layer = attention_spec.MultiHeadAttentionSpec(self_attention = True, relative_asymmetric_position = False)
        del self.adpt_attn_layer.layer_norm
        self.adpt_ffn_layer_norm = common_spec.LayerNormSpec()
        self.adpt_ffn = Wav2Vec2BertFeedForwardSpec()



class Wav2Vec2BertEncoderSpec(model_spec.LayerSpec):
    
    def __init__(self, num_hidden_layers, num_adapter_layers, return_hidden):
        self.fp_layer_norm = common_spec.LayerNormSpec()
        self.fp_projection = common_spec.LinearSpec()
        self.encoder_layers = range(num_hidden_layers)()
        self.adapter_layers = range(num_adapter_layers)()
        if not return_hidden:
            self.lm_head = common_spec.LinearSpec()
            return None
        return (lambda .0: [ AdapterSpec() for _ in .0 ])
