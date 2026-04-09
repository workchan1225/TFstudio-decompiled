# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: drama_genres.pyc (Python 3.11)

'''
Drama Genres - 드라마/스토리 계열 장르

드라마틱한 스토리텔링을 중심으로 하는 장르들.
감정적 몰입과 서사적 전개가 핵심.
'''
from typing import List, Dict
from base_genre import BaseGenre, GenreCategory, GenreSuccessFormula

def _get_drama_category_expansion_rules():
    '''드라마/스토리 카테고리 공통 확장 규칙 (도돌이표 현상 방지)'''
    return '\n## 드라마/스토리 콘텐츠 특화 규칙\n\n### 🚨 괄호() 문자 사용 완전 금지 (TTS 필수!)\n\n대본에 괄호 문자 `(` `)` 자체를 **절대 포함하지 마세요**. 아래 예시뿐 아니라 **어떤 용도로든** 괄호 사용이 금지됩니다.\n\n**핵심 원칙**: 괄호로 표현하고 싶은 내용은 모두 **별도 문장**이나 **쉼표+접속어**로 풀어쓰세요.\n\n**❌ → ✅ 변환 예시:**\n- (웃으며), (놀라며) → [나레이션]: 그가 웃으며 말했다.\n- 시그나(Cigna), 나사(NASA) → 시그나, 나사\n- 긍정적인 감정(사랑, 기쁨) → 사랑이나 기쁨 같은 긍정적인 감정\n- 매출(100억 원) → 매출이 100억 원에 달하며\n\n**⚠️ 예시에 없는 형태도 금지**: (참고), (예:), (단,), (약) 등 **모든 괄호 사용 금지**\n\n### 도돌이표 현상 방지 (★ 핵심)\n다음 구간의 **통째로 반복**은 절대 금지입니다:\n- 전문가 상담/조언 구간\n- 갈등/대면 구간\n- 해방/치유/결말 구간\n- 도입부의 비유나 상황 설정\n\n❌ 절대 금지:\n- 이미 등장한 상담 장면을 뒤쪽에서 다시 똑같이 서술\n- 이미 해결된 갈등을 다시 현재 진행형으로 묘사\n- 결말부 내용을 다른 챕터에서 복사\n\n### 서사 타임라인 보호\n인물의 심리적 여정을 **선형적으로** 전개하세요:\n1. **무지/평화 단계**: 문제를 인식하지 못함\n2. **갈등/고통 단계**: 문제와 직면\n3. **탐색/상담 단계**: 해결책 모색 (1회만!)\n4. **결심/행동 단계**: 변화를 위한 행동\n5. **해방/치유 단계**: 문제 해결 (1회만!)\n6. **성장/여운 단계**: 새로운 시작\n\n❌ 절대 금지:\n- 이미 "해방 단계"에 진입한 인물을 다시 "고통 단계"로 묘사\n- 상담을 받고 해결책을 얻은 후 다시 상담실로 돌아가는 묘사\n- 같은 깨달음을 여러 챕터에서 반복\n\n### 비유/은유 관리\n- "거미줄", "독 한 방울" 등 핵심 비유는 **대본 전체에서 1회만** 사용\n- 각 챕터는 **서로 다른 비유**로 감정을 전달\n- 도입부에 사용한 비유를 결말부에서 "회수"할 때만 재사용 허용\n\n### 감정 묘사 규칙\n- ❌ 추상적: "슬펐다", "화가 났다", "절망했다"\n- ✅ 구체적: "손가락 끝이 하얗게 질릴 정도로 주먹을 쥐었다"\n- ✅ 감각적: "매일 밤 천장을 바라보며 잠 못 이루었다"\n'


class DramaticGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class RevengeGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class TouchingGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class ConfessionGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class MysteryGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class ThrillerGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class SfFantasyGenre(BaseGenre):
    '''SF/판타지'''
    code = (lambda self = None: 'SF_FANTASY')()
    name = (lambda self = None: 'SF/판타지')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '상상력을 자극하는 미래 세계나 판타지 요소가 있는 이야기')()
    tone_style = (lambda self = None: '세계관 구축과 상상력이 돋보이는 서사. 현실을 벗어난 설정이지만 감정적 공감은 유지.')()
    required_elements = (lambda self = None: [
'독특한 세계관이나 설정',
'특별한 능력이나 기술',
'모험과 성장',
'선과 악의 대립'])()


class HistoricalGenre(BaseGenre):
    '''역사/시대극'''
    code = (lambda self = None: 'HISTORICAL')()
    name = (lambda self = None: '역사/시대극')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '역사적 배경을 바탕으로 한 드라마틱한 이야기')()
    tone_style = (lambda self = None: '시대적 분위기를 살린 격조 있는 서술. 역사적 사실과 드라마의 조화.')()
    required_elements = (lambda self = None: [
'역사적 배경과 시대상',
'시대에 맞는 의상과 언어',
'역사적 인물이나 사건',
'권력과 음모'])()
    image_prompt_style = (lambda self = None: '한복, 전통 건축, 역사적 소품, 시대극 분위기')()


class HeartWarmingGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class JoseonFolktaleGenre(BaseGenre):
    '''조선야담 (민담, 야담)'''
    code = (lambda self = None: 'JOSEON_FOLKTALE')()
    name = (lambda self = None: '조선야담')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '조선시대를 배경으로 한 풍자와 재치가 넘치는 전통 이야기. 전기수(傳奇叟)의 구연 스타일.')()
    tone_style = (lambda self = None: '풍자, 재치, 민속 유머. 구전 설화처럼 친근하고 매력적인 서술. 전통적인 표현과 약간 과장되고 연극적인 톤.')()
    required_elements = (lambda self = None: [
'고전적인 조선시대 캐릭터 (양반, 평민, 사또, 기생 등)',
'"옛날 옛적에~" 민담 도입',
'사회적 풍자와 재치',
'권선징악 또는 유머러스한 결말'])()
    synopsis_structure = (lambda self = None: {
'기': [
'"옛날 옛적에~" 고전 도입',
'시대 배경 설명'],
'승': [
'문제 발생',
'사회적 부조리 풍자'],
'전': [
'영리한 해결 시도',
'재치가 빛나는 순간'],
'결': [
'교훈과 웃음',
'권선징악'] })()
    image_prompt_style = (lambda self = None: '전통 한국 민화(民畫) 스타일, 익살스러운 캐릭터 표정')()


class LifeLessonsGenre(BaseGenre):
    '''사연으로 배우는 인생명언'''
    code = (lambda self = None: 'LIFE_LESSONS')()
    name = (lambda self = None: '사연으로 배우는 인생명언')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '명언과 함께 전하는 인생의 지혜. 실제 사연을 통해 명언의 의미를 깨닫는 이야기.')()
    tone_style = (lambda self = None: '교훈적이면서도 감동적인 서술. 명언이 삶에 어떻게 적용되는지 보여주는 스토리.')()
    required_elements = (lambda self = None: [
'강력한 명언으로 시작',
'명언의 의미 설명',
'명언이 적용되는 실제 사연',
'명언의 지혜로 결론'])()
    synopsis_structure = (lambda self = None: {
'기': [
'명언 제시',
'명언의 의미 설명'],
'승': [
'사연 시작',
'갈등 발생'],
'전': [
'명언의 지혜 적용',
'변화의 시작'],
'결': [
'교훈 정리',
'명언과 연결'] })()


class LifeChallengeGenre(BaseGenre):
    '''인생도전 (시니어 성공담)'''
    code = (lambda self = None: 'LIFE_CHALLENGE')()
    name = (lambda self = None: '인생도전')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '시니어의 새로운 도전과 성공 스토리. "나이는 숫자일 뿐!" 영감을 주는 이야기.')()
    tone_style = (lambda self = None: '역동적이고 영감을 주는 스토리. 유머와 감동이 공존. 1인칭 시점 권장.')()
    required_elements = (lambda self = None: [
'60대 이상 시니어 주인공',
'현대적이고 역동적인 도전 (유튜버, 기술, 온라인 사업 등)',
'초기 실패와 유머러스한 장면',
'멘토나 돌파구',
'성공과 동기 부여 메시지'])()
    success_formula = (lambda self = None: GenreSuccessFormula(emotional_arc = '정체감 → 도전 결심 → 고군분투 → 돌파 → 성공', key_elements = self.required_elements, pov = '1인칭 시점 (시니어 주인공)', target_audience = '50~70대', hook_psychology = '공감과 희망, 대리만족'))()


