# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _response.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import TypeVar
from _types import NotGiven
from _models import TypeAdapter, construct_type_unchecked
from _utils._utils import is_given
from types.beta.beta_message import BetaMessage
from types.beta.parsed_beta_message import ParsedBetaMessage, ParsedBetaTextBlock, ParsedBetaContentBlock
ResponseFormatT = TypeVar('ResponseFormatT', default = None)

def parse_text(text = None, output_format = None):
    if is_given(output_format):
        adapted_type = TypeAdapter(output_format)
        return adapted_type.validate_json(text)


def parse_response(*, output_format, response):
    content_list = []
# WARNING: Decompyle incomplete
