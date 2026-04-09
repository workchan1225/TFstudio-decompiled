# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base_transformers.pyc (Python 3.11)

'''Base transformers for Google GenAI SDK.'''
import base64

def t_bytes(data = None):
    if not isinstance(data, bytes):
        return data
    return None.b64encode(data).decode('ascii')
