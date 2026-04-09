# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: files.pyc (Python 3.11)

from __future__ import annotations
import os
import pathlib
import mimetypes
from typing import Iterable
import logging
from google.generativeai import protos
from itertools import islice
from io import IOBase
from google.generativeai.types import file_types
from google.generativeai.client import get_default_file_client
__all__ = [
    'upload_file',
    'get_file',
    'list_files',
    'delete_file']
mimetypes.add_type('image/webp', '.webp')

def upload_file(path = None, *, mime_type, name, display_name, resumable):
    """Calls the API to upload a file using a supported file service.

    Args:
        path: The path to the file or a file-like object (e.g., BytesIO) to be uploaded.
        mime_type: The MIME type of the file. If not provided, it will be
            inferred from the file extension.
        name: The name of the file in the destination (e.g., 'files/sample-image').
            If not provided, a system generated ID will be created.
        display_name: Optional display name of the file.
        resumable: Whether to use the resumable upload protocol. By default, this is enabled.
            See details at
            https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.http.MediaFileUpload-class.html#resumable

    Returns:
        file_types.File: The response of the uploaded file.
    """
    client = get_default_file_client()
# WARNING: Decompyle incomplete


def list_files(page_size = None):
    '''Calls the API to list files using a supported file service.'''
    pass
# WARNING: Decompyle incomplete


def get_file(name = None):
    '''Calls the API to retrieve a specified file using a supported file service.'''
    if '/' not in name:
        name = f'''files/{name}'''
    client = get_default_file_client()
    return file_types.File(client.get_file(name = name))


def delete_file(name = None):
    '''Calls the API to permanently delete a specified file using a supported file service.'''
    if isinstance(name, (file_types.File, protos.File)):
        name = name.name
    elif '/' not in name:
        name = f'''files/{name}'''
    request = protos.DeleteFileRequest(name = name)
    client = get_default_file_client()
    client.delete_file(request = request)
