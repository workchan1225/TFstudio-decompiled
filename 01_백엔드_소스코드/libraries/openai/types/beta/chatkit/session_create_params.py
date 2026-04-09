# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Required, TypedDict
from chat_session_workflow_param import ChatSessionWorkflowParam
from chat_session_rate_limits_param import ChatSessionRateLimitsParam
from chat_session_expires_after_param import ChatSessionExpiresAfterParam
from chat_session_chatkit_configuration_param import ChatSessionChatKitConfigurationParam
__all__ = [
    'SessionCreateParams']

def SessionCreateParams():
    '''SessionCreateParams'''
    rate_limits: 'ChatSessionRateLimitsParam' = 'SessionCreateParams'

SessionCreateParams = <NODE:27>(SessionCreateParams, 'SessionCreateParams', TypedDict, total = False)
