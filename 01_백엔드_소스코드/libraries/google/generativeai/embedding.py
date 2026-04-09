# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: embedding.pyc (Python 3.11)

from __future__ import annotations
import itertools
from typing import Any, Iterable, overload, TypeVar, Union, Mapping

generativelanguage
from google.generativeai import protos
import google.ai.generativelanguage, ai
from google.generativeai.client import get_default_generative_client
from google.generativeai.client import get_default_generative_async_client
from google.generativeai.types import helper_types
from google.generativeai.types import model_types
from google.generativeai.types import text_types
from google.generativeai.types import content_types
DEFAULT_EMB_MODEL = 'models/embedding-001'
EMBEDDING_MAX_BATCH_SIZE = 100
EmbeddingTaskType = protos.TaskType
EmbeddingTaskTypeOptions = Union[(int, str, EmbeddingTaskType)]
# WARNING: Decompyle incomplete
