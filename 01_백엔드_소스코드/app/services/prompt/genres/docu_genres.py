# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: docu_genres.pyc (Python 3.11)

'''
Docu Genres - 실화/다큐/뉴스/예능 계열 장르

사실 기반 콘텐츠와 특수 형식 장르들.
객관성, 신뢰성, 재미가 핵심.
'''
from typing import List
from base_genre import BaseGenre, GenreCategory, GenreSuccessFormula

class TrueStoryGenre(BaseGenre):
    '''실화 재연'''
    code = (lambda self = None: 'TRUE_STORY')()
    name = (lambda self = None: '실화 재연')()
    category = (lambda self = None: GenreCategory.DOCU)()
    definition = (lambda self = None: '실제 있었던 사건이나 이야기를 재구성. 사실에 기반한 드라마틱한 서사.')()
    tone_style = (lambda self = None: '신뢰감 있는 서술. 사실 기반이지만 드라마틱한 전개. "이것은 실화입니다" 강조.')()
    required_elements = (lambda self = None: [
'실제 사건임을 명시',
'시간, 장소, 인물 구체화',
'사실적인 디테일',
'교훈이나 메시지'])()
    recommended_tone = (lambda self = None: '다큐체')()
    recommended_narration_ratio = (lambda self = None: 65)()


class DocumentaryGenre(BaseGenre):
    '''다큐멘터리'''
    code = (lambda self = None: 'DOCUMENTARY')()
    name = (lambda self = None: '다큐멘터리')()
    category = (lambda self = None: GenreCategory.DOCU)()
    definition = (lambda self = None: '사실과 정보를 객관적으로 전달하는 다큐멘터리 형식')()
    tone_style = (lambda self = None: '객관적이고 신뢰감 있는 서술. 사실 기반, 시간/장소 명시. 전문적이면서도 이해하기 쉽게.')()
    required_elements = (lambda self = None: [
'정확한 사실과 데이터',
'시간순 또는 주제별 구성',
'전문가 의견이나 증언',
'결론 및 시사점'])()
    recommended_tone = (lambda self = None: '다큐체')()
    recommended_narration_ratio = (lambda self = None: 85)()
    image_prompt_style = (lambda self = None: '다큐멘터리 스타일, 리얼리스틱, 역사적 자료 느낌')()


class NewsReportGenre(BaseGenre):
    '''뉴스/리포트'''
    code = (lambda self = None: 'NEWS_REPORT')()
    name = (lambda self = None: '뉴스/리포트')()
    category = (lambda self = None: GenreCategory.NEWS)()
    definition = (lambda self = None: '최신 뉴스나 이슈를 분석하고 전달하는 리포트 형식')()
    tone_style = (lambda self = None: '신뢰감 있고 객관적인 뉴스 톤. 팩트 중심, 분석과 해설 포함.')()
    required_elements = (lambda self = None: [
'육하원칙 (누가, 언제, 어디서, 무엇을, 왜, 어떻게)',
'정확한 사실 전달',
'배경 설명',
'전망 및 시사점'])()
    recommended_tone = (lambda self = None: '설명체')()
    recommended_narration_ratio = (lambda self = None: 90)()


class ReviewAnalysisGenre(BaseGenre):
    '''리뷰/분석'''
    code = (lambda self = None: 'REVIEW_ANALYSIS')()
    name = (lambda self = None: '리뷰/분석')()
    category = (lambda self = None: GenreCategory.NEWS)()
    definition = (lambda self = None: '제품, 서비스, 콘텐츠 등에 대한 심층 리뷰와 분석')()
    tone_style = (lambda self = None: '객관적이면서도 개인 의견이 담긴 톤. 장단점을 균형 있게 분석.')()
    required_elements = (lambda self = None: [
'대상 소개',
'장점과 단점',
'비교 분석',
'결론 및 추천'])()
    recommended_tone = (lambda self = None: '설명체')()
    recommended_narration_ratio = (lambda self = None: 80)()


class VarietyGenre(BaseGenre):
    '''예능/버라이어티'''
    code = (lambda self = None: 'VARIETY')()
    name = (lambda self = None: '예능/버라이어티')()
    category = (lambda self = None: GenreCategory.VARIETY)()
    definition = (lambda self = None: '재미와 웃음을 주는 예능 스타일. 가벼운 톤과 유머.')()
    tone_style = (lambda self = None: '가볍고 재미있는 톤. 유머와 위트, 편안한 분위기.')()
    required_elements = (lambda self = None: [
'재미있는 에피소드',
'유머와 웃음 포인트',
'캐릭터성 있는 인물',
'가벼운 결말'])()
    recommended_tone = (lambda self = None: '유머체')()
    recommended_narration_ratio = (lambda self = None: 40)()


class HybridGenre(BaseGenre):
    '''하이브리드 (정보+스토리)'''
    code = (lambda self = None: 'HYBRID')()
    name = (lambda self = None: '하이브리드')()
    category = (lambda self = None: GenreCategory.VARIETY)()
    definition = (lambda self = None: '정보 전달과 스토리텔링을 결합한 형식. 인포테인먼트.')()
    tone_style = (lambda self = None: '정보성과 재미를 동시에. 스토리를 통해 정보를 자연스럽게 전달.')()
    required_elements = (lambda self = None: [
'흥미로운 스토리 프레임',
'중간중간 정보 삽입',
'정보와 이야기의 자연스러운 연결',
'교육과 재미 균형'])()
    recommended_tone = (lambda self = None: '친근체')()
    recommended_narration_ratio = (lambda self = None: 60)()
