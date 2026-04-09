# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reference_prompts.pyc (Python 3.11)

'''
Reference Mode Prompts

레퍼런스 기반 대본 생성을 위한 프롬프트 빌더
'''
from typing import Dict, Any, Optional, List
import logging
from reference_blueprint import build_reference_blueprint
from reference_content_guard import extract_focus_keywords
logger = logging.getLogger(__name__)

class ReferencePrompts:
    '''
    레퍼런스 기반 프롬프트 빌더

    레퍼런스 영상의 패턴 분석 결과를 활용하여
    제목, 시놉시스, 대본 생성 프롬프트를 구성합니다.
    '''
    _detect_content_format = (lambda analysis = None: pass# WARNING: Decompyle incomplete
)()
    _get_reference_blueprint = (lambda analysis = None: blueprint = analysis.get('referenceBlueprint')if isinstance(blueprint, dict) and blueprint:
blueprintNone(analysis_data = analysis, full_text = analysis.get('fullText', ''), video_info = {
'title': analysis.get('videoTitle', ''),
'channelName': analysis.get('channelName', '') }))()
    _build_blueprint_prompt_sections = (lambda analysis = None: blueprint = ReferencePrompts._get_reference_blueprint(analysis)style_profile = blueprint.get('styleProfile', { }) if isinstance(blueprint, dict) else { }structure_profile = blueprint.get('structureProfile', { }) if isinstance(blueprint, dict) else { }hook_profile = blueprint.get('hookProfile', { }) if isinstance(blueprint, dict) else { }constraints = blueprint.get('contentConstraints', { }) if isinstance(blueprint, dict) else { }anti_transfer = blueprint.get('antiTransfer', { }) if isinstance(blueprint, dict) else { }sentence_endings = style_profile.get('sentenceEndings', { }) if isinstance(style_profile, dict) else { }sentence_rhythm = style_profile.get('sentenceRhythm', { }) if isinstance(style_profile, dict) else { }section_ratios = structure_profile.get('sectionRatios', { }) if isinstance(structure_profile, dict) else { }style_lines = []if style_profile.get('contentStyle'):
style_lines.append(f'''- 콘텐츠 스타일: {style_profile.get('contentStyle')}''')if style_profile.get('primaryTone'):
style_lines.append(f'''- 주요 톤: {style_profile.get('primaryTone')}''')if style_profile.get('formality'):
style_lines.append(f'''- 격식 레벨: {style_profile.get('formality')}''')if style_profile.get('emotion'):
style_lines.append(f'''- 감정 톤: {style_profile.get('emotion')}''')if style_profile.get('narrationMode'):
style_lines.append(f'''- 서술 모드: {style_profile.get('narrationMode')}''')top_patterns = sentence_endings.get('topPatterns', [])if top_patterns:
style_lines.append(f'''- 문장 어미 패턴: {', '.join(top_patterns[:6])}''')if sentence_rhythm:
average_length = sentence_rhythm.get('averageLength')short_ratio = sentence_rhythm.get('shortSentenceRatio')long_ratio = sentence_rhythm.get('longSentenceRatio')if average_length:
if not short_ratio and long_ratio:
style_lines.append(f'''- 문장 리듬: 평균 {average_length}자 / 짧은 문장 비중 {int(0 * 100)}% / 긴 문장 비중 {int(0 * 100)}%''')structure_lines = []if section_ratios:
structure_lines.append(f'''- 구조 비율: 도입 {section_ratios.get('introduction', 15)} / 전개 {section_ratios.get('development', 50)} / 절정 {section_ratios.get('climax', 20)} / 결론 {section_ratios.get('conclusion', 15)}''')if structure_profile.get('openingMode'):
structure_lines.append(f'''- 오프닝 방식: {structure_profile.get('openingMode')}''')if structure_profile.get('openingHooks'):
structure_lines.append(f'''- 도입 훅: {', '.join(structure_profile.get('openingHooks', [])[:4])}''')if structure_profile.get('transitionPatterns'):
structure_lines.append(f'''- 전환 패턴: {', '.join(structure_profile.get('transitionPatterns', [])[:5])}''')if structure_profile.get('closingMode'):
structure_lines.append(f'''- 마무리 방식: {structure_profile.get('closingMode')}''')if structure_profile.get('chapterStrategy'):
structure_lines.append(f'''- 전개 전략: {structure_profile.get('chapterStrategy')}''')hook_lines = []if hook_profile.get('openingHookType'):
hook_lines.append(f'''- 오프닝 훅 타입: {hook_profile.get('openingHookType')}''')if hook_profile.get('midHookTypes'):
hook_lines.append(f'''- 중반 훅 타입: {', '.join(hook_profile.get('midHookTypes', [])[:4])}''')if hook_profile.get('closingHookType'):
hook_lines.append(f'''- 마무리 훅 타입: {hook_profile.get('closingHookType')}''')if hook_profile.get('retentionDevices'):
hook_lines.append(f'''- 리텐션 장치: {', '.join(hook_profile.get('retentionDevices', [])[:6])}''')maintain_lines = constraints.get('maintain', [])[:6]()replace_lines = constraints.get('replace', [])[:6]()avoid_lines = constraints.get('avoid', [])[:6]()anti_transfer_lines = [
f'''- 정책: {anti_transfer.get('policy')}''' if anti_transfer.get('policy') else '']if anti_transfer.get('sourceAnchors'):
anti_transfer_lines.append(f'''- 원본 앵커: {', '.join(anti_transfer.get('sourceAnchors', [])[:5])}''')if anti_transfer.get('bannedKeywords'):
anti_transfer_lines.append(f'''- 금지 키워드: {', '.join(anti_transfer.get('bannedKeywords', [])[:10])}''')anti_transfer_lines = anti_transfer_lines(){
'style': '\n'.join(style_lines) if style_lines else '- (blueprint 없음)',
'structure': '\n'.join(structure_lines) if structure_lines else '- (blueprint 없음)',
'hooks': '\n'.join(hook_lines) if hook_lines else '- (blueprint 없음)',
'maintain': '\n'.join(maintain_lines) if maintain_lines else '- 구조와 문체 유지',
'replace': '\n'.join(replace_lines) if replace_lines else '- 주제와 소재를 새롭게 치환',
'avoid': '\n'.join(avoid_lines) if avoid_lines else '- 원본 내용 직접 재사용 금지',
'anti_transfer': '\n'.join(anti_transfer_lines) if anti_transfer_lines else '- 원본 사실/고유명사 직접 재사용 금지',
'blueprint': blueprint })()
    _build_content_source_priority_section = (lambda selected_title = None, synopsis = None, topic_direction = staticmethod: focus_keywords = extract_focus_keywords(title = selected_title, synopsis = synopsis, topic_direction = topic_direction)keyword_lines = (lambda .0: pass# WARNING: Decompyle incomplete
)(focus_keywords[:10]()) if focus_keywords else '- (제목/시놉시스에서 추출된 핵심 키워드 없음)'
        section = f'''## 새 콘텐츠 설계 우선순위\n1. 선택된 제목\n2. 선택된 시놉시스\n3. 사용자 주제 방향\n4. Reference Blueprint\n5. 레퍼런스 원문/원본 사건/원본 주장\n\n### 새 주제 핵심 키워드 (반드시 반영)\n{keyword_lines}\n\n### 적용 규칙\n- 새 대본의 사건, 논점, 예시는 위 제목/시놉시스/주제 방향에서만 결정하세요.\n- Reference Blueprint는 구조, 톤, 문체, 훅, 전개 리듬을 결정하는 용도로만 사용하세요.\n- 레퍼런스 원문에 있던 소재가 아니라, 위 키워드를 중심으로 새 내용을 배치하세요.\n'''
        return {
            'focus_keywords': focus_keywords,
            'section': section }
)()
    _build_alignment_feedback_section = (lambda alignment_feedback = None: if not alignment_feedback:
''if not None.get('missingFocusKeywords', []):
missing_focus = []if not alignment_feedback.get('bannedKeywordHits', []):
banned_hits = []if not alignment_feedback.get('sourceAnchorTokenHits', []):
source_anchor_token_hits = []if not alignment_feedback.get('sourceAnchorHits', []):
source_hits = []if not alignment_feedback.get('matchedFocusKeywords', []):
matched_focus = []correction_lines = []if missing_focus:
correction_lines.append(f'''- 더 분명하게 반영할 새 주제 키워드: {', '.join(missing_focus[:6])}''')if matched_focus:
correction_lines.append(f'''- 이미 반영된 키워드는 유지: {', '.join(matched_focus[:6])}''')if banned_hits:
correction_lines.append(f'''- 제거해야 할 레퍼런스 키워드: {', '.join(banned_hits[:8])}''')if source_anchor_token_hits:
correction_lines.append(f'''- 제거해야 할 원본 사례/고유명사: {', '.join(source_anchor_token_hits[:8])}''')if source_hits:
correction_lines.append(f'''- 제거해야 할 원본 앵커 표현: {', '.join(source_hits[:4])}''')if not correction_lines:
correction_lines.append('- 새 제목/시놉시스 중심으로 내용을 다시 정렬하세요.')f'''\n## 재생성 보정 피드백\n이전 시도는 새 주제 정렬이 충분하지 않았습니다. 아래 내용만 보정하고, 레퍼런스의 톤/구조/말투는 유지하세요.\n{chr(10).join(correction_lines)}\n\n### 보정 원칙\n- 스타일, 어미, 훅 배치, 구조 비율은 유지하세요.\n- 내용만 새 제목과 새 시놉시스에 다시 맞추세요.\n- 원본 레퍼런스의 사건, 인물, 사례가 떠오르는 문장은 새 표현으로 완전히 교체하세요.\n''')()
    _extract_style_samples = (lambda full_text = None, max_samples = None, sample_length = staticmethod: if full_text or len(full_text) < 100:
''samples = Nonetext_length = len(full_text)if text_length > 0:
intro_end = min(sample_length, text_length)intro_sample = full_text[:intro_end].strip()if intro_sample:
samples.append(f'''[도입부]\n{intro_sample}''')if text_length > sample_length * 2 and max_samples >= 2:
mid_start = text_length // 2 - sample_length // 2mid_end = mid_start + sample_lengthmid_sample = full_text[mid_start:mid_end].strip()if mid_sample:
samples.append(f'''[중반부]\n{mid_sample}''')if text_length > sample_length and max_samples >= 3:
outro_start = max(0, text_length - sample_length)outro_sample = full_text[outro_start:].strip()if outro_sample:
samples.append(f'''[결론부]\n{outro_sample}''')'\n\n'.join(samples) if samples else '')()
    _extract_intro_dialogue_patterns = (lambda full_text = None, intro_length = None: pass# WARNING: Decompyle incomplete
)()
    _extract_sentence_endings = (lambda full_text = None, max_examples = None: pass# WARNING: Decompyle incomplete
)()
    build_title_prompt = (lambda analysis = None, topic_direction = None, language = staticmethod, count = (None, '한국어', 10, False), exclude_character_analysis = ('analysis', Dict[(str, Any)], 'topic_direction', Optional[str], 'language', str, 'count', int, 'exclude_character_analysis', bool, 'return', str): structural = analysis.get('structuralPattern', { })psychological = analysis.get('psychologicalPattern', { })video_title = analysis.get('videoTitle', '알 수 없음')title_optimization = analysis.get('titleOptimization', { })content_category = analysis.get('contentCategory', { })hook_timing = analysis.get('hookTiming', { })intro_hooks = structural.get('introduction', { }).get('hooks', [])curiosity_triggers = psychological.get('curiosityTriggers', [])retention_hooks = psychological.get('retentionHooks', [])hooks_text = ''if intro_hooks:
hooks_text += f'''- 도입부 후킹: {', '.join(intro_hooks[:5])}\n'''if curiosity_triggers:
hooks_text += f'''- 호기심 유발: {', '.join(curiosity_triggers[:5])}\n'''if retention_hooks:
retention_contents = retention_hooks[:3]()if retention_contents:
hooks_text += f'''- 시청 유지 훅: {', '.join(retention_contents)}\n'''title_opt_text = ''if title_optimization:
hook_words = title_optimization.get('hookWords', [])power_words = title_optimization.get('powerWords', [])emotion_triggers = title_optimization.get('emotionTriggers', [])curiosity_gaps = title_optimization.get('curiosityGaps', [])suggested_formats = title_optimization.get('suggestedFormats', [])if hook_words:
title_opt_text += f'''\n### 🪝 훅 키워드 (반드시 활용)\n- {', '.join(hook_words[:8])}\n'''if power_words:
title_opt_text += f'''\n### 💪 파워 워드 (감정 자극)\n- {', '.join(power_words[:8])}\n'''if emotion_triggers:
title_opt_text += f'''\n### 😮 감정 트리거\n- {', '.join(emotion_triggers[:5])}\n'''if curiosity_gaps:
title_opt_text += '\n### 🤔 호기심 갭 (정보 공백 활용)\n'for gap in curiosity_gaps[:3]:
title_opt_text += f'''- {gap}\n'''if suggested_formats:
title_opt_text += '\n### 📝 추천 제목 포맷\n'for fmt in suggested_formats[:3]:
title_opt_text += f'''- {fmt}\n'''category_text = ''category_constraint = ''if content_category:
primary = content_category.get('primary', '')secondary = content_category.get('secondary', '')sub_genre = content_category.get('subGenre', '')target = content_category.get('targetAudience', '')style = content_category.get('contentStyle', '')if primary:
category_text = '\n### 🎯 콘텐츠 카테고리 (필수 적용!)\n'category_text += f'''- **장르: {primary}**'''if secondary:
category_text += f''' > {secondary}'''if sub_genre:
category_text += f''' > {sub_genre}'''category_text += '\n'if target:
category_text += f'''- 타겟 오디언스: {target}\n'''if style:
category_text += f'''- 콘텐츠 스타일: {style}\n'''genre_full = primaryif secondary:
genre_full += f'''/{secondary}'''category_constraint = f'''\n⚠️ **장르 제약**: 반드시 **{genre_full}** 장르의 제목을 생성하세요. 다른 장르는 허용되지 않습니다.\n'''elif target:
category_text = '\n### 📁 콘텐츠 특성\n'category_text += f'''- 타겟 오디언스: {target}\n'''if style:
category_text += f'''- 콘텐츠 스타일: {style}\n'''hook_effectiveness = ''if hook_timing:
eff_score = hook_timing.get('effectivenessScore', 0)if eff_score:
hook_effectiveness = f'''\n### ⚡ 훅 효과 점수: {eff_score}/100\n'''opening_hook = hook_timing.get('openingHook', { })if opening_hook and opening_hook.get('content'):
hook_effectiveness += f'''- 오프닝 훅 예시: "{opening_hook.get('content')}"\n'''genre_info = ''if content_category:
primary = content_category.get('primary', '')secondary = content_category.get('secondary', '')if primary:
genre_info = primaryif secondary:
genre_info += f'''/{secondary}'''if topic_direction and topic_direction.strip():
topic_instruction = f'''## 주제 방향\n사용자가 원하는 주제: **{topic_direction}**\n\n레퍼런스의 후킹 패턴과 구조를 적용하되, 위 주제로 새로운 제목을 생성하세요.\n{f'''단, **{genre_info}** 장르/분야의 맥락을 유지하세요.''' if genre_info else ''}'''elif genre_info:
topic_instruction = f'''## 주제 방향 (장르 기반 자동 생성)\n레퍼런스 영상: {video_title}\n레퍼런스 장르: **{genre_info}**\n\n🎯 **핵심 지침**: 반드시 **{genre_info}** 장르 내에서 새로운 제목을 생성하세요.\n- 레퍼런스와 같은 장르/분야의 다른 소재를 다루는 제목이어야 합니다.\n- 전혀 다른 장르(예: 역사물 → 요리, 공포 → 코미디)로 바꾸지 마세요.\n- 레퍼런스의 성공 패턴(후킹, 구조)은 적용하되 소재만 새롭게 하세요.'''else:
topic_instruction = f'''## 주제 방향\n레퍼런스 영상: {video_title}\n\n레퍼런스와 **유사한 주제/분야**에서 새로운 제목을 생성하세요.\n같은 분야의 다른 소재를 다루는 제목이어야 합니다.'''f'''당신은 유튜브 제목 전문가입니다.\n\n레퍼런스 영상의 성공 패턴을 분석하여 새로운 제목을 생성합니다.\n\n## 레퍼런스 분석 결과\n\n### 후킹 패턴\n{hooks_text if hooks_text else '- (분석 데이터 없음)'}\n\n### 구조적 특징\n- 도입부 비율: {structural.get('introduction', { }).get('ratio', 15)}%\n- 전개부 비율: {structural.get('development', { }).get('ratio', 50)}%\n- 클라이맥스 비율: {structural.get('climax', { }).get('ratio', 20)}%\n- 결론부 비율: {structural.get('conclusion', { }).get('ratio', 15)}%\n{category_text}{category_constraint}{title_opt_text}{hook_effectiveness}\n{topic_instruction}\n\n## 요구사항\n1. **장르/카테고리를 반드시 유지**하세요 (가장 중요!)\n2. **레퍼런스의 후킹 패턴을 반드시 적용**하세요\n3. **훅 키워드와 파워 워드를 적극 활용**하세요\n4. 40-70자 길이로 작성하세요\n5. {count}개의 다양한 스타일 제목을 생성하세요\n6. **{language}**로 작성하세요\n7. 각 제목마다 50자 이내의 간단한 설명을 추가하세요\n\n## 출력 형식 (반드시 이 형식을 따르세요!)\n\n**중요**: 스타일 분류명(예: "충격적 스타일", "호기심 유발 스타일")을 제목으로 쓰지 마세요!\n실제 영상 제목을 작성하세요.\n\n다음 형식으로 출력 (대괄호 없이!):\n1. 제목 내용 | 50자 이내 설명\n2. 제목 내용 | 50자 이내 설명\n...\n{count}. 제목 내용 | 50자 이내 설명\n\n예시:\n1. 30년 충성했던 부하 직원에게 배신당한 회장의 분노 | 충격적인 반전이 기다린다\n2. 아무도 몰랐던 할머니의 비밀 금고, 손녀가 열어보니 | 3대에 걸친 감동 스토리\n''')()
    build_synopsis_prompt = (lambda analysis, selected_title, topic_direction, pattern_intensity = None, language = None, count = staticmethod, exclude_character_analysis = ('', 'moderate', '한국어', 5, False, None), alignment_feedback = ('analysis', Dict[(str, Any)], 'selected_title', str, 'topic_direction', str, 'pattern_intensity', str, 'language', str, 'count', int, 'exclude_character_analysis', bool, 'alignment_feedback', Optional[Dict[(str, Any)]], 'return', str): structural = analysis.get('structuralPattern', { })blueprint_sections = ReferencePrompts._build_blueprint_prompt_sections(analysis)blueprint = blueprint_sections.get('blueprint', { })style_profile = blueprint.get('styleProfile', { }) if isinstance(blueprint, dict) else { }content_priority = ReferencePrompts._build_content_source_priority_section(selected_title = selected_title, synopsis = '', topic_direction = topic_direction)alignment_feedback_section = ReferencePrompts._build_alignment_feedback_section(alignment_feedback)content_category = analysis.get('contentCategory', { })pace_analysis = analysis.get('paceAnalysis', { })detected_tone = analysis.get('detectedTone', { })category_text = ''if content_category:
primary = content_category.get('primary', '')secondary = content_category.get('secondary', '')target = content_category.get('targetAudience', '')style = content_category.get('contentStyle', '')if primary and target or style:
category_text = '\n### 📁 콘텐츠 특성\n'if primary:
category_text += f'''- 카테고리: {primary}'''if secondary:
category_text += f''' > {secondary}'''category_text += '\n'if target:
category_text += f'''- 타겟 오디언스: {target}\n'''if style:
category_text += f'''- 콘텐츠 스타일: {style}\n'''pace_text = ''if pace_analysis:
overall_pace = pace_analysis.get('overallPace', '')info_density = pace_analysis.get('informationDensity', '')pacing_style = pace_analysis.get('pacingStyle', '')if overall_pace or pacing_style:
pace_text = '\n### ⚡ 페이스 특성\n'if overall_pace:
pace_labels = {
'slow': '느림',
'medium': '보통',
'fast': '빠름' }pace_text += f'''- 전체 페이스: {pace_labels.get(overall_pace, overall_pace)}\n'''if info_density:
density_labels = {
'low': '낮음',
'medium': '보통',
'high': '높음' }pace_text += f'''- 정보 밀도: {density_labels.get(info_density, info_density)}\n'''if pacing_style:
pace_text += f'''- 페이싱 스타일: {pacing_style}\n'''tone_text = ''if detected_tone:
primary_tone = detected_tone.get('primary', '')formality = detected_tone.get('formality', '')emotion = detected_tone.get('emotion', '')if primary_tone:
tone_text = '\n### 🎭 톤 & 문체\n'tone_text += f'''- 주요 톤: {primary_tone}\n'''if formality:
formality_labels = {
'formal': '격식체',
'casual': '비격식체',
'mixed': '혼합' }tone_text += f'''- 격식: {formality_labels.get(formality, formality)}\n'''if emotion:
emotion_labels = {
'neutral': '중립',
'dramatic': '드라마틱',
'informative': '정보 전달형',
'humorous': '유머러스' }tone_text += f'''- 감정 톤: {emotion_labels.get(emotion, emotion)}\n'''format_info = ReferencePrompts._detect_content_format(analysis)blueprint_narration_mode = style_profile.get('narrationMode', '')if not blueprint_narration_mode == 'indirect':
use_indirect_speech = format_info.get('use_indirect_speech', False)content_format = 'informational' if use_indirect_speech else 'reference'primary_category = format_info.get('primary', '')content_style = format_info.get('style', '')primary_tone = format_info.get('tone', '')intensity_guidance_map = {
'strict': '레퍼런스의 구조 비율, 말투, 훅 배치를 최대한 가깝게 유지하세요.',
'moderate': '레퍼런스의 구조와 톤은 유지하되 새 주제에 맞게 자연스럽게 변형하세요.',
'loose': '레퍼런스는 참고하되 핵심 구조와 톤만 남기고 표현은 더 자유롭게 전개하세요.' }pattern_guidance = intensity_guidance_map.get(pattern_intensity, intensity_guidance_map['moderate'])if topic_direction and topic_direction.strip():
topic_instruction = f'''## 새 주제 방향\n사용자 주제 전환 지시: **{topic_direction.strip()}**\n\n선택된 제목과 위 주제 방향을 기준으로 내용을 설계하세요.\n레퍼런스는 표현 방식과 전개 구조에만 영향을 주고, 실제 소재/사건/주장은 새 주제로 다시 만들어야 합니다.'''else:
topic_instruction = '## 주제 전환 규칙\n선택된 제목을 기준으로 새 내용을 설계하세요.\n레퍼런스 영상의 구조, 문체, 훅 배치는 유지하되 원본 소재와 사건은 그대로 가져오지 마세요.'if not content_format == 'reference' and use_indirect_speech:
costume_section = '' if exclude_character_analysis else '\n[의상 스타일] 등장인물들의 시대에 맞는 복장 가이드 (남성/여성 구분, 신분별 차이 포함)'if not content_style:
passoutput_format = f'''=== 출력 형식 (서문 없이 바로 시작) ===\n\n## ⚠️ 레퍼런스 스타일 적용 필수!\n이 시놉시스는 레퍼런스 콘텐츠의 스타일({'분석됨'})을 따라야 합니다.\n- 톤/문체: {primary_tone if primary_tone or primary_tone else '레퍼런스와 동일'}\n- 화법: {content_style if content_style else '레퍼런스와 동일'}\n\n1.\n[로그라인] 100자 이내 핵심 요약 (레퍼런스 톤 반영)\n[시대/배경] 시대, 주요 장소, 계절/시간대{costume_section}\n[전개 구조] 레퍼런스 패턴에 맞는 구조 (도입-전개-절정-결말)\n[핵심 요소] 스토리의 핵심 (레퍼런스와 유사한 방식)\n[주제의식] 핵심 메시지\n\n---\n(동일 형식으로 {count}개 작성, 각각 다른 접근 방식)'''elif use_indirect_speech:
output_format = f'''=== 출력 형식 (서문 없이 바로 시작) ===\n\n## ⚠️ 정보성 콘텐츠 스타일 적용!\n이 시놉시스는 정보 전달형 콘텐츠입니다.\n- **드라마/갈등 구조 사용 금지**\n- **레퍼런스 톤/말투 유지**\n- 정보 전달 중심 구성\n\n1.\n[핵심 주제] 100자 이내 핵심 요약\n[콘텐츠 개요] 전달할 핵심 정보와 메시지\n[구성] 도입(문제제기/호기심) → 본론(핵심정보 전달) → 결론(요약/행동촉구)\n[타겟 오디언스] 누구를 위한 콘텐츠인가\n[차별점] 기존 콘텐츠와 다른 관점/정보\n\n---\n(동일 형식으로 {count}개 작성, 각각 다른 접근 방식)'''elif exclude_character_analysis:
passcostume_section = '\n[의상 스타일] 등장인물들의 시대에 맞는 복장 가이드 (남성/여성 구분, 신분별 차이 포함)'output_format = f'''=== 출력 형식 (서문 없이 바로 시작) ===\n1.\n[로그라인] 100자 이내 핵심 요약\n[시대/배경] 시대(예: 조선 중기, 1980년대, 현대, 근미래), 주요 장소(예: 한양 저잣거리, 서울 강남), 계절/시간대{costume_section}\n[3막 구조] 1막(설정), 2막(대립), 3막(해결)\n[중심 갈등] 외적/내적 갈등\n[주제의식] 핵심 메시지\n\n---\n(동일 형식으로 {count}개 작성, 각각 다른 접근 방식, 시대/배경은 일관되게 유지)'''[]['영상 기획 전문가로서 시놉시스 '][f'''{count}''']['개 작성.\n\n제목: '][f'''{selected_title}''']['\n'][f'''{f'''장르/카테고리: {primary_category}''' if primary_category else ''}''']['\n'][f'''{f'''콘텐츠 스타일: {content_style}''' if content_style else ''}''']['\n'][f'''{f'''톤/문체: {primary_tone}''' if primary_tone else ''}''']['\n언어: '][f'''{language}''']['\n패턴 적용 강도: '][f'''{pattern_intensity}''']['\n\n'][f'''{topic_instruction}''']['\n'][f'''{content_priority.get('section')}''']['\n'][f'''{alignment_feedback_section}''']['\n\n## 레퍼런스 분석 정보 (필수 참고!)\n'][f'''{category_text}'''][f'''{pace_text}'''][f'''{tone_text}''']['\n### 레퍼런스 구조 패턴\n- 도입부: '][f'''{structural.get('introduction', { }).get('ratio', 15)}''']['% | 전개부: '][f'''{structural.get('development', { }).get('ratio', 50)}''']['%\n- 클라이맥스: '][f'''{structural.get('climax', { }).get('ratio', 20)}''']['% | 결론부: '][f'''{structural.get('conclusion', { }).get('ratio', 15)}''']['%\n\n## Reference Blueprint (최우선 적용)\n### 따라야 할 스타일\n'][f'''{blueprint_sections.get('style')}''']['\n\n### 따라야 할 구조\n'][f'''{blueprint_sections.get('structure')}''']['\n\n### 따라야 할 훅 패턴\n'][f'''{blueprint_sections.get('hooks')}''']['\n\n### 유지할 요소\n'][f'''{blueprint_sections.get('maintain')}''']['\n\n### 반드시 교체할 요소\n'][f'''{blueprint_sections.get('replace')}''']['\n\n### 금지할 전이\n'][f'''{blueprint_sections.get('avoid')}''']['\n\n### 원본 내용 누수 금지 규칙\n'][f'''{blueprint_sections.get('anti_transfer')}''']['\n\n## 생성 원칙\n- '][f'''{pattern_guidance}''']['\n- 제목과 새 주제 방향에 맞는 새 소재를 사용하세요.\n- 레퍼런스의 고유명사, 사건, 주장, 사례, 사실 문구를 그대로 재사용하지 마세요.\n- 구조/톤/문체/전개 리듬만 유지하세요.\n\n'][f'''{output_format}''']([]['영상 기획 전문가로서 시놉시스 '][f'''{count}''']['개 작성.\n\n제목: '][f'''{selected_title}''']['\n'][f'''{f'''장르/카테고리: {primary_category}''' if primary_category else ''}''']['\n'][f'''{f'''콘텐츠 스타일: {content_style}''' if content_style else ''}''']['\n'][f'''{f'''톤/문체: {primary_tone}''' if primary_tone else ''}''']['\n언어: '][f'''{language}''']['\n패턴 적용 강도: '][f'''{pattern_intensity}''']['\n\n'][f'''{topic_instruction}''']['\n'][f'''{content_priority.get('section')}''']['\n'][f'''{alignment_feedback_section}''']['\n\n## 레퍼런스 분석 정보 (필수 참고!)\n'][f'''{category_text}'''][f'''{pace_text}'''][f'''{tone_text}''']['\n### 레퍼런스 구조 패턴\n- 도입부: '][f'''{structural.get('introduction', { }).get('ratio', 15)}''']['% | 전개부: '][f'''{structural.get('development', { }).get('ratio', 50)}''']['%\n- 클라이맥스: '][f'''{structural.get('climax', { }).get('ratio', 20)}''']['% | 결론부: '][f'''{structural.get('conclusion', { }).get('ratio', 15)}''']['%\n\n## Reference Blueprint (최우선 적용)\n### 따라야 할 스타일\n'][f'''{blueprint_sections.get('style')}''']['\n\n### 따라야 할 구조\n'][f'''{blueprint_sections.get('structure')}''']['\n\n### 따라야 할 훅 패턴\n'][f'''{blueprint_sections.get('hooks')}''']['\n\n### 유지할 요소\n'][f'''{blueprint_sections.get('maintain')}''']['\n\n### 반드시 교체할 요소\n'][f'''{blueprint_sections.get('replace')}''']['\n\n### 금지할 전이\n'][f'''{blueprint_sections.get('avoid')}''']['\n\n### 원본 내용 누수 금지 규칙\n'][f'''{blueprint_sections.get('anti_transfer')}''']['\n\n## 생성 원칙\n- '][f'''{pattern_guidance}''']['\n- 제목과 새 주제 방향에 맞는 새 소재를 사용하세요.\n- 레퍼런스의 고유명사, 사건, 주장, 사례, 사실 문구를 그대로 재사용하지 마세요.\n- 구조/톤/문체/전개 리듬만 유지하세요.\n\n'][f'''{output_format}''']['\n']))()
    build_script_prompt = (lambda analysis, synopsis, selected_title, topic_direction, pattern_intensity, target_length = None, tone = None, chapter_count = staticmethod, exclude_character_analysis = ('', '', 'moderate', 4000, '소설체', 6, False, None), alignment_feedback = ('analysis', Dict[(str, Any)], 'synopsis', str, 'selected_title', str, 'topic_direction', str, 'pattern_intensity', str, 'target_length', int, 'tone', str, 'chapter_count', int, 'exclude_character_analysis', bool, 'alignment_feedback', Optional[Dict[(str, Any)]], 'return', str): structural = analysis.get('structuralPattern', { })blueprint_sections = ReferencePrompts._build_blueprint_prompt_sections(analysis)blueprint = blueprint_sections.get('blueprint', { })style_profile = blueprint.get('styleProfile', { }) if isinstance(blueprint, dict) else { }structure_profile = blueprint.get('structureProfile', { }) if isinstance(blueprint, dict) else { }hook_profile = blueprint.get('hookProfile', { }) if isinstance(blueprint, dict) else { }anti_transfer = blueprint.get('antiTransfer', { }) if isinstance(blueprint, dict) else { }content_priority = ReferencePrompts._build_content_source_priority_section(selected_title = selected_title, synopsis = synopsis, topic_direction = topic_direction)alignment_feedback_section = ReferencePrompts._build_alignment_feedback_section(alignment_feedback)detected_tone = analysis.get('detectedTone', { })intensity_instructions = {
'strict': '## 패턴 적용 강도: 엄격 (Strict)\n레퍼런스의 구조와 패턴을 **최대한 그대로** 따르세요.\n- 섹션 비율을 정확히 맞추세요\n- 후킹 요소를 거의 동일한 방식으로 사용하세요\n- 전환 문구 스타일을 그대로 적용하세요',
'moderate': '## 패턴 적용 강도: 적당 (Moderate)\n레퍼런스의 **핵심 패턴은 유지**하되, 내용에 맞게 조정하세요.\n- 섹션 비율은 ±5% 범위에서 조정 가능\n- 후킹 요소의 유형은 유지하되 내용은 새롭게\n- 전환 스타일은 참고하되 자연스럽게 변형',
'loose': '## 패턴 적용 강도: 느슨 (Loose)\n레퍼런스를 **참고만** 하고 창의적으로 변형하세요.\n- 전체적인 구조 흐름만 참고\n- 후킹 요소는 새로운 방식으로 시도\n- 자신만의 스타일로 재해석' }intensity_text = intensity_instructions.get(pattern_intensity, intensity_instructions['moderate'])intro = structural.get('introduction', { })dev = structural.get('development', { })climax = structural.get('climax', { })conclusion = structural.get('conclusion', { })section_ratios = structure_profile.get('sectionRatios', { }) if isinstance(structure_profile, dict) else { }execution_lines = []execution_lines.append(f'''- 구조 비율: 도입 {section_ratios.get('introduction', intro.get('ratio', 15))}% / 전개 {section_ratios.get('development', dev.get('ratio', 50))}% / 절정 {section_ratios.get('climax', climax.get('ratio', 20))}% / 결론 {section_ratios.get('conclusion', conclusion.get('ratio', 15))}%''')if structure_profile.get('openingMode'):
execution_lines.append(f'''- 오프닝 방식: {structure_profile.get('openingMode')}''')if structure_profile.get('openingHooks'):
execution_lines.append(f'''- 오프닝 훅 패턴: {', '.join(structure_profile.get('openingHooks', [])[:4])}''')if structure_profile.get('transitionPatterns'):
execution_lines.append(f'''- 전환 패턴: {', '.join(structure_profile.get('transitionPatterns', [])[:5])}''')if structure_profile.get('closingMode'):
execution_lines.append(f'''- 마무리 방식: {structure_profile.get('closingMode')}''')if structure_profile.get('chapterStrategy'):
execution_lines.append(f'''- 챕터 전략: {structure_profile.get('chapterStrategy')}''')if hook_profile.get('openingHookType'):
execution_lines.append(f'''- 오프닝 훅 타입: {hook_profile.get('openingHookType')}''')if hook_profile.get('midHookTypes'):
execution_lines.append(f'''- 중반 훅 타입: {', '.join(hook_profile.get('midHookTypes', [])[:4])}''')if hook_profile.get('retentionDevices'):
execution_lines.append(f'''- 리텐션 장치: {', '.join(hook_profile.get('retentionDevices', [])[:6])}''')pattern_execution_text = '### 레퍼런스 실행 패턴\n' + '\n'.join(execution_lines)tone_guidance = ''if detected_tone:
primary_tone = detected_tone.get('primary', '')formality = detected_tone.get('formality', '')emotion = detected_tone.get('emotion', '')description = detected_tone.get('description', '')if primary_tone:
tone_guidance = '\n### 7. 톤 가이드 (v2)\n'tone_guidance += f'''**레퍼런스 톤: {primary_tone}**\n'''if description:
tone_guidance += f'''- {description}\n'''if formality:
formality_labels = {
'formal': '격식체',
'casual': '비격식체',
'mixed': '혼합' }tone_guidance += f'''- 격식: {formality_labels.get(formality, formality)}\n'''if emotion:
emotion_labels = {
'neutral': '중립적',
'dramatic': '드라마틱하게',
'informative': '정보 전달 중심',
'humorous': '유머러스하게' }tone_guidance += f'''- 감정 톤: {emotion_labels.get(emotion, emotion)}\n'''if primary_tone == '다채로운 문체':
tone_guidance += '- 다채로운 문체 규칙: 사건의 뼈대(진행/동작/팩트)는 ~습니다, 사건의 살(묘사/감정/여운)은 ~지요를 사용하세요.\n'tone_guidance += '- 한 줄씩 기계적으로 번갈아 쓰지 말고 문장 역할에 따라 선택하세요.\n'tone_guidance += '\n⚠️ **레퍼런스 톤 우선 적용!** 위 분석된 톤/문체를 **반드시 따르세요**.\n'tone_guidance += '레퍼런스의 말투, 어미, 화법을 그대로 사용하세요. 사용자 지정 톤은 무시합니다.\n'format_info = ReferencePrompts._detect_content_format(analysis)blueprint_narration_mode = style_profile.get('narrationMode', '')if not blueprint_narration_mode == 'indirect':
is_informational = format_info.get('use_indirect_speech', False)content_format = 'informational' if is_informational else 'reference'is_reference = content_format == 'reference'if not bool(style_profile):
has_reference_data = format_info.get('has_reference_data', False)if not style_profile.get('primaryTone', ''):
ref_tone_from_analysis = format_info.get('tone', '')tone_styles = {
'소설체': '~했다 (소설체, 감정 몰입과 서사가 풍부한 문학적 문체)',
'극적체': '~했다 (극적체, 드라마틱하고 긴장감 있는 강렬한 문체)',
'친근체': '~했어요 (친근체, 부드럽고 대화하듯 친근한 문체)',
'설명체': '~했습니다 (설명체, 객관적이고 정보 전달 중심의 문체)',
'담담체': '~했다 (담담체, 감정 절제된 차분하고 건조한 문체)',
'유머체': '~했다/~했어요 (유머체, 위트 있고 가볍게 풀어가는 재미있는 문체)',
'감성체': '~했다 (감성체, 서정적이고 감정을 섬세하게 표현하는 문체)',
'다큐체': '~했습니다 (다큐체, 사실 기반의 객관적인 다큐멘터리 문체)',
'다채로운 문체': '~습니다/~지요 (다채로운 문체, 진행/팩트는 ~습니다, 묘사/여운은 ~지요)',
'구어체': '~거든요, ~잖아요 (구어체, 실제 대화하듯 자연스럽고 친숙한 말투)',
'대화체': '~할게요, ~하는데요 (대화체, 청자와 대화하듯 친밀한 톤)' }effective_tone = ref_tone_from_analysis if ref_tone_from_analysis else tonetone_desc = tone_styles.get(effective_tone, f'''{effective_tone} (레퍼런스 분석 톤)''')tone_example_line = {
'소설체': '상황이 전개되고 있었다. 분위기는 점점 긴장감으로 가득 차올랐고, 모두가 숨을 죽이고 있었다.',
'극적체': '상황이 전개되고 있었다! 분위기는 점점 긴장감으로 가득 차올랐다!',
'친근체': '상황이 전개되고 있었어요. 분위기가 점점 긴장감으로 가득 차올랐어요.',
'설명체': '상황이 전개되고 있었습니다. 분위기는 점점 긴장감으로 가득 차올랐습니다.',
'담담체': '상황이 전개되고 있었다. 분위기는 점점 긴장감으로 가득 차올랐다.',
'유머체': '상황이 전개되고 있었다. 분위기가 점점 긴장감으로 가득 차올랐다.',
'감성체': '상황이 전개되고 있었다. 분위기는 점점 긴장감으로 가득 차올랐다.',
'다큐체': '상황이 전개되고 있었습니다. 분위기는 점점 긴장감으로 가득 차올랐습니다.',
'다채로운 문체': '상황이 전개되고 있습니다. 분위기가 점점 조여 오고 있지요. 모두가 숨을 죽인 채 결과를 기다리고 있습니다.',
'구어체': '상황이 전개되고 있거든요. 분위기가 점점 긴장감으로 가득 차올랐잖아요.',
'대화체': '상황이 전개되고 있는데요. 분위기가 점점 긴장감으로 가득 차오르고 있어요.' }full_text = analysis.get('fullText', '')example_narration = tone_example_line.get(effective_tone, tone_example_line.get(tone, tone_example_line['소설체']))if not style_profile.get('contentStyle', ''):
ref_style = format_info.get('style', '')ref_primary = format_info.get('primary', '')ref_secondary = format_info.get('secondary', '')if not style_profile.get('primaryTone', ''):
ref_tone = format_info.get('tone', '')if not style_profile.get('emotion', ''):
ref_emotion = format_info.get('emotion', '')if not style_profile.get('toneDescription', ''):
ref_tone_description = format_info.get('tone_description', '')use_indirect_speech = is_informationalsentence_endings_profile = style_profile.get('sentenceEndings', { }) if isinstance(style_profile, dict) else { }opening_mode = structure_profile.get('openingMode', '')# WARNING: Decompyle incomplete
)()
    get_pattern_intensity_description = (lambda intensity = None: descriptions = {
'strict': '레퍼런스 패턴을 최대한 그대로 적용합니다. 검증된 구조를 정확히 따릅니다.',
'moderate': '핵심 패턴은 유지하면서 내용에 맞게 자연스럽게 조정합니다. (권장)',
'loose': '레퍼런스를 참고만 하고 창의적으로 변형합니다. 새로운 시도에 적합합니다.' }descriptions.get(intensity, descriptions['moderate']))()
