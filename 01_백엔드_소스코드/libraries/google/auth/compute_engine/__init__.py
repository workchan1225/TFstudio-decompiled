# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Google Compute Engine authentication.'''
from google.auth.compute_engine._metadata import detect_gce_residency_linux
from google.auth.compute_engine.credentials import Credentials
from google.auth.compute_engine.credentials import IDTokenCredentials
__all__ = [
    'Credentials',
    'IDTokenCredentials',
    'detect_gce_residency_linux']
