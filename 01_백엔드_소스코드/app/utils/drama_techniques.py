# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: drama_techniques.pyc (Python 3.11)

__doc__ = '\nDrama Techniques Library\n\n드라마/영상 제작에서 사용되는 기법들을 정의합니다.\n하드코딩된 예시 없이 기법의 원리와 적용 지침만 제공합니다.\n'
from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from enum import Enum

class TechniqueCategory(Enum):
    '''기법 카테고리'''
    CURIOSITY = '궁금증/몰입 유발'
    EMOTION = '감정 몰입'
    RHYTHM = '리듬/구조'
    SERIAL = '연재형'

DramaTechnique = <NODE:12>()
CLIFFHANGER = DramaTechnique(id = 'cliffhanger', name = 'Cliffhanger', korean_name = '클리프헹어', category = TechniqueCategory.CURIOSITY, description = '절정 직전에 끊어버려서 다음을 보게 만드는 장치', instruction = '챕터의 마지막을 긴장감 최고조에서 끊으세요. 결과를 보여주지 말고 "그때..." 또는 "문을 열자..."로 끝내세요.', psychology = '완결되지 않은 과제는 기억에 더 오래 남음 (자이가르닉 효과)', when_to_use = '챕터 전환 시, 특히 중간 지점에서 효과적', constraints = [
    '결과를 바로 보여주지 않음',
    '긴장감이 최고조인 순간에 끊음',
    '다음 챕터에서 반드시 해결'])
FORESHADOWING = DramaTechnique(id = 'foreshadowing', name = 'Foreshadowing', korean_name = '복선', category = TechniqueCategory.CURIOSITY, description = '미래에 벌어질 사건을 은근히 암시', instruction = '초반에 사소해 보이는 디테일을 언급하세요. 나중에 이것이 중요한 의미를 가지게 됩니다.', psychology = '시청자가 나중에 "아, 그래서 그랬구나!"라고 깨닫는 만족감', when_to_use = '초반부에 심어두고 후반부에서 회수', constraints = [
    '너무 노골적이면 안 됨',
    '반드시 후반에 회수해야 함',
    '자연스러운 맥락에서 등장'])
RED_HERRING = DramaTechnique(id = 'red_herring', name = 'Red Herring', korean_name = '미끼/속임수', category = TechniqueCategory.CURIOSITY, description = '시청자의 주의를 잘못된 방향으로 돌려 반전 효과 극대화', instruction = '의심스러운 인물이나 상황을 의도적으로 부각시키세요. 진짜 핵심은 다른 곳에 있습니다.', psychology = '예상이 빗나갈 때 오는 놀라움과 쾌감', when_to_use = '미스터리/추리 장르, 반전이 있는 이야기', constraints = [
    '미끼도 논리적으로 말이 되어야 함',
    '진짜 답도 공정하게 힌트 제공',
    '속임수가 너무 많으면 신뢰 상실'])
CHEKHOVS_GUN = DramaTechnique(id = 'chekhovs_gun', name = "Chekhov's Gun", korean_name = '체호프의 총', category = TechniqueCategory.CURIOSITY, description = '등장한 요소는 반드시 활용된다는 법칙', instruction = '초반에 언급한 물건, 능력, 관계는 반드시 후반에 중요한 역할을 해야 합니다.', psychology = '서사적 완결성, 불필요한 요소가 없다는 신뢰감', when_to_use = '모든 장르, 특히 구조가 탄탄한 이야기', constraints = [
    '등장시킨 것은 반드시 사용',
    '사용하지 않을 것은 언급하지 않음',
    '자연스러운 회수'])
PLOT_TWIST = DramaTechnique(id = 'plot_twist', name = 'Plot Twist', korean_name = '반전', category = TechniqueCategory.CURIOSITY, description = '예상과 정반대 결과로 충격 주기', instruction = '시청자가 믿고 있던 것이 사실이 아니었음을 폭로하세요. 단, 돌이켜보면 단서가 있어야 합니다.', psychology = '예측 오류가 클수록 강한 감정적 반응', when_to_use = '클라이맥스 직전, 결말부', constraints = [
    '공정한 반전 (돌이켜보면 단서 있음)',
    '반전을 위한 반전은 금지',
    '캐릭터와 스토리에 봉사하는 반전'])
MACGUFFIN = DramaTechnique(id = 'macguffin', name = 'MacGuffin', korean_name = '맥거핀', category = TechniqueCategory.CURIOSITY, description = '실제로는 중요하지 않지만 인물들을 움직이게 만드는 목표물', instruction = '캐릭터들이 쫓는 목표를 설정하되, 진짜 중요한 것은 그 과정에서의 변화입니다.', psychology = '목표는 수단일 뿐, 여정 자체가 이야기', when_to_use = '여정형 이야기, 추격 플롯', constraints = [
    '맥거핀 자체보다 캐릭터에 집중',
    '결말에서 맥거핀은 사라져도 됨'])
DRAMATIC_IRONY = DramaTechnique(id = 'dramatic_irony', name = 'Dramatic Irony', korean_name = '극적 아이러니', category = TechniqueCategory.EMOTION, description = '시청자는 알지만 주인공은 모르는 정보로 긴장감 유발', instruction = '시청자에게 먼저 중요한 정보를 알려주고, 그것을 모르는 캐릭터의 행동을 보여주세요.', psychology = '시청자가 "안 돼! 그러면 안 돼!"라고 외치게 만드는 긴장감', when_to_use = '비극적 상황, 서스펜스 장면', constraints = [
    '정보 격차가 명확해야 함',
    '캐릭터가 모르는 것이 합리적이어야 함'])
