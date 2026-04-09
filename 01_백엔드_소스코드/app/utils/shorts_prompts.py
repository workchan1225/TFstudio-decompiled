# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shorts_prompts.pyc (Python 3.11)

__doc__ = '\n쇼츠(Shorts) 전용 프롬프트 시스템\n\n쇼츠 콘텐츠의 특징:\n- 1-3분 길이 (200-700자)\n- 강력한 후킹 (첫 3초 안에 시선 사로잡기)\n- 빠른 전개 + 서사 구조\n- 대사 중심 (80% 이상)\n- 일관성 유지\n'
from typing import Optional, List, Dict
from app.utils.narration_style_guide import TONE_FORBIDDEN_ENDINGS, TONE_REQUIRED_ENDINGS
from app.services.prompt.constraints.character_enforcer import CharacterEnforcer
from app.services.prompt.constraints.human_touch_enforcer import GENRE_TO_STYLE, HumanTouchStyle, STYLE_TEMPLATES
from app.utils.long_script_prompts import DRAMA_STORYTELLING_ELEMENTS, INFO_STORYTELLING_ELEMENTS, ALL_STORYTELLING_ELEMENTS, GENRE_STORYTELLING_COMBINATION
from app.utils.genre_categories import get_genre_category
DIALOGUE_START_GENRES = [
    'DRAMATIC',
    'REVENGE',
    'MYSTERY',
    'JOSEON_FOLKTALE',
    'HEARTWARMING',
    'HISTORICAL',
    'THRILLER',
    'HORROR',
    'ROMANCE',
    'ACTION',
    'WAR_MILITARY',
    'YOUTH_DRAMA',
    'REAL_LIFE',
    'TRUE_STORY']
NARRATION_START_GENRES = [
    'LIFE_KNOWLEDGE',
    'OFFICE_SURVIVAL',
    'MONEY_SENSE',
    'RELATIONSHIP_EQ',
    'PSYCHOLOGY',
    'LIFE_CHOICES',
    'KNOWLEDGE_BITE',
    'SCIENCE',
    'SPACE',
    'NATURAL_DISASTER',
    'SOCIAL_ISSUES',
    'SOCIAL_ISSUE',
    'NEWS_REPORT',
    'REVIEW_ANALYSIS',
    'INFORMATIONAL',
    'ENCYCLOPEDIA',
    'LIFE_TIPS',
    'LIFE_LESSONS',
    'HEALTH',
    'FINANCE',
    'TECH',
    'ECONOMY',
    'CURRENT_AFFAIRS',
    'INTERNATIONAL',
    'POLITICS',
    'DOCUMENTARY',
    'BIOGRAPHY',
    'SOCIAL_ISSUE']
SHORTS_TONE_EXAMPLES = {
    '소설체': [
        '"그의 눈이 흔들렸다. 진실이 드러나는 순간이었다."',
        '"차가운 바람이 뺨을 스쳤다. 모든 것이 끝나가고 있었다."',
        '"그녀는 돌아서지 않았다. 다시는."'],
    '극적체': [
        '"거짓말이야!" 그녀가 소리쳤다. 모든 게 무너지는 순간이었다!',
        '"시간이 없어!" 그가 뛰기 시작했다!',
        '"바로 그 순간! 모든 것이 뒤집혔다!"'],
    '친근체': [
        '"근데 있잖아요, 그날 진짜 이상한 일이 있었어요."',
        '"그래서요, 결국 어떻게 됐냐면요... 대박이었죠."',
        '"진짜 믿기 어렵죠? 저도 처음엔 못 믿었어요."'],
    '설명체': [
        '"이것이 바로 핵심입니다. 많은 사람들이 모르는 사실입니다."',
        '"그때, 상황이 급변했습니다. 예상치 못한 일이 벌어진 것입니다."',
        '"결론적으로, 이 선택이 모든 것을 바꾸게 됩니다."'],
    '담담체': [
        '"그는 떠났다. 아무도 막지 않았다."',
        '"문이 닫혔다. 그것뿐이었다."',
        '"아무 일도 없었다. 처음부터."'],
    '유머체': [
        '"완벽했다. 진짜 완벽했다. 망할 때까지는."',
        '"계획대로였다. 아, 물론 실패할 계획."',
        '"인생이 뭐 있나요. 그냥 웃기게 살죠."'],
    '감성체': [
        '"그 순간, 시간이 멈춘 것 같았다. 그녀의 눈물이 볼을 타고 흘렀다."',
        '"바람이 불어왔다. 마치 그를 데려가려는 것처럼."',
        '"어디선가 익숙한 노래가 들려왔다. 가슴이 먹먹해졌다."'],
    '다큐체': [
        '"2024년 1월, 충격적인 사건이 발생했습니다."',
        '"이 순간이 역사를 바꾸게 됩니다. 전문가들은 이렇게 분석합니다."',
        '"당시 현장에 있던 사람들의 증언입니다."'],
    '다채로운 문체': [
        '"상황이 빠르게 전개되고 있습니다. 그 짧은 침묵이 유난히 길게 느껴지지요."',
        '"핵심 사실은 분명합니다. 그런데 그 한 문장이 마음에 오래 남지요."',
        '"결정은 이미 내려졌습니다. 모두가 그 의미를 조용히 받아들이고 있지요."'] }
