# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: opennmt_tf.pyc (Python 3.11)

import argparse
import copy
import os
from typing import Optional, Union
from ctranslate2.converters import utils
from ctranslate2.converters.converter import Converter
from ctranslate2.specs import common_spec, transformer_spec
_SUPPORTED_ACTIVATIONS = {
    'gelu': common_spec.Activation.GELUTanh,
    'relu': common_spec.Activation.RELU,
    'swish': common_spec.Activation.SWISH }

class OpenNMTTFConverter(Converter):
    '''Converts OpenNMT-tf models.'''
    from_config = (lambda cls = None, config = None, auto_config = classmethod, checkpoint_path = (False, None, None), model = ('config', Union[(str, dict)], 'auto_config', bool, 'checkpoint_path', Optional[str], 'model', Optional[str]): config_util = configimport opennmtCheckpoint = Checkpointimport opennmt.utils.checkpointif isinstance(config, str):
config = config_util.load_config([
config])else:
config = copy.deepcopy(config)# WARNING: Decompyle incomplete
)()
    
    def __init__(self, model):
        '''Initializes the converter.

        Arguments:
          model: An initialized and fully-built ``opennmt.models.Model`` instance.
        '''
        self._model = model

    
    def _load(self):
        import opennmt
        if isinstance(self._model, opennmt.models.LanguageModel):
            spec_builder = TransformerDecoderSpecBuilder()
        else:
            spec_builder = TransformerSpecBuilder()
        return spec_builder(self._model)



class TransformerSpecBuilder:
    
    def __call__(self, model):
        pass
    # WARNING: Decompyle incomplete

    
    def set_transformer_encoder(self, spec, module, inputter):
        pass
    # WARNING: Decompyle incomplete

    
    def set_transformer_decoder(self, spec, module, inputter):
        self.set_embeddings(spec.embeddings, inputter)
    # WARNING: Decompyle incomplete

    
    def set_ffn(self, spec, module):
        self.set_linear(spec.linear_0, module.layer.inner)
        self.set_linear(spec.linear_1, module.layer.outer)
        self.set_layer_norm_from_wrapper(spec.layer_norm, module)

    
    def set_multi_head_attention(self, spec, module, self_attention = (False,)):
        split_layers = range(3)()
        self.set_linear(split_layers[0], module.layer.linear_queries)
        self.set_linear(split_layers[1], module.layer.linear_keys)
        self.set_linear(split_layers[2], module.layer.linear_values)
    # WARNING: Decompyle incomplete

    
    def set_layer_norm_from_wrapper(self, spec, module):
        pass
    # WARNING: Decompyle incomplete

    
    def set_layer_norm(self, spec, module):
        spec.gamma = module.gamma.numpy()
        spec.beta = module.beta.numpy()

    
    def set_linear(self, spec, module):
        spec.weight = module.kernel.numpy()
        if not module.transpose:
            spec.weight = spec.weight.transpose()
    # WARNING: Decompyle incomplete

    
    def set_embeddings(self, spec, module):
        spec.weight = module.embedding.numpy()

    
    def set_position_encodings(self, spec, module):
        import opennmt
        if isinstance(module, opennmt.layers.PositionEmbedder):
            spec.encodings = module.embedding.numpy()[1:]
            return None



class TransformerDecoderSpecBuilder(TransformerSpecBuilder):
    
    def __call__(self, model):
        import opennmt
        check = utils.ConfigurationChecker()
        check(isinstance(model.decoder, opennmt.decoders.SelfAttentionDecoder), 'Only self-attention decoders are supported')
        check.validate()
        mha = model.decoder.layers[0].self_attention.layer
        ffn = model.decoder.layers[0].ffn.layer
        activation_name = ffn.inner.activation.__name__
        check(activation_name in _SUPPORTED_ACTIVATIONS, f'''Activation {activation_name!s} is not supported (supported activations are: {', '.join(_SUPPORTED_ACTIVATIONS.keys())!s})''')
        check.validate()
        spec = transformer_spec.TransformerDecoderModelSpec.from_config(len(model.decoder.layers), mha.num_heads, pre_norm = model.decoder.layer_norm is not None, activation = _SUPPORTED_ACTIVATIONS[activation_name])
        spec.register_vocabulary(_load_vocab(model.features_inputter.vocabulary_file))
        self.set_transformer_decoder(spec.decoder, model.decoder, model.features_inputter)
        return spec



def _get_inputters(inputter):
    import opennmt
    return inputter.inputters if isinstance(inputter, opennmt.inputters.MultiInputter) else [
        inputter]


def _load_vocab(vocab, unk_token = ('<unk>',)):
    import opennmt
    if isinstance(vocab, opennmt.data.Vocab):
        tokens = list(vocab.words)
    elif isinstance(vocab, list):
        tokens = list(vocab)
    elif isinstance(vocab, str):
        tokens = opennmt.data.Vocab.from_file(vocab).words
    else:
        raise TypeError('Invalid vocabulary type')
    if unk_token not in tokens:
        tokens.append(unk_token)
    return tokens


def main():
    parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config', help = 'Path to the YAML configuration.')
    parser.add_argument('--auto_config', action = 'store_true', help = 'Use the model automatic configuration values.')
    parser.add_argument('--model_path', help = 'Path to the checkpoint or checkpoint directory to load. If not set, the latest checkpoint from the model directory is loaded.')
    parser.add_argument('--model_type', help = 'If the model instance cannot be resolved from the model directory, this argument can be set to either the name of the model in the catalog or the path to the model configuration.')
    parser.add_argument('--src_vocab', help = 'Path to the source vocabulary (required if no configuration is set).')
    parser.add_argument('--tgt_vocab', help = 'Path to the target vocabulary (required if no configuration is set).')
    Converter.declare_arguments(parser)
    args = parser.parse_args()
    config = args.config
    if not config:
        if not args.model_path and args.src_vocab or args.tgt_vocab:
            raise ValueError('Options --model_path, --src_vocab, --tgt_vocab are required when a configuration is not set')
        model_dir = args.model_path if os.path.isdir(args.model_path) else os.path.dirname(args.model_path)
        config = {
            'model_dir': model_dir,
            'data': {
                'source_vocabulary': args.src_vocab,
                'target_vocabulary': args.tgt_vocab } }
    converter = OpenNMTTFConverter.from_config(config, auto_config = args.auto_config, checkpoint_path = args.model_path, model = args.model_type)
    converter.convert_from_args(args)

if __name__ == '__main__':
    main()
    return None
