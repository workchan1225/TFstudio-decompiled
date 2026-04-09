# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: drama_storytelling_system.pyc (Python 3.11)

__doc__ = '\n드라마/스토리 장르를 위한 고급 스토리텔링 시스템\n\n이 모듈은 감동적인 스토리텔링을 위한 6단계 서사 구조, 심리학적 기제,\n캐릭터 아키타입, 감각적 트리거를 정의합니다.\n\n적용 장르 (18개):\n- DRAMATIC, TOUCHING, CONFESSION, MYSTERY, THRILLER, REVENGE\n- JOSEON_FOLKTALE, SF_FANTASY, HISTORICAL, HEARTWARMING\n- LIFE_LESSONS, LIFE_CHALLENGE, WAR_MILITARY, DISASTER_APOCALYPSE\n- HORROR, EPIC_FANTASY, YOUTH_DRAMA, HYBRID\n'
from typing import Dict, List, Optional
DRAMA_NARRATIVE_STRUCTURE = {
    'stages': {
        '1_결핍': {
            'name': '결핍 (Deficiency)',
            'description': '주인공의 결핍/불완전함 제시 - 시청자 공감 유도',
            'elements': [
                '주인공의 현재 상황 (가난, 고독, 상실)',
                '결핍으로 인한 내적 갈망',
                '평범한 일상 속 불안정한 균형'],
            'writing_tip': '구체적인 환경 묘사로 주인공의 처지를 선명하게 그려라' },
        '2_만남': {
            'name': '만남 (Encounter)',
            'description': '새로운 환경/인물 진입 - 극명한 대비 설정',
            'elements': [
                '새로운 세계로의 진입 (취업, 우연한 방문)',
                '극명한 환경적 대비 (가난 vs 부유)',
                '첫 번째 감각적 트리거 등장'],
            'writing_tip': '두 세계의 대비를 시각적, 감각적으로 극대화하라' },
        '3_의구심': {
            'name': '의구심 (Doubt)',
            'description': '감각적 트리거로 미스터리 암시',
            'elements': [
                '설명할 수 없는 익숙함/데자뷰',
                '감각적 트리거 심화 (향기, 소리, 직감)',
                "주인공의 내면 독백 '왜 눈물이 나는가?'"],
            'writing_tip': '논리적 설명 대신 감각과 직관으로 서스펜스를 만들어라' },
        '4_위기_갈등': {
            'name': '위기/갈등 (Crisis)',
            'description': '금기(Taboo) 설정과 파기 - 진실에 접근',
            'elements': [
                '금기 설정 (절대 들어가면 안 되는 방, 언급 금지 과거)',
                '주인공의 금기 파기 (순수한 의도 또는 우연)',
                '진실에 다가가는 증거 발견 (사진, 서류, 흉터)'],
            'writing_tip': '금기 파기의 긴장감과 발견의 충격을 교차시켜라' },
        '5_진실_규명': {
            'name': '진실 규명 (Revelation)',
            'description': '복선 수렴 - 감각 기억과 물리적 증거 일치',
            'elements': [
                '모든 복선이 하나로 합쳐지는 순간',
                '감각적 기억 + 물리적 증거 일치 (발등의 점, DNA, 녹취록)',
                '숨겨진 배신자/진범 폭로'],
            'writing_tip': '복선들이 퍼즐처럼 맞춰지는 쾌감을 선사하라' },
        '6_카타르시스': {
            'name': '카타르시스 (Catharsis)',
            'description': '감정 폭발 + 인과응보 + 새 가족 형성',
            'elements': [
                '폭포수 같은 감정 분출 (오열, 부둥켜안음, 무릎 꿇고 사죄)',
                '악인의 처벌/축출, 선인의 보상',
                '새로운 형태의 가족 탄생 (혈연 + 인연)',
                '삶의 교훈과 여운'],
            'writing_tip': '신체 반응과 대사로 감정의 정점을 생생하게 전달하라' } },
    'flow_pattern': '결핍 → 만남 → 의구심 → 위기/갈등 → 진실 규명 → 카타르시스' }
