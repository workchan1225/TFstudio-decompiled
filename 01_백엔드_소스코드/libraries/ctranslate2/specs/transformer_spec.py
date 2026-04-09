# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transformer_spec.pyc (Python 3.11)

'''Declares specification of the Transformer model.'''
from typing import Optional, Tuple, Union
import numpy as np
from ctranslate2.specs import attention_spec, common_spec, model_spec

class TransformerEncoderSpec(model_spec.LayerSpec):
    
    def __init__(self, num_layers, num_heads, pre_norm, no_final_norm, activation, num_source_embeddings, embeddings_merge, layernorm_embedding, relative_position = None, relative_attention_bias = None, ffn_glu = None, rms_norm = (True, False, common_spec.Activation.RELU, 1, common_spec.EmbeddingsMerge.CONCAT, False, False, False, False, False, False), multi_query_attention = ('num_layers', int, 'num_heads', int, 'pre_norm', bool, 'no_final_norm', bool, 'activation', common_spec.Activation, 'num_source_embeddings', int, 'embeddings_merge', common_spec.EmbeddingsMerge, 'layernorm_embedding', bool, 'relative_position', bool, 'relative_attention_bias', bool, 'ffn_glu', bool, 'rms_norm', bool, 'multi_query_attention', bool)):
        '''Initializes a Transformer encoder specification.

        Args:
          num_layers: Number of layers.
          num_heads: Number of attention heads.
          pre_norm: Enable the pre-norm Transformer architecture.
          no_final_norm: Disable the final layer norm in the pre-norm architecture.
          activation: Activation to apply in the feed-forward network.
          num_source_embeddings: Number of source embeddings.
          embeddings_merge: When :obj:`num_source_embeddings` > 1, specify how the
            embeddings are merged.
          layernorm_embedding: Apply layer normalization after the embedding layer.
          relative_position: Use relative position representations in the self-attention
            layers as described in https://arxiv.org/abs/1803.02155.
          relative_attention_bias: Use relative attention bias in the self-attention
            layers as described in the T5 paper https://arxiv.org/abs/1910.10683.
          ffn_glu: Use gated linear units in the FFN layers as described in
            https://arxiv.org/abs/2002.05202.
          rms_norm: Use the root mean square layer normalization.
          multi_query_attention: Use multi-query attention.
        '''
        pass
    # WARNING: Decompyle incomplete



class TransformerDecoderSpec(model_spec.LayerSpec):
    
    def __init__(self, num_layers, num_heads, pre_norm, activation, layernorm_embedding, with_encoder_attention, no_final_norm, project_in_out, relative_position, relative_attention_bias, alignment_layer, alignment_heads, ffn_glu, rms_norm, alibi, alibi_use_positive_positions, scale_alibi, rotary_dim, rotary_interleave, rotary_scaling_type, rotary_scaling_factor, rotary_base, original_max_position_embeddings, max_position_embeddings, parallel_residual, shared_layer_norm, pre_post_layer_norm, multi_query_attention, num_heads_kv, head_dim, sliding_window = None, quant_type = None, quant_group_size = None, quant_bits = (True, common_spec.Activation.RELU, False, True, False, False, False, False, -1, 1, False, False, False, False, False, None, True, None, 1, 10000, 0, 0, False, False, False, False, None, None, None, None, None, None, False), qk_norm = ('num_layers', int, 'num_heads', int, 'pre_norm', bool, 'activation', common_spec.Activation, 'layernorm_embedding', bool, 'with_encoder_attention', bool, 'no_final_norm', bool, 'project_in_out', bool, 'relative_position', bool, 'relative_attention_bias', bool, 'alignment_layer', int, 'alignment_heads', int, 'ffn_glu', bool, 'rms_norm', bool, 'alibi', bool, 'alibi_use_positive_positions', bool, 'scale_alibi', bool, 'rotary_dim', Optional[int], 'rotary_interleave', bool, 'rotary_scaling_type', Optional[attention_spec.RotaryScalingType], 'rotary_scaling_factor', float, 'rotary_base', float, 'original_max_position_embeddings', int, 'max_position_embeddings', int, 'parallel_residual', bool, 'shared_layer_norm', bool, 'pre_post_layer_norm', bool, 'multi_query_attention', bool, 'num_heads_kv', Optional[int], 'head_dim', Optional[int], 'sliding_window', Optional[int], 'quant_type', Optional[common_spec.Quantization], 'quant_group_size', Optional[int], 'quant_bits', Optional[int], 'qk_norm', Optional[bool])):
        '''Initializes a Transformer decoder specification.

        Args:
          num_layers: Number of layers.
          num_heads: Number of attention heads.
          pre_norm: Enable the pre-norm Transformer architecture.
          activation: Activation to apply in the feed-forward network.
          layernorm_embedding: Apply layer normalization after the embedding layer.
          with_encoder_attention: Enable the encoder attention sublayers.
          no_final_norm: Disable the final layer norm in the pre-norm architecture.
          project_in_out: Add linear transformations after the embedding layer and before
            the final layer.
          relative_position: Use relative position representations in the self-attention
            layers as described in https://arxiv.org/abs/1803.02155.
          relative_attention_bias: Use relative attention bias in the self-attention
            layers as described in the T5 paper https://arxiv.org/abs/1910.10683.
          alignment_layer: Layer index selected for alignment.
          alignment_heads: Number of attention heads selected for alignment.
          ffn_glu: Use gated linear units in the FFN layers as described in
            https://arxiv.org/abs/2002.05202.
          rms_norm: Use the root mean square layer normalization.
          alibi: Use attention with linear biases.
          alibi_use_positive_positions: Use positive positions in the ALiBi definition.
          scale_alibi: Apply the dot product scale factor to ALiBi.
          rotary_dim: Apply rotary embeddings to these first N dimensions. If 0, rotary
            embeddings are applied to all dimensions.
          rotary_interleave: Interleave the head dimensions when rotary embeddings are applied.
            Otherwise the head dimensions are sliced in half.
          rotary_scaling_type: Type of RoPE scaling.
          rotary_scaling_factor: Factor used in the RoPE scaling.
          rotary_base: The base period of the rotary embeddings.
          original_max_position_embeddings: The original max position embeddings
            for Su rope embeddings
          max_position_embeddings: The max position embeddings for Su rope embeddings
          parallel_residual: Use parallel residual connections in each layer block, as used
            by the GPT-J and GPT-NeoX models.
          shared_layer_norm: When using parallel residual, share the input and post
            attention layer norms.
          pre_post_layer_norm: Add post layer norm for each pre norm layer
          multi_query_attention: Use multi-query attention (alias for num_heads_kv=1).
          num_heads_kv: Number of attention heads for the key and value.
          sliding_window: Max sequence length to retain in KV Cache.
          quant_type: quantization type used (like awq... for lower bit quantization)
          quant_group_size: group size of the lower bit quantization
          quant_bits: number of bit of the quantization (ex: 4bit)
        '''
        pass
    # WARNING: Decompyle incomplete

    config = (lambda self: self._config)()


