# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_framing_policy.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
_ACTOR_TYPE_PRIORITY = {
    'registered_character': 5,
    'unregistered_named_actor': 4,
    'relational_role_actor': 3,
    'occupational_or_social_role_actor': 2,
    'group_actor': 1,
    'crowd_actor': 0,
    'background_actor': -1 }
_IMPORTANCE_PRIORITY = {
    'primary': 2,
    'secondary': 1,
    'background': 0 }
_NON_FOCAL_ACTOR_TYPES = {
    'crowd_actor',
    'group_actor',
    'background_actor'}
_PRESENTATION_VERB_PATTERN = re.compile('\\b(?:present(?:s|ing)?|lecture(?:s|ing)?|brief(?:s|ing)?|teach(?:es|ing)?|demonstrat(?:es|ing)?)\\b|(?:발표하|강의하|브리핑하|가르치|시연하)', re.IGNORECASE)
_PRESENTATION_OBJECT_PATTERN = re.compile('\\b(?:board|whiteboard|blackboard|screen|monitor|map|chart|diagram|slide|slides|display|projection|projector|podium|classroom|lecture hall|briefing room)\\b|(?:보드|칠판|화면|모니터|지도|차트|도표|슬라이드|디스플레이|프로젝터|연단|교실|강의실|브리핑룸)', re.IGNORECASE)
_PRESENTATION_ROLE_PATTERN = re.compile('\\b(?:presenter|analyst|speaker|host|teacher|lecturer|guide|instructor|expert)\\b|(?:발표자|분석가|연설자|사회자|선생|강사|가이드|전문가)', re.IGNORECASE)
_DIALOGUE_PATTERN = re.compile('\\b(?:talk(?:s|ing)?|speak(?:s|ing)?|say(?:s|ing)?|ask(?:s|ing)?|answer(?:s|ing)?|conversation|dialogue|discuss(?:es|ing)?|whisper(?:s|ing)?|argu(?:e|es|ing)|comfort(?:s|ing)?|console(?:s|ing)?|listen(?:s|ing)?)\\b|(?:대화하|말하|묻|답하|속삭이|토론하|논쟁하|위로하|달래|듣)', re.IGNORECASE)
_EMOTION_PATTERN = re.compile('\\b(?:cry(?:ing)?|tears?|sorrow|sad(?:ness)?|fear|panic|anger|angry|grief|joy|shocked|surprised|anxious|tense|emotional)\\b|(?:울|눈물|슬픔|두려|공포|분노|기쁨|충격|놀라|불안|긴장|감정)', re.IGNORECASE)
_ACTION_PATTERN = re.compile('\\b(?:fight(?:s|ing)?|attack(?:s|ing)?|run(?:s|ning)?|chase(?:s|d|ing)?|jump(?:s|ing)?|leap(?:s|ing)?|swing(?:s|ing)?|strike(?:s|ing)?|rescue(?:s|d|ing)?|dodge(?:s|d|ing)?|crash(?:es|ed|ing)?|kneel(?:s|ing)?|train(?:s|ing)?|wrap(?:s|ped|ping)?|bind(?:s|ing)?|drag(?:s|ged|ging)?|pull(?:s|ed|ing)?|grip(?:s|ped|ping)?|clutch(?:es|ed|ing)?|patrol(?:s|led|ling)?|scan(?:s|ned|ning)?|raise(?:s|d|ing)?)\\b|(?:싸우|공격하|달리|추격하|뛰|도약하|휘두르|내리치|구하|피하|충돌하|무릎[^ ]*꿇|훈련하|수련하|감싸|감기|묶|결박하|끌고 가|끌어당기|붙잡|움켜쥐|쥐|순찰하|살피|둘러보|치켜들)', re.IGNORECASE)
_CROWD_PATTERN = re.compile('\\b(?:crowd|packed|busy market|plaza|street full of|filled with people|assembly|gathered|parade|ceremony|audience|spectators|bystanders|procession|marketplace)\\b|(?:군중|인파|붐비|광장|거리 가득|사람들로 가득|집회|모여|행렬|의식|청중|관중|구경꾼|시장통)', re.IGNORECASE)
_ESTABLISHING_PATTERN = re.compile('\\b(?:establishing|overview|panoramic|sweeping|full view|city view|location intro|whole area|entire square|entire hall)\\b|(?:전경|전반|파노라마|전체 모습|도시 전경|장소 소개|광장 전체|홀 전체)', re.IGNORECASE)
_HUMAN_ROLE_PATTERN = re.compile('\\b(?:man|woman|person|figure|subject|presenter|teacher|student|analyst|speaker|guard|soldier|worker|villager|father|mother|mentor|master|child|boy|girl)\\b|(?:남성|여성|사람|인물|주체|발표자|선생|학생|분석가|경비병|군인|노동자|마을 사람|아버지|어머니|스승|사부|아이|소년|소녀)', re.IGNORECASE)
_SCENE_TYPE_LABELS = {
    'character_focus': 'character-focus scene',
    'emotion_dialogue': 'emotion/dialogue scene',
    'explanation_presentation': 'explanation/presentation scene',
    'crowd_establishing': 'crowd/establishing scene',
    'action_focus': 'action/focus scene' }