PSYCHOLOGICAL_MECHANISMS = {
    'lost_child_archetype': {
        'name': '원형적 그리움 (The Lost Child Archetype)',
        'description': "'잃어버린 부모/자식'은 인류 공통의 원형적 공포이자 소망",
        'effect': '해결 과정에서 시청자는 대리 만족과 정서적 정화를 경험',
        'application': [
            '잃어버린 자식을 찾는 부모',
            '생이별한 가족의 재회',
            '버려진 아이의 뿌리 찾기'] },
    'proust_effect': {
        'name': '프루스트 현상 (The Proust Effect)',
        'description': '특정 향기나 소리가 과거의 기억을 소환하는 심리 기제',
        'effect': "논리적 개연성보다 더 강력한 '운명적 필연성' 부여",
        'triggers': [
            '어머니가 부르던 콧노래',
            '아버지의 담배 냄새',
            '할머니 집 마당의 꽃향기',
            '어린 시절 비 오는 날의 냄새'] },
    'projective_identification': {
        'name': '투사적 동일시 (Projective Identification)',
        'description': '돈 많고 외로운 부자가 순수한 주인공을 통해 구원받는 서사',
        'effect': "현대인의 '부유함에 대한 갈망'과 '정서적 결핍'을 동시에 위로",
        'pattern': '고독한 권력자 + 순수한 구원자 = 상호 치유' },
    'defense_dissolution': {
        'name': '방어기제의 해체',
        'description': "권력자의 '차가운 갑옷(사회적 지위)'이 순수함에 의해 해체",
        'effect': '인간미를 회복하는 심리적 치유 과정 시각화',
        'stages': [
            '차가운 거부',
            '호기심과 관찰',
            '균열의 시작',
            '감정적 방어 붕괴',
            '인간적 교감'] } }
CHARACTER_ARCHETYPES = {
    'protagonist': {
        'name': '주인공',
        'traits': [
            '가난하지만 당당함',
            '특별한 감각(직관, 청각, 후각) 보유',
            '순수하고 정직한 성품',
            '고난에도 굴하지 않는 강인함'],
        'role': '이야기의 중심, 변화와 성장의 주체',
        'writing_guide': '주인공의 특별한 감각을 서사 전개의 핵심 장치로 활용' },
    'helper': {
        'name': '조력자',
        'traits': [
            '헌신적인 노인 또는 가난한 가족',
            '주인공의 도덕적 근간',
            '무조건적 사랑의 원천',
            '지혜와 인생 경험 보유'],
        'role': '주인공에게 가치관과 삶의 방향을 제시',
        'writing_guide': '조력자의 희생과 헌신이 주인공 성장의 토대임을 보여줘라' },
    'counterpart': {
        'name': '상대역',
        'traits': [
            '부유함 속에 상처를 숨긴 고독한 권력자',
            '과거의 트라우마 (잃어버린 자식, 배신의 상처)',
            '차가운 외면 아래 따뜻한 본성',
            '구원받기를 갈망하는 영혼'],
        'role': '주인공과 대비되며, 상호 구원의 대상',
        'writing_guide': '권력자의 약점과 상처를 서서히 드러내며 인간미를 부여' },
    'antagonist': {
        'name': '악역/장애물',
        'traits': [
            '탐욕적 배신자 또는 사회적 편견',
            '주인공을 시기하고 방해',
            '권력자 곁에서 이익을 탐하는 자',
            '진실을 은폐하려는 세력'],
        'role': '갈등의 원인, 인과응보의 대상',
        'writing_guide': '악역의 몰락이 카타르시스를 극대화하도록 설계' } }
