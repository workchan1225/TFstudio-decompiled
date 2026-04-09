# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batches.pyc (Python 3.11)

import json
import logging
from typing import Any, Optional, Union
from urllib.parse import urlencode
from  import _api_module
from  import _common
from  import _extra_utils
from  import _transformers as t
from  import types
from _api_client import BaseApiClient
from _common import get_value_by_path as getv
from _common import move_value_by_path as movev
from _common import set_value_by_path as setv
from pagers import AsyncPager, Pager
logger = logging.getLogger('google_genai.batches')

def _BatchJobDestination_from_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _BatchJobDestination_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _BatchJobDestination_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _BatchJobSource_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _BatchJobSource_to_mldev(api_client = None, from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _BatchJobSource_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _BatchJob_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _BatchJob_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Blob_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CancelBatchJobParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CancelBatchJobParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Candidate_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CitationMetadata_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Content_to_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _CreateBatchJobConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateBatchJobConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateBatchJobParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateBatchJobParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateEmbeddingsBatchJobConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CreateEmbeddingsBatchJobParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteBatchJobParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteBatchJobParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteResourceJob_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteResourceJob_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EmbedContentBatch_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EmbedContentConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EmbeddingsBatchJobSource_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _FileData_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _FunctionCall_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _FunctionCallingConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateContentConfig_to_mldev(api_client = None, from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateContentResponse_from_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GetBatchJobParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetBatchJobParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GoogleMaps_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GoogleSearch_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ImageConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _InlinedRequest_to_mldev(api_client = None, from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _InlinedResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListBatchJobsConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListBatchJobsConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListBatchJobsParameters_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListBatchJobsParameters_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListBatchJobsResponse_from_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _ListBatchJobsResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _Part_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _SafetySetting_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ToolConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Tool_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


class Batches(_api_module.BaseModule):
    
    def _create(self = None, *, model, src, config):
        parameter_model = types._CreateBatchJobParameters(model = model, src = src, config = config)
        if self._api_client.vertexai:
            request_dict = _CreateBatchJobParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batchPredictionJobs'.format_map(request_url_dict)
            else:
                path = 'batchPredictionJobs'
        else:
            request_dict = _CreateBatchJobParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:batchGenerateContent'.format_map(request_url_dict)
            else:
                path = '{model}:batchGenerateContent'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _create_embeddings(self = None, *, model, src, config):
        parameter_model = types._CreateEmbeddingsBatchJobParameters(model = model, src = src, config = config)
        if self._api_client.vertexai:
            raise ValueError('This method is only supported in the Gemini Developer client.')
        request_dict = _CreateEmbeddingsBatchJobParameters_to_mldev(self._api_client, parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{model}:asyncBatchEmbedContent'.format_map(request_url_dict)
        else:
            path = '{model}:asyncBatchEmbedContent'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def get(self = None, *, name, config):
        '''Gets a batch job.

    Args:
      name (str): A fully-qualified BatchJob resource name or ID.
        Example: "projects/.../locations/.../batchPredictionJobs/456" or "456"
          when project and location are initialized in the Vertex AI client. Or
          "batches/abc" using the Gemini Developer AI client.

    Returns:
      A BatchJob object that contains details about the batch job.

    Usage:

    .. code-block:: python

      batch_job = client.batches.get(name=\'123456789\')
      print(f"Batch job: {batch_job.name}, state {batch_job.state}")
    '''
        parameter_model = types._GetBatchJobParameters(name = name, config = config)
        if self._api_client.vertexai:
            request_dict = _GetBatchJobParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batchPredictionJobs/{name}'.format_map(request_url_dict)
            else:
                path = 'batchPredictionJobs/{name}'
        else:
            request_dict = _GetBatchJobParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batches/{name}'.format_map(request_url_dict)
            else:
                path = 'batches/{name}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def cancel(self = None, *, name, config):
        '''Cancels a batch job.

    Only available for batch jobs that are running or pending.

    Args:
      name (str): A fully-qualified BatchJob resource name or ID.
        Example: "projects/.../locations/.../batchPredictionJobs/456" or "456"
          when project and location are initialized in the Vertex AI client. Or
          "batches/abc" using the Gemini Developer AI client.

    Usage:

    .. code-block:: python

      client.batches.cancel(name=\'123456789\')
    '''
        parameter_model = types._CancelBatchJobParameters(name = name, config = config)
        if self._api_client.vertexai:
            request_dict = _CancelBatchJobParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batchPredictionJobs/{name}:cancel'.format_map(request_url_dict)
            else:
                path = 'batchPredictionJobs/{name}:cancel'
        else:
            request_dict = _CancelBatchJobParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batches/{name}:cancel'.format_map(request_url_dict)
            else:
                path = 'batches/{name}:cancel'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _list(self = None, *, config):
        parameter_model = types._ListBatchJobsParameters(config = config)
        if self._api_client.vertexai:
            request_dict = _ListBatchJobsParameters_to_vertex(parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batchPredictionJobs'.format_map(request_url_dict)
            else:
                path = 'batchPredictionJobs'
        else:
            request_dict = _ListBatchJobsParameters_to_mldev(parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batches'.format_map(request_url_dict)
            else:
                path = 'batches'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def delete(self = None, *, name, config):
        '''Deletes a batch job.

    Args:
      name (str): A fully-qualified BatchJob resource name or ID.
        Example: "projects/.../locations/.../batchPredictionJobs/456" or "456"
          when project and location are initialized in the client.

    Returns:
      A DeleteResourceJob object that shows the status of the deletion.

    Usage:

    .. code-block:: python

      client.batches.delete(name=\'123456789\')
    '''
        parameter_model = types._DeleteBatchJobParameters(name = name, config = config)
        if self._api_client.vertexai:
            request_dict = _DeleteBatchJobParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batchPredictionJobs/{name}'.format_map(request_url_dict)
            else:
                path = 'batchPredictionJobs/{name}'
        else:
            request_dict = _DeleteBatchJobParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = 'batches/{name}'.format_map(request_url_dict)
            else:
                path = 'batches/{name}'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def create(self = None, *, model, src, config):
        '''Creates a batch job.

    Args:
      model (str): The model to use for the batch job.
      src: The source of the batch job. Currently Vertex AI supports GCS URI(-s)
        or BigQuery URI. Example: "gs://path/to/input/data" or
        "bq://projectId.bqDatasetId.bqTableId". Gemini Developer API supports
        List of inlined_request, or file name. Example: "files/file_name".
      config (CreateBatchJobConfig): Optional configuration for the batch job.

    Returns:
      A BatchJob object that contains details about the batch job.

    Usage:

    .. code-block:: python

      batch_job = client.batches.create(
          model="gemini-2.0-flash-001",
          src="gs://path/to/input/data",
      )
      print(batch_job.state)
    '''
        src = t.t_batch_job_source(self._api_client, src)
        parameter_model = types._CreateBatchJobParameters(model = model, src = src, config = config)
        if self._api_client.vertexai:
            config = _extra_utils.format_destination(src, parameter_model.config)
            return self._create(model = model, src = src, config = config)
        return None._create(model = model, src = src, config = config)

    
    def create_embeddings(self = None, *, model, src, config):
        '''**Experimental** Creates an embedding batch job.

    Args:
      model (str): The model to use for the batch job.
      src: Gemini Developer API supports List of inlined_request, or file name.
        Example: "files/file_name".
      config (CreateBatchJobConfig): Optional configuration for the batch job.

    Returns:
      A BatchJob object that contains details about the batch job.

    Usage:

    .. code-block:: python

      batch_job = client.batches.create_embeddings(
          model="text-embedding-004",
          src="files/my_embedding_input",
      )
      print(batch_job.state)
    '''
        import warnings
        warnings.warn('batches.create_embeddings() is experimental and may change without notice.', category = _common.ExperimentalWarning, stacklevel = 2)
        src = t.t_embedding_batch_job_source(self._api_client, src)
        parameter_model = types._CreateEmbeddingsBatchJobParameters(model = model, src = src, config = config)
        if self._api_client.vertexai:
            raise ValueError('Vertex AI does not support batches.create_embeddings.')
        return self._create_embeddings(model = model, src = src, config = config)

    
    def list(self = None, *, config):
        """Lists batch jobs.

    Args:
      config (ListBatchJobsConfig): Optional configuration for the list request.

    Returns:
      A Pager object that contains one page of batch jobs. When iterating over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python
      config = {'page_size': 10}
      for batch_job in client.batches.list(config):
        print(batch_job.name)
    """
        list_request = self._list
        return Pager('batch_jobs', list_request, self._list(config = config), config)



class AsyncBatches(_api_module.BaseModule):
    
    async def _create(self = None, *, model, src, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def _create_embeddings(self = None, *, model, src, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def get(self = None, *, name, config):
        '''Gets a batch job.

    Args:
      name (str): A fully-qualified BatchJob resource name or ID.
        Example: "projects/.../locations/.../batchPredictionJobs/456" or "456"
          when project and location are initialized in the Vertex AI client. Or
          "batches/abc" using the Gemini Developer AI client.

    Returns:
      A BatchJob object that contains details about the batch job.

    Usage:

    .. code-block:: python

      batch_job = await client.aio.batches.get(name=\'123456789\')
      print(f"Batch job: {batch_job.name}, state {batch_job.state}")
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def cancel(self = None, *, name, config):
        '''Cancels a batch job.

    Only available for batch jobs that are running or pending.

    Args:
      name (str): A fully-qualified BatchJob resource name or ID.
        Example: "projects/.../locations/.../batchPredictionJobs/456" or "456"
          when project and location are initialized in the Vertex AI client. Or
          "batches/abc" using the Gemini Developer AI client.

    Usage:

    .. code-block:: python

      await client.aio.batches.cancel(name=\'123456789\')
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _list(self = None, *, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, *, name, config):
        '''Deletes a batch job.

    Args:
      name (str): A fully-qualified BatchJob resource name or ID.
        Example: "projects/.../locations/.../batchPredictionJobs/456" or "456"
          when project and location are initialized in the client.

    Returns:
      A DeleteResourceJob object that shows the status of the deletion.

    Usage:

    .. code-block:: python

      await client.aio.batches.delete(name=\'123456789\')
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def create(self = None, *, model, src, config):
        '''Creates a batch job asynchronously.

    Args:
      model (str): The model to use for the batch job.
      src: The source of the batch job. Currently Vertex AI supports GCS URI(-s)
        or BigQuery URI. Example: "gs://path/to/input/data" or
        "bq://projectId.bqDatasetId.bqTableId". Gemini Develop API supports List
        of inlined_request, or file name. Example: "files/file_name".
      config (CreateBatchJobConfig): Optional configuration for the batch job.

    Returns:
      A BatchJob object that contains details about the batch job.

    Usage:

    .. code-block:: python

      batch_job = await client.aio.batches.create(
          model="gemini-2.0-flash-001",
          src="gs://path/to/input/data",
      )
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def create_embeddings(self = None, *, model, src, config):
        '''**Experimental** Creates an asynchronously embedding batch job.

    Args:
      model (str): The model to use for the batch job.
      src: Gemini Developer API supports inlined_requests, or file name.
        Example: "files/file_name".
      config (CreateBatchJobConfig): Optional configuration for the batch job.

    Returns:
      A BatchJob object that contains details about the batch job.

    Usage:

    .. code-block:: python

      batch_job = await client.aio.batches.create_embeddings(
          model="text-embedding-004",
          src="files/my_embedding_input",
      )
      print(batch_job.state)
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def list(self = None, *, config):
        '''Lists batch jobs asynchronously.

    Args:
      config (ListBatchJobsConfig): Optional configuration for the list request.

    Returns:
      A Pager object that contains one page of batch jobs. When iterating over
      the pager, it automatically fetches the next page if there are more.

    Usage:

    .. code-block:: python
      async for batch_job in await client.aio.batches.list():
        print(batch_job.name)
    '''
        pass
    # WARNING: Decompyle incomplete