class ConspiracyGenre(BaseGenre):
    '''음모론/미스터리'''
    code = (lambda self = None: 'CONSPIRACY')()
    name = (lambda self = None: '음모론 미스터리')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '숨겨진 진실과 음모를 파헤치는 스릴러')()
    tone_style = (lambda self = None: '의심과 긴장이 가득한 분위기. 믿을 수 없는 진실의 연속.')()
    required_elements = (lambda self = None: [
'감춰진 진실이나 음모',
'여러 단서와 복선',
'신뢰할 수 없는 인물들',
'충격적인 진실 공개'])()


class NationalPrideGenre(BaseGenre):
    '''국뽕 드라마'''
    code = (lambda self = None: 'NATIONAL_PRIDE')()
    name = (lambda self = None: '국뽕 드라마')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '대한민국의 자부심을 느끼게 하는 이야기. 한국의 성공, 문화, 역사적 업적.')()
    tone_style = (lambda self = None: '자부심과 감동을 주는 서술. 한국의 저력과 성공을 부각.')()
    required_elements = (lambda self = None: [
'한국의 성공 사례 또는 업적',
'외국인의 인정 또는 감탄',
'한국적 가치나 문화',
'뿌듯한 결말'])()


class MunchkinGenre(BaseGenre):
    '''힘숨찐/먼치킨 - 숨겨진 압도적 능력의 반전과 통쾌함

    평소에는 약하거나 평범해 보이지만 실제로는 압도적인 능력을 가진
    주인공의 반전과 통쾌함을 다루는 장르.

    핵심 요소:
    - 힘숨찐: 겉모습(약함) vs 내면(강함)의 극대한 갭
    - 먼치킨: 처음부터 또는 드러나면 압도적으로 강함
    - 사이다: 무시하던 자들의 경악과 통쾌한 역전
    '''
    code = (lambda self = None: 'MUNCHKIN')()
    name = (lambda self = None: '힘숨찐/먼치킨')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '평범하거나 무시당하던 주인공이 숨겨둔 압도적 능력을 드러내며 모든 것을 역전시키는 통쾌한 스토리')()
    tone_style = (lambda self = None: '초반 답답함에서 중후반 통쾌함으로의 극적 전환. 능력 발휘 순간의 압도적 카리스마와 무시하던 자들의 경악을 생생하게 묘사.')()
    required_elements = (lambda self = None: [
'주인공의 평범하거나 무시당하는 초반 모습',
'숨겨진 압도적 능력 또는 정체 (설정)',
'능력을 숨기는 명확한 이유',
'무시/멸시하는 적대자들의 오만함',
'결정적 순간의 능력 발휘 (반전)',
'경악하는 적대자들과 통쾌한 역전',
'사이다 요소와 적절한 고난의 균형'])()
    success_formula = (lambda self = None: GenreSuccessFormula(emotional_arc = '무시/답답함 → 위기 고조 → 결정적 순간 → 능력 발휘 → 통쾌한 역전 → 카타르시스', key_elements = self.required_elements, pov = '3인칭 전지적 작가 시점', target_audience = '30~50대', hook_psychology = '반전의 쾌감, 대리만족, 역전 기대감, 숨겨진 능력에 대한 호기심', chapter_structure = {
'기': '주인공의 평범/무시당하는 일상, 숨긴 능력 암시',
'승': '적대자의 오만함, 주인공의 고난 심화',
'전': '결정적 위기, 능력 발휘의 순간',
'결': '압도적 역전, 경악과 통쾌함' }))()
    synopsis_structure = (lambda self = None: {
'기': [
'주인공의 평범한 모습',
'무시하는 주변인들',
'숨긴 능력 복선'],
'승': [
'적대자의 오만한 도발',
'주인공의 인내와 고난',
'위기 고조'],
'전': [
'결정적 순간 도래',
'더 이상 숨길 수 없는 상황',
'능력 발휘'],
'결': [
'압도적 실력 차이',
'경악하는 적대자',
'통쾌한 역전과 여운'] })()
    image_prompt_style = (lambda self = None: '극적인 대비 (평범한 모습 vs 압도적 카리스마), 경악하는 표정, 역전의 순간, 강렬한 조명 대비')()
    recommended_tone = (lambda self = None: '극적체')()
    recommended_narration_ratio = (lambda self = None: 45)()


