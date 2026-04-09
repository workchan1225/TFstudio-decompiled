# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: model_types.pyc (Python 3.11)

'''Type definitions for the models service.'''
from __future__ import annotations
from collections.abc import Mapping
import csv
import dataclasses
import datetime
import json
import pathlib
import re
from typing import Any, Iterable, Union
import urllib.request as urllib
from typing_extensions import TypedDict
from google.generativeai import protos
from google.generativeai.types import permission_types
from google.generativeai import string_utils
__all__ = [
    'Model',
    'ModelNameOptions',
    'AnyModelNameOptions',
    'BaseModelNameOptions',
    'TunedModelNameOptions',
    'ModelsIterable',
    'TunedModel',
    'TunedModelState']
TunedModelState = protos.TunedModel.State
TunedModelStateOptions = Union[(None, str, int, TunedModelState)]
_TUNED_MODEL_VALID_NAME = '[a-z](([a-z0-9-]{0,61}[a-z0-9])?)$'
TUNED_MODEL_NAME_ERROR_MSG = 'The `name` must consist of alphanumeric characters (or -) and be at most 63 characters; The name you entered:\n\tlen(name)== {length}\n\tname={name}\n'

def valid_tuned_model_name(name = None):
    return re.match(_TUNED_MODEL_VALID_NAME, name) is not None

_TUNED_MODEL_STATES: 'dict[TunedModelStateOptions, TunedModelState]' = {
    None: TunedModelState.STATE_UNSPECIFIED,
    'unspecified': TunedModelState.STATE_UNSPECIFIED,
    'state_unspecified': TunedModelState.STATE_UNSPECIFIED,
    int(TunedModelState.STATE_UNSPECIFIED): TunedModelState.STATE_UNSPECIFIED,
    TunedModelState.STATE_UNSPECIFIED: TunedModelState.STATE_UNSPECIFIED,
    'failed': TunedModelState.FAILED,
    int(TunedModelState.FAILED): TunedModelState.FAILED,
    TunedModelState.FAILED: TunedModelState.FAILED,
    'creating': TunedModelState.CREATING,
    int(TunedModelState.CREATING): TunedModelState.CREATING,
    TunedModelState.CREATING: TunedModelState.CREATING,
    'active': TunedModelState.ACTIVE,
    int(TunedModelState.ACTIVE): TunedModelState.ACTIVE,
    TunedModelState.ACTIVE: TunedModelState.ACTIVE }

def to_tuned_model_state(x = None):
    if isinstance(x, str):
        x = x.lower()
    return _TUNED_MODEL_STATES[x]

Model = <NODE:12>()()

def _fix_microseconds(match):
    fraction = float(match.group(0))
    return f'''.{int(round(fraction * 1e+06)):06d}'''


def idecode_time(parent = None, name = string_utils.prettyprint):
    time = parent.pop(name, None)
# WARNING: Decompyle incomplete


def decode_tuned_model(tuned_model = None):
    if isinstance(tuned_model, protos.TunedModel):
        tuned_model = type(tuned_model).to_dict(tuned_model, including_default_value_fields = False)
    tuned_model['state'] = to_tuned_model_state(tuned_model.pop('state', None))
    base_model = tuned_model.pop('base_model', None)
    tuned_model_source = tuned_model.pop('tuned_model_source', None)
# WARNING: Decompyle incomplete

TunedModel = <NODE:12>()()
TuningTask = <NODE:12>()()

class TuningExampleDict(TypedDict):
    output: 'str' = 'TuningExampleDict'

TuningExampleOptions = Union[(TuningExampleDict, protos.TuningExample, tuple[(str, str)], list[str])]
TuningDataOptions = Union[(pathlib.Path, str, protos.Dataset, Mapping[(str, Iterable[str])], Iterable[TuningExampleOptions])]

def encode_tuning_data(data = string_utils.prettyprint, input_key = dataclasses.dataclass, output_key = None):
    if isinstance(data, protos.Dataset):
        return data
    if None(data, str):
        if re.match('^\\w+://\\S+$', data):
            data = _normalize_url(data)
        else:
            data = pathlib.Path(data)
    if isinstance(data, (str, pathlib.Path)):
        if str(data).lower().endswith('.json'):
            f
            data = json.load(f)
            None(None, None)
        else:
            with None:
                if not None if isinstance(data, str) else (lambda .0: pass# WARNING: Decompyle incomplete
):
                    pass
    else:
        f
        data = csv.DictReader(content)
        None(None, None)
        return 
        with None:
            if not None, _convert_iterable(data, input_key, output_key):
                pass
    if hasattr(data, 'keys'):
        return _convert_dict(data, input_key, output_key)
    return None(data, input_key, output_key)


def _normalize_url(url = None):
    sheet_base = 'https://docs.google.com/spreadsheets'
# WARNING: Decompyle incomplete


def _convert_dict(data, input_key, output_key):
    new_data = list()
    
    try:
        inputs = data[input_key]
    except KeyError:
        raise KeyError(f'''Invalid key: The input key \'{input_key}\' does not exist in the data. Available keys are: {sorted(data.keys())}.''')

    
    try:
        outputs = data[output_key]
    except KeyError:
        raise KeyError(f'''Invalid key: The output key \'{output_key}\' does not exist in the data. Available keys are: {sorted(data.keys())}.''')

    for i, o in zip(inputs, outputs):
        new_data.append(protos.TuningExample({
            'text_input': str(i),
            'output': str(o) }))
        return protos.Dataset(examples = protos.TuningExamples(examples = new_data))


def _convert_iterable(data, input_key, output_key):
    new_data = list()
    for example in data:
        example = encode_tuning_example(example, input_key, output_key)
        new_data.append(example)
        return protos.Dataset(examples = protos.TuningExamples(examples = new_data))


def encode_tuning_example(example = None, input_key = None, output_key = None):
    if isinstance(example, protos.TuningExample):
        return example
    if None(example, (tuple, list)):
        (a, b) = example
        example = protos.TuningExample(text_input = a, output = b)
    else:
        example = protos.TuningExample(text_input = example[input_key], output = example[output_key])
    return example

TuningSnapshot = <NODE:12>()()
Hyperparameters = <NODE:12>()()
BaseModelNameOptions = Union[(str, Model, protos.Model)]
TunedModelNameOptions = Union[(str, TunedModel, protos.TunedModel)]
AnyModelNameOptions = Union[(str, Model, protos.Model, TunedModel, protos.TunedModel)]
ModelNameOptions = AnyModelNameOptions

def make_model_name(name = dataclasses.dataclass):
    if isinstance(name, (Model, protos.Model, TunedModel, protos.TunedModel)):
        name = name.name
    elif isinstance(name, str):
        if '/' not in name:
            name = 'models/' + name
        else:
            name = name
    else:
        raise TypeError('Invalid input type. Expected one of the following types: `str`, `Model`, or `TunedModel`.')
    if not name.startswith('models/') and name.startswith('tunedModels/'):
        raise ValueError(f'''Invalid model name: \'{name}\'. Model names should start with \'models/\' or \'tunedModels/\'.''')
    return name

ModelsIterable = Iterable[Model]
TunedModelsIterable = Iterable[TunedModel]
TokenCount = <NODE:12>()()
