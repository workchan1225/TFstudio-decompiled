# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_types.pyc (Python 3.11)

from __future__ import annotations
import datetime
from typing import Any, Union
from typing_extensions import TypedDict
from google.rpc.status_pb2 import Status
from google.generativeai.client import get_default_file_client
from google.generativeai import protos
import pprint

class File:
    
    def __init__(self = None, proto = None):
        if isinstance(proto, File):
            proto = proto.to_proto()
        self._proto = protos.File(proto)

    
    def to_proto(self = None):
        return self._proto

    
    def to_dict(self = None):
        return type(self._proto).to_dict(self._proto, use_integers_for_enums = False)

    
    def __str__(self):
        
        def sort_key(pair):
            (name, value) = pair
            if name == 'name':
                return ''
            if None in name:
                return 'zz_' + name

        dict_format = dict(sorted(self.to_dict().items(), key = sort_key))
        dict_format = pprint.pformat(dict_format, sort_dicts = False)
        dict_format = '{\n ' + dict_format[1:]
        dict_format = '\n   '.join(dict_format.splitlines())
        return dict_format.join([
            'genai.File(',
            ')'])

    __repr__ = __str__
    name = (lambda self = None: self._proto.name)()
    display_name = (lambda self = None: self._proto.display_name)()
    mime_type = (lambda self = None: self._proto.mime_type)()
    size_bytes = (lambda self = None: self._proto.size_bytes)()
    create_time = (lambda self = None: self._proto.create_time)()
    update_time = (lambda self = None: self._proto.update_time)()
    expiration_time = (lambda self = None: self._proto.expiration_time)()
    sha256_hash = (lambda self = None: self._proto.sha256_hash)()
    uri = (lambda self = None: self._proto.uri)()
    state = (lambda self = None: self._proto.state)()
    video_metadata = (lambda self = None: self._proto.video_metadata)()
    error = (lambda self = None: self._proto.error)()
    
    def delete(self):
        client = get_default_file_client()
        client.delete_file(name = self.name)



class FileDataDict(TypedDict):
    file_uri: 'str' = 'FileDataDict'

FileDataType = Union[(FileDataDict, protos.FileData, protos.File, File)]

def to_file_data(file_data = None):
    if isinstance(file_data, dict):
        if 'file_uri' in file_data:
            file_data = protos.FileData(file_data)
        else:
            file_data = protos.File(file_data)
    if isinstance(file_data, File):
        file_data = file_data.to_proto()
    if isinstance(file_data, protos.File):
        file_data = protos.FileData(mime_type = file_data.mime_type, file_uri = file_data.uri)
    if isinstance(file_data, protos.FileData):
        return file_data
    raise None(f'''Invalid input type. Failed to convert input to `FileData`.\nReceived an object of type: {type(file_data)}.\nObject Value: {file_data}''')
