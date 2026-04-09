# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_templates.pyc (Python 3.11)

'''
Intro Templates - 인트로 템플릿 상수

YouTube 후킹/인트로에 최적화된 6개 기본 템플릿
'''
INTRO_TEMPLATES = [
    {
        'id': 'highlight_question_01',
        'name': 'Dramatic Question',
        'nameKo': '극적 질문형',
        'type': 'highlight_question',
        'hookTextPattern': '이 {캐릭터}가 {키워드}한 이유는?',
        'duration': 8,
        'effect': 'fast_zoom',
        'description': 'Pose a dramatic question with a highlight scene',
        'descriptionKo': '하이라이트 장면과 함께 극적인 질문을 던짐' },
    {
        'id': 'highlight_question_02',
        'name': 'Shocking Reveal',
        'nameKo': '충격 반전형',
        'type': 'highlight_question',
        'hookTextPattern': '아무도 예상하지 못한 결말...',
        'duration': 6,
        'effect': 'flash_cut',
        'description': 'Tease an unexpected twist',
        'descriptionKo': '예상치 못한 반전을 예고' },
    {
        'id': 'highlight_teaser_01',
        'name': 'Action Teaser',
        'nameKo': '액션 티저형',
        'type': 'highlight_teaser',
        'hookTextPattern': '',
        'duration': 5,
        'effect': 'fast_zoom',
        'description': 'Quick montage of highlight scenes',
        'descriptionKo': '하이라이트 장면의 빠른 몽타주' },
    {
        'id': 'highlight_teaser_02',
        'name': 'Emotional Teaser',
        'nameKo': '감정 티저형',
        'type': 'highlight_teaser',
        'hookTextPattern': '',
        'duration': 10,
        'effect': 'fade_dramatic',
        'description': 'Emotional highlight with dramatic fade',
        'descriptionKo': '극적 페이드와 감성적 하이라이트' },
    {
        'id': 'hook_text_01',
        'name': 'Bold Statement',
        'nameKo': '강렬한 선언형',
        'type': 'hook_text_only',
        'hookTextPattern': '{핵심문장}',
        'duration': 5,
        'effect': 'none',
        'description': 'Bold text hook without scene image',
        'descriptionKo': '장면 없이 강렬한 텍스트 후킹' },
    {
        'id': 'custom_01',
        'name': 'Custom Intro',
        'nameKo': '직접 입력',
        'type': 'custom',
        'hookTextPattern': '',
        'duration': 8,
        'effect': 'none',
        'description': 'Fully customizable intro',
        'descriptionKo': '모든 요소를 직접 커스터마이징' }]

def get_template_by_id(template_id = None):
    '''ID로 템플릿 조회'''
    for template in INTRO_TEMPLATES:
        if template['id'] == template_id:
            
            return None, template
        return None


def get_templates_by_type(intro_type = None):
    '''타입별 템플릿 목록 조회'''
    pass
# WARNING: Decompyle incomplete
