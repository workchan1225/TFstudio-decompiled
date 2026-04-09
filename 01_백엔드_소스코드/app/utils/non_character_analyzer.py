# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: non_character_analyzer.pyc (Python 3.11)

'''
Non-Character Content Analyzer - 비캐릭터 콘텐츠 고급 분석기

정보성 콘텐츠(info, documentary, news)를 위한 다차원 분석:
- 구조 분석: 단계/타임라인/비교/인용 등
- 시각 유형: 데이터/개념/위치/감정/객체
- 데이터 존재: 숫자/통계/퍼센트
- 감정 톤: 긍정/부정/영감/경고
- 장면 위치: 인트로/본론/아웃트로

다중 템플릿 조합 추천 지원
'''
from typing import Dict, List, Optional, Tuple, TypedDict
from enum import Enum

class StructureType(Enum, str):
    '''콘텐츠 구조 유형'''
    PROCESS = 'process'
    TIMELINE = 'timeline'
    COMPARISON = 'comparison'
    LIST = 'list'
    QUOTE = 'quote'
    NARRATIVE = 'narrative'
    HIERARCHICAL = 'hierarchical'
    CAUSE_EFFECT = 'cause_effect'


class VisualType(Enum, str):
    '''시각화 유형'''
    DATA = 'data'
    CONCEPT = 'concept'
    LOCATION = 'location'
    EMOTION = 'emotion'
    OBJECT = 'object'
    PERSON_HISTORICAL = 'person_historical'
    SYSTEM = 'system'
    TRANSFORMATION = 'transformation'


class EmotionalTone(Enum, str):
    '''감정 톤'''
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    NEUTRAL = 'neutral'
    INSPIRING = 'inspiring'
    CAUTIONARY = 'cautionary'
    REFLECTIVE = 'reflective'


class ScenePosition(Enum, str):
    '''장면 위치'''
    INTRO = 'intro'
    BODY = 'body'
    CONCLUSION = 'conclusion'
    TRANSITION = 'transition'


def ContentAnalysisResult():
    '''ContentAnalysisResult'''
    dynamic_prompt_ko: str = '콘텐츠 분석 결과'

ContentAnalysisResult = <NODE:27>(ContentAnalysisResult, 'ContentAnalysisResult', TypedDict, total = False)
STRUCTURE_KEYWORDS: Dict[(str, List[str])] = {
    StructureType.CAUSE_EFFECT: [
        '때문에',
        '그래서',
        '따라서',
        '결과적으로',
        '결국',
        '원인',
        '결과',
        '영향',
        '효과',
        '이유',
        '왜냐하면',
        '그 이유는',
        '덕분에',
        '탓에'],
    StructureType.HIERARCHICAL: [
        '상위',
        '하위',
        '분류',
        '카테고리',
        '범주',
        '대분류',
        '소분류',
        '가지',
        '갈래',
        '종류',
        '체계',
        '구조',
        '계층',
        '레벨'],
    StructureType.LIST: [
        '그리고',
        '또한',
        '더불어',
        '게다가',
        '뿐만 아니라',
        '하나',
        '둘',
        '셋',
        '여러 가지',
        '다양한',
        '첫째로',
        '둘째로',
        '셋째로'],
    StructureType.QUOTE: [
        '라고 말했다',
        '이렇게 말했습니다',
        '명언',
        '격언',
        '속담',
        '말을 남겼다',
        '인용하면',
        '"',
        "'",
        '『',
        '「',
        '」',
        '』'],
    StructureType.COMPARISON: [
        '반면',
        '반대로',
        '비교하면',
        '차이점',
        '공통점',
        'vs',
        'VS',
        '대비',
        '비해',
        '보다',
        '한편',
        '다른 한편',
        '이와 달리',
        '장점',
        '단점',
        '좋은 점',
        '나쁜 점',
        '전자',
        '후자',
        'A와 B'],
    StructureType.TIMELINE: [
        '년',
        '월',
        '일',
        '세기',
        '시대',
        '그 후',
        '이전에',
        '이후에',
        '그때',
        '당시',
        '처음에는',
        '나중에',
        '결국',
        '마침내',
        '역사',
        '연대기',
        '시작',
        '시초',
        '기원',
        '과거',
        '현재',
        '미래',
        '전',
        '후'],
    StructureType.PROCESS: [
        '첫째',
        '둘째',
        '셋째',
        '넷째',
        '다섯째',
        '1단계',
        '2단계',
        '3단계',
        '4단계',
        '5단계',
        '첫 번째',
        '두 번째',
        '세 번째',
        '네 번째',
        '다섯 번째',
        '먼저',
        '다음으로',
        '그 다음',
        '마지막으로',
        '최종적으로',
        '방법은',
        '순서는',
        '절차는',
        '과정은',
        '단계는',
        'step',
        '스텝',
        '프로세스',
        '워크플로우'] }