INTERIOR_MONOLOGUE = DramaTechnique(id = 'interior_monologue', name = 'Interior Monologue', korean_name = '내적 독백', category = TechniqueCategory.EMOTION, description = '주인공의 생각을 직접 드러내 공감 유도', instruction = '캐릭터의 내면 생각을 나레이션으로 보여주세요. 겉으로 드러나지 않는 감정을 전달합니다.', psychology = '캐릭터와의 동일시, 깊은 공감', when_to_use = '감정적 순간, 결정의 순간', constraints = [
    '과도한 설명 금지',
    '행동으로 보여줄 수 있는 것은 독백 불필요'])
SENSORY_IMAGERY = DramaTechnique(id = 'sensory_imagery', name = 'Sensory Imagery', korean_name = '공감각적 묘사', category = TechniqueCategory.EMOTION, description = '시각, 청각, 후각 등 감각 자극으로 장면 몰입 강화', instruction = '장면을 묘사할 때 시각뿐 아니라 소리, 냄새, 촉감 등을 포함하세요.', psychology = '다중 감각 자극으로 생생한 체험', when_to_use = '중요한 장면, 분위기 설정', constraints = [
    '모든 장면에 과도하게 사용하지 않음',
    '스토리 흐름을 방해하지 않음'])
TRAGIC_IRONY = DramaTechnique(id = 'tragic_irony', name = 'Tragic Irony', korean_name = '비극적 아이러니', category = TechniqueCategory.EMOTION, description = '시청자는 비극적 결말을 아는데 주인공은 모르는 상황', instruction = '피할 수 없는 비극으로 향하는 주인공을 보여주세요. 시청자는 이미 결말을 알고 있습니다.', psychology = '카타르시스, 깊은 슬픔과 정화', when_to_use = '비극적 이야기, 감동 장르', constraints = [
    '비극이 의미 있어야 함',
    '단순한 불행이 아닌 숭고함'])
IN_MEDIAS_RES = DramaTechnique(id = 'in_medias_res', name = 'In Medias Res', korean_name = '중간에서 시작', category = TechniqueCategory.RHYTHM, description = '이야기를 중간부터 시작해 호기심 자극', instruction = '가장 임팩트 있는 순간(클라이맥스 일부)을 먼저 보여주고, "어떻게 이런 일이?" 하며 과거로 돌아가세요.', psychology = '강렬한 첫인상, 즉각적인 호기심 유발', when_to_use = '인트로, 첫 번째 챕터', constraints = [
    '티저 장면은 짧게 (5-10초)',
    '바로 시간 역행으로 전환',
    '티저 장면은 마지막에 다시 나와야 함'])
CIRCULAR_NARRATIVE = DramaTechnique(id = 'circular_narrative', name = 'Circular Narrative', korean_name = '순환 구조', category = TechniqueCategory.RHYTHM, description = '시작과 결말을 같은 장면으로 이어 반복적 의미 부여', instruction = '첫 장면과 마지막 장면을 유사하게 구성하되, 의미는 완전히 다르게 만드세요.', psychology = '완결성, 변화의 극적 대비', when_to_use = '성장 이야기, 변화가 핵심인 이야기', constraints = [
    '같은 장면이지만 다른 의미',
    '변화가 눈에 보여야 함'])
FLASHBACK = DramaTechnique(id = 'flashback', name = 'Flashback', korean_name = '플래시백', category = TechniqueCategory.RHYTHM, description = '시간의 흐름을 깨고 과거 장면을 삽입', instruction = '현재 상황을 이해하는 데 필요한 과거 장면을 적절한 타이밍에 삽입하세요.', psychology = '정보 공개의 타이밍 조절, 미스터리 해소', when_to_use = '캐릭터 배경 설명, 숨겨진 진실 공개', constraints = [
    '현재와 과거 구분 명확',
    '플래시백이 현재 스토리에 봉사',
    '과도한 플래시백 금지'])
PACING = DramaTechnique(id = 'pacing', name = 'Pacing', korean_name = '속도 조절', category = TechniqueCategory.RHYTHM, description = '빠른 장면과 느린 장면을 섞어 긴장 완급 조절', instruction = '액션/위기 장면은 짧은 문장으로 빠르게, 감정 장면은 길게 묘사하세요.', psychology = '긴장과 이완의 리듬으로 지루함 방지', when_to_use = '모든 이야기', constraints = [
    '한 속도로만 가면 지루함',
    '중요한 순간에는 속도 변화'])
HOOKING_OPENING = DramaTechnique(id = 'hooking_opening', name = 'Hooking Opening', korean_name = '후킹 오프닝', category = TechniqueCategory.SERIAL, description = '시작부터 강렬한 사건이나 대사로 시청자를 붙잡음', instruction = '첫 3초 안에 시청자의 관심을 사로잡으세요. "안녕하세요"로 시작하지 마세요.', psychology = '예측 오류, 초두 효과', when_to_use = '영상 시작, 챕터 시작', constraints = [
    '인사말 금지',
    '배경 설명으로 시작 금지',
    '충격/궁금증/공감 중 하나'])
OPEN_ENDING = DramaTechnique(id = 'open_ending', name = 'Open Ending', korean_name = '열린 결말', category = TechniqueCategory.SERIAL, description = '일부러 결말을 열어둬서 해석을 시청자에게 맡김', instruction = '모든 것을 설명하지 말고 여운을 남기세요. 시청자가 스스로 의미를 찾게 하세요.', psychology = '능동적 해석, 더 오래 기억에 남음', when_to_use = '철학적 이야기, 예술적 이야기', constraints = [
    '주요 갈등은 해결',
    '열린 것은 의미와 해석'])
# WARNING: Decompyle incomplete
