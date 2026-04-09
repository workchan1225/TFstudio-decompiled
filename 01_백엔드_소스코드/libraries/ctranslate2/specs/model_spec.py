# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: model_spec.pyc (Python 3.11)

'''Specifications declare the expected variables layout of CTranslate2 models
that do not load a computation graph. The model converter should make sure that
each required variable of the specification is set.
'''
import abc
import ctypes
import json
import os
import shutil
import struct
from typing import Dict, List, Optional
import numpy as np

try:
    import torch
    torch_is_available = True
except ImportError:
    torch_is_available = False

OPTIONAL = '__optional'
CURRENT_BINARY_VERSION = 6
ACCEPTED_MODEL_TYPES = ('int8', 'int8_float32', 'int8_float16', 'int8_bfloat16', 'int16', 'float16', 'bfloat16', 'float32')
SKIP_CREATING_ALIAS = ('rotary_scaling_long_factor', 'rotary_scaling_short_factor')

def _join_scope(scope, name):
    if not scope:
        return name
    return f'''{None!s}/{name!s}'''


def _split_scope(scope):
    return scope.split('/')


def _parent_scope(scope):
    keys = _split_scope(scope)
    attr = keys[-1]
    scope = keys[:-1]
    return ('/'.join(scope), attr)


def visit_spec(spec, fn, scope = ('',)):
    '''Recursively visits a layer spec.'''
    for name, value in list(spec.__dict__.items()):
        if name.startswith('_'):
            continue
        if isinstance(value, list):
            for i, elem in enumerate(value):
                visit_spec(elem, fn, scope = _join_scope(scope, '%s_%d' % (name, i)))
                if isinstance(value, LayerSpec):
                    visit_spec(value, fn, scope = _join_scope(scope, name))
                    continue
        fn(spec, _join_scope(scope, name), value)
        return None


def index_spec(spec, index):
    if not index:
        return spec
    keys = None(index)
    for key in keys:
        spec = getattr(spec, key)
        except AttributeError:
            (attr, index) = key.rsplit('_', 1)
            spec = getattr(spec, attr)[int(index)]
            continue
        return spec


class FrozenMeta(type):
    pass
# WARNING: Decompyle incomplete


class FrozenAttr:
    pass
# WARNING: Decompyle incomplete


def LayerSpec():
    '''LayerSpec'''
    __doc__ = 'A layer specification declares the weights that should be set by the converters.'
    
    def validate(self = None):
        '''Verify that the required weights are set.

        Raises:
          ValueError: If a required weight is not set in the specification.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def variables(self = None, prefix = None, ordered = None):
        '''Recursively returns the weights from this layer and its children.

        Arguments:
          prefix: Prefix to prepend to all variable names.
          ordered: If set, an ordered list is returned instead.

        Returns:
          Dictionary mapping variables name to value.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _alias_variables(self):
        '''Find duplicate variables in spec and create aliases.'''
        variables = self.variables(ordered = True)
        for name, value in reversed(variables):
            for other_name, other_value in variables:
                if name == other_name:
                    pass
                else:
                    (scope, attr_name) = _parent_scope(name)
                    if value.is_scalar() and value.equal(other_value) and attr_name not in SKIP_CREATING_ALIAS:
                        spec = index_spec(self, scope)
                        setattr(spec, attr_name, other_name)
                    
            return None

    
    def _quantize(self, quantization):
        '''Possibly quantizes the variable of the layer.'''
        pass
    # WARNING: Decompyle incomplete

    
    def optimize(self = None, quantization = None):
        '''Recursively applies some optimizations to this layer:

        * Alias variables with the same shape and value.
        * Quantize weights.

        Arguments:
          quantization: Weight quantization scheme (possible values are: int8, int8_float32,
            int8_float16, int8_bfloat16, int16, float16, bfloat16, float32).
        '''
        self._alias_variables()
        self._quantize(quantization)

    
    def _visit(self, fn):
        '''Recursively visits this layer and its children.'''
        visit_spec(self, fn)