_COMPOSITION_RULE_LABELS = {
    'subject_dominant_single': 'subject-dominant single frame',
    'focused_two_shot': 'focused two-shot',
    'presenter_dominant': 'presenter-dominant frame',
    'subject_centered_action': 'subject-centered action frame',
    'focal_cluster_establishing': 'focal-cluster establishing frame',
    'focused_pair': 'focused pair frame',
    'object_focus_insert': 'object-focused insert frame',
    'over_shoulder_exchange': 'over-the-shoulder exchange frame',
    'reaction_layered_group': 'layered reaction group frame',
    'supporting_reaction_focus': 'supporting reaction frame' }
PROMPT_PRIORITY_ORDER = [
    'scene_semantic_intent',
    'main_subject_dominance',
    'shot_framing_policy',
    'style_consistency',
    'background_support',
    'crowd_depth_diversity']
_DETAIL_PROP_PATTERN = re.compile('\\b(?:wrist|hand(?:s)?|chain|shackle|rope|restraint|bruise|scar|blood mark|red mark|prop|amulet|necklace|letter|page|book|map|document|screen|monitor|phone|sword|knife|lantern|bracelet)\\b|(?:손목|손|쇠사슬|사슬|결박|밧줄|핏자국|붉은 반점|붉은 자국|상처 자국|흉터|물건|오브젝트|부적|목걸이|편지|페이지|책|지도|문서|화면|모니터|스마트폰|검|칼|등불|팔찌)', re.IGNORECASE)
_BODY_PART_FOCUS_PATTERN = re.compile('\\b(?:wrist|hand(?:s)?|face|eye(?:s)?|mouth|shoulder|upper body|silhouette|profile|rear view|back view)\\b|(?:손목|손|얼굴|눈|입|어깨|상체|실루엣|옆모습|측면|뒷모습|등진)', re.IGNORECASE)
_LISTENING_PATTERN = re.compile('\\b(?:listen(?:s|ing)?|hears?|hearing|sound|noise|rustle|footstep|off-screen|dark woods|tree line)\\b|(?:듣|기척|소리|발소리|숲 쪽|숲속|수풀|어둠|오프스크린)', re.IGNORECASE)
_REACTION_PATTERN = re.compile('\\b(?:watch(?:es|ing)?|observe(?:s|d|ing)?|witness(?:es|ing)?|glance(?:s|d|ing)?|stare(?:s|d|ing)?|bow(?:s|ed|ing)?|kneel(?:s|ing)?|react(?:s|ing)?|freeze(?:s|ing)?|from the doorway|behind|in the background)\\b|(?:지켜보|바라보|응시|엎드|절하|무릎|반응하|얼어붙|문가|뒤에서|배경)', re.IGNORECASE)
_COUNTERPART_PATTERN = re.compile('\\b(?:face(?:s|ing)? each other|look(?:s|ing)? at each other|toward each other|counterpart|conversation|dialogue|exchange|rebuttal|comfort|console)\\b|(?:마주보|서로|상대|대화|주고받|반박|위로|달래)', re.IGNORECASE)
_THREAT_AXIS_PATTERN = re.compile('\\b(?:threat|monster|demon|ghost|reaper|attack(?:er)?|claw|beam|weapon|danger|objective)\\b|(?:위협|악귀|귀신|괴물|사신|공격자|손톱|광선|무기|위험|목표물)', re.IGNORECASE)
_ESTABLISHING_REQUIRED_PATTERN = re.compile("\\b(?:establishing|overview|wide overview|panoramic|sweeping|full view|bird's-eye|aerial|whole village|entire village|village square|entire square|entire hall|gathered villagers|crowd spread|location intro|ceremony)\\b|(?:전경|개관|넓은 전경|파노라마|한눈에|마을 전체|광장 전체|홀 전체|마을 사람들 전체|의식 전경)", re.IGNORECASE)
_BROAD_ENVIRONMENT_PATTERN = re.compile('\\b(?:village|village road|plaza|courtyard|hall|mountain|ridge|forest edge|outer road|shrine grounds|marketplace|gate|field|open area|entrance path)\\b|(?:마을|마을 길|광장|마당|홀|산|산등성이|숲 가장자리|바깥길|사당 앞|시장통|성문|들판|트인 공간|입구 길)', re.IGNORECASE)
_SCENE_TARGET_PATTERNS: 'List[Tuple[re.Pattern[str], str]]' = [
    (re.compile('\\b(?:bound wrist|wrist bound|shackled wrist|glowing wrist)\\b|(?:묶인 손목|빛나는 손목|결박된 손목)', re.IGNORECASE), 'the bound wrist'),
    (re.compile('\\b(?:chain|shackle|restraint|rope)\\b|(?:쇠사슬|사슬|결박|밧줄)', re.IGNORECASE), 'the chain'),
    (re.compile('\\b(?:demon hand|ghost hand|reaper hand|monster hand|claw)\\b|(?:악귀의 손|귀신의 손|사신의 손|괴물의 손|손톱)', re.IGNORECASE), 'the threatening hand'),
    (re.compile('\\b(?:red mark|blood mark|bruise|scar|stain|spot)\\b|(?:붉은 반점|붉은 자국|핏자국|멍|흉터|얼룩)', re.IGNORECASE), 'the red mark'),
    (re.compile('\\b(?:forest|dark woods|tree line|off-screen woods|sound in the forest)\\b|(?:숲 쪽 어둠|숲속|수풀|나무 사이|숲 쪽)', re.IGNORECASE), 'the dark forest where the sound came from'),
    (re.compile('\\b(?:distant mountain|mountain ridge|far ridge|mountain)\\b|(?:먼 산|산등성이|능선|산자락|산 정상|산 위|산 아래|산 쪽|산길|산속)', re.IGNORECASE), 'the distant mountain'),
    (re.compile('\\b(?:villagers|bowed villagers|kneeling villagers|people on the ground)\\b|(?:엎드린 마을 사람들|무릎 꿇은 마을 사람들|마을 사람들)', re.IGNORECASE), 'the bowed villagers'),
    (re.compile('\\b(?:screen|page|chart|map|document|phone|book)\\b|(?:화면|페이지|차트|지도|문서|스마트폰|책)', re.IGNORECASE), 'the scene-critical object')]

def build_scene_framing_policy(*, scene_actors, base_profile, scene_text, structured_prompt, render_mode):
    pass
# WARNING: Decompyle incomplete


def resolve_scene_composition_subject_count(*, registered_count, profile, fallback_count):