class MuhyupGenre(BaseGenre):
    '''무협 - 동양 정통 무협 서사

    정의로운 협객이 악의 세력을 평정하며 성장하는 동양 정통 무협 장르.
    시련-수련-승리의 반복 구조로 나선형 성장을 표현.

    핵심 요소:
    - 3막 12요소 영웅의 여정 (Vogler)
    - 무공 수련 5단계 (자질확인→내공신법→무기술→보신경→경지상승)
    - 무림 등급 체계 (이류→일류→상수→절정→대가)
    - 캐릭터 심리 8유형 (지배자, 조력자, 영웅 등)
    '''
    code = (lambda self = None: 'MUHYUP')()
    name = (lambda self = None: '무협')()
    category = (lambda self = None: GenreCategory.DRAMA)()
    definition = (lambda self = None: '정의로운 협객이 악의 세력을 평정하며 성장하는 동양 정통 무협 서사. 시련-수련-승리의 반복 구조로 나선형 성장을 표현.')()
    tone_style = (lambda self = None: '웅장하고 비장한 무림 세계관. 화려한 무공 액션과 깊이 있는 인간 드라마의 조화. 권선징악이 명확하고 성장과 극복의 메시지.')()
    required_elements = (lambda self = None: [
'정의로운 주인공과 명확한 악의 세력 대립',
'무공 수련 과정과 경지 상승 (이류→일류→상수→절정→대가)',
'스승과의 만남과 비급/무공 전수',
'시련-수련-승리 반복 구조',
'내적 갈등 (정의 vs 복수, 힘 vs 인성)',
'무림의 등급 체계와 세계관',
'결정적 대결과 카타르시스'])()
    success_formula = (lambda self = None: GenreSuccessFormula(emotional_arc = '평범한 일상 → 무림 진입 → 시련과 패배 → 수련과 깨달음 → 경지 상승 → 최종 승리', key_elements = self.required_elements, pov = '3인칭 전지적 작가 시점', target_audience = '40~60대', hook_psychology = '성장의 쾌감, 역전의 통쾌함, 정의 실현 욕구', chapter_structure = {
'1막_진입': '일상 세계에서 무림으로, 스승과의 만남, 첫 관문 통과',
'2막_성장': '시험과 시련, 동료와 적, 수련과 깨달음, 경지 상승',
'3막_귀환': '최종 대결, 승리, 무림의 전설로 거듭남' }))()
    synopsis_structure = (lambda self = None: {
'기': [
'주인공의 평범한 일상',
'무림과의 첫 접촉',
'스승 등장'],
'승': [
'기초 수련과 내공 축적',
'첫 대결과 패배',
'더 강해지려는 결심'],
'전': [
'결정적 위기',
'마지막 수련',
'새로운 경지 도달'],
'결': [
'최종 대결',
'승리와 성장',
'무림 고수로 인정'] })()
    image_prompt_style = (lambda self = None: '동양 무협 스타일, 화려한 검무, 내공 발현의 오라, 웅장한 무림 배경, 전통 복장의 협객')()
    recommended_tone = (lambda self = None: '극적체')()
    recommended_narration_ratio = (lambda self = None: 40)()
