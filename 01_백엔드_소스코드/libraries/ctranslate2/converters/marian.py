# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: marian.pyc (Python 3.11)

import argparse
import re
from typing import List
import numpy as np
import yaml
from ctranslate2.converters import utils
from ctranslate2.converters.converter import Converter
from ctranslate2.specs import common_spec, transformer_spec
_SUPPORTED_ACTIVATIONS = {
    'gelu': common_spec.Activation.GELUSigmoid,
    'relu': common_spec.Activation.RELU,
    'swish': common_spec.Activation.SWISH }
_SUPPORTED_POSTPROCESS_EMB = {
    '',
    'd',
    'n',
    'nd'}

class MarianConverter(Converter):
    '''Converts models trained with Marian.'''
    
    def __init__(self = None, model_path = None, vocab_paths = None):
        '''Initializes the Marian converter.

        Arguments:
          model_path: Path to the Marian model (.npz file).
          vocab_paths: Paths to the vocabularies (.yml files).
        '''
        self._model_path = model_path
        self._vocab_paths = vocab_paths

    
    def _load(self):
        model = np.load(self._model_path)
        config = _get_model_config(model)
        vocabs = list(map(load_vocab, self._vocab_paths))
        activation = config['transformer-ffn-activation']
        pre_norm = 'n' in config['transformer-preprocess']
        postprocess_emb = config['transformer-postprocess-emb']
        check = utils.ConfigurationChecker()
        check(config['type'] == 'transformer', "Option --type must be 'transformer'")
        check(config['transformer-decoder-autoreg'] == 'self-attention', "Option --transformer-decoder-autoreg must be 'self-attention'")
        check(not config['transformer-no-projection'], 'Option --transformer-no-projection is not supported')
        check(activation in _SUPPORTED_ACTIVATIONS, f'''Option --transformer-ffn-activation {activation!s} is not supported (supported activations are: {', '.join(_SUPPORTED_ACTIVATIONS.keys())!s})''')
        check(postprocess_emb in _SUPPORTED_POSTPROCESS_EMB, f'''Option --transformer-postprocess-emb {postprocess_emb!s} is not supported (supported values are: {', '.join(_SUPPORTED_POSTPROCESS_EMB)!s})''')
        if pre_norm:
            if config['transformer-preprocess'] == 'n':
                if config['transformer-postprocess'] == 'da':
                    check(config.get('transformer-postprocess-top', '') == 'n', 'Unsupported pre-norm Transformer architecture, expected the following combination of options: --transformer-preprocess n --transformer-postprocess da --transformer-postprocess-top n')
                elif config['transformer-preprocess'] == '':
                    if config['transformer-postprocess'] == 'dan':
                        config['transformer-preprocess'] == ''(config.get('transformer-postprocess-top', '') == '', "Unsupported post-norm Transformer architecture, excepted the following combination of options: --transformer-preprocess '' --transformer-postprocess dan --transformer-postprocess-top ''")
                        check.validate()
                        alignment_layer = config['transformer-guided-alignment-layer']
        alignment_layer = -1 if alignment_layer == 'last' else int(alignment_layer) - 1
        layernorm_embedding = 'n' in postprocess_emb
        model_spec = transformer_spec.TransformerSpec.from_config((config['enc-depth'], config['dec-depth']), config['transformer-heads'], pre_norm = pre_norm, activation = _SUPPORTED_ACTIVATIONS[activation], alignment_layer = alignment_layer, alignment_heads = 1, layernorm_embedding = layernorm_embedding)
        set_transformer_spec(model_spec, model)
        model_spec.register_source_vocabulary(vocabs[0])
        model_spec.register_target_vocabulary(vocabs[-1])
        model_spec.config.add_source_eos = True
        return model_spec



def _get_model_config(model):
    config = model['special:model.yml']
    config = config[:-1].tobytes()
    config = yaml.safe_load(config)
    return config


def load_vocab(path):
    vocab = open(path, encoding = 'utf-8')
    tokens = []
    token = None
    idx = None
# WARNING: Decompyle incomplete


def set_transformer_spec(spec, weights):
    set_transformer_encoder(spec.encoder, weights, 'encoder')
    set_transformer_decoder(spec.decoder, weights, 'decoder')


def set_transformer_encoder(spec, weights, scope):
    set_common_layers(spec, weights, scope)
    for i, layer_spec in enumerate(spec.layer):
        set_transformer_encoder_layer(layer_spec, weights, '%s_l%d' % (scope, i + 1))
        return None


