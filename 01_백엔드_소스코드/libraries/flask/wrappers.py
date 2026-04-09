# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wrappers.pyc (Python 3.11)

from __future__ import annotations
import typing as t
from werkzeug.exceptions import BadRequest
from werkzeug.wrappers import Request as RequestBase
from werkzeug.wrappers import Response as ResponseBase
from  import json
from globals import current_app
from helpers import _split_blueprint_path
if t.TYPE_CHECKING:
    from werkzeug.routing import Rule

class Request(RequestBase):
    pass
# WARNING: Decompyle incomplete


class Response(ResponseBase):
    pass
# WARNING: Decompyle incomplete
