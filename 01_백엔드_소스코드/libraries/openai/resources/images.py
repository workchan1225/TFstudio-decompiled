# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: images.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Mapping, Optional, cast
from typing_extensions import Literal, overload
import httpx
from  import _legacy_response
from types import image_edit_params, image_generate_params, image_create_variation_params
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from _utils import extract_files, required_args, maybe_transform, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _streaming import Stream, AsyncStream
from _base_client import make_request_options
from types.image_model import ImageModel
from types.images_response import ImagesResponse
from types.image_gen_stream_event import ImageGenStreamEvent
from types.image_edit_stream_event import ImageEditStreamEvent
__all__ = [
    'Images',
    'AsyncImages']

class Images(SyncAPIResource):
    with_raw_response = (lambda self = None: ImagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ImagesWithStreamingResponse(self))()
    
    def create_variation(self = None, *, image, model, n, response_format, size, user, extra_headers, extra_query, extra_body, timeout):
        '''Creates a variation of a given image.

        This endpoint only supports `dall-e-2`.

        Args:
          image: The image to use as the basis for the variation(s). Must be a valid PNG file,
              less than 4MB, and square.

          model: The model to use for image generation. Only `dall-e-2` is supported at this
              time.

          n: The number of images to generate. Must be between 1 and 10.

          response_format: The format in which the generated images are returned. Must be one of `url` or
              `b64_json`. URLs are only valid for 60 minutes after the image has been
              generated.

          size: The size of the generated images. Must be one of `256x256`, `512x512`, or
              `1024x1024`.

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        body = deepcopy_minimal({
            'image': image,
            'model': model,
            'n': n,
            'response_format': response_format,
            'size': size,
            'user': user })
        files = extract_files(cast(Mapping[(str, object)], body), paths = [
            [
                'image']])
    # WARNING: Decompyle incomplete

    edit = (lambda self = None, *, image: pass)()
    edit = (lambda self = None, *, image: pass)()
    edit = (lambda self = None, *, image: pass)()
    edit = (lambda self = None, *, image: body = deepcopy_minimal({
'image': image,
'prompt': prompt,
'background': background,
'input_fidelity': input_fidelity,
'mask': mask,
'model': model,
'n': n,
'output_compression': output_compression,
'output_format': output_format,
'partial_images': partial_images,
'quality': quality,
'response_format': response_format,
'size': size,
'stream': stream,
'user': user })files = extract_files(cast(Mapping[(str, object)], body), paths = [
[
'image'],
[
'image',
'<array>'],
[
'mask']])# WARNING: Decompyle incomplete
)()
    generate = (lambda self = None, *, prompt: pass)()
    generate = (lambda self = None, *, prompt: pass)()
    generate = (lambda self = None, *, prompt: pass)()
    generate = (lambda self = None, *, prompt:
