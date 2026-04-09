# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: converter.pyc (Python 3.11)

import abc
import argparse
import os
import shutil
from typing import Optional
from ctranslate2.specs.model_spec import ACCEPTED_MODEL_TYPES, ModelSpec

class Converter(abc.ABC):
    '''Base class for model converters.'''
    declare_arguments = (lambda parser = None: parser.add_argument('--output_dir', required = True, help = 'Output model directory.')parser.add_argument('--vocab_mapping', default = None, help = 'Vocabulary mapping file (optional).')parser.add_argument('--quantization', default = None, choices = ACCEPTED_MODEL_TYPES, help = 'Weight quantization type.')parser.add_argument('--force', action = 'store_true', help = 'Force conversion even if the output directory already exists.')parser)()
    
    def convert_from_args(self = None, args = None):
        '''Helper function to call :meth:`ctranslate2.converters.Converter.convert`
        with the parsed command line options.

        Arguments:
          args: Namespace containing parsed arguments.

        Returns:
          Path to the output directory.
        '''
        return self.convert(args.output_dir, vmap = args.vocab_mapping, quantization = args.quantization, force = args.force)

    
    def convert(self = None, output_dir = None, vmap = None, quantization = (None, None, False), force = ('output_dir', str, 'vmap', Optional[str], 'quantization', Optional[str], 'force', bool, 'return', str)):
        '''Converts the model to the CTranslate2 format.

        Arguments:
          output_dir: Output directory where the CTranslate2 model is saved.
          vmap: Optional path to a vocabulary mapping file that will be included
            in the converted model directory.
          quantization: Weight quantization scheme (possible values are: int8, int8_float32,
            int8_float16, int8_bfloat16, int16, float16, bfloat16, float32).
          force: Override the output directory if it already exists.

        Returns:
          Path to the output directory.

        Raises:
          RuntimeError: If the output directory already exists and :obj:`force`
            is not set.
          NotImplementedError: If the converter cannot convert this model to the
            CTranslate2 format.
        '''
        if not os.path.exists(output_dir) and force:
            raise RuntimeError('output directory %s already exists, use --force to override' % output_dir)
        model_spec = self._load()
    # WARNING: Decompyle incomplete

    _load = (lambda self: raise NotImplementedError())()