class TransformerEncoderLayerSpec(model_spec.LayerSpec):
    
    def __init__(self, relative_position, relative_attention_bias, ffn_glu, rms_norm, num_heads_kv, sliding_window = (False, False, False, False, None, None)):
        self.self_attention = attention_spec.MultiHeadAttentionSpec(self_attention = True, relative_position = relative_position, relative_attention_bias = relative_attention_bias, rms_norm = rms_norm, num_heads_kv = num_heads_kv, sliding_window = sliding_window)
        self.ffn = FeedForwardSpec(glu = ffn_glu, rms_norm = rms_norm)



class TransformerDecoderLayerSpec(model_spec.LayerSpec):
    
    def __init__(self, with_encoder_attention, relative_position, relative_attention_bias, ffn_glu, rms_norm, rotary_dim, rotary_interleave, rotary_scaling_type, rotary_scaling_factor, rotary_base, original_max_position_embeddings, max_position_embeddings, parallel_residual, shared_layer_norm, pre_post_layer_norm, num_heads_kv, head_dim, sliding_window, qk_norm = (True, False, False, False, False, None, True, None, 1, 10000, 0, 0, False, False, False, None, None, None, False)):
        self.self_attention = attention_spec.MultiHeadAttentionSpec(self_attention = True, relative_position = relative_position, relative_attention_bias = relative_attention_bias, rms_norm = rms_norm, rotary_dim = rotary_dim, rotary_interleave = rotary_interleave, rotary_scaling_type = rotary_scaling_type, rotary_scaling_factor = rotary_scaling_factor, rotary_base = rotary_base, original_max_position_embeddings = original_max_position_embeddings, max_position_embeddings = max_position_embeddings, num_heads_kv = num_heads_kv, head_dim = head_dim, sliding_window = sliding_window, qk_norm = qk_norm)
        if with_encoder_attention:
            self.attention = attention_spec.MultiHeadAttentionSpec(rms_norm = rms_norm, num_heads_kv = num_heads_kv, sliding_window = sliding_window, qk_norm = qk_norm)
        self.ffn = FeedForwardSpec(glu = ffn_glu, rms_norm = rms_norm)
        if parallel_residual:
            if shared_layer_norm:
                self.shared_layer_norm = common_spec.LayerNormSpec()
            else:
                self.input_layer_norm = common_spec.LayerNormSpec()
                self.post_attention_layer_norm = common_spec.LayerNormSpec()
            delattr(self.self_attention, 'layer_norm')
            delattr(self.ffn, 'layer_norm')
        if pre_post_layer_norm:
            self.input_layer_norm = common_spec.LayerNormSpec(rms_norm = rms_norm)
            self.post_attention_layer_norm = common_spec.LayerNormSpec(rms_norm = rms_norm)
            self.pre_feedforward_layer_norm = common_spec.LayerNormSpec(rms_norm = rms_norm)
            self.post_feedforward_layer_norm = common_spec.LayerNormSpec(rms_norm = rms_norm)
            delattr(self.self_attention, 'layer_norm')
            delattr(self.ffn, 'layer_norm')
            return None



class FeedForwardSpec(model_spec.LayerSpec):
    
    def __init__(self, glu, rms_norm = (False, False)):
        self.layer_norm = common_spec.LayerNormSpec(rms_norm = rms_norm)
        self.linear_0 = common_spec.LinearSpec()
        self.linear_1 = common_spec.LinearSpec()
        if glu:
            self.linear_0_noact = common_spec.LinearSpec()
            return None



class PositionEncoderSpec(model_spec.LayerSpec):
    
    def __init__(self):
        self.encodings = model_spec.OPTIONAL



class TransformerConfig(model_spec.SequenceToSequenceModelConfig):
    pass
# WARNING: Decompyle incomplete


class TransformerSpec(model_spec.SequenceToSequenceModelSpec):
    pass
# WARNING: Decompyle incomplete


class TransformerDecoderModelConfig(model_spec.LanguageModelConfig):
    pass
# WARNING: Decompyle incomplete


class TransformerDecoderModelSpec(model_spec.LanguageModelSpec):
    pass
# WARNING: Decompyle incomplete


class TransformerEncoderModelConfig(model_spec.LanguageModelConfig):
    pass
# WARNING: Decompyle incomplete


class TransformerEncoderModelSpec(model_spec.LanguageModelSpec):
    pass
# WARNING: Decompyle incomplete
