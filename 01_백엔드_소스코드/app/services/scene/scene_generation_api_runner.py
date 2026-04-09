# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_generation_api_runner.pyc (Python 3.11)

import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List
SceneNoImageDiagnostics = <NODE:12>()
SceneApiGenerationResult = <NODE:12>()

def build_scene_prompt_debug_lines(*, contents, model_name, aspect_ratio, gemini_resolution, reference_image_count):
    lines = [
        f'''\n{'================================================================================'}''',
        '[SceneImage] ★★★ FINAL PROMPT SENT TO API ★★★',
        f'''{'================================================================================'}''',
        f'''Model: {model_name}''',
        f'''Aspect Ratio: {aspect_ratio}''',
        f'''Resolution: {gemini_resolution}''']
    if isinstance(contents, str):
        lines.append('Type: text-only')
        lines.append(f'''\n{contents}''')
    elif isinstance(contents, list):
        lines.append(f'''Type: multimodal (text + {reference_image_count} images)''')
        for index, part in enumerate(contents):
            if isinstance(part, str):
                lines.append(f'''\n--- Text Part [{index}] ---''')
                lines.append(part)
                continue
            lines.append(f'''\n--- [Part {index}]: (image data) ---''')
            lines.extend([
                f'''\n{'================================================================================'}''',
                '[SceneImage] ★★★ END OF FINAL PROMPT ★★★',
                f'''{'================================================================================'}\n'''])
            return lines


def collect_inline_image_parts(api_response = None):
    collected_parts = []
    response_parts = getattr(api_response, 'parts', None)
# WARNING: Decompyle incomplete


def inspect_no_image_response(api_response = None, *, attempt_number):
    diagnostics = [
        f'''[SceneImage] No image part in API response (attempt {attempt_number}/1)''']
    result = SceneNoImageDiagnostics(is_safety_blocked = False, diagnostics = diagnostics)
    if not getattr(api_response, 'candidates', None):
        candidates = []
        for index, candidate in enumerate(candidates[:3]):
            finish_reason = getattr(candidate, 'finish_reason', None)
            if finish_reason:
                finish_reason_str = str(finish_reason)
                result.finish_reasons.append(finish_reason_str)
                diagnostics.append(f'''[SceneImage] Candidate {index} finish_reason: {finish_reason_str}''')
                if 'SAFETY' in finish_reason_str.upper() or 'PROHIBITED' in finish_reason_str.upper():
                    result.is_safety_blocked = True
            if not getattr(candidate, 'safety_ratings', None):
                safety_ratings = []
                blocked_categories = safety_ratings()
                if blocked_categories:
                    result.blocked_categories.extend(blocked_categories)
                    result.is_safety_blocked = True
                    diagnostics.append(f'''[SceneImage] Candidate blocked by safety: {blocked_categories}''')
            prompt_feedback = getattr(api_response, 'prompt_feedback', None)
    block_reason = getattr(prompt_feedback, 'block_reason', None) if prompt_feedback else None
    if block_reason:
        block_reason_str = str(block_reason)
        result.block_reason = block_reason_str
        result.is_safety_blocked = True
        diagnostics.append(f'''[SceneImage] Prompt blocked: {block_reason_str}''')
    return result

_SIMPLIFY_STRIP_PATTERNS = [
    re.compile('\\([^)]{10,}\\)'),
    re.compile(';[^.]*(?=\\.)'),
    re.compile('((?:\\w+,\\s*){2})\\w+(?:,\\s*\\w+)+')]

def _simplify_prompt_text(text = None):
    '''NO_IMAGE 재시도용 프롬프트 단순화.

    긴 부연설명, 세미콜론 뒤 부가 지시, 과다 형용사를 제거하여
    Gemini가 이미지를 생성할 수 있도록 프롬프트를 짧게 만든다.
    '''
    simplified = text
    for pattern in _SIMPLIFY_STRIP_PATTERNS:
        simplified = pattern.sub((lambda m: m.group(1) if m.lastindex else ''), simplified)
        simplified = re.sub('\\s{2,}', ' ', simplified).strip()
        if len(simplified) > 1500:
            simplified = simplified[:1500].rsplit('.', 1)[0] + '.'
    return simplified


def _simplify_contents_for_retry(contents = None):
    '''contents 내 텍스트 부분만 단순화하여 새 contents 반환.'''
    if isinstance(contents, str):
        return _simplify_prompt_text(contents)
# WARNING: Decompyle incomplete


def run_scene_generation_api_request(*, client, types_module, model_name, contents, aspect_ratio, gemini_resolution, engine, ensure_not_cancelled_fn, classify_scene_generation_error_fn, get_scene_retry_policy_fn, sleep_fn, utcnow_fn):
