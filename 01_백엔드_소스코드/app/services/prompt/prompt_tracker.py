# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_tracker.pyc (Python 3.11)

'''
PromptTracker - 프롬프트 생성 추적

디버깅 및 회귀 분석용 프롬프트 이력 기록.
각 씬의 프롬프트 생성 모드, 입력, 출력, 일관성 점수를 추적합니다.

사용 예:
    tracker = PromptTracker(project_id="proj_123")
    tracker.track_generation(
        scene_id="scene_1",
        mode="batch",
        base_prompt="original...",
        final_prompt="generated..."
    )
    history = tracker.get_scene_history("scene_1")
'''
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
import json
import logging
logger = logging.getLogger(__name__)
PromptTrace = <NODE:12>()

class PromptTracker:
    '''
    프롬프트 추적기

    프로젝트/세션 단위로 프롬프트 생성 이력을 관리합니다.
    현재는 메모리 기반이며, 필요시 DB 저장으로 확장 가능합니다.
    '''
    MAX_TRACES = 1000
    
    def __init__(self = None, project_id = None):
        '''
        Args:
            project_id: 프로젝트 ID
        '''
        self.project_id = project_id
        self.traces = []
        self._scene_index = { }

    
    def track(self = None, trace = None):
        '''
        추적 레코드 추가

        Args:
            trace: 프롬프트 추적 레코드
        '''
        if len(self.traces) >= self.MAX_TRACES:
            old_trace = self.traces.pop(0)
            if old_trace.scene_id in self._scene_index:
                self._scene_index[old_trace.scene_id] = self._scene_index[old_trace.scene_id]()
        idx = len(self.traces)
        self.traces.append(trace)
        if trace.scene_id not in self._scene_index:
            self._scene_index[trace.scene_id] = []
        self._scene_index[trace.scene_id].append(idx)
        logger.debug(f'''Tracked prompt: scene={trace.scene_id}, mode={trace.mode}, score={trace.consistency_score}''')

    
    def track_generation(self, scene_id, mode, base_prompt, final_prompt, direction, previous_scenes_count, anchors_preserved, anchors_lost = None, consistency_score = None, model_type = None, style_template_id = (None, 0, None, None, 1, None, None, None), warnings = ('scene_id', str, 'mode', str, 'base_prompt', str, 'final_prompt', str, 'direction', Optional[str], 'previous_scenes_count', int, 'anchors_preserved', List[str], 'anchors_lost', List[str], 'consistency_score', float, 'model_type', Optional[str], 'style_template_id', Optional[str], 'warnings', List[str])):
