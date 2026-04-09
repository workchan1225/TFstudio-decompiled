# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

import json
import logging
from typing import Any, AsyncIterator, Awaitable, Iterator, Optional, Union
from urllib.parse import urlencode
from  import _api_module
from  import _base_transformers as base_t
from  import _common
from  import _extra_utils
from  import _mcp_utils
from  import _transformers as t
from  import errors
from  import types
from _api_client import BaseApiClient
from _common import get_value_by_path as getv
from _common import set_value_by_path as setv
from pagers import AsyncPager, Pager
logger = logging.getLogger('google_genai.models')

def _PersonGeneration_to_mldev_enum_validate(enum_value = None):
    if enum_value in set([
        'ALLOW_ALL']):
        raise ValueError(f'''{enum_value} enum value is not supported in Gemini API.''')


def _SafetyFilterLevel_to_mldev_enum_validate(enum_value = None):
    if enum_value in set([
        'BLOCK_NONE']):
        raise ValueError(f'''{enum_value} enum value is not supported in Gemini API.''')


def _VideoGenerationReferenceType_to_mldev_enum_validate(enum_value = None):
    if enum_value in set([
        'STYLE']):
        raise ValueError(f'''{enum_value} enum value is not supported in Gemini API.''')


def _Blob_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Candidate_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CitationMetadata_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ComputeTokensParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ComputeTokensResponse_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ContentEmbeddingStatistics_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ContentEmbedding_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Content_to_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _ControlReferenceConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CountTokensConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CountTokensConfig_to_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _CountTokensParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _CountTokensParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CountTokensResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _CountTokensResponse_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteModelParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteModelParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteModelResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _DeleteModelResponse_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EditImageConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EditImageParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _EditImageResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _EmbedContentConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EmbedContentConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EmbedContentParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EmbedContentParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EmbedContentResponse_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _EmbedContentResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _Endpoint_from_vertex(from_object = None, parent_object = None):
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


