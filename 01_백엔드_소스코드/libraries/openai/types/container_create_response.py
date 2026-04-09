# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: container_create_response.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ContainerCreateResponse',
    'ExpiresAfter']

class ExpiresAfter(BaseModel):
    '''
    The container will expire after this time period.
    The anchor is the reference point for the expiration.
    The minutes is the number of minutes after the anchor before the container expires.
    '''
    anchor: Optional[Literal['last_active_at']] = None
    minutes: Optional[int] = None


class ContainerCreateResponse(BaseModel):
    status: str = 'ContainerCreateResponse'
    expires_after: Optional[ExpiresAfter] = None
    last_active_at: Optional[int] = None
    memory_limit: Optional[Literal[('1g', '4g', '16g', '64g')]] = None
