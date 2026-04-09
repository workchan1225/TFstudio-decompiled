# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transformers.pyc (Python 3.11)

import abc
import argparse
import gc
import itertools
import os
from typing import List, Optional
import numpy as np

try:
    import huggingface_hub
    import torch
    import transformers
except ImportError:
    pass

from ctranslate2.converters import utils
from ctranslate2.converters.converter import Converter
from ctranslate2.specs import attention_spec, common_spec, model_spec, transformer_spec, wav2vec2_spec, wav2vec2bert_spec, whisper_spec
_SUPPORTED_ACTIVATIONS = {
    'gelu': common_spec.Activation.GELU,
    'gelu_fast': common_spec.Activation.GELUTanh,
    'gelu_new': common_spec.Activation.GELUTanh,
    'gelu_python': common_spec.Activation.GELU,
    'gelu_pytorch_tanh': common_spec.Activation.GELUTanh,
    'quick_gelu': common_spec.Activation.GELUSigmoid,
    'relu': common_spec.Activation.RELU,
    'silu': common_spec.Activation.SWISH,
    'swish': common_spec.Activation.SWISH }
_SUPPORTED_ROPE_SCALING = {
    'linear': attention_spec.RotaryScalingType.Linear,
    'su': attention_spec.RotaryScalingType.Su,
    'llama3': attention_spec.RotaryScalingType.Llama3,
    'longrope': attention_spec.RotaryScalingType.Su }
_SUPPORTED_QUANTIZATION = {
    'gemm': common_spec.Quantization.AWQ_GEMM,
    'gemv': common_spec.Quantization.AWQ_GEMV }
_MODEL_LOADERS = { }

def register_loader(config_name):
    '''Registers a model loader for this configuration name.'''
    pass
# WARNING: Decompyle incomplete


