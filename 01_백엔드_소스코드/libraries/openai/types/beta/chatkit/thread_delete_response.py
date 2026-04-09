# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thread_delete_response.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ThreadDeleteResponse']

class ThreadDeleteResponse(BaseModel):
    object: Literal['chatkit.thread.deleted'] = 'Confirmation payload returned after deleting a thread.'