LayerSpec = <NODE:27>(LayerSpec, 'LayerSpec', FrozenAttr, metaclass = FrozenMeta)

def _dtype_to_type_id(object_dtype):
    dtypes = ('float32', 'int8', 'int16', 'int32', 'float16', 'bfloat16')
    
    try:
        return dtypes.index(object_dtype)
    except ValueError:
        raise ValueError(f'''{object_dtype!s} is not in list of supported dtypes: {', '.join(dtypes)!s}''')



def ModelConfig():
    '''ModelConfig'''
    __doc__ = 'Base class for model configurations.'
    
    def __init__(self, **kwargs):
        '''Initializes the configuration with a set of parameters.'''
        for key, value in kwargs.items():
            setattr(self, key, value)
            return None

    
    def to_dict(self):
        '''Returns the configuration as a dictionary.'''
        return self.__dict__.items()()

    
    def add_attribute(self, key, value):
        self.__dict__[key] = value

    
    def save_as_json(self, path):
        '''Saves the configuration as a JSON file.'''
        config_file = open(path, 'w', encoding = 'utf-8')
        json.dump(self.to_dict(), config_file, indent = 2, sort_keys = True)
        config_file.write('\n')
        None(None, None)
        return None
        with None:
            if not None:
                pass


ModelConfig = <NODE:27>(ModelConfig, 'ModelConfig', FrozenAttr, metaclass = FrozenMeta)

class ModelSpec(LayerSpec):
    '''The top level layer specification.'''
    
    def __init__(self):
        '''Initializes the model specification.'''
        self._config = self.get_default_config()
        self._files = { }

    name = (lambda self: raise NotImplementedError())()
    revision = (lambda self: 1)()
    config = (lambda self: self._config)()
    
    def get_default_config(self):
        '''Returns the default configuration used by this model.'''
        pass

    
    def register_file(self = property, path = property, filename = property):
        '''Registers a file to be saved in the model directory.'''
        if not os.path.isfile(path):
            raise ValueError('File %s does not exist' % path)
    # WARNING: Decompyle incomplete

    
    def save(self = None, output_dir = None):
        '''Saves this model on disk.

        Arguments:
          output_dir: Output directory where the model is saved.
        '''
        self._serialize(os.path.join(output_dir, 'model.bin'))
    # WARNING: Decompyle incomplete

    
    def _serialize(self, path):
        '''Serializes the model variables.'''
        pass
    # WARNING: Decompyle incomplete



def _flatten_vocabularies(vocabularies):
    pass
# WARNING: Decompyle incomplete


class SequenceToSequenceModelConfig(ModelConfig):
    pass
# WARNING: Decompyle incomplete


class SequenceToSequenceModelSpec(ModelSpec):
    pass
# WARNING: Decompyle incomplete


class LanguageModelConfig(ModelConfig):
    pass
# WARNING: Decompyle incomplete


class LanguageModelSpec(ModelSpec):
    pass
# WARNING: Decompyle incomplete


def _save_vocabulary(output_dir, name, tokens):
    vocabulary_path = os.path.join(output_dir, '%s.json' % name)
    vocabulary_file = open(vocabulary_path, 'w', encoding = 'utf-8')
    json.dump(tokens, vocabulary_file, indent = 2)
    None(None, None)
    return None
    with None:
        if not None:
            pass


class Variable(abc.ABC):
    '''Abstract base class for model variables.'''
    shape = (lambda self = None: raise NotImplementedError())()()
    
    def is_scalar(self = None):
        return len(self.shape) == 0

    dtype = (lambda self = None: raise NotImplementedError())()()
    
    def to(self = None, dtype = None):
        if dtype == self.dtype:
            return self
        return None._to(dtype)

    numpy = (lambda self = None: raise NotImplementedError())()
    
    def equal(self = None, other = None):