class TransformersConverter(Converter):
    '''Converts models from Hugging Face Transformers.'''
    
    def __init__(self, model_name_or_path, activation_scales, copy_files = None, load_as_float16 = None, revision = None, low_cpu_mem_usage = (None, None, False, None, False, False), trust_remote_code = ('model_name_or_path', str, 'activation_scales', Optional[str], 'copy_files', Optional[List[str]], 'load_as_float16', bool, 'revision', Optional[str], 'low_cpu_mem_usage', bool, 'trust_remote_code', bool)):
        '''Initializes the converter.

        Arguments:
          model_name_or_path: Name of the pretrained model to download, or path to the
            directory containing the pretrained model.
          activation_scales: Path to the pre-computed activation scales. Models may
            use them to rescale some weights to smooth the intermediate activations
            and improve the quantization accuracy. See
            https://github.com/mit-han-lab/smoothquant.
          copy_files: List of filenames to copy from the Hugging Face model to the
            converted model directory.
          load_as_float16: Load the model weights as float16. More precisely, the model
            will be loaded with ``from_pretrained(..., torch_dtype=torch.float16)``.
          revision: Revision of the model to download from the Hugging Face Hub.
          low_cpu_mem_usage: Enable the flag ``low_cpu_mem_usage`` when loading the model
            with ``from_pretrained``.
          trust_remote_code: Allow converting models using custom code.
        '''
        self._model_name_or_path = model_name_or_path
        self._activation_scales = activation_scales
        self._copy_files = copy_files
        self._load_as_float16 = load_as_float16
        self._revision = revision
        self._low_cpu_mem_usage = low_cpu_mem_usage
        self._trust_remote_code = trust_remote_code

    
    def _load(self):
        torch.no_grad()
        config = transformers.AutoConfig.from_pretrained(self._model_name_or_path, trust_remote_code = self._trust_remote_code)
        config_name = config.__class__.__name__
        loader = _MODEL_LOADERS.get(config_name)
    # WARNING: Decompyle incomplete

    
    def load_model(self, model_class, model_name_or_path, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def load_tokenizer(self, tokenizer_class, model_name_or_path, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def get_model_file(self, filename):
        if os.path.isdir(self._model_name_or_path):
            path = os.path.join(self._model_name_or_path, filename)
    # WARNING: Decompyle incomplete



class ModelLoader(abc.ABC):
    '''Base class for loading Transformers models into a CTranslate2 model specification.'''
    architecture_name = (lambda self: pass)()
    get_model_spec = (lambda self, model: raise NotImplementedError())()
    
    def __call__(self, model, tokenizer):
        spec = self.get_model_spec(model)
        self.set_config(spec.config, model, tokenizer)
        tokens = self.get_vocabulary(model, tokenizer)
        self.set_vocabulary(spec, tokens)
        return spec

    
    def get_vocabulary(self, model, tokenizer):
        return sorted(tokenizer.get_vocab().items(), key = (lambda item: item[1]))()

    
    def set_vocabulary(self, spec, tokens):
        pass

    
    def set_config(self, config, model, tokenizer):
        pass

    
    def set_layer_norm(self, spec, module):
        spec.gamma = module.weight
        spec.beta = module.bias

    
    def set_linear(self, spec, module, quant_type = (common_spec.Quantization.CT2,)):
        if quant_type == common_spec.Quantization.CT2:
            spec.weight = module.weight
        else:
            spec.weight = module.qweight
            spec.weight_scale = module.scales
            spec.weight_zero = module.qzeros
        if isinstance(module, transformers.Conv1D):
            spec.weight = spec.weight.transpose(0, 1)
    # WARNING: Decompyle incomplete

    
    def set_embeddings(self, spec, module):
        spec.weight = module.weight

    
    def set_position_encodings(self, spec, module):
        spec.encodings = module.weight
        offset = getattr(module, 'offset', 0)
        if offset > 0:
            spec.encodings = spec.encodings[offset:]
            return None

    
    def smooth_activation(self, spec, activation_scales):
        raise NotImplementedError('No activation smoothing logic is defined for this model')


BartLoader = <NODE:12>()
MarianMTLoader = <NODE:12>()
M2M100Loader = <NODE:12>()
MBartLoader = <NODE:12>()
PegasusLoader = <NODE:12>()
OPTLoader = <NODE:12>()
GPTBigCodeMHALoader = <NODE:12>()
GPT2Loader = <NODE:12>()
GPTJLoader = <NODE:12>()
CodeGenLoader = <NODE:12>()
GPTNeoXLoader = <NODE:12>()
WhisperLoader = <NODE:12>()
Wav2Vec2Loader = <NODE:12>()
Wav2Vec2BertLoader = <NODE:12>()
T5Loader = <NODE:12>()
MT5Loader = <NODE:12>()
BloomLoader = <NODE:12>()
MPTLoader = <NODE:12>()
GemmaLoader = <NODE:12>()
Gemma2Loader = <NODE:12>()
LlamaLoader = <NODE:12>()
Gemma3Loader = <NODE:12>()()
MistralLoader = <NODE:12>()
Qwen2Loader = <NODE:12>()
Qwen3Loader = <NODE:12>()
MixFormerSequentialLoader = <NODE:12>()
PhiLoader = <NODE:12>()
Phi3Loader = <NODE:12>()
RWLoader = <NODE:12>()
FalconLoader = <NODE:12>()
DistilBertLoader = <NODE:12>()
BertLoader = <NODE:12>()
XLMRobertaLoader = <NODE:12>()
RobertaLoader = <NODE:12>()
CamembertLoader = <NODE:12>()

def main():
    parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--model', required = True, help = 'Name of the pretrained model to download, or path to a directory containing the pretrained model.')
    parser.add_argument('--activation_scales', help = 'Path to the pre-computed activation scales. Models may use them to rescale some weights to smooth the intermediate activations and improve the quantization accuracy. See https://github.com/mit-han-lab/smoothquant.')
    parser.add_argument('--copy_files', nargs = '+', help = 'List of filenames to copy from the Hugging Face model to the converted model directory.')
    parser.add_argument('--revision', help = 'Revision of the model to download from the Hugging Face Hub.')
    parser.add_argument('--low_cpu_mem_usage', action = 'store_true', help = 'Enable the flag low_cpu_mem_usage when loading the model with from_pretrained.')
    parser.add_argument('--trust_remote_code', action = 'store_true', help = 'Allow converting models using custom code.')
    Converter.declare_arguments(parser)
    args = parser.parse_args()
    converter = TransformersConverter(args.model, activation_scales = args.activation_scales, copy_files = args.copy_files, load_as_float16 = args.quantization in ('float16', 'int8_float16'), revision = args.revision, low_cpu_mem_usage = args.low_cpu_mem_usage, trust_remote_code = args.trust_remote_code)
    converter.convert_from_args(args)

if __name__ == '__main__':
    main()
_WHISPER_ALIGNMENT_HEADS = {
    'openai/whisper-tiny.en': [
        (1, 0),
        (2, 0),
        (2, 5),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 4)],
    'openai/whisper-tiny': [
        (2, 2),
        (3, 0),
        (3, 2),
        (3, 3),
        (3, 4),
        (3, 5)],
    'openai/whisper-base.en': [
        (3, 3),
        (4, 7),
        (5, 1),
        (5, 5),
        (5, 7)],
    'openai/whisper-base': [
        (3, 1),
        (4, 2),
        (4, 3),
        (4, 7),
        (5, 1),
        (5, 2),
        (5, 4),
        (5, 6)],
    'openai/whisper-small.en': [
        (6, 6),
        (7, 0),
        (7, 3),
        (7, 8),
        (8, 2),
        (8, 5),
        (8, 7),
        (9, 0),
        (9, 4),
        (9, 8),
        (9, 10),
        (10, 0),
        (10, 1),
        (10, 2),
        (10, 3),
        (10, 6),
        (10, 11),
        (11, 2),
        (11, 4)],
    'openai/whisper-small': [
        (5, 3),
        (5, 9),
        (8, 0),
        (8, 4),
        (8, 7),
        (8, 8),
        (9, 0),
        (9, 7),
        (9, 9),
        (10, 5)],
    'openai/whisper-medium.en': [
        (11, 4),
        (14, 1),
        (14, 12),
        (14, 14),
        (15, 4),
        (16, 0),
        (16, 4),
        (16, 9),
        (17, 12),
        (17, 14),
        (18, 7),
        (18, 10),
        (18, 15),
        (20, 0),
        (20, 3),
        (20, 9),
        (20, 14),
        (21, 12)],
    'openai/whisper-medium': [
        (13, 15),
        (15, 4),
        (15, 15),
        (16, 1),
        (20, 0),
        (23, 4)],
    'openai/whisper-large': [
        (9, 19),
        (11, 2),
        (11, 4),
        (11, 17),
        (22, 7),
        (22, 11),
        (22, 17),
        (23, 2),
        (23, 15)],
    'openai/whisper-large-v2': [
        (10, 12),
        (13, 17),
        (16, 11),
        (16, 12),
        (16, 13),
        (17, 15),
        (17, 16),
        (18, 4),
        (18, 11),
        (18, 19),
        (19, 11),
        (21, 2),
        (21, 3),
        (22, 3),
        (22, 9),
        (22, 12),
        (23, 5),
        (23, 7),
        (23, 13),
        (25, 5),
        (26, 1),
        (26, 12),
        (27, 15)],
    'openai/whisper-large-v3': [
        (7, 0),
        (10, 17),
        (12, 18),
        (13, 12),
        (16, 1),
        (17, 14),
        (19, 11),
        (21, 4),
        (24, 1),
        (25, 6)] }
