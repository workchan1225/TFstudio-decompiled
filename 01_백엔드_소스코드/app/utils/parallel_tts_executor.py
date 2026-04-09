# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parallel_tts_executor.pyc (Python 3.11)

'''
병렬 TTS 실행 유틸리티

ThreadPoolExecutor 기반 병렬 처리로 TTS 생성 시간을 대폭 단축합니다.
- 동시 처리 수 제한 (기본 5개)
- Rate Limit 자동 대기
- 결과 순서 보장
- 진행률 콜백 지원
'''
import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from typing import List, Dict, Callable, Generator, Optional, Any
from dataclasses import dataclass, field
logger = logging.getLogger(__name__)
TTSTask = <NODE:12>()
TTSResult = <NODE:12>()

class ParallelTTSExecutor:
    '''
    병렬 TTS 실행기

    여러 라인의 TTS를 동시에 생성하여 처리 시간을 단축합니다.
    결과 순서는 보장되며, Rate Limit 자동 대기를 지원합니다.

    Usage:
        executor = ParallelTTSExecutor(max_workers=5)

        def generate_single(task: TTSTask) -> TTSResult:
            # TTS 생성 로직
            return TTSResult(index=task.index, success=True, ...)

        for event in executor.execute_streaming(tasks, generate_single):
            if event[\'type\'] == \'progress\':
                print(f"진행: {event[\'percent\']}%")
            elif event[\'type\'] == \'complete\':
                results = event[\'results\']
    '''
    
    def __init__(self = None, max_workers = None, rate_limit_delay = None, retry_on_rate_limit = (5, 0, True, 3), max_retries = ('max_workers', int, 'rate_limit_delay', float, 'retry_on_rate_limit', bool, 'max_retries', int)):
        '''
        Args:
            max_workers: 동시 실행 스레드 수 (기본 5)
            rate_limit_delay: 각 요청 사이 강제 대기 시간 (초, 기본 0)
            retry_on_rate_limit: Rate Limit 시 자동 재시도 (기본 True)
            max_retries: 최대 재시도 횟수 (기본 3)
        '''
        self.max_workers = max_workers
        self.rate_limit_delay = rate_limit_delay
        self.retry_on_rate_limit = retry_on_rate_limit
        self.max_retries = max_retries
        self._lock = threading.Lock()
        self._last_request_time = 0
        self._cancelled = False

    
    def cancel(self):
        '''실행 취소'''
        self._cancelled = True

    
    def _wait_for_rate_limit(self):
