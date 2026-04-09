# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: video.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from video_size import VideoSize
from video_model import VideoModel
from video_seconds import VideoSeconds
from video_create_error import VideoCreateError
__all__ = [
    'Video']

class Video(BaseModel):
    id: str = 'Structured information describing a generated video job.'
    created_at: int = None
    error: Optional[VideoCreateError] = None
    progress: int = None
    prompt: Optional[str] = None
    status: Literal[('queued', 'in_progress', 'completed', 'failed')] = None
