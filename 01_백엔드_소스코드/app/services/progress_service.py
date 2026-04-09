# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: progress_service.pyc (Python 3.11)

'''
영상 생성 진행률 추적 서비스
SSE를 통해 실시간 진행률 전송
'''
import threading
from typing import Dict, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import time
import logging
logger = logging.getLogger(__name__)

class ProgressStatus(Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    ERROR = 'error'
    STOPPED = 'stopped'

ProgressInfo = <NODE:12>()

class ProgressService:
    pass
# WARNING: Decompyle incomplete

progress_service = ProgressService()