VISUAL_KEYWORDS: Dict[(str, List[str])] = {
    VisualType.TRANSFORMATION: [
        '변화',
        '변환',
        '전환',
        '개선',
        '발전',
        '성장',
        '진화',
        '혁신',
        '개혁',
        '혁명',
        '전',
        '후',
        '이전',
        '이후',
        '달라졌다'],
    VisualType.SYSTEM: [
        '시스템',
        '구조',
        '체계',
        '메커니즘',
        '프로세스',
        '작동',
        '원리',
        '방식',
        '기술',
        '과학',
        '뇌',
        '신경',
        '회로',
        '네트워크'],
    VisualType.PERSON_HISTORICAL: [
        '인물',
        '위인',
        '영웅',
        '지도자',
        '대통령',
        '왕',
        '황제',
        '장군',
        '학자',
        '과학자',
        '그는',
        '그녀는',
        '그의',
        '그녀의'],
    VisualType.OBJECT: [
        '제품',
        '물건',
        '상품',
        '아이템',
        '도구',
        '기기',
        '장비',
        '소품',
        '물품',
        '용품',
        '구매',
        '판매',
        '가격',
        '비용'],
    VisualType.EMOTION: [
        '감정',
        '느낌',
        '마음',
        '기분',
        '정서',
        '행복',
        '슬픔',
        '기쁨',
        '분노',
        '두려움',
        '사랑',
        '희망',
        '절망',
        '불안',
        '평화'],
    VisualType.LOCATION: [
        '장소',
        '위치',
        '지역',
        '국가',
        '도시',
        '나라',
        '대륙',
        '지도',
        '거리',
        '길',
        '어디',
        '곳',
        '현장',
        '지점',
        '구역'],
    VisualType.CONCEPT: [
        '개념',
        '원리',
        '원칙',
        '이론',
        '법칙',
        '철학',
        '사상',
        '관점',
        '시각',
        '패러다임',
        '아이디어',
        '생각',
        '의미',
        '가치',
        '본질'],
    VisualType.DATA: [
        '퍼센트',
        '%',
        '숫자',
        '통계',
        '데이터',
        '수치',
        '그래프',
        '차트',
        '증가',
        '감소',
        '비율',
        '평균',
        '최대',
        '최소',
        '합계',
        '분석',
        '조사',
        '연구 결과',
        '설문'] }
TONE_KEYWORDS: Dict[(str, List[str])] = {
    EmotionalTone.REFLECTIVE: [
        '생각해보면',
        '돌아보면',
        '깊이',
        '의미',
        '교훈',
        '깨달음',
        '성찰',
        '반성',
        '숙고'],
    EmotionalTone.CAUTIONARY: [
        '주의',
        '경고',
        '조심',
        '위험',
        '피해야',
        '절대',
        '금지',
        '삼가',
        '반드시',
        '꼭',
        '하지 마',
        '조심해야',
        '유의'],
    EmotionalTone.INSPIRING: [
        '감동',
        '영감',
        '동기',
        '도전',
        '꿈',
        '열정',
        '노력',
        '극복',
        '승리',
        '기적',
        '용기',
        '결심',
        '의지'],
    EmotionalTone.NEGATIVE: [
        '실패',
        '문제',
        '위기',
        '위험',
        '손해',
        '나쁜',
        '심각한',
        '최악',
        '끔찍한',
        '하락',
        '감소',
        '악화',
        '붕괴'],
    EmotionalTone.POSITIVE: [
        '성공',
        '달성',
        '성취',
        '희망',
        '기회',
        '좋은',
        '훌륭한',
        '최고',
        '완벽',
        '멋진',
        '발전',
        '성장',
        '향상',
        '개선'] }
