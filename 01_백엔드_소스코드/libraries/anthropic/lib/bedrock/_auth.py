# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _auth.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
import httpx
from _utils import lru_cache
if TYPE_CHECKING:
    import boto3
_get_session = (lambda *: import boto3boto3.Session(profile_name = profile, region_name = region, aws_access_key_id = aws_access_key, aws_secret_access_key = aws_secret_key, aws_session_token = aws_session_token))()

def get_auth_headers(*, method, url, headers, aws_access_key, aws_secret_key, aws_session_token, region, profile, data):
    SigV4Auth = SigV4Auth
    import botocore.auth
    AWSRequest = AWSRequest
    import botocore.awsrequest
    session = _get_session(profile = profile, region = region, aws_access_key = aws_access_key, aws_secret_key = aws_secret_key, aws_session_token = aws_session_token)
    headers = headers.copy()
    del headers['connection']
    request = AWSRequest(method = method.upper(), url = url, headers = headers, data = data)
    credentials = session.get_credentials()
    if not credentials:
        raise RuntimeError('could not resolve credentials from session')
    signer = SigV4Auth(credentials, 'bedrock', session.region_name)
    signer.add_auth(request)
    prepped = request.prepare()
    return dict(prepped.headers).items()()
