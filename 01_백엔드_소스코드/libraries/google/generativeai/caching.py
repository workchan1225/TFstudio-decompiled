# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: caching.pyc (Python 3.11)

from __future__ import annotations
import datetime
import textwrap
from typing import Iterable, Optional
from google.generativeai import protos
from google.generativeai.types import caching_types
from google.generativeai.types import content_types
from google.generativeai.client import get_default_cache_client
from google.protobuf import field_mask_pb2
_USER_ROLE = 'user'
_MODEL_ROLE = 'model'

class CachedContent:
    '''Cached content resource.'''
    
    def __init__(self, name):
        '''Fetches a `CachedContent` resource.

        Identical to `CachedContent.get`.

        Args:
            name: The resource name referring to the cached content.
        '''
        client = get_default_cache_client()
        if 'cachedContents/' not in name:
            name = 'cachedContents/' + name
        request = protos.GetCachedContentRequest(name = name)
        response = client.get_cached_content(request)
        self._proto = response

    name = (lambda self = None: self._proto.name)()
    model = (lambda self = None: self._proto.model)()
    display_name = (lambda self = None: self._proto.display_name)()
    usage_metadata = (lambda self = None: self._proto.usage_metadata)()
    create_time = (lambda self = None: self._proto.create_time)()
    update_time = (lambda self = None: self._proto.update_time)()
    expire_time = (lambda self = None: self._proto.expire_time)()
    
    def __str__(self):
        return textwrap.dedent(f'''            CachedContent(\n                name=\'{self.name}\',\n                model=\'{self.model}\',\n                display_name=\'{self.display_name}\',\n                usage_metadata={'{'}\n                    \'total_token_count\': {self.usage_metadata.total_token_count},\n                {'}'},\n                create_time={self.create_time},\n                update_time={self.update_time},\n                expire_time={self.expire_time}\n            )''')

    __repr__ = __str__
    _from_obj = (lambda cls = None, obj = None: self = cls.__new__(cls)self._proto = protos.CachedContent()self._update(obj)self)()
    
    def _update(self, updates):
        """Updates this instance inplace, does not call the API's `update` method"""
        if isinstance(updates, CachedContent):
            updates = updates._proto
        if not isinstance(updates, dict):
            updates = type(updates).to_dict(updates, including_default_value_fields = False)
        for key, value in updates.items():
            setattr(self._proto, key, value)
            return None

    _prepare_create_request = (lambda model = None, *, display_name: if ttl and expire_time:
raise ValueError('Exclusive arguments: Please provide either `ttl` or `expire_time`, not both.')if '/' not in model:
model = 'models/' + modelif display_name and len(display_name) > 128:
raise ValueError('`display_name` must be no more than 128 unicode characters.')if system_instruction:
system_instruction = content_types.to_content(system_instruction)tools_lib = content_types.to_function_library(tools)if tools_lib:
tools_lib = tools_lib.to_proto()if tool_config:
tool_config = content_types.to_tool_config(tool_config)if contents:
contents = content_types.to_contents(contents)if not contents[-1].role:
contents[-1].role = _USER_ROLEttl = caching_types.to_optional_ttl(ttl)expire_time = caching_types.to_optional_expire_time(expire_time)cached_content = protos.CachedContent(model = model, display_name = display_name, system_instruction = system_instruction, contents = contents, tools = tools_lib, tool_config = tool_config, ttl = ttl, expire_time = expire_time)protos.CreateCachedContentRequest(cached_content = cached_content))()
    create = (lambda cls = None, model = None, *, display_name, system_instruction: client = get_default_cache_client()request = cls._prepare_create_request(model = model, display_name = display_name, system_instruction = system_instruction, contents = contents, tools = tools, tool_config = tool_config, ttl = ttl, expire_time = expire_time)response = client.create_cached_content(request)result = CachedContent._from_obj(response)result)()
    get = (lambda cls = None, name = None: client = get_default_cache_client()if 'cachedContents/' not in name:
name = 'cachedContents/' + namerequest = protos.GetCachedContentRequest(name = name)response = client.get_cached_content(request)result = CachedContent._from_obj(response)result)()
    list = (lambda cls = None, page_size = None: pass# WARNING: Decompyle incomplete
)()
    
    def delete(self = None):
        '''Deletes `CachedContent` resource.'''
        client = get_default_cache_client()
        request = protos.DeleteCachedContentRequest(name = self.name)
        client.delete_cached_content(request)

    
    def update(self = None, *, ttl, expire_time):
        '''Updates requested `CachedContent` resource.

        Args:
            ttl: TTL for cached resource (in seconds). Defaults to 1 hour.
                 `ttl` and `expire_time` are exclusive arguments.
            expire_time: Expiration time for cached resource.
                         `ttl` and `expire_time` are exclusive arguments.
        '''
        client = get_default_cache_client()
        if ttl and expire_time:
            raise ValueError('Exclusive arguments: Please provide either `ttl` or `expire_time`, not both.')
        ttl = caching_types.to_optional_ttl(ttl)
        expire_time = caching_types.to_optional_expire_time(expire_time)
        updates = protos.CachedContent(name = self.name, ttl = ttl, expire_time = expire_time)
        field_mask = field_mask_pb2.FieldMask()
        if ttl:
            field_mask.paths.append('ttl')
        elif expire_time:
            field_mask.paths.append('expire_time')
        else:
            raise ValueError('Bad update name: Only `ttl`  or `expire_time` can be updated for `CachedContent`.')
        request = protos.UpdateCachedContentRequest(cached_content = updates, update_mask = field_mask)
        updated_cc = client.update_cached_content(request)
        self._update(updated_cc)
