# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_gen_stream_event.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from image_gen_completed_event import ImageGenCompletedEvent
from image_gen_partial_image_event import ImageGenPartialImageEvent
__all__ = [
    'ImageGenStreamEvent']
ImageGenStreamEvent: TypeAlias = Annotated[(Union[(ImageGenPartialImageEvent, ImageGenCompletedEvent)], PropertyInfo(discriminator = 'type'))]
