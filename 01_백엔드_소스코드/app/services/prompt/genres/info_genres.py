# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: info_genres.pyc (Python 3.11)

'''
Info Genres - 정보/교양 계열 장르

정보 전달과 교육을 중심으로 하는 장르들.
실용적인 지식과 인사이트 제공이 핵심.
'''
from typing import List
from base_genre import BaseGenre, GenreCategory, GenreSuccessFormula

def _get_info_category_expansion_rules():
    '''정보/교양 카테고리 공통 확장 규칙'''
    return '\n## 정보/교양 콘텐츠 특화 규칙\n\n### 🚨 괄호() 문자 사용 완전 금지 (TTS 필수!)\n\n대본에 괄호 문자 `(` `)` 자체를 **절대 포함하지 마세요**. 아래 예시뿐 아니라 **어떤 용도로든** 괄호 사용이 금지됩니다.\n\n**핵심 원칙**: 괄호로 표현하고 싶은 내용은 모두 **별도 문장**이나 **쉼표+접속어**로 풀어쓰세요.\n\n**❌ → ✅ 변환 예시:**\n- 카이퍼 벨트(Kuiper Belt) → 카이퍼 벨트\n- 해왕성 바깥 천체(TNO) → 해왕성 바깥 천체, 줄여서 TNO라 불리는\n- 긍정적인 단어(파티, 사랑) → 파티나 사랑 같은 긍정적인 단어\n- 매출(100억 원) → 매출이 100억 원에 달하며\n\n**⚠️ 예시에 없는 형태도 금지**: (참고), (예:), (영어:), (단,), (약), (즉) 등 **모든 괄호 사용 금지**\n\n### 논리적 구조 강제\n- 챕터 흐름: **현상 소개 → 원인 분석 → 영향 설명 → 대응 방안 → 핵심 교훈**\n- 각 챕터는 이전 챕터의 내용을 기반으로 발전해야 합니다.\n- 결론이나 교훈은 마지막 챕터에서만 종합적으로 제시하세요.\n\n### 금지 표현 목록\n다음 표현들은 대본 전체에서 **1회만** 사용하거나 아예 사용하지 마세요:\n- "10만원이 사라지는 충격" 류의 자극적 비유 반복\n- "여러분의 월급에서..." 류의 과도한 직접 호소\n- "자, 잘 들어보세요" / "이건 꼭 알아야 합니다" 류의 추임새\n- "솔직히 말해서" / "이렇게 반박하는 분들 분명히 나옵니다" 반복\n\n### 데이터 기반 서술 필수\n- 추상적 표현 대신 구체적 수치를 사용하세요.\n- ❌ "대출 이자가 너무 많이 올랐습니다."\n- ✅ "기준금리가 0.5%포인트씩 빅 스텝을 밟기 시작하자, 매달 이자가 50만원 이상 늘어났습니다."\n\n### 전문 용어 활용 (괄호 없이!)\n- 전문 용어는 한글 표기만 사용하거나, 별도 문장으로 설명하세요.\n- ❌ "리츠(REITs, 부동산 투자 신탁)"\n- ✅ "리츠, 즉 부동산 투자 신탁은..."\n- ❌ "GTX(수도권 광역급행철도)"\n- ✅ "수도권 광역급행철도인 GTX는..."\n'


class LifeKnowledgeGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class OfficeSurvivalGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class MoneySenseGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class RelationshipEqGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class PsychologyGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class LifeChoicesGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete


class KnowledgeBiteGenre(BaseGenre):
    pass
# WARNING: Decompyle incomplete
