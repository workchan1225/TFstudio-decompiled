# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tunings.pyc (Python 3.11)

import json
import logging
from typing import Any, Optional, Union
from urllib.parse import urlencode
from  import _api_module
from  import _common
from  import _transformers as t
from  import types
from _common import get_value_by_path as getv
from _common import set_value_by_path as setv
from pagers import AsyncPager, Pager
logger = logging.getLogger('google_genai.tunings')

def _AutoraterConfig_from_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _AutoraterConfig_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CancelTuningJobParameters_to_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CancelTuningJobParameters_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CancelTuningJobResponse_from_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CancelTuningJobResponse_from_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateTuningJobConfig_to_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateTuningJobConfig_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
    discriminator = getv(root_object, [
        'config',
        'method'])
# WARNING: Decompyle incomplete


def _CreateTuningJobParametersPrivate_to_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateTuningJobParametersPrivate_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EvaluationConfig_from_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EvaluationConfig_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerationConfig_from_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerationConfig_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetTuningJobParameters_to_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetTuningJobParameters_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListTuningJobsConfig_to_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListTuningJobsConfig_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListTuningJobsParameters_to_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListTuningJobsParameters_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListTuningJobsResponse_from_mldev(from_object = None, parent_object = None, root_object = None):
    pass
# WARNING: Decompyle incomplete


def _ListTuningJobsResponse_from_vertex(from_object = None, parent_object = None, root_object = None):
    pass
# WARNING: Decompyle incomplete


def _SpeechConfig_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _TunedModel_from_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _TuningDataset_to_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _TuningDataset_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
    discriminator = getv(root_object, [
        'config',
        'method'])
# WARNING: Decompyle incomplete


