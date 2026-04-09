# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_session_chatkit_configuration_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import TypedDict
__all__ = [
    'ChatSessionChatKitConfigurationParam',
    'AutomaticThreadTitling',
    'FileUpload',
    'History']

def AutomaticThreadTitling():
    '''AutomaticThreadTitling'''
    enabled: 'bool' = 'Configuration for automatic thread titling.\n\n    When omitted, automatic thread titling is enabled by default.\n    '

AutomaticThreadTitling = <NODE:27>(AutomaticThreadTitling, 'AutomaticThreadTitling', TypedDict, total = False)

def FileUpload():
    '''FileUpload'''
    max_files: 'int' = 'Configuration for upload enablement and limits.\n\n    When omitted, uploads are disabled by default (max_files 10, max_file_size 512 MB).\n    '

FileUpload = <NODE:27>(FileUpload, 'FileUpload', TypedDict, total = False)

def History():
    '''History'''
    recent_threads: 'int' = 'Configuration for chat history retention.\n\n    When omitted, history is enabled by default with no limit on recent_threads (null).\n    '

History = <NODE:27>(History, 'History', TypedDict, total = False)

def ChatSessionChatKitConfigurationParam():
    '''ChatSessionChatKitConfigurationParam'''
    history: 'History' = 'Optional per-session configuration settings for ChatKit behavior.'

ChatSessionChatKitConfigurationParam = <NODE:27>(ChatSessionChatKitConfigurationParam, 'ChatSessionChatKitConfigurationParam', TypedDict, total = False)
