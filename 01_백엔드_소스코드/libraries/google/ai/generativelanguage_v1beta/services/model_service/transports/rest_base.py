# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rest_base.pyc (Python 3.11)

import json
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
from google.api_core import gapic_v1, path_template
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf import json_format
from google.ai.generativelanguage_v1beta.types import tuned_model as gag_tuned_model
from google.ai.generativelanguage_v1beta.types import model, model_service
from google.ai.generativelanguage_v1beta.types import tuned_model
from base import DEFAULT_CLIENT_INFO, ModelServiceTransport

class _BaseModelServiceRestTransport(ModelServiceTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('_BaseModelServiceRestTransport',)
