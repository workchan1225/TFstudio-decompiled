# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_types.pyc (Python 3.11)

from __future__ import annotations
import sys
import abc
import dataclasses
from typing import Any, Dict, List
from typing_extensions import TypedDict
from google.generativeai import string_utils
from google.generativeai.types import citation_types

class EmbeddingDict(TypedDict):
    embedding: 'list[float]' = 'EmbeddingDict'


class BatchEmbeddingDict(TypedDict):
    embedding: 'list[list[float]]' = 'BatchEmbeddingDict'
