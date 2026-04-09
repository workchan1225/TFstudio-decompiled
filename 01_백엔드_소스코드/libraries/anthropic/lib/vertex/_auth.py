# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _auth.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, cast
from _extras import google_auth
if TYPE_CHECKING:
    from google.auth.credentials import Credentials

def load_auth(*, project_id):
    
    try:
        Request = Request
        import google.auth.transport.requests
    except ModuleNotFoundError:
        err = None
        raise RuntimeError('Could not import google.auth, you need to install the SDK with `pip install anthropic[vertex]`'), err
        err = None
        del err

    (credentials, loaded_project_id) = google_auth.default(scopes = [
        'https://www.googleapis.com/auth/cloud-platform'])
    credentials = cast(Any, credentials)
    credentials.refresh(Request())
    if not project_id:
        project_id = loaded_project_id
    if not project_id:
        raise ValueError('Could not resolve project_id')
    if not isinstance(project_id, str):
        raise TypeError(f'''Expected project_id to be a str but got {type(project_id)}''')
    return (credentials, project_id)


def refresh_auth(credentials = None):
    Request = Request
    import google.auth.transport.requests
    credentials.refresh(Request())