SENSORY_TRIGGERS = {
    'auditory': {
        'name': '청각적 트리거',
        'examples': [
            '어머니가 부르던 콧노래',
            '아버지의 휘파람 소리',
            '오래된 오르골 멜로디',
            '특정 동요나 자장가',
            '비 오는 날 처마 끝 물방울 소리'],
        'effect': '무의식 깊은 곳의 기억을 소환하는 강력한 매개체',
        'writing_guide': '청각 트리거는 감정의 급격한 전환점에 배치' },
    'olfactory': {
        'name': '후각적 트리거',
        'examples': [
            '특정 샴푸/비누 향기',
            '손때 묻은 책 냄새',
            '어린 시절 집의 냄새',
            '특정 요리 냄새',
            '계절의 꽃향기'],
        'effect': '프루스트 현상의 가장 직접적 발현',
        'writing_guide': '후각 트리거는 무의식적 반응(눈물, 떨림)과 함께 묘사' },
    'supernatural': {
        'name': '초자연적 트리거',
        'examples': [
            '관상으로 보이는 운명',
            '꿈에서의 예지',
            '설명할 수 없는 직감',
            '데자뷰 현상',
            '심장이 끌리는 느낌'],
        'effect': "논리를 초월한 '운명적 연결감' 형성",
        'writing_guide': '초자연적 요소는 은유적으로 처리하여 현실감 유지' },
    'tactile': {
        'name': '촉각적 트리거',
        'examples': [
            '낡은 손수건의 감촉',
            '특정 재질의 옷감',
            '손의 온기',
            '발등의 점, 손톱 모양 등 신체적 특징'],
        'effect': '물리적 접촉을 통한 기억과 감정의 연결',
        'writing_guide': '촉각 트리거는 진실 규명 단계의 결정적 증거로 활용' } }
DRAMA_WRITING_STYLE = {
    'pov': {
        'rule': '대화체(구어체) 위주로 작성',
        'effect': '듣는 이가 옆에서 이야기를 듣는 것처럼 느끼게 함',
        'example': "그때 그 사람이 그랬어요. '너, 왜 울어?'라고..." },
    'description': {
        'rule': '추상적인 단어보다 구체적인 행동과 세밀한 감각 묘사 사용',
        'bad_example': '슬펐다',
        'good_example': '손가락 끝이 하얗게 질릴 정도로 가방끈을 꽉 움켜쥐었다',
        'bad_example_2': '화가 났다',
        'good_example_2': '이를 악물고 있는데 관자놀이가 욱신거렸다' },
    'emotion_pacing': {
        'rule': '문단마다 감정의 고저를 조절',
        'pattern': '긴장 → 이완 → 긴장 → 폭발',
        'tip': '타임스탬프를 의식하여 감정 곡선을 설계' },
    'setting': {
        'rule': '한국적 정서를 반영하되, 필요시 해외 배경도 가능',
        'elements': [
            '지명과 인명은 친숙하게',
            '계절감과 시대감 반영',
            '공간의 분위기 묘사'] },
    'climax_techniques': {
        'physical_reactions': [
            '눈물이 볼을 타고 흘러내렸다',
            '무릎에서 힘이 빠져 주저앉았다',
            '심장이 터질 것 같았다',
            '숨이 막혀왔다',
            '온몸에 소름이 돋았다'],
        'emotional_outbursts': [
            '오열하며 부둥켜안았다',
            '무릎 꿇고 용서를 빌었다',
            '말없이 등을 토닥였다',
            '손을 꼭 잡고 놓지 않았다'] } }
STORY_ELEMENTS = {
    'extreme_contrast': {
        'name': '극명한 환경적 대비',
        'description': '가난하지만 선한 주인공 vs 화려하지만 상처 있는 부유층',
        'effect': '시청자의 감정이입 극대화, 동경과 연민 동시 자극',
        'examples': [
            '명문대생 vs 평창동 저택',
            '시골 소년 vs 글로벌 기업 회장',
            '고아원 출신 vs 재벌가'] },
    'taboo_and_break': {
        'name': '금기(Taboo)와 파기',
        'description': '금지된 영역 설정 후 주인공이 이를 어기며 진실에 접근',
        'effect': '서사의 긴장감 고조',
        'examples': [
            '서재에 절대 들어가지 마라',
            '그 사람 이름은 언급하지 마라',
            '3층은 올라가지 마라'] },
    'poetic_justice': {
        'name': '반전과 인과응보',
        'description': '숨겨진 배신자 폭로, 악인 몰락, 선인 보상',
        'effect': '도덕적 만족감과 카타르시스 제공',
        'pattern': '악행 → 은폐 → 폭로 → 응보' } }
# WARNING: Decompyle incomplete