def _FunctionDeclaration_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateContentConfig_to_mldev(api_client = None, from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateContentConfig_to_vertex(api_client = None, from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateContentParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateContentParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateContentResponse_from_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateContentResponse_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateImagesConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateImagesConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateImagesParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateImagesParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateImagesResponse_from_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateImagesResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateVideosConfig_to_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateVideosConfig_to_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateVideosOperation_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateVideosOperation_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateVideosParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateVideosParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateVideosResponse_from_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateVideosResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _GenerateVideosSource_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerateVideosSource_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GeneratedImageMask_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GeneratedImage_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GeneratedImage_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GeneratedVideo_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GeneratedVideo_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GenerationConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetModelParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _GetModelParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
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


def _ImageConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Image_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Image_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Image_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Image_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListModelsConfig_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListModelsConfig_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListModelsParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListModelsParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ListModelsResponse_from_mldev(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _ListModelsResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _MaskReferenceConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Model_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Model_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _Part_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ProductImage_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _RecontextImageConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _RecontextImageParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _RecontextImageResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _RecontextImageSource_to_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _ReferenceImageAPI_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _SafetyAttributes_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _SafetyAttributes_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _SafetySetting_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ScribbleImage_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _SegmentImageConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _SegmentImageParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _SegmentImageResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _SegmentImageSource_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _SpeechConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _ToolConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Tool_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Tool_to_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _TunedModelInfo_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpdateModelConfig_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpdateModelConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpdateModelParameters_to_mldev(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpdateModelParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpscaleImageAPIConfig_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpscaleImageAPIParameters_to_vertex(api_client = None, from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _UpscaleImageResponse_from_vertex(from_object = None, parent_object = None):
    pass
# WARNING: Decompyle incomplete


def _VideoGenerationMask_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _VideoGenerationReferenceImage_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _VideoGenerationReferenceImage_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Video_from_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Video_from_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Video_to_mldev(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


def _Video_to_vertex(from_object = None, parent_object = None):
    to_object = { }
# WARNING: Decompyle incomplete


class Models(_api_module.BaseModule):
    
    def _generate_content(self = None, *, model, contents, config):
        parameter_model = types._GenerateContentParameters(model = model, contents = contents, config = config)
        if self._api_client.vertexai:
            request_dict = _GenerateContentParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:generateContent'.format_map(request_url_dict)
            else:
                path = '{model}:generateContent'
        else:
            request_dict = _GenerateContentParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:generateContent'.format_map(request_url_dict)
            else:
                path = '{model}:generateContent'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _generate_content_stream(self = None, *, model, contents, config):
        pass
    # WARNING: Decompyle incomplete

    
    def embed_content(self = None, *, model, contents, config):
        """Calculates embeddings for the given contents. Only text is supported.

    Args:
      model (str): The model to use.
      contents (list[Content]): The contents to embed.
      config (EmbedContentConfig): Optional configuration for embeddings.

    Usage:

    .. code-block:: python

      embeddings = client.models.embed_content(
          model= 'text-embedding-004',
          contents=[
              'What is your name?',
              'What is your favorite color?',
          ],
          config={
              'output_dimensionality': 64
          },
      )
    """
        parameter_model = types._EmbedContentParameters(model = model, contents = contents, config = config)
        if self._api_client.vertexai:
            request_dict = _EmbedContentParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:predict'.format_map(request_url_dict)
            else:
                path = '{model}:predict'
        else:
            request_dict = _EmbedContentParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:batchEmbedContents'.format_map(request_url_dict)
            else:
                path = '{model}:batchEmbedContents'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _generate_images(self = None, *, model, prompt, config):
        '''Private method for generating images.'''
        parameter_model = types._GenerateImagesParameters(model = model, prompt = prompt, config = config)
        if self._api_client.vertexai:
            request_dict = _GenerateImagesParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:predict'.format_map(request_url_dict)
            else:
                path = '{model}:predict'
        else:
            request_dict = _GenerateImagesParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:predict'.format_map(request_url_dict)
            else:
                path = '{model}:predict'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _edit_image(self = None, *, model, prompt, reference_images, config):
        '''Private method for editing an image.'''
        parameter_model = types._EditImageParameters(model = model, prompt = prompt, reference_images = reference_images, config = config)
        if not self._api_client.vertexai:
            raise ValueError('This method is only supported in the Vertex AI client.')
        request_dict = _EditImageParameters_to_vertex(self._api_client, parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{model}:predict'.format_map(request_url_dict)
        else:
            path = '{model}:predict'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _upscale_image(self = None, *, model, image, upscale_factor, config):
        '''Private method for upscaling an image.'''
        parameter_model = types._UpscaleImageAPIParameters(model = model, image = image, upscale_factor = upscale_factor, config = config)
        if not self._api_client.vertexai:
            raise ValueError('This method is only supported in the Vertex AI client.')
        request_dict = _UpscaleImageAPIParameters_to_vertex(self._api_client, parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{model}:predict'.format_map(request_url_dict)
        else:
            path = '{model}:predict'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def recontext_image(self = None, *, model, source, config):
        '''Recontextualizes an image.

    There are two types of recontextualization currently supported:
    1) Imagen Product Recontext - Generate images of products in new scenes
       and contexts.
    2) Virtual Try-On: Generate images of persons modeling fashion products.

    Args:
      model (str): The model to use.
      source (RecontextImageSource): An object containing the source inputs
        (prompt, person_image, product_images) for image recontext. prompt is
        optional for product recontext and disallowed for virtual try-on.
        person_image is required for virtual try-on, disallowed for product
        recontext. product_images is required for both product recontext and
        virtual try-on. Only one product image is supported for virtual try-on,
        and up to 3 product images (different angles of the same product) are
        supported for product recontext.
      config (RecontextImageConfig): Configuration for recontextualization.

    Usage:

      ```
      product_recontext_response = client.models.recontext_image(
          model="imagen-product-recontext-preview-06-30",
          source=types.RecontextImageSource(
              prompt="In a modern kitchen setting.",
              product_images=[types.ProductImage.from_file(IMAGE_FILE_PATH)],
          ),
          config=types.RecontextImageConfig(
              number_of_images=1,
          ),
      )
      image = product_recontext_response.generated_images[0].image

      virtual_try_on_response = client.models.recontext_image(
          model="virtual-try-on-preview-08-04",
          source=types.RecontextImageSource(
              person_image=types.Image.from_file(IMAGE1_FILE_PATH),
              product_images=[types.ProductImage.from_file(IMAGE2_FILE_PATH)],
          ),
          config=types.RecontextImageConfig(
              number_of_images=1,
          ),
      )
      image = virtual_try_on_response.generated_images[0].image
      ```
    '''
        parameter_model = types._RecontextImageParameters(model = model, source = source, config = config)
        if not self._api_client.vertexai:
            raise ValueError('This method is only supported in the Vertex AI client.')
        request_dict = _RecontextImageParameters_to_vertex(self._api_client, parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{model}:predict'.format_map(request_url_dict)
        else:
            path = '{model}:predict'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def segment_image(self = None, *, model, source, config):
        '''Segments an image, creating a mask of a specified area.

    Args:
      model (str): The model to use.
      source (SegmentImageSource): An object containing the source inputs
        (prompt, image, scribble_image) for image segmentation. The prompt is
        required for prompt mode and semantic mode, disallowed for other modes.
        scribble_image is required for the interactive mode, disallowed for
        other modes.
      config (SegmentImageConfig): Configuration for segmentation.

    Usage:

      ```
      response = client.models.segment_image(
          model="image-segmentation-001",
          source=types.SegmentImageSource(
              image=types.Image.from_file(IMAGE_FILE_PATH),
          ),
      )

      mask_image = response.generated_masks[0].mask
      ```
    '''
        parameter_model = types._SegmentImageParameters(model = model, source = source, config = config)
        if not self._api_client.vertexai:
            raise ValueError('This method is only supported in the Vertex AI client.')
        request_dict = _SegmentImageParameters_to_vertex(self._api_client, parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{model}:predict'.format_map(request_url_dict)
        else:
            path = '{model}:predict'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def get(self = None, *, model, config):
        parameter_model = types._GetModelParameters(model = model, config = config)
        if self._api_client.vertexai:
            request_dict = _GetModelParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        else:
            request_dict = _GetModelParameters_to_mldev(self._api_client, parameter_model)
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
        parameter_model = types._ListModelsParameters(config = config)
        if self._api_client.vertexai:
            request_dict = _ListModelsParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{models_url}'.format_map(request_url_dict)
            else:
                path = '{models_url}'
        else:
            request_dict = _ListModelsParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{models_url}'.format_map(request_url_dict)
            else:
                path = '{models_url}'
        query_params = request_dict.get('_query')
        if query_params and query_params.get('filter'):
            query_param_filter = query_params.pop('filter')
            path = f'''{path}?filter={query_param_filter}'''
            if query_params:
                path += f'''&{urlencode(query_params)}'''
            elif query_params:
                path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def update(self = None, *, model, config):
        parameter_model = types._UpdateModelParameters(model = model, config = config)
        if self._api_client.vertexai:
            request_dict = _UpdateModelParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}'.format_map(request_url_dict)
            else:
                path = '{model}'
        else:
            request_dict = _UpdateModelParameters_to_mldev(self._api_client, parameter_model)
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

    
    def delete(self = None, *, model, config):
        parameter_model = types._DeleteModelParameters(model = model, config = config)
        if self._api_client.vertexai:
            request_dict = _DeleteModelParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{name}'.format_map(request_url_dict)
            else:
                path = '{name}'
        else:
            request_dict = _DeleteModelParameters_to_mldev(self._api_client, parameter_model)
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

    
    def count_tokens(self = None, *, model, contents, config):
        """Counts the number of tokens in the given content.

    Multimodal input is supported for Gemini models.

    Args:
      model (str): The model to use for counting tokens.
      contents (list[types.Content]): The content to count tokens for.
      config (CountTokensConfig): The configuration for counting tokens.

    Usage:

    .. code-block:: python

      response = client.models.count_tokens(
          model='gemini-2.0-flash',
          contents='What is your name?',
      )
      print(response)
      # total_tokens=5 cached_content_token_count=None
    """
        parameter_model = types._CountTokensParameters(model = model, contents = contents, config = config)
        if self._api_client.vertexai:
            request_dict = _CountTokensParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:countTokens'.format_map(request_url_dict)
            else:
                path = '{model}:countTokens'
        else:
            request_dict = _CountTokensParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:countTokens'.format_map(request_url_dict)
            else:
                path = '{model}:countTokens'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def compute_tokens(self = None, *, model, contents, config):
        """Given a list of contents, returns a corresponding TokensInfo containing the

    list of tokens and list of token ids.

    This method is not supported by the Gemini Developer API.

    Args:
      model (str): The model to use.
      contents (list[shared.Content]): The content to compute tokens for.

    Usage:

    .. code-block:: python

      response = client.models.compute_tokens(
          model='gemini-2.0-flash',
          contents='What is your name?',
      )
      print(response)
      # tokens_info=[TokensInfo(role='user', token_ids=['1841', ...],
      # tokens=[b'What', b' is', b' your', b' name', b'?'])]
    """
        parameter_model = types._ComputeTokensParameters(model = model, contents = contents, config = config)
        if not self._api_client.vertexai:
            raise ValueError('This method is only supported in the Vertex AI client.')
        request_dict = _ComputeTokensParameters_to_vertex(self._api_client, parameter_model)
        request_url_dict = request_dict.get('_url')
        if request_url_dict:
            path = '{model}:computeTokens'.format_map(request_url_dict)
        else:
            path = '{model}:computeTokens'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def _generate_videos(self = None, *, model, prompt, image, video, source, config):
        '''Private method for generating videos.'''
        parameter_model = types._GenerateVideosParameters(model = model, prompt = prompt, image = image, video = video, source = source, config = config)
        if self._api_client.vertexai:
            request_dict = _GenerateVideosParameters_to_vertex(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:predictLongRunning'.format_map(request_url_dict)
            else:
                path = '{model}:predictLongRunning'
        else:
            request_dict = _GenerateVideosParameters_to_mldev(self._api_client, parameter_model)
            request_url_dict = request_dict.get('_url')
            if request_url_dict:
                path = '{model}:predictLongRunning'.format_map(request_url_dict)
            else:
                path = '{model}:predictLongRunning'
        query_params = request_dict.get('_query')
        if query_params:
            path = f'''{path}?{urlencode(query_params)}'''
        request_dict.pop('config', None)
        http_options = None
    # WARNING: Decompyle incomplete

    
    def generate_content(self = None, *, model, contents, config):
        """Makes an API request to generate content using a model.

    For the `model` parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
      'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
      'publishers/google/models/gemini-2.0-flash' or
    - `/` separated publisher and model name, for example:
      'google/gemini-2.0-flash'

    For the `model` parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
      'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
      for example:
      'tunedModels/1234567890123456789'

    Some models support multimodal input and output.

    Built-in MCP support is an experimental feature.

    Usage:

    .. code-block:: python

      from google.genai import types
      from google import genai

      client = genai.Client(
          vertexai=True, project='my-project-id', location='us-central1'
      )

      response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents='''What is a good name for a flower shop that specializes in
          selling bouquets of dried flowers?'''
      )
      print(response.text)
      # **Elegant & Classic:**
      # * The Dried Bloom
      # * Everlasting Florals
      # * Timeless Petals

      response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[
          types.Part.from_text(text='What is shown in this image?'),
          types.Part.from_uri(file_uri='gs://generativeai-downloads/images/scones.jpg',
          mime_type='image/jpeg')
        ]
      )
      print(response.text)
      # The image shows a flat lay arrangement of freshly baked blueberry
      # scones.
    """
        incompatible_tools_indexes = _extra_utils.find_afc_incompatible_tool_indexes(config)
        parsed_config = _extra_utils.parse_config_for_mcp_usage(config)
        if parsed_config and parsed_config.tools and _mcp_utils.has_mcp_session_usage(parsed_config.tools):
            raise errors.UnsupportedFunctionError('MCP sessions are not supported in synchronous methods.')
        if _extra_utils.should_disable_afc(parsed_config):
            return self._generate_content(model = model, contents = contents, config = parsed_config)
        if None:
            original_tools_length = 0
            if isinstance(config, types.GenerateContentConfig):
                if config.tools:
                    original_tools_length = len(config.tools)
                elif isinstance(config, dict):
                    tools = config.get('tools', [])
                    if tools:
                        original_tools_length = len(tools)
            if len(incompatible_tools_indexes) != original_tools_length:
                indices_str = ', '.join(map(str, incompatible_tools_indexes))
                logger.warning('Tools at indices [%s] are not compatible with automatic function calling (AFC). AFC is disabled. If AFC is intended, please include python callables in the tool list, and do not include function declaration in the tool list.', indices_str)
            return self._generate_content(model = model, contents = contents, config = parsed_config)
        remaining_remote_calls_afc = None.get_max_remote_calls_afc(parsed_config)
        logger.info(f'''AFC is enabled with max remote calls: {remaining_remote_calls_afc}.''')
        automatic_function_calling_history = []
        response = types.GenerateContentResponse()
        i = 0
    # WARNING: Decompyle incomplete

    
    def generate_content_stream(self = None, *, model, contents, config):
        """Makes an API request to generate content using a model and yields the model's response in chunks.

    For the `model` parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
      'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
      'publishers/google/models/gemini-2.0-flash' or
    - `/` separated publisher and model name, for example:
      'google/gemini-2.0-flash'

    For the `model` parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
      'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
      for example:
      'tunedModels/1234567890123456789'

    Some models support multimodal input and output.

    Built-in MCP support is an experimental feature.

    Usage:

    .. code-block:: python

      from google.genai import types
      from google import genai

      client = genai.Client(
          vertexai=True, project='my-project-id', location='us-central1'
      )

      for chunk in client.models.generate_content_stream(
        model='gemini-2.0-flash',
        contents='''What is a good name for a flower shop that specializes in
          selling bouquets of dried flowers?'''
      ):
        print(chunk.text)
      # **Elegant & Classic:**
      # * The Dried Bloom
      # * Everlasting Florals
      # * Timeless Petals

      for chunk in client.models.generate_content_stream(
        model='gemini-2.0-flash',
        contents=[
          types.Part.from_text('What is shown in this image?'),
          types.Part.from_uri('gs://generativeai-downloads/images/scones.jpg',
          'image/jpeg')
        ]
      ):
        print(chunk.text)
      # The image shows a flat lay arrangement of freshly baked blueberry
      # scones.
    """
        pass
    # WARNING: Decompyle incomplete

    
    def generate_images(self = None, *, model, prompt, config):
        """Generates images based on a text description and configuration.

    Args:
      model (str): The model to use.
      prompt (str): A text description of the images to generate.
      config (GenerateImagesConfig): Configuration for generation.

    Usage:

    .. code-block:: python

      response = client.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt='Man with a dog',
        config=types.GenerateImagesConfig(
            number_of_images= 1,
            include_rai_reason= True,
        )
      )
      response.generated_images[0].image.show()
      # Shows a man with a dog.
    """
        api_response = self._generate_images(model = model, prompt = prompt, config = config)
        positive_prompt_safety_attributes = None
        generated_images = []
        if not api_response or api_response.generated_images:
            return api_response
        for generated_image in None.generated_images:
            if generated_image.safety_attributes and generated_image.safety_attributes.content_type == 'Positive Prompt':
                positive_prompt_safety_attributes = generated_image.safety_attributes
                continue
            generated_images.append(generated_image)
            response = types.GenerateImagesResponse(generated_images = generated_images, positive_prompt_safety_attributes = positive_prompt_safety_attributes)
            return response

    
    def edit_image(self = None, *, model, prompt, reference_images, config):
        '''Edits an image based on a text description and configuration.

    Args:
      model (str): The model to use.
      prompt (str): A text description of the edit to apply to the image.
        reference_images (list[Union[RawReferenceImage, MaskReferenceImage,
        ControlReferenceImage, StyleReferenceImage, SubjectReferenceImage]): The
        reference images for editing.
      config (EditImageConfig): Configuration for editing.

    Usage:

    .. code-block:: python

      from google.genai.types import RawReferenceImage, MaskReferenceImage

      raw_ref_image = RawReferenceImage(
        reference_id=1,
        reference_image=types.Image.from_file(IMAGE_FILE_PATH),
      )

      mask_ref_image = MaskReferenceImage(
        reference_id=2,
        config=types.MaskReferenceConfig(
            mask_mode=\'MASK_MODE_FOREGROUND\',
            mask_dilation=0.06,
        ),
      )
      response = client.models.edit_image(
        model=\'imagen-3.0-capability-001\',
        prompt=\'man with dog\',
        reference_images=[raw_ref_image, mask_ref_image],
        config=types.EditImageConfig(
            edit_mode= "EDIT_MODE_INPAINT_INSERTION",
            number_of_images= 1,
            include_rai_reason= True,
        )
      )
      response.generated_images[0].image.show()
      # Shows a man with a dog instead of a cat.
    '''
        return self._edit_image(model = model, prompt = prompt, reference_images = reference_images, config = config)

    
    def upscale_image(self = None, *, model, image, upscale_factor, config):
        '''Makes an API request to upscale a provided image.

    Args:
      model (str): The model to use.
      image (Image): The input image for upscaling.
      upscale_factor (str): The factor to upscale the image (x2 or x4).
      config (UpscaleImageConfig): Configuration for upscaling.

    Usage:

    .. code-block:: python

      from google.genai.types import Image

      IMAGE_FILE_PATH="my-image.png"
      response=client.models.upscale_image(
          model=\'imagen-3.0-generate-001\',
          image=types.Image.from_file(IMAGE_FILE_PATH),
          upscale_factor=\'x2\',
      )
      response.generated_images[0].image.show()
      # Opens my-image.png which is upscaled by a factor of 2.
    '''
        types.UpscaleImageParameters(model = model, image = image, upscale_factor = upscale_factor, config = config)
        if not config:
            config = { }
            if isinstance(config, types.UpscaleImageConfig):
                config_dct = config.model_dump()
            else:
                config_dct = dict(config)
        api_config = types._UpscaleImageAPIConfigDict(http_options = config_dct.get('http_options', None), output_gcs_uri = config_dct.get('output_gcs_uri', None), safety_filter_level = config_dct.get('safety_filter_level', None), person_generation = config_dct.get('person_generation', None), include_rai_reason = config_dct.get('include_rai_reason', None), output_mime_type = config_dct.get('output_mime_type', None), output_compression_quality = config_dct.get('output_compression_quality', None), enhance_input_image = config_dct.get('enhance_input_image', None), image_preservation_factor = config_dct.get('image_preservation_factor', None), labels = config_dct.get('labels', None))
        api_config['mode'] = 'upscale'
        api_config['number_of_images'] = 1
        return self._upscale_image(model = model, image = image, upscale_factor = upscale_factor, config = api_config)

    
    def generate_videos(self = None, *, model, prompt, image, video, source, config):
        '''Generates videos based on an input (text, image, or video) and configuration.

    The following use cases are supported:
    1. Text to video generation.
    2a. Image to video generation (additional text prompt is optional).
    2b. Image to video generation with frame interpolation (specify last_frame
    in config).
    3. Video extension (additional text prompt is optional)

    Args:
      model: The model to use.
      prompt: The text prompt for generating the videos. Optional for image to
        video and video extension use cases. This argument is deprecated, please
        use source instead.
      image: The input image for generating the videos. Optional if prompt is
        provided. This argument is deprecated, please use source instead.
      video: The input video for video extension use cases. Optional if prompt
        or image is provided. This argument is deprecated, please use source
        instead.
      source: The input source for generating the videos (prompt, image, and/or
        video)
      config: Configuration for generation.

    Usage:

      ```
      operation = client.models.generate_videos(
          model="veo-2.0-generate-001",
          source=types.GenerateVideosSource(
              prompt="A neon hologram of a cat driving at top speed",
          ),
      )
      while not operation.done:
          time.sleep(10)
          operation = client.operations.get(operation)

      operation.result.generated_videos[0].video.uri
      ```
    '''
        if (prompt and image or video) and source:
            raise ValueError('Source and prompt/image/video are mutually exclusive. Please only use source.')
        video_dct = { }
        if self._api_client.vertexai and video:
            if isinstance(video, types.Video):
                video_dct = video.model_dump()
            else:
                video_dct = dict(video)
            if video_dct.get('uri') and video_dct.get('video_bytes'):
                video = types.Video(uri = video_dct.get('uri'), mime_type = video_dct.get('mime_type'))
            elif self._api_client.vertexai and source:
                if isinstance(source, types.GenerateVideosSource):
                    source_dct = source.model_dump()
                    video_dct = source_dct.get('video', { })
                else:
                    source_dct = dict(source)
                    if isinstance(source_dct.get('video'), types.Video):
                        video_obj = source_dct.get('video', types.Video())
                        video_dct = video_obj.model_dump()
                if video_dct and video_dct.get('uri') and video_dct.get('video_bytes'):
                    source = types.GenerateVideosSource(prompt = source_dct.get('prompt'), image = source_dct.get('image'), video = types.Video(uri = video_dct.get('uri'), mime_type = video_dct.get('mime_type')))
        return self._generate_videos(model = model, prompt = prompt, image = image, video = video, source = source, config = config)

    
    def list(self = None, *, config):
        """Makes an API request to list the available models.

    If `query_base` is set to True in the config or not set (default), the
    API will return all available base models. If set to False, it will return
    all tuned models.

    Args:
      config (ListModelsConfigOrDict): Configuration for retrieving models.

    Usage:

    .. code-block:: python

      response=client.models.list(config={'page_size': 5})
      print(response.page)
      # [Model(name='projects/./locations/./models/123', display_name='my_model'

      response=client.models.list(config={'page_size': 5, 'query_base': True})
      print(response.page)
      # [Model(name='publishers/google/models/gemini-2.0-flash-exp' ...
    """
        pass
    # WARNING: Decompyle incomplete



class AsyncModels(_api_module.BaseModule):
    
    async def _generate_content(self = None, *, model, contents, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def _generate_content_stream(self = None, *, model, contents, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def embed_content(self = None, *, model, contents, config):
        """Calculates embeddings for the given contents. Only text is supported.

    Args:
      model (str): The model to use.
      contents (list[Content]): The contents to embed.
      config (EmbedContentConfig): Optional configuration for embeddings.

    Usage:

    .. code-block:: python

      embeddings = await client.aio.models.embed_content(
          model= 'text-embedding-004',
          contents=[
              'What is your name?',
              'What is your favorite color?',
          ],
          config={
              'output_dimensionality': 64
          },
      )
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def _generate_images(self = None, *, model, prompt, config):
        '''Private method for generating images asynchronously.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def _edit_image(self = None, *, model, prompt, reference_images, config):
        '''Private method for editing an image asynchronously.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def _upscale_image(self = None, *, model, image, upscale_factor, config):
        '''Private method for upscaling an image asynchronously.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def recontext_image(self = None, *, model, source, config):
        '''Recontextualizes an image.

    There are two types of recontextualization currently supported:
    1) Imagen Product Recontext - Generate images of products in new scenes
       and contexts.
    2) Virtual Try-On: Generate images of persons modeling fashion products.

    Args:
      model (str): The model to use.
      source (RecontextImageSource): An object containing the source inputs
        (prompt, person_image, product_images) for image recontext. prompt is
        optional for product recontext and disallowed for virtual try-on.
        person_image is required for virtual try-on, disallowed for product
        recontext. product_images is required for both product recontext and
        virtual try-on. Only one product image is supported for virtual try-on,
        and up to 3 product images (different angles of the same product) are
        supported for product recontext.
      config (RecontextImageConfig): Configuration for recontextualization.

    Usage:

      ```
      product_recontext_response = client.models.recontext_image(
          model="imagen-product-recontext-preview-06-30",
          source=types.RecontextImageSource(
              prompt="In a modern kitchen setting.",
              product_images=[types.ProductImage.from_file(IMAGE_FILE_PATH)],
          ),
          config=types.RecontextImageConfig(
              number_of_images=1,
          ),
      )
      image = product_recontext_response.generated_images[0].image

      virtual_try_on_response = client.models.recontext_image(
          model="virtual-try-on-preview-08-04",
          source=types.RecontextImageSource(
              person_image=types.Image.from_file(IMAGE1_FILE_PATH),
              product_images=[types.ProductImage.from_file(IMAGE2_FILE_PATH)],
          ),
          config=types.RecontextImageConfig(
              number_of_images=1,
          ),
      )
      image = virtual_try_on_response.generated_images[0].image
      ```
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def segment_image(self = None, *, model, source, config):
        '''Segments an image, creating a mask of a specified area.

    Args:
      model (str): The model to use.
      source (SegmentImageSource): An object containing the source inputs
        (prompt, image, scribble_image) for image segmentation. The prompt is
        required for prompt mode and semantic mode, disallowed for other modes.
        scribble_image is required for the interactive mode, disallowed for
        other modes.
      config (SegmentImageConfig): Configuration for segmentation.

    Usage:

      ```
      response = client.models.segment_image(
          model="image-segmentation-001",
          source=types.SegmentImageSource(
              image=types.Image.from_file(IMAGE_FILE_PATH),
          ),
          config=types.SegmentImageConfig(
              mode=types.SegmentMode.foreground,
          ),
      )

      mask_image = response.generated_masks[0].mask
      ```
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get(self = None, *, model, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def _list(self = None, *, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def update(self = None, *, model, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, *, model, config):
        pass
    # WARNING: Decompyle incomplete

    
    async def count_tokens(self = None, *, model, contents, config):
        """Counts the number of tokens in the given content.

    Multimodal input is supported for Gemini models.

    Args:
      model (str): The model to use for counting tokens.
      contents (list[types.Content]): The content to count tokens for.
      config (CountTokensConfig): The configuration for counting tokens.

    Usage:

    .. code-block:: python

      response = await client.aio.models.count_tokens(
          model='gemini-2.0-flash',
          contents='What is your name?',
      )
      print(response)
      # total_tokens=5 cached_content_token_count=None
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def compute_tokens(self = None, *, model, contents, config):
        """Given a list of contents, returns a corresponding TokensInfo containing the

    list of tokens and list of token ids.


    Args:
      model (str): The model to use.
      contents (list[shared.Content]): The content to compute tokens for.

    Usage:

    .. code-block:: python

      response = await client.aio.models.compute_tokens(
          model='gemini-2.0-flash',
          contents='What is your name?',
      )
      print(response)
      # tokens_info=[TokensInfo(role='user', token_ids=['1841', ...],
      # tokens=[b'What', b' is', b' your', b' name', b'?'])]
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def _generate_videos(self = None, *, model, prompt, image, video, source, config):
        '''Private method for generating videos asynchronously.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def generate_content(self = None, *, model, contents, config):
        """Makes an API request to generate content using a model.

    Some models support multimodal input and output.

    Built-in MCP support is an experimental feature.

    Usage:

    .. code-block:: python

      from google.genai import types
      from google import genai

      client = genai.Client(
          vertexai=True, project='my-project-id', location='us-central1'
      )

      response = await client.aio.models.generate_content(
          model='gemini-2.0-flash',
          contents='User input: I like bagels. Answer:',
          config=types.GenerateContentConfig(
              system_instruction=
                [
                  'You are a helpful language translator.',
                  'Your mission is to translate text in English to French.'
                ]
          ),
      )
      print(response.text)
      # J'aime les bagels.
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def generate_content_stream(self = None, *, model, contents, config):
        """Makes an API request to generate content using a model and yields the model's response in chunks.

    For the `model` parameter, supported formats for Vertex AI API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The full resource name starts with 'projects/', for example:
      'projects/my-project-id/locations/us-central1/publishers/google/models/gemini-2.0-flash'
    - The partial resource name with 'publishers/', for example:
      'publishers/google/models/gemini-2.0-flash' or
    - `/` separated publisher and model name, for example:
      'google/gemini-2.0-flash'

    For the `model` parameter, supported formats for Gemini API include:
    - The Gemini model ID, for example: 'gemini-2.0-flash'
    - The model name starts with 'models/', for example:
      'models/gemini-2.0-flash'
    - For tuned models, the model name starts with 'tunedModels/',
      for example:
      'tunedModels/1234567890123456789'

    Some models support multimodal input and output.

    Built-in MCP support is an experimental feature.

    Usage:

    .. code-block:: python

      from google.genai import types
      from google import genai

      client = genai.Client(
          vertexai=True, project='my-project-id', location='us-central1'
      )

      async for chunk in await client.aio.models.generate_content_stream(
        model='gemini-2.0-flash',
        contents='''What is a good name for a flower shop that specializes in
          selling bouquets of dried flowers?'''
      ):
        print(chunk.text)
      # **Elegant & Classic:**
      # * The Dried Bloom
      # * Everlasting Florals
      # * Timeless Petals

      async for chunk in await client.aio.models.generate_content_stream(
        model='gemini-2.0-flash',
        contents=[
          types.Part.from_text('What is shown in this image?'),
          types.Part.from_uri('gs://generativeai-downloads/images/scones.jpg',
          'image/jpeg')
        ]
      ):
        print(chunk.text)
      # The image shows a flat lay arrangement of freshly baked blueberry
      # scones.
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def edit_image(self = None, *, model, prompt, reference_images, config):
        '''Edits an image based on a text description and configuration.

    Args:
      model (str): The model to use.
      prompt (str): A text description of the edit to apply to the image.
        reference_images (list[Union[RawReferenceImage, MaskReferenceImage,
        ControlReferenceImage, StyleReferenceImage, SubjectReferenceImage]): The
        reference images for editing.
      config (EditImageConfig): Configuration for editing.

    Usage:

    .. code-block:: python

      from google.genai.types import RawReferenceImage, MaskReferenceImage

      raw_ref_image = RawReferenceImage(
        reference_id=1,
        reference_image=types.Image.from_file(IMAGE_FILE_PATH),
      )

      mask_ref_image = MaskReferenceImage(
        reference_id=2,
        config=types.MaskReferenceConfig(
            mask_mode=\'MASK_MODE_FOREGROUND\',
            mask_dilation=0.06,
        ),
      )
      response = await client.aio.models.edit_image(
        model=\'imagen-3.0-capability-001\',
        prompt=\'man with dog\',
        reference_images=[raw_ref_image, mask_ref_image],
        config=types.EditImageConfig(
            edit_mode= "EDIT_MODE_INPAINT_INSERTION",
            number_of_images= 1,
            include_rai_reason= True,
        )
      )
      response.generated_images[0].image.show()
      # Shows a man with a dog instead of a cat.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def list(self = None, *, config):
        """Makes an API request to list the available models.

    If `query_base` is set to True in the config or not set (default), the
    API will return all available base models. If set to False, it will return
    all tuned models.

    Args:
      config (ListModelsConfigOrDict): Configuration for retrieving models.

    Usage:

    .. code-block:: python

      response = await client.aio.models.list(config={'page_size': 5})
      print(response.page)
      # [Model(name='projects/./locations/./models/123', display_name='my_model'

      response = await client.aio.models.list(
          config={'page_size': 5, 'query_base': True}
        )
      print(response.page)
      # [Model(name='publishers/google/models/gemini-2.0-flash-exp' ...
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def generate_images(self = None, *, model, prompt, config):
        """Generates images based on a text description and configuration.

    Args:
      model (str): The model to use.
      prompt (str): A text description of the images to generate.
      config (GenerateImagesConfig): Configuration for generation.

    Usage:

    .. code-block:: python

      response = await client.aio.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt='Man with a dog',
        config=types.GenerateImagesConfig(
            number_of_images= 1,
            include_rai_reason= True,
        )
      )
      response.generated_images[0].image.show()
      # Shows a man with a dog.
    """
        pass
    # WARNING: Decompyle incomplete

    
    async def upscale_image(self = None, *, model, image, upscale_factor, config):
        '''Makes an API request to upscale a provided image.

    Args:
      model (str): The model to use.
      image (Image): The input image for upscaling.
      upscale_factor (str): The factor to upscale the image (x2 or x4).
      config (UpscaleImageConfig): Configuration for upscaling.

    Usage:

    .. code-block:: python

      from google.genai.types import Image

      IMAGE_FILE_PATH="my-image.png"
      response = await client.aio.models.upscale_image(
          model=\'imagen-3.0-generate-001\',
          image=types.Image.from_file(IMAGE_FILE_PATH),
          upscale_factor=\'x2\',
      )
      response.generated_images[0].image.show()
      # Opens my-image.png which is upscaled by a factor of 2.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    async def generate_videos(self = None, *, model, prompt, image, video, source, config):
        '''Generates videos based on an input (text, image, or video) and configuration.

    The following use cases are supported:
    1. Text to video generation.
    2a. Image to video generation (additional text prompt is optional).
    2b. Image to video generation with frame interpolation (specify last_frame
    in config).
    3. Video extension (additional text prompt is optional)

    Args:
      model: The model to use.
      prompt: The text prompt for generating the videos. Optional for image to
        video and video extension use cases. This argument is deprecated, please
        use source instead.
      image: The input image for generating the videos. Optional if prompt is
        provided. This argument is deprecated, please use source instead.
      video: The input video for video extension use cases. Optional if prompt
        or image is provided. This argument is deprecated, please use source
        instead.
      source: The input source for generating the videos (prompt, image, and/or
        video)
      config: Configuration for generation.

    Usage:

      ```
      operation = client.models.generate_videos(
          model="veo-2.0-generate-001",
          source=types.GenerateVideosSource(
              prompt="A neon hologram of a cat driving at top speed",
          ),
      )
      while not operation.done:
          time.sleep(10)
          operation = client.operations.get(operation)

      operation.result.generated_videos[0].video.uri
      ```
    '''
        pass
    # WARNING: Decompyle incomplete
