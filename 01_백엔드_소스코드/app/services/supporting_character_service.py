# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: supporting_character_service.pyc (Python 3.11)

__doc__ = '\n조연 캐릭터(Supporting Character) 감지 및 관리 서비스\n\n대본에서 조연을 자동으로 감지하고, 역할 기반 외모를 생성합니다.\n반복 등장 조연(2회+)은 참조 이미지 생성 대상으로 표시됩니다.\n'
import re
import logging
from typing import List, Dict, Optional, Set
logger = logging.getLogger(__name__)
# WARNING: Decompyle incomplete