POSITION_KEYWORDS: Dict[(str, List[str])] = {
    ScenePosition.TRANSITION: [
        '자, 그럼',
        '이제',
        '다음으로',
        '여기서',
        '그렇다면',
        '한편',
        '그런데'],
    ScenePosition.CONCLUSION: [
        '결론',
        '정리하면',
        '요약하면',
        '마무리',
        '기억하세요',
        '잊지 마세요',
        '마지막으로',
        '핵심은',
        '중요한 것은',
        '결국',
        '끝으로'],
    ScenePosition.INTRO: [
        '오늘은',
        '지금부터',
        '이번에는',
        '소개',
        '시작',
        '먼저',
        '우선',
        '첫 번째로',
        '안녕하세요',
        '여러분',
        '궁금하시죠'] }
STRUCTURE_TO_TEMPLATE: Dict[(str, str)] = {
    StructureType.NARRATIVE: 'Text Overlay Background',
    StructureType.CAUSE_EFFECT: 'Technical Diagram',
    StructureType.HIERARCHICAL: 'Mindmap Hierarchy',
    StructureType.LIST: 'Infographic Base',
    StructureType.QUOTE: 'Quote Highlight',
    StructureType.COMPARISON: 'Comparison Split',
    StructureType.TIMELINE: 'Timeline Sequence',
    StructureType.PROCESS: 'Process Steps' }
VISUAL_TO_TEMPLATE: Dict[(str, str)] = {
    VisualType.TRANSFORMATION: 'Before After',
    VisualType.SYSTEM: 'Technical Diagram',
    VisualType.PERSON_HISTORICAL: 'Timeline Sequence',
    VisualType.OBJECT: 'Product Showcase',
    VisualType.EMOTION: 'Metaphor Visual',
    VisualType.LOCATION: 'Location Map',
    VisualType.CONCEPT: 'Abstract Concept',
    VisualType.DATA: 'Statistics Chart' }
GENRE_TO_NON_CHARACTER_TEMPLATES: Dict[(str, List[Tuple[(str, float)]])] = {
    'LIFE_KNOWLEDGE': [
        ('Process Steps', 0.9),
        ('Quote Highlight', 0.7),
        ('Infographic Base', 0.6)],
    'OFFICE_SURVIVAL': [
        ('Process Steps', 0.9),
        ('Comparison Split', 0.7),
        ('Mindmap Hierarchy', 0.6)],
    'MONEY_SENSE': [
        ('Statistics Chart', 0.9),
        ('Before After', 0.8),
        ('Comparison Split', 0.7)],
    'RELATIONSHIP_EQ': [
        ('Metaphor Visual', 0.9),
        ('Quote Highlight', 0.8),
        ('Abstract Concept', 0.6)],
    'PSYCHOLOGY': [
        ('Technical Diagram', 0.9),
        ('Metaphor Visual', 0.8),
        ('Mindmap Hierarchy', 0.7)],
    'LIFE_CHOICES': [
        ('Mindmap Hierarchy', 0.9),
        ('Comparison Split', 0.8),
        ('Metaphor Visual', 0.7)],
    'KNOWLEDGE_BITE': [
        ('Technical Diagram', 0.9),
        ('Infographic Base', 0.8),
        ('Timeline Sequence', 0.6)],
    'TRUE_STORY': [
        ('Timeline Sequence', 0.9),
        ('Location Map', 0.8),
        ('Quote Highlight', 0.6)],
    'DOCUMENTARY': [
        ('Statistics Chart', 0.9),
        ('Timeline Sequence', 0.8),
        ('Location Map', 0.7)],
    'NEWS_REPORT': [
        ('News Report', 0.95),
        ('Statistics Chart', 0.8),
        ('Location Map', 0.7)],
    'REVIEW_ANALYSIS': [
        ('Comparison Split', 0.9),
        ('Product Showcase', 0.8),
        ('Statistics Chart', 0.7)],
    'VARIETY': [
        ('Text Overlay Background', 0.8),
        ('Abstract Concept', 0.6)],
    'HYBRID': [
        ('Infographic Base', 0.8),
        ('Quote Highlight', 0.7),
        ('Process Steps', 0.6)] }

