# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

from __future__ import annotations
import typing
from typing import Any, Literal

generativelanguage
from google.generativeai import protos
import google.ai.generativelanguage, ai
from google.generativeai import operations
from google.generativeai.client import get_default_model_client
from google.generativeai.types import model_types
from google.generativeai.types import helper_types
from google.api_core import operation
from google.api_core import protobuf_helpers
from google.protobuf import field_mask_pb2
from google.generativeai.utils import flatten_update_paths

def get_model(name = None, *, client, request_options):
    """Calls the API to fetch a model by name.

    ```
    import pprint
    model = genai.get_model('models/gemini-1.5-flash')
    pprint.pprint(model)
    ```

    Args:
        name: The name of the model to fetch. Should start with `models/`
        client: The client to use.
        request_options: Options for the request.

    Returns:
        A `types.Model`
    """
    name = model_types.make_model_name(name)
    if name.startswith('models/'):
        return get_base_model(name, client = client, request_options = request_options)
    if None.startswith('tunedModels/'):
        return get_tuned_model(name, client = client, request_options = request_options)
    raise None(f'''Invalid model name: Model names must start with `models/` or `tunedModels/`. Received: {name}''')


def get_base_model(name = None, *, client, request_options):
    """Calls the API to fetch a base model by name.

    ```
    import pprint
    model = genai.get_base_model('models/chat-bison-001')
    pprint.pprint(model)
    ```

    Args:
        name: The name of the model to fetch. Should start with `models/`
        client: The client to use.
        request_options: Options for the request.

    Returns:
        A `types.Model`.
    """
    pass
# WARNING: Decompyle incomplete


def get_tuned_model(name = None, *, client, request_options):
    """Calls the API to fetch a tuned model by name.

    ```
    import pprint
    model = genai.get_tuned_model('tunedModels/gemini-1.5-flash')
    pprint.pprint(model)
    ```

    Args:
        name: The name of the model to fetch. Should start with `tunedModels/`
        client: The client to use.
        request_options: Options for the request.

    Returns:
        A `types.TunedModel`.
    """
    pass
# WARNING: Decompyle incomplete


def get_base_model_name(model = None, client = None):
    '''Calls the API to fetch the base model name of a model.'''
    if isinstance(model, str):
        if model.startswith('tunedModels/'):
            model = get_model(model, client = client)
            base_model = model.base_model
        else:
            base_model = model
    elif isinstance(model, model_types.TunedModel):
        base_model = model.base_model
    elif isinstance(model, model_types.Model):
        base_model = model.name
    elif isinstance(model, protos.Model):
        base_model = model.name
    elif isinstance(model, protos.TunedModel):
        base_model = getattr(model, 'base_model', None)
        if not base_model:
            base_model = model.tuned_model_source.base_model
        else:
            raise TypeError(f'''Invalid model: The provided model \'{model}\' is not recognized or supported. Supported types are: str, model_types.TunedModel, model_types.Model, protos.Model, and protos.TunedModel.''')
        return base_model


def list_models(*, page_size, client, request_options):
    '''Calls the API to list all available models.

    ```
    import pprint
    for model in genai.list_models():
        pprint.pprint(model)
    ```

    Args:
        page_size: How many `types.Models` to fetch per page (api call).
        client: You may pass a `glm.ModelServiceClient` instead of using the default client.
        request_options: Options for the request.

    Yields:
        `types.Model` objects.

    '''
    pass
# WARNING: Decompyle incomplete


def list_tuned_models(*, page_size, client, request_options):
    '''Calls the API to list all tuned models.

    ```
    import pprint
    for model in genai.list_tuned_models():
        pprint.pprint(model)
    ```

    Args:
        page_size: How many `types.Models` to fetch per page (api call).
        client: You may pass a `glm.ModelServiceClient` instead of using the default client.
        request_options: Options for the request.

    Yields:
        `types.TunedModel` objects.
    '''
    pass
# WARNING: Decompyle incomplete


def create_tuned_model(source_model = None, training_data = None, *, id, display_name, description, temperature, top_p, top_k, epoch_count, batch_size, learning_rate, input_key, output_key, client, request_options):
    '''Calls the API to initiate a tuning process that optimizes a model for specific data, returning an operation object to track and manage the tuning progress.

    Since tuning a model can take significant time, this API doesn\'t wait for the tuning to complete.
    Instead, it returns a `google.api_core.operation.Operation` object that lets you check on the
    status of the tuning job, or wait for it to complete, and check the result.

    After the job completes you can either find the resulting `TunedModel` object in
    `Operation.result()` or `palm.list_tuned_models` or `palm.get_tuned_model(model_id)`.

    ```
    my_id = "my-tuned-model-id"
    operation = palm.create_tuned_model(
      id = my_id,
      source_model="models/text-bison-001",
      training_data=[{\'text_input\': \'example input\', \'output\': \'example output\'},...]
    )
    tuned_model=operation.result()      # Wait for tuning to finish

    palm.generate_text(f"tunedModels/{my_id}", prompt="...")
    ```

    Args:
        source_model: The name of the model to tune.
        training_data: The dataset to tune the model on. This must be either:
          * A `protos.Dataset`, or
          * An `Iterable` of:
            *`protos.TuningExample`,
            * `{\'text_input\': text_input, \'output\': output}` dicts
            * `(text_input, output)` tuples.
          * A `Mapping` of `Iterable[str]` - use `input_key` and `output_key` to choose which
            columns to use as the input/output
          * A csv file (will be read with `pd.read_csv` and handles as a `Mapping`
            above). This can be:
            * A local path as a `str` or `pathlib.Path`.
            * A url for a csv file.
            * The url of a Google Sheets file.
          * A JSON file - Its contents will be handled either as an `Iterable` or `Mapping`
            above. This can be:
            * A local path as a `str` or `pathlib.Path`.
        id: The model identifier, used to refer to the model in the API
          `tunedModels/{id}`. Must be unique.
        display_name: A human-readable name for display.
        description: A description of the tuned model.
        temperature: The default temperature for the tuned model, see `types.Model` for details.
        top_p: The default `top_p` for the model, see `types.Model` for details.
        top_k: The default `top_k` for the model, see `types.Model` for details.
        epoch_count: The number of tuning epochs to run. An epoch is a pass over the whole dataset.
        batch_size: The number of examples to use in each training batch.
        learning_rate: The step size multiplier for the gradient updates.
        client: Which client to use.
        request_options: Options for the request.

    Returns:
        A [`google.api_core.operation.Operation`](https://googleapis.dev/python/google-api-core/latest/operation.html)
    '''
    pass
# WARNING: Decompyle incomplete

update_tuned_model = (lambda tuned_model = None, updates = None, *, client, request_options: pass)()
update_tuned_model = (lambda tuned_model = None, updates = None, *, client, request_options: pass)()

def update_tuned_model(tuned_model = None, updates = None, *, client, request_options):
    '''Calls the API to push updates to a specified tuned model where only certain attributes are updatable.'''
    pass
# WARNING: Decompyle incomplete


def _apply_update(thing, path, value):
    parts = path.split('.')
    for part in parts[:-1]:
        thing = getattr(thing, part)
        setattr(thing, parts[-1], value)
        return None


def delete_tuned_model(tuned_model = None, client = None, request_options = None):
    '''Calls the API to delete a specified tuned model'''
    pass
# WARNING: Decompyle incomplete
