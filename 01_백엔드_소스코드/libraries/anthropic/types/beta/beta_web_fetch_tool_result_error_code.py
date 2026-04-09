# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_web_fetch_tool_result_error_code.pyc (Python 3.11)

from typing_extensions import Literal, TypeAlias
__all__ = [
    'BetaWebFetchToolResultErrorCode']
BetaWebFetchToolResultErrorCode: TypeAlias = Literal[('invalid_tool_input', 'url_too_long', 'url_not_allowed', 'url_not_accessible', 'unsupported_content_type', 'too_many_requests', 'max_uses_exceeded', 'unavailable')]
