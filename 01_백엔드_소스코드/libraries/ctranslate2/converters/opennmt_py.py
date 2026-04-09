# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: opennmt_py.pyc (Python 3.11)

import argparse
from ctranslate2.converters import utils
from ctranslate2.converters.converter import Converter
from ctranslate2.specs import common_spec, transformer_spec
_SUPPORTED_ACTIVATIONS = {
    'gelu': common_spec.Activation.GELU,
    'fast_gelu': common_spec.Activation.GELUTanh,
    'relu': common_spec.Activation.RELU,
    'silu': common_spec.Activation.SWISH }
_SUPPORTED_FEATURES_MERGE = {
    'concat': common_spec.EmbeddingsMerge.CONCAT,
    'sum': common_spec.EmbeddingsMerge.ADD }

def check_opt(opt, num_source_embeddings):
