# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: step_runners.pyc (Python 3.11)

'''
Auto Production - Step Runner Functions

각 단계의 실행 로직. 기존 서비스를 직접 호출.
'''
import logging
import threading
from typing import Callable, Optional
from types import AutoProductionConfig, SceneData
logger = logging.getLogger(__name__)
CancelCheck = Callable[([], bool)]

def run_project_setup(config = None, is_cancelled = None):