SHORTS_TONE_STYLES = {
    '소설체': {
        'style': '문학적이고 감각적인 표현',
        'ending': '~했다, ~였다',
        'example': '그의 눈이 흔들렸다. 진실이 드러나는 순간이었다.',
        'instruction': '짧지만 묘사가 살아있는 문장. 감정의 결을 담아라.' },
    '극적체': {
        'style': '긴장감 넘치는 강렬한 문장',
        'ending': '~했다, ~였다',
        'example': '"거짓말이야!" 그녀가 소리쳤다. 모든 게 무너지는 순간이었다.',
        'instruction': '짧고 강렬하게. 대사에 힘을 실어라.' },
    '친근체': {
        'style': '대화하듯 편안한 톤',
        'ending': '~했어요, ~죠, ~거든요',
        'example': '근데 있잖아요, 그날 진짜 이상한 일이 있었어요.',
        'instruction': '친구에게 이야기하듯. 공감을 이끌어내라.' },
    '설명체': {
        'style': '객관적이고 명확한 정보 전달',
        'ending': '~합니다, ~입니다',
        'example': '이것이 바로 핵심입니다. 많은 사람들이 모르는 사실이죠.',
        'instruction': '핵심만 간결하게. 정보를 명확히 전달하라.' },
    '담담체': {
        'style': '감정 절제된 건조한 문체',
        'ending': '~했다, ~였다',
        'example': '그는 떠났다. 아무도 막지 않았다.',
        'instruction': '감정을 억제할수록 오히려 강렬해진다.' },
    '유머체': {
        'style': '위트 있고 가벼운 톤',
        'ending': '~했다, ~했어요 (혼용)',
        'example': '완벽했다. 진짜 완벽했다. 망할 때까지는.',
        'instruction': '반전과 타이밍. 펀치라인을 살려라.' },
    '감성체': {
        'style': '서정적이고 감정이 살아있는 문체',
        'ending': '~했다, ~였다',
        'example': '그 순간, 시간이 멈춘 것 같았다. 그녀의 눈물이 볼을 타고 흘렀다.',
        'instruction': '감정의 순간을 포착하라. 여운을 남겨라.' },
    '다큐체': {
        'style': '사실 기반의 객관적 진술',
        'ending': '~했습니다, ~입니다',
        'example': '2024년 1월, 충격적인 사건이 발생했습니다.',
        'instruction': '팩트 중심. 신뢰감을 주는 톤으로.' },
    '다채로운 문체': {
        'style': '문장 역할에 따라 타격감과 여운을 병행하는 문체',
        'ending': '~습니다 (뼈대), ~지요 (살)',
        'example': '결정은 이미 내려졌습니다. 그 결말이 왜 이렇게 먹먹한지, 다들 느끼고 있지요.',
        'instruction': '한 줄 교대가 아니라 문장 역할로 선택. 진행/팩트는 ~습니다, 묘사/감정은 ~지요.' } }

def get_shorts_tone_style(tone = None):
    '''
    톤에 맞는 쇼츠 스타일 지침 반환 (강화 버전)

    금지/필수 어미 규칙 + 구체적 예시 + 혼용 금지 경고 포함
    '''
    tone_data = SHORTS_TONE_STYLES.get(tone, SHORTS_TONE_STYLES['소설체'])
    required = TONE_REQUIRED_ENDINGS.get(tone, TONE_REQUIRED_ENDINGS.get('소설체', [
        '했다',
        '였다']))
    forbidden = TONE_FORBIDDEN_ENDINGS.get(tone, [])
    examples = SHORTS_TONE_EXAMPLES.get(tone, [
        tone_data['example']])
    examples_str = (lambda .0: [ f'''  {ex}''' for ex in .0 ])(examples[:3]())
    required_str = (lambda .0: [ f'''~{e}''' for e in .0 ])(required[:5]())
    forbidden_str = (lambda .0: [ f'''~{e}''' for e in .0 ])(forbidden[:5]()) if forbidden else '없음'
    return f'''**★★★ 선택된 톤: {tone} ★★★** (모든 나레이션에 적용!)\n\n**스타일**: {tone_data['style']}\n**적용법**: {tone_data['instruction']}\n\n**{tone} 나레이션 예시**:\n{examples_str}\n\n**✅ 필수 어미** (나레이션에서 반드시 사용):\n  {required_str}\n\n**❌ 금지 어미** (절대 사용 금지!):\n  {forbidden_str}\n\n{mixing_rule}\n\n{final_check}'''