class NonCharacterContentAnalyzer:
    '''비캐릭터 콘텐츠 고급 분석기'''
    analyze = (lambda cls = None, narration = None, genre = classmethod, scene_index = (None, 0, 1), total_scenes = ('narration', str, 'genre', Optional[str], 'scene_index', int, 'total_scenes', int, 'return', ContentAnalysisResult): if not narration:
cls._get_default_result(genre)(structure_type, structure_conf) = None.detect_structure_type(narration)(visual_type, visual_conf) = cls.detect_visual_type(narration)(has_data, data_keywords) = cls.detect_data_presence(narration)emotional_tone = cls.detect_emotional_tone(narration)scene_position = cls.estimate_scene_position(narration, scene_index, total_scenes)templates = cls.recommend_templates(structure_type, structure_conf, visual_type, visual_conf, has_data, emotional_tone, scene_position, genre)primary = templates[0] if templates else ('Text Overlay Background', 0.5)secondary = templates[1] if len(templates) > 1 else Nonevisual_category = ''visual_category_confidence = 0extracted_keywords = []composition_hint = ''lighting_hint = ''color_hint = ''prompt_modifiers = ''dynamic_prompt_en = ''dynamic_prompt_ko = ''try:
InformationalSceneAnalyzer = InformationalSceneAnalyzerDynamicPromptBuilder = DynamicPromptBuilderimport informational_visualizerscene_analysis = InformationalSceneAnalyzer.analyze(narration = narration, genre = genre, scene_index = scene_index, total_scenes = total_scenes)visual_category = str(scene_analysis.get('primary_category', ''))visual_category_confidence = scene_analysis.get('confidence', 0)extracted_keywords = scene_analysis.get('extracted_keywords', [])composition_hint = str(scene_analysis.get('composition', ''))lighting_hint = str(scene_analysis.get('lighting', ''))color_hint = str(scene_analysis.get('color_palette', ''))prompt_modifiers = scene_analysis.get('prompt_modifiers', '')prompt_result = DynamicPromptBuilder.build_prompt(analysis_result = scene_analysis, narration = narration, scene_position = scene_position, aspect_ratio = '16:9')dynamic_prompt_en = prompt_result.get('prompt_en', '')dynamic_prompt_ko = prompt_result.get('prompt_ko', '')except ImportError:
e = Noneprint(f'''[NonCharacterContentAnalyzer] InformationalSceneAnalyzer import failed: {e}''')e = Nonedel eexcept Exception:
e = Noneprint(f'''[NonCharacterContentAnalyzer] Dynamic analysis error: {e}''')e = Nonedel eexcept:
e = Nonedel e# WARNING: Decompyle incomplete
)()
    detect_structure_type = (lambda cls = None, narration = None: pass# WARNING: Decompyle incomplete
)()
    detect_visual_type = (lambda cls = None, narration = None: pass# WARNING: Decompyle incomplete
)()
    detect_data_presence = (lambda cls = None, narration = None: import redata_keywords_found = []number_pattern = '\\d+(?:\\.\\d+)?(?:%|퍼센트|개|명|원|달러|만|억|조)?'numbers = re.findall(number_pattern, narration)if numbers:
data_keywords_found.extend(numbers[:5])for kw in VISUAL_KEYWORDS[VisualType.DATA]:
if kw in narration:
data_keywords_found.append(kw)has_data = len(data_keywords_found) > 0(has_data, data_keywords_found[:10]))()
    detect_emotional_tone = (lambda cls = None, narration = None: pass# WARNING: Decompyle incomplete
)()
    estimate_scene_position = (lambda cls = None, narration = None, scene_index = classmethod, total_scenes = ('narration', str, 'scene_index', int, 'total_scenes', int, 'return', str): pass# WARNING: Decompyle incomplete
)()
    recommend_templates = (lambda cls, structure_type, structure_conf, visual_type, visual_conf, has_data = None, emotional_tone = None, scene_position = classmethod, genre = ('structure_type', str, 'structure_conf', float, 'visual_type', str, 'visual_conf', float, 'has_data', bool, 'emotional_tone', str, 'scene_position', str, 'genre', Optional[str], 'return', List[Tuple[(str, float)]]): candidates = { }if structure_conf > 0.5:
struct_template = STRUCTURE_TO_TEMPLATE.get(structure_type)if struct_template:
candidates[struct_template] = structure_conf * 0.9if visual_conf > 0.4:
vis_template = VISUAL_TO_TEMPLATE.get(visual_type)if vis_template:
existing = candidates.get(vis_template, 0)candidates[vis_template] = max(existing, visual_conf * 0.7)if has_data:
existing = candidates.get('Statistics Chart', 0)candidates['Statistics Chart'] = max(existing, 0.6)if genre and genre in GENRE_TO_NON_CHARACTER_TEMPLATES:
for template, conf in GENRE_TO_NON_CHARACTER_TEMPLATES[genre]:
existing = candidates.get(template, 0)candidates[template] = max(existing, conf * 0.5)if scene_position == ScenePosition.INTRO:
existing = candidates.get('Text Overlay Background', 0)candidates['Text Overlay Background'] = max(existing, 0.4)elif scene_position == ScenePosition.CONCLUSION:
existing = candidates.get('Quote Highlight', 0)candidates['Quote Highlight'] = max(existing, 0.4)if emotional_tone == EmotionalTone.INSPIRING:
existing = candidates.get('Quote Highlight', 0)candidates['Quote Highlight'] = max(existing, 0.5)elif emotional_tone == EmotionalTone.CAUTIONARY:
existing = candidates.get('News Report', 0)candidates['News Report'] = max(existing, 0.4)sorted_templates = sorted(candidates.items(), key = (lambda x: x[1]), reverse = True)
        if not sorted_templates:
            sorted_templates = [
                ('Text Overlay Background', 0.5)]
        return sorted_templates[:3]
)()
    _get_default_result = (lambda cls = None, genre = None: default_template = 'Text Overlay Background'if genre and genre in GENRE_TO_NON_CHARACTER_TEMPLATES:
templates = GENRE_TO_NON_CHARACTER_TEMPLATES[genre]default_template = templates[0][0]ContentAnalysisResult(structure_type = StructureType.NARRATIVE, structure_confidence = 0.5, visual_type = VisualType.CONCEPT, visual_confidence = 0.5, has_data = False, data_keywords = [], emotional_tone = EmotionalTone.NEUTRAL, scene_position = ScenePosition.BODY, recommended_templates = [
{
'name': default_template,
'confidence': 0.5 }], primary_template = default_template, secondary_template = None, combined_confidence = 0.5))()
    get_combined_template_ids = (lambda cls = None, analysis_result = None, template_cache = classmethod: template_ids = []nc_cache = template_cache.get('non_character', { })primary = analysis_result.get('primary_template')if primary and primary in nc_cache:
template_ids.append(nc_cache[primary])secondary = analysis_result.get('secondary_template')if secondary and secondary in nc_cache:
for rec in analysis_result.get('recommended_templates', []):
if rec['name'] == secondary and rec['confidence'] >= 0.6:
template_ids.append(nc_cache[secondary])template_ids)()


def analyze_non_character_content(narration = None, genre = None, scene_index = None, total_scenes = (None, 0, 1)):
    '''비캐릭터 콘텐츠 분석 (편의 함수)'''
    return NonCharacterContentAnalyzer.analyze(narration = narration, genre = genre, scene_index = scene_index, total_scenes = total_scenes)
