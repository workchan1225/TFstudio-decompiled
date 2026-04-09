# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _stream_decoder.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Iterator, AsyncIterator
from _utils import lru_cache
from _streaming import ServerSentEvent
if TYPE_CHECKING:
    from botocore.model import Shape
    from botocore.eventstream import EventStreamMessage
get_response_stream_shape = (lambda : ServiceModel = ServiceModelimport botocore.modelLoader = Loaderimport botocore.loadersloader = Loader()bedrock_service_dict = loader.load_service_model('bedrock-runtime', 'service-2')bedrock_service_model = ServiceModel(bedrock_service_dict)bedrock_service_model.shape_for('ResponseStream'))()

class AWSEventStreamDecoder:
    
    def __init__(self = None):
        EventStreamJSONParser = EventStreamJSONParser
        import botocore.parsers
        self.parser = EventStreamJSONParser()

    
    def iter_bytes(self = None, iterator = None):
        '''Given an iterator that yields lines, iterate over it & yield every event encountered'''
        pass
    # WARNING: Decompyle incomplete

    
    def aiter_bytes(self = None, iterator = None):
        '''Given an async iterator that yields lines, iterate over it & yield every event encountered'''
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_message_from_event(self = None, event = None):
        response_dict = event.to_response_dict()
        parsed_response = self.parser.parse(response_dict, get_response_stream_shape())
        if response_dict['status_code'] != 200:
            raise ValueError(f'''Bad response code, expected 200: {response_dict}''')
        chunk = parsed_response.get('chunk')
        if not chunk:
            return None
        return None.get('bytes').decode()