def _TuningJob_from_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _TuningJob_from_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _TuningOperation_from_mldev(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _TuningValidationDataset_to_vertex(from_object = None, parent_object = None, root_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


class Tunings(_api_module.BaseModule):
    
    def _get(self = None, *, name, config):
        '''Gets a TuningJob.

    Args:
      name: The resource name of the tuning job.

    Returns:
      A TuningJob object.
    '''
        parameter_model = types._GetTuningJobParameters(name = name, config = config)
        if self._api_client.vertexai:
            request_dict = _GetTuningJobParameters_to_vertex(parameter_model, None, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        else:
            request_dict = _GetTuningJobParameters_to_mldev(parameter_model, None, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _list(self = None, *, config):
        parameter_model = types._ListTuningJobsParameters(config = config)
        if self._api_client.vertexai:
            request_dict = _ListTuningJobsParameters_to_vertex(parameter_model, None, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'tuningJobs'.format_map(request_url_dict)
            else:
                path = 'tuningJobs'
        else:
            request_dict = _ListTuningJobsParameters_to_mldev(parameter_model, None, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'tunedModels'.format_map(request_url_dict)
            else:
                path = 'tunedModels'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def cancel(self = None, *, name, config):
        '''Cancels a tuning job.

    Args:
      name (str): TuningJob resource name.
    '''
        parameter_model = types._CancelTuningJobParameters(name = name, config = config)
        if self._api_client.vertexai:
            request_dict = _CancelTuningJobParameters_to_vertex(parameter_model, None, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}:cancel'.format_map(request_url_dict)
            else:
                path = '{name}:cancel'
        else:
            request_dict = _CancelTuningJobParameters_to_mldev(parameter_model, None, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}:cancel'.format_map(request_url_dict)
            else:
                path = '{name}:cancel'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _tune(self = None, *, base_model, pre_tuned_model, training_dataset, config):
        '''Creates a tuning job and returns the TuningJob object.

    Args:
      base_model: The name of the model to tune.
      training_dataset: The training dataset to use.
      config: The configuration to use for the tuning job.

    Returns:
      A TuningJob object.
    '''
        parameter_model = types._CreateTuningJobParametersPrivate(base_model = base_model, pre_tuned_model = pre_tuned_model, training_dataset = training_dataset, config = config)
        if not self._api_client.vertexai:
            raise ValueError('This method is only supported in the Vertex AI client.')
        request_dict = _CreateTuningJobParametersPrivate_to_vertex(parameter_model, None, parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'tuningJobs'.format_map(request_url_dict)
        else:
            path = 'tuningJobs'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _tune_mldev(self = None, *, base_model, pre_tuned_model, training_dataset, config):
        '''Creates a tuning job and returns the TuningJob object.

    Args:
      base_model: The name of the model to tune.
      training_dataset: The training dataset to use.
      config: The configuration to use for the tuning job.

    Returns:
      A TuningJob operation.
    '''
        parameter_model = types._CreateTuningJobParametersPrivate(base_model = base_model, pre_tuned_model = pre_tuned_model, training_dataset = training_dataset, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _CreateTuningJobParametersPrivate_to_mldev(parameter_model, None, parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = 'tunedModels'.format_map(request_url_dict)
        else:
            path = 'tunedModels'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def get(self = None, *, name, config):
        job = self._get(name = name, config = config)
    # WARNING: Decompyle incomplete

    tune = (lambda self = None, *, base_model: pass# WARNING: Decompyle incomplete
)()
    
    def list(self = None, *, config):
        '''Lists `TuningJob` objects.

    Args:
      config: The configuration for the list request.

    Returns:
      A Pager object that contains one page of tuning jobs. When iterating over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python
        for tuning_job in client.tunings.list():
            print(tuning_job.name)
    '''
        list_request = self._list
        return Pager('tuning_jobs', list_request, self._list(config = config), config)



class AsyncTunings(_api_module.BaseModule):
    
    async def _get(self = None, *, name, config):
        '''Gets a TuningJob.

    Args:
      name: The resource name of the tuning job.

    Returns:
      A TuningJob object.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _list(self = None, *, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def cancel(self = None, *, name, config):
        '''Cancels a tuning job asynchronously.

    Args:
      name (str): A TuningJob resource name.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _tune(self = None, *, base_model, pre_tuned_model, training_dataset, config):
        '''Creates a tuning job and returns the TuningJob object.

    Args:
      base_model: The name of the model to tune.
      training_dataset: The training dataset to use.
      config: The configuration to use for the tuning job.

    Returns:
      A TuningJob object.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _tune_mldev(self = None, *, base_model, pre_tuned_model, training_dataset, config):
        '''Creates a tuning job and returns the TuningJob object.

    Args:
      base_model: The name of the model to tune.
      training_dataset: The training dataset to use.
      config: The configuration to use for the tuning job.

    Returns:
      A TuningJob operation.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get(self = None, *, name, config):
        pass
    # WARNING: Decompyle incomplete

    tune = (lambda self = None, *, base_model: pass# WARNING: Decompyle incomplete
)()
    
    async def list(self = None, *, config):
        '''Lists `TuningJob` objects asynchronously.

    Args:
      config: The configuration for the list request.

    Returns:
      A Pager object that contains one page of tuning jobs. When iterating over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python
        async for tuning_job in await client.aio.tunings.list():
            print(tuning_job.name)
    '''
        pass
    # WARNING: Decompyle incomplete



class _IpythonUtils:
    '''Temporary class to hold the IPython related functions.'''
    displayed_experiments: set[str] = set()
    _get_ipython_shell_name = (lambda : import sysif 'IPython' in sys.modules:
get_ipython = get_ipythonimport IPythonget_ipython().__class__.__name__)()
    is_ipython_available = (lambda : bool(_IpythonUtils._get_ipython_shell_name()))()
    _get_styles = (lambda : '\n    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">\n    <style>\n      .view-vertex-resource,\n      .view-vertex-resource:hover,\n      .view-vertex-resource:visited {\n        position: relative;\n        display: inline-flex;\n        flex-direction: row;\n        height: 32px;\n        padding: 0 12px;\n          margin: 4px 18px;\n        gap: 4px;\n        border-radius: 4px;\n\n        align-items: center;\n        justify-content: center;\n        background-color: rgb(255, 255, 255);\n        color: rgb(51, 103, 214);\n\n        font-family: Roboto,"Helvetica Neue",sans-serif;\n        font-size: 13px;\n        font-weight: 500;\n        text-transform: uppercase;\n        text-decoration: none !important;\n\n        transition: box-shadow 280ms cubic-bezier(0.4, 0, 0.2, 1) 0s;\n        box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2), 0px 2px 2px 0px rgba(0,0,0,0.14), 0px 1px 5px 0px rgba(0,0,0,0.12);\n      }\n      .view-vertex-resource:active {\n        box-shadow: 0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);\n      }\n      .view-vertex-resource:active .view-vertex-ripple::before {\n        position: absolute;\n        top: 0;\n        bottom: 0;\n        left: 0;\n        right: 0;\n        border-radius: 4px;\n        pointer-events: none;\n\n        content: \'\';\n        background-color: rgb(51, 103, 214);\n        opacity: 0.12;\n      }\n      .view-vertex-icon {\n        font-size: 18px;\n      }\n    </style>\n  ')()
    _parse_resource_name = (lambda marker = None, resource_parts = None: for i in range(len(resource_parts)):
if resource_parts[i] == marker and i + 1 < len(resource_parts):
None, resource_parts[i + 1]'')()
    _display_link = (lambda text = None, url = None, icon = staticmethod: CLOUD_UI_URL = 'https://console.cloud.google.com'if not url.startswith(CLOUD_UI_URL):
raise ValueError(f'''Only urls starting with {CLOUD_UI_URL} are allowed.''')import uuidbutton_id = f'''view-vertex-resource-{str(uuid.uuid4())}'''html = f'''\n        {_IpythonUtils._get_styles()}\n        <a class="view-vertex-resource" id="{button_id}" href="#view-{button_id}">\n          <span class="material-icons view-vertex-icon">{icon}</span>\n          <span>{text}</span>\n        </a>\n        '''html += f'''\n        <script>\n          (function () {{\n            const link = document.getElementById(\'{button_id}\');\n            link.addEventListener(\'click\', (e) => {{\n              if (window.google?.colab?.openUrl) {{\n                window.google.colab.openUrl(\'{url}\');\n              }} else {{\n                window.open(\'{url}\', \'_blank\');\n              }}\n              e.stopPropagation();\n              e.preventDefault();\n            }});\n          }})();\n        </script>\n    '''display = displayimport IPython.displayHTML = HTMLimport IPython.displaydisplay(HTML(html)))()
    display_experiment_button = (lambda experiment = None, project = None: if _IpythonUtils.is_ipython_available() or experiment in _IpythonUtils.displayed_experiments:
Noneresource_parts = None.split('/')location = resource_parts[3]experiment_name = resource_parts[-1]uri = 'https://console.cloud.google.com/vertex-ai/experiments/locations/' + f'''{location}/experiments/{experiment_name}/''' + f'''runs?project={project}'''_IpythonUtils._display_link('View Experiment', uri, 'science')_IpythonUtils.displayed_experiments.add(experiment))()
    display_model_tuning_button = (lambda tuning_job_resource = None: if not _IpythonUtils.is_ipython_available():
Noneresource_parts = None.split('/')project = resource_parts[1]location = resource_parts[3]tuning_job_id = resource_parts[-1]uri = 'https://console.cloud.google.com/vertex-ai/generative/language/' + f'''locations/{location}/tuning/tuningJob/{tuning_job_id}''' + f'''?project={project}'''_IpythonUtils._display_link('View Tuning Job', uri, 'tune'))()
