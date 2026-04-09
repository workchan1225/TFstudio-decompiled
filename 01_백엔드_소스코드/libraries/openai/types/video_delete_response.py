# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: video_delete_response.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'VideoDeleteResponse']

class VideoDeleteResponse(BaseModel):
    object: Literal['video.deleted'] = 'Confirmation payload returned after deleting a video.'
