# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: progress_tracker.pyc (Python 3.11)

'''
Auto Production - SSE Progress Event Builder
'''
import json
import logging
from typing import Optional
from types import AutoProductionPhase, PHASE_WEIGHTS
logger = logging.getLogger(__name__)

class ProgressTracker:
    '''SSE 이벤트 빌더 - 단계별 진행률을 전체 진행률로 환산'''
    
    def __init__(self):
        self._phase_progress = { }
        self._current_phase = None
        self._project_id = None
        self._error = None

    
    def set_project_id(self = None, project_id = None):
        self._project_id = project_id

    
    def start_phase(self = None, phase = None):
        self._current_phase = phase
        self._phase_progress[phase] = 0
        return self._build_event('processing')

    
    def update_phase(self = None, phase = None, progress = None, message = ('',)):
        self._phase_progress[phase] = min(progress, 100)
        return self._build_event('processing', message)

    
    def complete_phase(self = None, phase = None):
        self._phase_progress[phase] = 100
        return self._build_event('processing', f'''{phase.value} 완료''')

    
    def complete_all(self = None, message = None):
        return self._build_event('completed', message)

    
    def fail(self = None, error = None):
        self._error = error
        return self._build_event('error', error)

    
    def cancel(self = None):
        return self._build_event('cancelled', '제작이 취소되었습니다')

    
    def _calculate_overall_progress(self = None):
        total = 0
        for phase, weight in PHASE_WEIGHTS.items():
            phase_pct = self._phase_progress.get(phase, 0)
            total += (phase_pct / 100) * weight
            return min(total, 100)

    
    def _build_event(self = None, status = None, message = None):
        overall = self._calculate_overall_progress()
        stage = self._current_phase.value if self._current_phase else 'project_setup'
        stage_progress = self._phase_progress.get(self._current_phase, 0) if self._current_phase else 0
        data = {
            'status': status,
            'progress': round(overall, 1),
            'stage': stage,
            'stageProgress': round(stage_progress, 1),
            'message': message,
            'projectId': self._project_id,
            'error': self._error }
        return f'''data: {json.dumps(data, ensure_ascii = False)}\n\n'''