SHORTS_CONFIG = {
    '1min': {
        'target_length': 420,
        'chapter_count': 1,
        'narration_ratio': 25,
        'structure': '후킹(5%) → 인트로5턴(30%) → 갈등(35%) → 반전결말(30%)',
        'description': '단일 갈등, 빠른 반전. 여운 있는 마무리.',
        'intro_turns': 5,
        'min_length': 350,
        'max_length': 490 },
    '2min': {
        'target_length': 840,
        'chapter_count': 1,
        'narration_ratio': 30,
        'structure': '후킹(5%) → 인트로5턴(20%) → 갈등전개(35%) → 위기(20%) → 반전결말(20%)',
        'description': '갈등 심화 → 위기 → 반전. 감정의 롤러코스터.',
        'intro_turns': 5,
        'min_length': 700,
        'max_length': 980 },
    '3min': {
        'target_length': 1260,
        'chapter_count': 2,
        'narration_ratio': 35,
        'structure': '후킹(5%) → 인트로5턴(15%) → 갈등(25%) → 위기(20%) → 클라이맥스(20%) → 결말(15%)',
        'description': '완전한 서사 구조. 캐릭터 성장 가능.',
        'intro_turns': 5,
        'min_length': 1050,
        'max_length': 1450 } }
HOOKING_PATTERNS = {
    'question': {
        'name': '충격적 질문',
        'description': '시청자의 호기심을 자극하는 질문',
        'examples': [
            '"죽기 전에 딱 하루만 살 수 있다면?"',
            '"왜 아무도 이걸 말해주지 않았을까?"',
            '"진짜 사랑은 뭘까?"'],
        'best_for': [
            'HEARTWARMING',
            'MYSTERY',
            'INFORMATIONAL'] },
    'spoiler': {
        'name': '반전 스포일러',
        'description': '결말을 미리 언급하여 궁금증 유발',
        'examples': [
            '"그런데, 그 남자는 이미 죽어있었다."',
            '"결국 그녀는 모든 걸 버렸다."',
            '"그날이 마지막이 될 줄은 몰랐다."'],
        'best_for': [
            'DRAMATIC',
            'MYSTERY',
            'REVENGE'] },
    'emotion': {
        'name': '감정 폭발',
        'description': '강렬한 감정 표현으로 시작',
        'examples': [
            '"미쳤어! 진짜 미쳤어!"',
            '"너무 행복해서 눈물이 났다."',
            '"분노가 터져버렸다."'],
        'best_for': [
            'DRAMATIC',
            'REVENGE',
            'HEARTWARMING'] },
    'countdown': {
        'name': '카운트다운',
        'description': '시간적 긴장감 조성',
        'examples': [
            '"3초 후, 모든 게 바뀌었다."',
            '"1분. 그게 내게 주어진 전부였다."',
            '"10년 전 그날."'],
        'best_for': [
            'DRAMATIC',
            'MYSTERY',
            'ACTION'] },
    'provocation': {
        'name': '도발적 주장',
        'description': '논쟁적이거나 반전적인 주장',
        'examples': [
            '"솔직히 말할게, 다 거짓말이야."',
            '"사실 그건 잘못된 거야."',
            '"아무도 진실을 모른다."'],
        'best_for': [
            'INFORMATIONAL',
            'MYSTERY',
            'DRAMATIC'] },
    'secret': {
        'name': '비밀 폭로',
        'description': '숨겨진 정보를 공개하는 느낌',
        'examples': [
            '"아무도 모르는 진실이 있어."',
            '"이건 비밀인데..."',
            '"숨겨왔던 이야기를 할게."'],
        'best_for': [
            'MYSTERY',
            'DRAMATIC',
            'INFORMATIONAL'] },
    'emergency': {
        'name': '긴급 상황',
        'description': '급박한 상황으로 시작',
        'examples': [
            '"지금 당장 도망쳐!"',
            '"빨리! 시간이 없어!"',
            '"큰일났어. 진짜 큰일났어."'],
        'best_for': [
            'ACTION',
            'DRAMATIC',
            'MYSTERY'] },
    'paradox': {
        'name': '역설적 상황',
        'description': '모순적이거나 아이러니한 상황',
        'examples': [
            '"행복해서 울었다."',
            '"그녀를 사랑했기에 떠났다."',
            '"가장 가까운 사람이 적이었다."'],
        'best_for': [
            'HEARTWARMING',
            'DRAMATIC',
            'REVENGE'] },
    'direct': {
        'name': '직접 호출',
        'description': '시청자를 직접 부르는 형식',
        'examples': [
            '"너, 지금 이거 보고 있지?"',
            '"잠깐, 이건 꼭 들어봐."',
            '"네 얘기야. 바로 너."'],
        'best_for': [
            'INFORMATIONAL',
            'HEARTWARMING',
            'COMEDY'] },
    'mystery': {
        'name': '미스터리',
        'description': '의문점을 남기며 시작',
        'examples': [
            '"그날 밤, 뭔가 이상했다."',
            '"아직도 설명할 수 없는 일이 있다."',
            '"이상한 점을 발견했다."'],
        'best_for': [
            'MYSTERY',
            'DRAMATIC',
            'HORROR'] } }
# WARNING: Decompyle incomplete