def set_transformer_decoder(spec, weights, scope):
    spec.start_from_zero_embedding = True
    set_common_layers(spec, weights, scope)
    for i, layer_spec in enumerate(spec.layer):
        set_transformer_decoder_layer(layer_spec, weights, '%s_l%d' % (scope, i + 1))
        set_linear(spec.projection, weights, '%s_ff_logit_out' % scope, reuse_weight = spec.embeddings.weight)
        return None


def set_common_layers(spec, weights, scope):
    embeddings_specs = spec.embeddings
    if not isinstance(embeddings_specs, list):
        embeddings_specs = [
            embeddings_specs]
    set_embeddings(embeddings_specs[0], weights, scope)
    set_position_encodings(spec.position_encodings, weights, dim = embeddings_specs[0].weight.shape[1])
    if hasattr(spec, 'layernorm_embedding'):
        set_layer_norm(spec.layernorm_embedding, weights, '%s_emb' % scope, pre_norm = True)
    if hasattr(spec, 'layer_norm'):
        set_layer_norm(spec.layer_norm, weights, '%s_top' % scope)
        return None


def set_transformer_encoder_layer(spec, weights, scope):
    set_ffn(spec.ffn, weights, '%s_ffn' % scope)
    set_multi_head_attention(spec.self_attention, weights, '%s_self' % scope, self_attention = True)


def set_transformer_decoder_layer(spec, weights, scope):
    set_ffn(spec.ffn, weights, '%s_ffn' % scope)
    set_multi_head_attention(spec.self_attention, weights, '%s_self' % scope, self_attention = True)
    set_multi_head_attention(spec.attention, weights, '%s_context' % scope)


def set_multi_head_attention(spec, weights, scope, self_attention = (False,)):
    split_layers = range(3)()
    set_linear(split_layers[0], weights, scope, 'q')
    set_linear(split_layers[1], weights, scope, 'k')
    set_linear(split_layers[2], weights, scope, 'v')
    set_linear(spec.linear[-1], weights, scope, 'o')
    set_layer_norm_auto(spec.layer_norm, weights, '%s_Wo' % scope)


def set_ffn(spec, weights, scope):
    set_layer_norm_auto(spec.layer_norm, weights, '%s_ffn' % scope)
    set_linear(spec.linear_0, weights, scope, '1')
    set_linear(spec.linear_1, weights, scope, '2')


def set_layer_norm_auto(spec, weights, scope):
    
    try:
        set_layer_norm(spec, weights, scope, pre_norm = True)
        return None
    except KeyError:
        set_layer_norm(spec, weights, scope)
        return None



def set_layer_norm(spec, weights, scope, pre_norm = (False,)):
    suffix = '_pre' if pre_norm else ''
    spec.gamma = weights[f'''{scope!s}_ln_scale{suffix!s}'''].squeeze()
    spec.beta = weights[f'''{scope!s}_ln_bias{suffix!s}'''].squeeze()


def set_linear(spec, weights, scope, suffix, reuse_weight = ('', None)):
    weight = weights.get(f'''{scope!s}_W{suffix!s}''')
# WARNING: Decompyle incomplete


def set_embeddings(spec, weights, scope):
    spec.weight = weights.get('%s_Wemb' % scope)
# WARNING: Decompyle incomplete


def set_position_encodings(spec, weights, dim = (None,)):
    spec.encodings = weights.get('Wpos', _make_sinusoidal_position_encodings(dim))


def _make_sinusoidal_position_encodings(dim, num_positions = (2048,)):
    positions = np.arange(num_positions)
    timescales = np.power(10000, 2 * (np.arange(dim) // 2) / dim)
    position_enc = np.expand_dims(positions, 1) / np.expand_dims(timescales, 0)
    table = np.zeros_like(position_enc)
    table[(:, :dim // 2)] = np.sin(position_enc[(:, 0::2)])
    table[(:, dim // 2:)] = np.cos(position_enc[(:, 1::2)])
    return table


def main():
    parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--model_path', required = True, help = 'Path to the model .npz file.')
    parser.add_argument('--vocab_paths', required = True, nargs = '+', help = 'List of paths to the YAML vocabularies.')
    Converter.declare_arguments(parser)
    args = parser.parse_args()
    converter = MarianConverter(args.model_path, args.vocab_paths)
    converter.convert_from_args(args)

if __name__ == '__main__':
    main()
    return None
