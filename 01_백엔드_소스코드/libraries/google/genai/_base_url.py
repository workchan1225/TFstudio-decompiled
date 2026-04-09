# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base_url.pyc (Python 3.11)

import os
from typing import Optional
from types import HttpOptions
_default_base_gemini_url = None
_default_base_vertex_url = None

def set_default_base_urls(gemini_url = None, vertex_url = None):
    '''Overrides the base URLs for the Gemini API and Vertex AI API.'''
    global _default_base_gemini_url, _default_base_vertex_url
    _default_base_gemini_url = gemini_url
    _default_base_vertex_url = vertex_url


def get_base_url(vertexai = None, http_options = None):
