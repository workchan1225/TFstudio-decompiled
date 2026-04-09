# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grok_prompt_analyzer.pyc (Python 3.11)

'''
Grok Prompt Analyzer - AI 기반 이미지 분석으로 Grok 비디오 프롬프트 생성

7단계 시네마틱 프롬프트 구조:
1. 포맷 선언 (9:16/16:9)
2. 장소/조명 상세
3. 캐릭터 외모+감정+포즈+동작
4. 카메라 의도 (앵글+목적)
5. 대사 통합 ("speaks in Korean: \'대사\'")
6. 분위기 마무리 (3 키워드)

Features:
- Gemini Vision API로 이미지 + 나레이션 분석 (Structured Output)
- 200-500자 상세 시네마틱 프롬프트 생성
- 캐릭터 이름 → 시각적 외모 묘사로 자동 변환
- 대사/핵심 문장을 프롬프트에 직접 통합
- 씬 문맥 연속성 지원
'''
import logging
import json
from typing import Optional, List
from io import BytesIO
from dataclasses import dataclass, field
from PIL import Image
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
logger = logging.getLogger(__name__)
GROK_PROMPT_SCHEMA = {
    'type': 'object',
    'properties': {
        'prompt': {
            'type': 'string',
            'description': 'Detailed scene description prompt under 200 characters' },
        'subject_action': {
            'type': 'string',
            'description': 'Main subject and its motion' },
        'camera_movement': {
            'type': 'string',
            'description': 'Camera technique' },
        'environment_lighting': {
            'type': 'string',
            'description': 'Atmosphere and lighting' },
        'video_feel': {
            'type': 'string',
            'description': 'Best matching video style category',
            'enum': [
                'news-info',
                'cinematic-drama',
                'action-thriller',
                'romantic',
                'horror-mystery',
                'documentary',
                'commercial'] },
        'korean_dialogue': {
            'type': 'string',
            'description': 'Korean dialogue extracted from narration, empty if none' } },
    'required': [
        'prompt',
        'subject_action',
        'camera_movement',
        'environment_lighting',
        'video_feel',
        'korean_dialogue'] }
GROK_CINEMATIC_PROMPT_SCHEMA = {
    'type': 'object',
    'properties': {
        'format_declaration': {
            'type': 'string',
            'description': "Format: 'vertical 9:16' or 'horizontal 16:9' or 'square 1:1'" },
        'setting_lighting': {
            'type': 'string',
            'description': "Detailed location + lighting description (e.g., 'lavish Korean mansion ballroom illuminated by crystal chandelier')" },
        'characters': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'description': {
                        'type': 'string',
                        'description': "Visual description (NO character names, e.g., 'elegant Korean woman in her 30s')" },
                    'emotion': {
                        'type': 'string',
                        'description': "Emotional state (e.g., 'cold confidence', 'visible tension')" },
                    'pose_gesture': {
                        'type': 'string',
                        'description': "Body pose and gestures (e.g., 'stands tall', 'trembling hands')" },
                    'action': {
                        'type': 'string',
                        'description': "Action being performed (e.g., 'places photographs onto table')" },
                    'dialogue': {
                        'type': 'string',
                        'description': 'Korean dialogue or key sentence this character speaks' } },
                'required': [
                    'description',
                    'emotion',
                    'pose_gesture',
                    'action'] },
            'description': 'Array of character details (1-3 characters)' },
        'camera_intent': {
            'type': 'string',
            'description': "Camera technique + motion direction + emotional purpose (e.g., 'Slow dolly in at eye level to build suffocating intimacy')" },
        'atmosphere_keywords': {
            'type': 'array',
            'items': {
                'type': 'string' },
            'description': "3 atmosphere keywords reinforcing camera and mood (e.g., ['cold', 'tense', 'claustrophobic'])" },
        'cinematic_prompt': {
            'type': 'string',
            'description': 'Full cinematic prompt combining all sections with motivated camera movement (300-500 characters)' },
        'video_feel': {
            'type': 'string',
            'description': 'Best matching video style category',
            'enum': [
                'news-info',
                'cinematic-drama',
                'action-thriller',
                'romantic',
                'horror-mystery',
                'documentary',
                'commercial'] } },
    'required': [
        'format_declaration',
        'setting_lighting',
        'characters',
        'camera_intent',
        'atmosphere_keywords',
        'cinematic_prompt',
        'video_feel'] }
CharacterDetail = <NODE:12>()
GrokPromptResult = <NODE:12>()

class GrokPromptAnalyzer:
    '''
    Grok Image-to-Video 프롬프트 생성기

    두 가지 모드 지원:
    1. 기본 모드 (호환성): 200자 이내 간결한 프롬프트
    2. 시네마틱 모드: 200-500자 7단계 구조 프롬프트

    7단계 시네마틱 프롬프트 구조:
    - 포맷 선언 (9:16/16:9)
    - 장소/조명 상세
    - 캐릭터 외모+감정+포즈+동작
    - 카메라 의도 (앵글+목적)
    - 대사 통합 ("speaks in Korean: \'대사\'")
    - 분위기 마무리 (3 키워드)
    '''
    GEMINI_MODEL = 'gemini-2.5-flash'
    
    def __init__(self = None, api_key = None):
        '''Initialize with API key from settings.'''
        configure_legacy_genai = configure_legacy_genai
        import app.utils.google_sdk
        Settings = Settings
        import app.models.settings
        if not api_key:
            settings = Settings.get_or_create()
            api_key = get_google_api_key_or_runtime_token(settings = settings)
        if not api_key:
            raise ValueError(get_google_configuration_error_message())
        self.genai = configure_legacy_genai(api_key)
        self.model = self.genai.GenerativeModel(self.GEMINI_MODEL)
        logger.info(f'''Grok Prompt Analyzer initialized: {self.GEMINI_MODEL}''')

    
    def analyze_image(self, image_path, image_bytes = None, image_url = None, narration_hint = None, cinematic_mode = (None, None, None, '', True, '9:16'), aspect_ratio = ('image_path', str, 'image_bytes', bytes, 'image_url', str, 'narration_hint', str, 'cinematic_mode', bool, 'aspect_ratio', str, 'return', GrokPromptResult)):
        '''
        이미지 분석하여 Grok 프롬프트 생성

        Args:
            image_path: 로컬 이미지 경로
            image_bytes: 이미지 바이트 데이터
            image_url: 이미지 URL (data: 또는 /data/ 형식)
            narration_hint: 나레이션 텍스트 (분위기 힌트로 활용)
            cinematic_mode: True=7단계 시네마틱 프롬프트, False=기존 200자 모드
            aspect_ratio: 영상 비율 ("9:16", "16:9", "1:1")

        Returns:
            GrokPromptResult: 생성된 프롬프트
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _load_image(self = None, image_path = None, image_bytes = None, image_url = (None, None, None)):
        '''이미지 로드 (data 디렉토리 기준 상대경로 지원)'''
        Path = Path
        import pathlib
        get_data_path = get_data_path
        import app.config.paths
        
        try:
            if image_bytes:
                return Image.open(BytesIO(image_bytes))
            if None:
                p = Path(image_path)
                if p.is_absolute() and p.exists():
                    return Image.open(p)
                abs_path = get_data_path() / image_path
                if abs_path.exists():
                    logger.debug(f'''Resolved image path: {abs_path}''')
                    return Image.open(abs_path)
                if None:
                    if image_url.startswith('data:'):
                        import base64
                        (header, data) = image_url.split(',', 1)
                        decoded = base64.b64decode(data)
                        return Image.open(BytesIO(decoded))
                    if None.startswith('/data/'):
                        relative_path = image_url[len('/data/'):]
                        file_path = get_data_path() / relative_path
                        if file_path.exists():
                            return Image.open(file_path)
                        None.warning(f'''Image not found at: {file_path}''')
            logger.warning(f'''No valid image source: path={image_path}, url={image_url}''')
            return None
        except Exception:
            e = None
            logger.error(f'''Failed to load image: {e}''', exc_info = True)
            e = None
            del e
            return None
            e = None
            del e


    
    def _analyze_with_gemini(self = None, image = None, narration_hint = None):
        '''Gemini Vision API로 이미지 분석 후 Grok 프롬프트 생성'''
        
        try:
            if narration_hint:
                context_section = f'''\n## 🎬 SCRIPT CONTEXT (DIALOGUE PRIORITY):\n"{narration_hint}"\n\n**DIALOGUE/SPEECH EXTRACTION PRIORITY (MOST IMPORTANT):**\n\n1. **FIRST PRIORITY - Character Dialogue (대사):**\n   - Look for patterns like [화자]: "대사", [Speaker]: "dialogue", "quoted speech"\n   - Extract the ACTUAL SPOKEN WORDS - this is what the character is saying\n   - Example: [진우]: "왜 이러는 거야..." → Focus on emotional expression of saying "왜 이러는 거야..."\n   - Example: [미래]: "정말 미안해..." → Show character expressing apology\n\n2. **SECOND PRIORITY - Key Dramatic Sentence:**\n   - If NO character dialogue exists, identify the MOST IMPACTFUL sentence\n   - Look for emotional peaks, conflict moments, revelations\n   - Extract the core dramatic statement that defines this scene\n\n3. **LAST PRIORITY - Narration Context:**\n   - Use [나레이션]/[Narration] only if no dialogue or key sentence exists\n\n**Your prompt MUST reflect the EMOTIONAL CONTENT of the dialogue/speech:**\n- If someone says "왜 이러는 거야..." → show desperation, pleading, emotional confrontation\n- If someone says "다 끝났어..." → show defeat, resignation, emotional collapse\n- The visual scene should MATCH what the character is expressing in their words\n\n**VISUAL GROUNDING RULE (CRITICAL):**\n- Use the CURRENT IMAGE as the primary source of truth.\n- Do NOT invent time/weather/location details not visible in the image.\n- Do NOT add "sunset/golden hour/night/rain" unless clearly visible.\n- If narration conflicts with image, follow the image.\n'''
            else:
                context_section = ''
            prompt = f'''You are a cinematic scene description expert for Grok Image-to-Video.\n\n{context_section}\n## 🚨 ABSOLUTE RULE - NO CHARACTER NAMES (CRITICAL):\nGrok AI CANNOT understand names like "Jinwoo", "Heukpung", "진우", "흑풍", "Mirae", etc.\nYou MUST replace ALL names with VISUAL DESCRIPTIONS:\n- "young man with dark hair" NOT "Jinwoo"\n- "menacing figure in shadow" NOT "Heukpung"\n- "woman in red dress" NOT "Mirae"\n- "old man with white beard" NOT "Elder Kim"\n\n## 📝 PROMPT PRIORITY (under 200 characters - USE AS MUCH AS POSSIBLE):\n\n**85% = SCENE DESCRIPTION** (based on DIALOGUE/SPEECH first, then context):\n- Describe the ACTION, EMOTION that MATCHES the spoken dialogue\n- If dialogue says "왜 이러는 거야..." → show confrontation, desperation, emotional appeal\n- If dialogue says "미안해..." → show regret, apology, emotional vulnerability\n- Be very specific: "man collapses to knees, hands trembling, mouth forming desperate plea" NOT "sad man"\n- Include body language, facial expressions that reflect the SPOKEN WORDS\n\n**10% = ATMOSPHERE/MOOD**:\n- lighting (golden, harsh, dim, flickering), weather, emotional tone\n\n**5% = CAMERA** (keep very brief at the end):\n- Just add "slow push-in" or "tracking shot"\n\n## LENGTH REQUIREMENT:\n- **TARGET: 150-199 CHARACTERS** - longer = better scene detail\n- Short prompts produce generic results. FILL the space with rich scene description.\n\n## 🎬 VIDEO FEEL ANALYSIS (AUTO-DETECT):\nAnalyze the scene and select the BEST matching video style:\n- "news-info": 뉴스/정보 - 고정 카메라, 깔끔한 구도, 중립적\n- "cinematic-drama": 시네마틱 드라마 - 영화적 구도, 감정 중심, 드라마틱\n- "action-thriller": 액션/스릴러 - 역동적 카메라, 긴장감, 빠른 전개\n- "romantic": 로맨틱 - 부드러운 조명, 따뜻한 톤, 감성적\n- "horror-mystery": 호러/미스터리 - 어두운 조명, 불안한 카메라, 서스펜스\n- "documentary": 다큐멘터리 - 자연스러운 촬영, 관찰자 시점\n- "commercial": 광고/CM - 세련된 구도, 밝은 조명, 역동적\n\n## 🗣️ KOREAN DIALOGUE/KEY SENTENCE EXTRACTION (PRIORITY ORDER):\n**Step 1 - Extract Character Dialogue:**\n- Look for [화자]: "대사" or [Speaker]: "dialogue" patterns (NOT [나레이션])\n- Extract the KOREAN dialogue text ONLY (not speaker name)\n- Example: [진우]: "왜 이러는 거야..." → "왜 이러는 거야..."\n\n**Step 2 - If NO dialogue, extract KEY SENTENCE:**\n- Find the most emotionally impactful or dramatically important Korean sentence\n- Rewrite it as direct character speech, not narration/exposition\n- This should be the core message/feeling of the scene\n- Example: "그는 모든 것을 잃었다는 것을 깨달았다" → "모든 것을 잃었어..."\n\n**Step 3 - Return empty if nothing meaningful:**\n- Only return "" if there\'s truly no dialogue or key sentence\n\n**Hard constraints for korean_dialogue:**\n- Must be a SHORT key phrase (max 15 chars). Compress to emotional core.\n- Return ONLY the raw Korean spoken words. Do NOT include "캐릭터는", age, gender, or voice descriptions.\n- Do NOT copy narration/exposition verbatim.\n- Do NOT use third-person explanatory style (e.g., "그는 ...했다").\n- Remove fillers (그런데, 사실은, 정말로). Keep only the dramatic essence.\n- Example: "이 기존 자세가 흔들리고 있다면..." → "정말 심각한 걸까?"\n- Example: "모든 것을 잃었다는 것을 깨달았다" → "다 끝났어..."\n- The line must sound like what the visible character says right now in this scene.\n\n## EXAMPLES:\n- "Young man in torn clothes falls to his knees in pouring rain, hands reaching desperately toward fading golden light, face twisted in anguish, slow zoom out"\n- "Woman in white dress clutches crumpled letter to her chest, tears streaming down pale cheeks, single candle flickers casting dancing shadows, static shot"\n- "Dark hooded figure looms menacingly over cowering man backed against cold stone wall, long shadows stretch across floor, harsh angular lighting, slow push-in"\n\nRespond ONLY in JSON:\n{{\n    "prompt": "DETAILED scene description (150-199 chars), visual subjects only, NO CHARACTER NAMES, reflecting DIALOGUE emotion",\n    "subject_action": "Very detailed visual description matching the SPOKEN DIALOGUE or key dramatic moment (NO NAMES)",\n    "camera_movement": "Brief camera technique",\n    "environment_lighting": "Mood and atmosphere matching dialogue/speech emotion",\n    "video_feel": "one of: news-info, cinematic-drama, action-thriller, romantic, horror-mystery, documentary, commercial",\n    "korean_dialogue": "인물이 직접 말하는 한국어 한 문장 (나레이션 복사 금지, 대사 우선/없으면 핵심문장 대사체 재작성)"\n}}'''
            response = self.model.generate_content([
                prompt,
                image], generation_config = {
                'temperature': 0.7,
                'max_output_tokens': 2000,
                'response_mime_type': 'application/json',
                'response_schema': GROK_PROMPT_SCHEMA })
            response_text = response.text.strip()
            
            try:
                data = json.loads(response_text)
                
                try:
                    pass
                except json.JSONDecodeError:
                    e = None
                    logger.warning(f'''JSON parse failed, trying fallback: {e}''')
                    import re
                    json_match = re.search('\\{[^{}]*\\}', response_text, re.DOTALL)
                    if json_match:
                        data = json.loads(json_match.group())
                    else:
                        
                        try:
                            del e
                            return None
                            
                            try:
                                None = 
                                del e
                            e = None
                            del e
                            try:
                                generated_prompt = data.get('prompt', '')
                                if len(generated_prompt) > 200:
                                    generated_prompt = generated_prompt[:197].rsplit(' ', 1)[0] + '...'
                                return GrokPromptResult(success = True, prompt = generated_prompt, subject_action = data.get('subject_action', ''), camera_movement = data.get('camera_movement', ''), environment_lighting = data.get('environment_lighting', ''), video_feel = data.get('video_feel', 'cinematic-drama'), korean_dialogue = data.get('korean_dialogue', ''))
                            except Exception:
                                e = None
                                logger.error(f'''Gemini analysis failed: {e}''', exc_info = True)
                                del e
                                return None
                                None = 
                                del e






    
    def _analyze_cinematic(self = None, image = None, narration_hint = None, aspect_ratio = ('', '9:16')):
        '''
        7단계 시네마틱 프롬프트 생성

        Args:
            image: PIL 이미지
            narration_hint: 나레이션 텍스트
            aspect_ratio: 영상 비율 ("9:16", "16:9", "1:1")

        Returns:
            GrokPromptResult: 시네마틱 프롬프트 포함
        '''
        
        try:
            format_map = {
                '9:16': 'vertical 9:16',
                '16:9': 'horizontal 16:9',
                '1:1': 'square 1:1' }
            format_declaration = format_map.get(aspect_ratio, 'vertical 9:16')
            if narration_hint:
                context_section = f'''\n## 🎬 SCRIPT/NARRATION CONTEXT:\n"{narration_hint}"\n\n**DIALOGUE EXTRACTION (CRITICAL):**\n1. Look for [화자]: "대사" patterns → Extract the Korean dialogue\n2. If no dialogue, extract the most dramatic/emotional Korean sentence\n3. Rewrite narration into direct character speech (do not copy narration verbatim)\n4. Compress to emotional core (max 15 chars). Remove fillers (그런데, 사실은, 정말로).\n5. Return ONLY the raw spoken dialogue text. Do NOT wrap it with character descriptions or voice instructions.\n\n**Dialogue quality rules:**\n- Return ONLY the raw Korean spoken words (e.g., "정말 심각한 걸까?"), NOT wrapped in any format.\n- Do NOT include "캐릭터는", age, gender, or voice descriptions in the dialogue field.\n- Spoken by the character in this scene, not narrator summary.\n- One SHORT key phrase (max 15 chars) in natural conversational Korean.\n- Avoid explanatory style and third-person narration.\n- Example: "이 기존 자세가 흔들리고 있다면..." → "정말 심각한 걸까?"\n\n**Scene fidelity rules (CRITICAL):**\n- Prioritize what is visible in the CURRENT image over narration/context text.\n- Do not add ungrounded time/weather clues (sunset, golden hour, rain, dawn, etc.).\n- If context conflicts with visible scene, follow visible scene.\n'''
            else:
                context_section = ''
            prompt = f'''You are a premium cinematic prompt engineer for Grok Image-to-Video.\n\n{context_section}\n\n## 🎯 7-SECTION CINEMATIC PROMPT STRUCTURE\n\nGenerate a detailed prompt following this EXACT structure. Front-load core subject/action in the first 30 words.\n\n### SECTION 1: FORMAT DECLARATION (MANDATORY)\nStart with: "A {format_declaration} cinematic shot"\n\n### SECTION 2: SETTING & LIGHTING\n- Detailed location description with specific lighting source\n- Example: "in a lavish Korean mansion ballroom illuminated by a massive crystal chandelier"\n- Lighting/time must be visually grounded in the current image only\n- Use active descriptors: "bathed in", "illuminated by", "cast in the glow of"\n\n### SECTION 3: CHARACTER(S) - FOR EACH CHARACTER:\n**CRITICAL: NO CHARACTER NAMES - Use visual descriptions only**\n- Visual appearance: "elegant Korean woman in her 30s", "young man with dark wavy hair"\n- Emotion: "with cold confidence", "visibly tense and emotional"\n- Pose/Gesture: "stands tall", "trembling hands reaching out"\n- Action: Use KINETIC VERBS (glides, drifts, rushes, clutches, slams) not passive descriptions\n- If multiple characters: include interaction dynamics (eye contact, distance, power balance)\n- Expressions and gestures must be grounded in visible cues from the current image\n\n### SECTION 4: CAMERA INTENT (CRITICAL - SCENE-APPROPRIATE MOVEMENT)\nChoose camera movement that MATCHES the scene\'s emotional intent. Every shot needs motivated movement.\n\n**CAMERA VOCABULARY - Select based on scene type:**\n\nFor DIALOGUE/CONVERSATION scenes:\n- "Slow dolly in toward the speaker to intensify emotional weight"\n- "Eye-level medium shot with subtle push-in during key line"\n- "Over-the-shoulder perspective shifting focus between characters"\n\nFor TENSION/CONFRONTATION scenes:\n- "Low-angle perspective slowly pushing forward to emphasize dominance"\n- "Handheld camera with subtle instability to heighten unease"\n- "Snap zoom into character\'s eyes at the moment of revelation"\n\nFor EMOTIONAL/DRAMATIC scenes:\n- "Slow crane up pulling away to reveal isolation"\n- "Close-up tracking shot drifting across the character\'s face to capture vulnerability"\n- "Gentle dolly out as character processes grief, expanding negative space"\n\nFor ACTION/MOVEMENT scenes:\n- "Dynamic tracking shot following the subject at matched pace"\n- "Whip pan to follow rapid motion with directional blur"\n- "Steadicam orbit circling the subject during decisive action"\n\nFor ESTABLISHING/LANDSCAPE scenes:\n- "Sweeping crane shot rising to reveal the full environment"\n- "Slow lateral truck across the scene to establish spatial context"\n- "Aerial descending shot settling onto the subject"\n\nFor INFORMATION/NEWS scenes:\n- "Locked-off static shot with clean centered framing"\n- "Gentle push-in to direct attention toward key visual element"\n\n**FORMAT: "[Camera technique] + [motion direction] + [emotional purpose]"**\nExample: "Slow dolly in at eye level to build intimacy before the confession"\nExample: "Low-angle handheld with slight drift to amplify the character\'s growing panic"\n\n### SECTION 5: DIALOGUE INTEGRATION (MANDATORY for ALL scenes)\n- Do NOT include dialogue in the cinematic_prompt. The frontend will add it separately.\n- Instead, put the raw spoken Korean phrase (max 15 chars) in the character\'s "dialogue" field only.\n- If no dialogue: Extract most dramatic sentence from narration, compress to emotional core (max 15 chars)\n- Remove fillers. Keep only the dramatic essence. Example: "이 기존 자세가 흔들리고 있다면..." → "정말 심각한 걸까?"\n- Dialogue tone must match visible expression and camera intent\n\n### SECTION 6: ATMOSPHERE CLOSURE\nEnd with 3 atmospheric keywords that reinforce the camera choice:\n- Tension scenes: "cold, tense, claustrophobic"\n- Emotional scenes: "melancholic, intimate, fading"\n- Action scenes: "urgent, kinetic, explosive"\n\n## 🚨 ABSOLUTE RULES:\n1. NO CHARACTER NAMES - Grok cannot understand "Jinwoo", "진우", etc.\n2. DIALOGUE MUST BE INTEGRATED into the prompt, not separate\n3. LENGTH: 300-500 characters (longer = better, richer results)\n4. Every character needs emotion + pose + kinetic action verb\n5. Camera movement MUST feel motivated by the scene, never arbitrary\n6. Static scenes feel artificial — add subtle or intentional movement always\n\n## 📋 EXAMPLE OUTPUTS:\n\n**Dialogue scene (cinematic_prompt should NOT contain dialogue - it goes in character dialogue field):**\n"A vertical 9:16 cinematic shot in a dimly lit Korean apartment kitchen bathed in cold fluorescent light. A weary man in his 40s with hollow eyes grips the edge of the counter, knuckles whitening, jaw clenched as he stares at a crumpled letter. Slow dolly in at eye level to compress the space and build suffocating intimacy. Desolate, confined, final."\n→ character dialogue field: "다 끝났어..."\n\n**Confrontation scene:**\n"A vertical 9:16 cinematic shot in a lavish Korean mansion ballroom illuminated by a massive crystal chandelier. A cold, elegant Korean woman in her 30s stands tall, sharp piercing gaze directed downward as she places photographs onto an ornate table with firm emphasis. Low-angle perspective pushing slowly forward to emphasize authority and dominance. Cold, tense, high-fashion."\n→ character dialogue field: "기억나?"\n\n**Action scene:**\n"A horizontal 16:9 cinematic shot on rain-soaked Seoul rooftop at night, neon signs reflecting off wet concrete. A hooded figure sprints toward the edge, coat billowing, arms pumping. Dynamic tracking shot at matched pace following the runner with shallow depth of field and motion blur. Urgent, kinetic, desperate."\n\nRespond ONLY in JSON with this structure:\n{{\n    "format_declaration": "{format_declaration}",\n    "setting_lighting": "Detailed location + lighting",\n    "characters": [\n        {{\n            "description": "Visual description (NO names)",\n            "emotion": "Emotional state",\n            "pose_gesture": "Body pose and gestures",\n            "action": "Action with KINETIC verb",\n            "dialogue": "Korean dialogue or key sentence"\n        }}\n    ],\n    "camera_intent": "[Camera technique] + [motion direction] + [emotional purpose]",\n    "atmosphere_keywords": ["keyword1", "keyword2", "keyword3"],\n    "cinematic_prompt": "FULL combined prompt (300-500 chars) with dialogue and camera integrated",\n    "video_feel": "one of: news-info, cinematic-drama, action-thriller, romantic, horror-mystery, documentary, commercial"\n}}'''
            response = self.model.generate_content([
                prompt,
                image], generation_config = {
                'temperature': 0.7,
                'max_output_tokens': 3000,
                'response_mime_type': 'application/json',
                'response_schema': GROK_CINEMATIC_PROMPT_SCHEMA })
            response_text = response.text.strip()
            
            try:
                data = json.loads(response_text)
                
                try:
                    pass
                except json.JSONDecodeError:
                    e = None
                    logger.warning(f'''Cinematic JSON parse failed, trying fallback: {e}''')
                    import re
                    json_match = re.search('\\{.*\\}', response_text, re.DOTALL)
                    if json_match:
                        data = json.loads(json_match.group())
                    else:
                        
                        try:
                            del e
                            return None
                            
                            try:
                                None = 
                                del e
                            e = None
                            del e
                            try:
                                characters = []
                                for char_data in data.get('characters', []):
                                    characters.append(CharacterDetail(description = char_data.get('description', ''), emotion = char_data.get('emotion', ''), pose_gesture = char_data.get('pose_gesture', ''), action = char_data.get('action', ''), dialogue = char_data.get('dialogue', '')))
                                    cinematic_prompt = data.get('cinematic_prompt', '')
                                    if len(cinematic_prompt) > 500:
                                        cinematic_prompt = cinematic_prompt[:497].rsplit(' ', 1)[0] + '...'
                                korean_dialogue = ''
                                for char in characters:
                                    if char.dialogue:
                                        korean_dialogue = char.dialogue
                                        None, GrokPromptResult(success = False, error = 'Failed to parse cinematic response')
                                    
                                legacy_prompt = cinematic_prompt[:200] if len(cinematic_prompt) > 200 else cinematic_prompt
                                return GrokPromptResult(success = True, prompt = legacy_prompt, subject_action = characters[0].action if characters else '', camera_movement = data.get('camera_intent', ''), environment_lighting = data.get('setting_lighting', ''), video_feel = data.get('video_feel', 'cinematic-drama'), korean_dialogue = korean_dialogue, cinematic_prompt = cinematic_prompt, format_declaration = data.get('format_declaration', format_declaration), setting_lighting = data.get('setting_lighting', ''), characters = characters, camera_intent = data.get('camera_intent', ''), atmosphere_keywords = data.get('atmosphere_keywords', []))
                            except Exception:
                                e = None
                                logger.error(f'''Cinematic analysis failed: {e}''', exc_info = True)
                                del e
                                return None
                                None = 
                                del e






    
    def analyze_batch(self = None, images = None, cinematic_mode = None, aspect_ratio = (True, '9:16')):
        '''
        여러 이미지 일괄 분석

        Args:
            images: [{"image_path": str, "narration_hint": str}, ...]
            cinematic_mode: True=7단계 시네마틱 프롬프트, False=기존 200자 모드
            aspect_ratio: 영상 비율 ("9:16", "16:9", "1:1")

        Returns:
            list[GrokPromptResult]: 분석 결과 리스트
        '''
        results = []
        for img_info in images:
            result = self.analyze_image(image_path = img_info.get('image_path'), image_bytes = img_info.get('image_bytes'), image_url = img_info.get('image_url'), narration_hint = img_info.get('narration_hint', ''), cinematic_mode = cinematic_mode, aspect_ratio = aspect_ratio)
            results.append(result)
            return results

    
    def analyze_batch_with_context(self, images = None, story_context = None, chapter_title = None, cinematic_mode = (None, None, True, '9:16'), aspect_ratio = ('images', list[dict], 'story_context', str, 'chapter_title', str, 'cinematic_mode', bool, 'aspect_ratio', str, 'return', list[GrokPromptResult])):
        '''
        문맥 연속성을 반영한 배치 분석

        이전 씬의 분석 결과를 다음 씬 분석 시 컨텍스트로 전달하여
        영상 연속성을 높임.

        Args:
            images: [{
                "scene_id": str,
                "image_path": str,
                "image_url": str,
                "narration_hint": str,
                "previous_narration": str,  # 이전 씬 나레이션
                "next_narration": str       # 다음 씬 나레이션
            }, ...]
            story_context: 전체 스토리 맥락 (예: "rising action", "climax")
            chapter_title: 현재 챕터 제목
            cinematic_mode: True=7단계 시네마틱 프롬프트, False=기존 200자 모드
            aspect_ratio: 영상 비율 ("9:16", "16:9", "1:1")

        Returns:
            list[GrokPromptResult]: 분석 결과 리스트 (연속성 반영)
        '''
        results = []
        previous_result = None
        for i, img_info in enumerate(images):
            context_parts = []
            if story_context:
                context_parts.append(f'''Story arc: {story_context}''')
            if chapter_title:
                context_parts.append(f'''Chapter: {chapter_title}''')
            prev_narration = img_info.get('previous_narration', '')
            if prev_narration:
                context_parts.append(f'''Previous scene: {prev_narration[:100]}''')
            if previous_result and previous_result.success:
                if not previous_result.camera_intent:
                    camera_info = previous_result.camera_movement
                    context_parts.append(f'''Previous camera: {camera_info}''')
                    next_narration = img_info.get('next_narration', '')
                    if next_narration:
                        context_parts.append(f'''Next scene: {next_narration[:100]}''')
            current_narration = img_info.get('narration_hint', '')
            if context_parts:
                enhanced_hint = f'''{current_narration}\n\n[CONTEXT]\n''' + '\n'.join(context_parts)
            else:
                enhanced_hint = current_narration
            result = self.analyze_image(image_path = img_info.get('image_path'), image_bytes = img_info.get('image_bytes'), image_url = img_info.get('image_url'), narration_hint = enhanced_hint, cinematic_mode = cinematic_mode, aspect_ratio = aspect_ratio)
            results.append(result)
            previous_result = result
            return results


_analyzer_instance = None

def get_grok_prompt_analyzer():
    '''Get singleton instance of GrokPromptAnalyzer'''
    pass
# WARNING: Decompyle incomplete
