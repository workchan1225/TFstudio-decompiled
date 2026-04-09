# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tone_analysis_service.pyc (Python 3.11)

'''
Tone Analysis Service - 화자 톤 분석 서비스

화자의 대사를 Gemini 2.5로 분석하여 Gemini TTS에 적합한 톤 프롬프트를 생성합니다.
캐릭터의 성격, 나이, 감정 상태 등을 추론하여 영어 프롬프트로 변환합니다.

Enhancement v2:
- 나이대별 음성 특성 상세화 (아동/청소년/청년/중년/노년)
- 대인 관계 태도 분석 (권위, 온기, 소통 스타일)
- 캐릭터 정보 없을 때 대사에서 자동 추론
'''
import logging
import re
from typing import List, Optional, Dict, Any
from app.utils.google_sdk import configure_legacy_genai
logger = logging.getLogger(__name__)
AGE_VOICE_CHARACTERISTICS = {
    'child': {
        'pitch': 'higher pitch',
        'energy': 'energetic and lively',
        'quality': 'innocent, bright, and playful',
        'pacing': 'fast-paced with bursts of excitement',
        'keywords': [
            '아동',
            '어린이',
            '아이',
            '초등',
            '유아',
            '10대 초반',
            '10세',
            '11세',
            '12세',
            '7세',
            '8세',
            '9세'] },
    'teen': {
        'pitch': 'slightly higher pitch with youthful uncertainty',
        'energy': 'fluctuating between confident and awkward',
        'quality': 'youthful, sometimes rebellious or self-conscious',
        'pacing': 'variable tempo, fast when excited, hesitant when unsure',
        'keywords': [
            '청소년',
            '10대',
            '중학생',
            '고등학생',
            '십대',
            '13세',
            '14세',
            '15세',
            '16세',
            '17세',
            '18세',
            '19세'] },
    'young_adult': {
        'pitch': 'clear, natural pitch',
        'energy': 'confident or cautiously optimistic',
        'quality': 'fresh, articulate, modern speech patterns',
        'pacing': 'natural conversational rhythm',
        'keywords': [
            '청년',
            '20대',
            '30대 초반',
            '대학생',
            '사회초년생',
            '젊은',
            '20세',
            '25세',
            '30세',
            '35세'] },
    'middle_aged': {
        'pitch': 'deeper, more resonant voice',
        'energy': 'measured, authoritative, experienced',
        'quality': 'gravitas, weight of experience, steady confidence',
        'pacing': 'deliberate pacing with strategic pauses',
        'keywords': [
            '중년',
            '40대',
            '50대',
            '30대 후반',
            '40대 중반',
            '50대 초반',
            '36세',
            '40세',
            '45세',
            '50세',
            '55세'] },
    'elderly': {
        'pitch': 'aged vocal quality, potentially slightly raspy',
        'energy': 'calm wisdom, gentle authority',
        'quality': 'weathered, wise, contemplative',
        'pacing': 'slower, more measured delivery with reflective pauses',
        'keywords': [
            '노년',
            '60대',
            '70대',
            '80대',
            '할머니',
            '할아버지',
            '노인',
            '어르신',
            '56세',
            '60세',
            '65세',
            '70세'] } }
RELATIONSHIP_ATTITUDE_FRAMEWORK = "\n## Interpersonal Relationship Analysis\nAnalyze the speaker's attitude in relationships and reflect it in their vocal delivery:\n\n1. **Authority Level** (affects tone and confidence)\n   - Commanding: Takes control, gives orders, expects compliance → firm, unwavering tone\n   - Equal: Peer-to-peer interaction, mutual respect → balanced, conversational tone\n   - Submissive: Deferent, seeks approval, follows others' lead → softer, uncertain tone\n\n2. **Social Warmth** (affects emotional coloring)\n   - Warm/Friendly: Open, approachable, emotionally available → inviting, gentle inflections\n   - Neutral/Professional: Appropriate distance, task-focused → measured, controlled delivery\n   - Cold/Distant: Emotionally guarded, calculated responses → flat affect, minimal warmth\n   - Cautious: Hesitant, testing boundaries, protective → careful pacing, guarded tone\n\n3. **Communication Style** (affects speech patterns)\n   - Direct: Says exactly what they mean, no sugarcoating → clear, assertive delivery\n   - Diplomatic: Tactful, considers feelings, softens difficult messages → gentle, measured speech\n   - Evasive: Avoids direct answers, deflects, changes subject → trailing off, hesitations\n   - Manipulative: Strategic word choices to influence others → honeyed, persuasive tones\n"
TONE_ANALYSIS_SYSTEM_PROMPT_WITH_CHARACTER_ENHANCED = 'You are an elite voice director for premium audiobook and drama productions.\nYour task is to analyze a character based on their profile AND dialogue lines, creating an EXTREMELY DETAILED voice direction prompt for text-to-speech generation.\n\n## Character Profile Integration\nUse the provided character information as your FOUNDATION:\n- Age dictates vocal quality, energy level, and pitch range\n- Gender determines pitch baseline and speech patterns\n- Appearance/clothing hints at social status and demeanor\n- Profile/personality defines emotional delivery and attitude\n\n## Age-Specific Voice Characteristics (CRITICAL - Apply precisely)\n{age_characteristics}\n\n{relationship_framework}\n\n## Dialogue Pattern Analysis\nSupplement the profile by analyzing the dialogues to understand:\n- How does this character EXPRESS their personality through speech?\n- What emotional undertones are present?\n- What is their attitude toward others (authority, warmth, style)?\n- What subtext is hidden beneath the words?\n\n## Output Requirements\nCreate a voice direction prompt (80-150 words) that:\n1. MATCHES the character\'s age with SPECIFIC vocal characteristics (pitch, energy, pacing)\n2. MATCHES the character\'s gender with appropriate pitch/tone\n3. REFLECTS their stated personality traits\n4. INCORPORATES relationship attitude patterns from dialogue analysis\n5. ADDS nuance discovered from dialogue patterns\n\nCRITICAL RULES:\n- Output ONLY the voice direction prompt - no analysis, no headers, no explanations\n- Write in English only\n- Be SPECIFIC and VIVID - avoid generic descriptions like "speaks naturally"\n- The character profile is FACT - do not contradict it\n- Include age-appropriate pacing, pitch, and energy descriptions\n- Start with "Speak as..." followed by detailed character vocal portrait'
TONE_ANALYSIS_SYSTEM_PROMPT_AUTO_INFER = 'You are an elite voice director for premium audiobook and drama productions.\nYour task is to FIRST INFER the character\'s identity from their Korean dialogue, then create an EXTREMELY DETAILED voice direction prompt.\n\n## Step 1: Character Inference (CRITICAL for characters without profile data)\nBefore creating voice direction, you MUST analyze the Korean dialogues to infer:\n\n### Gender Inference\n- Speech endings: ~해요/~합니다 vs ~하지/~한다 patterns\n- Self-reference: 나/저 usage, 오빠/언니/형/누나 references to/from others\n- Vocabulary choices: typically masculine/feminine expressions in Korean\n- Context clues: topics discussed, social dynamics\n\n### Age Range Inference\n- Vocabulary sophistication and slang usage (MZ세대 vs 기성세대 expressions)\n- Energy level and speech patterns\n- Topics discussed and life experience implied\n- Formality patterns: 존댓말/반말 usage and switching\n- Generational speech markers\n\n### Atmosphere/Mood Inference\n- Dominant emotional undertone\n- Tension or relaxation in speech\n- Relationship dynamics with others\n\n## Step 2: Age-Appropriate Voice Characteristics\nApply these characteristics based on inferred age:\n\n### Child (아동, ~12세)\n- Higher pitch, energetic and lively delivery\n- Innocent, bright, and playful quality\n- Fast-paced with bursts of excitement\n\n### Teen (청소년, 13-19세)\n- Slightly higher pitch with youthful uncertainty\n- Fluctuating between confident and awkward\n- Variable tempo based on emotional state\n\n### Young Adult (청년, 20-35세)\n- Clear, natural pitch\n- Fresh, articulate, modern speech patterns\n- Natural conversational rhythm\n\n### Middle-Aged (중년, 36-55세)\n- Deeper, more resonant voice\n- Measured, authoritative, experienced\n- Deliberate pacing with strategic pauses\n\n### Elderly (노년, 56세+)\n- Aged vocal quality with wisdom\n- Calm, gentle authority\n- Slower, contemplative delivery\n\n{relationship_framework}\n\n## Output Requirements\nCreate a voice direction prompt (80-150 words) that:\n1. Reflects your INFERRED gender (state it clearly)\n2. Reflects your INFERRED age range with SPECIFIC vocal characteristics\n3. Captures the INFERRED atmosphere and mood\n4. Incorporates relationship attitude patterns discovered\n5. Is SPECIFIC and VIVID - avoid generic descriptions\n\nCRITICAL RULES:\n- Output ONLY the voice direction prompt - no analysis, no headers, no explanations\n- Write in English only\n- Begin with "Speak as..." followed by your inferred character description\n- Include specific vocal qualities (pitch, pacing, energy, tone)\n- Reference relationship dynamics where relevant'
TONE_ANALYSIS_SYSTEM_PROMPT_WITH_CHARACTER = "You are an elite voice director for premium audiobook and drama productions.\nYour task is to analyze a character based on their profile AND dialogue lines, creating an EXTREMELY DETAILED voice direction prompt for text-to-speech generation.\n\n## Character Profile Analysis\nUse the provided character information (age, gender, appearance, personality) as the FOUNDATION for your voice direction. This is explicit information - use it directly!\n\n## Dialogue Analysis\nSupplement the character profile by analyzing the dialogues to understand:\n- How does this character EXPRESS their personality through speech?\n- What emotional undertones are present?\n- What subtext is hidden beneath the words?\n\n## Output Requirements\nCreate a voice direction that:\n1. MATCHES the character's age and gender exactly\n2. REFLECTS their stated personality traits\n3. INCORPORATES their social role/profession\n4. ADDS nuance discovered from their dialogue patterns\n\nCRITICAL RULES:\n- Output ONLY the voice direction prompt - no analysis, no headers, no explanations\n- Write in English only\n- Be SPECIFIC and VIVID - avoid generic descriptions\n- The character profile is FACT - do not contradict it\n- Make every word count toward creating a unique vocal portrait"
TONE_ANALYSIS_SYSTEM_PROMPT = 'You are an elite voice director for premium audiobook and drama productions.\nYour task is to analyze a character\'s dialogue lines and create an EXTREMELY DETAILED voice direction prompt for text-to-speech generation.\n\n## Analysis Framework\nDeeply analyze the dialogues to determine:\n\n1. **Character Archetype & Role**\n   - What type of person is this? (villain, hero, mentor, victim, authority figure, etc.)\n   - What is their social position or profession?\n   - What life experiences shaped them?\n\n2. **Psychological Profile**\n   - Core personality traits (arrogant, humble, cunning, naive, bitter, hopeful)\n   - Hidden emotions beneath the surface\n   - Attitude toward others (contemptuous, caring, manipulative, sincere)\n   - Internal conflicts or motivations\n\n3. **Voice Characteristics**\n   - Age and gender-appropriate vocal quality\n   - Pitch range (deep, mid, high)\n   - Speaking rhythm (slow and deliberate, rapid and nervous, measured and controlled)\n   - Unique vocal mannerisms (sighs, pauses, emphasis patterns)\n\n4. **Emotional Delivery**\n   - Dominant emotional undertone\n   - How emotions manifest in speech (suppressed anger, barely contained excitement)\n   - Intensity level (subtle, moderate, intense)\n\n5. **Contextual Behavior**\n   - How do they speak to different people?\n   - What are they trying to achieve with their words?\n   - What do they NOT say but imply?\n\n## Output Format\nWrite a RICH, DETAILED voice direction prompt (3-5 sentences, 80-150 words) that paints a vivid picture of exactly how this character should sound. Include:\n- WHO they are (archetype + background)\n- HOW they feel (emotional state + attitude)\n- HOW they speak (vocal qualities + delivery style)\n- WHAT they convey (subtext + intention)\n\n## Example Output\n"Speak as an oppressive dictator who has ruthlessly amassed wealth through exploitation. His voice should drip with barely concealed contempt for ordinary citizens, each word delivered with cold, measured precision that hints at the violence lurking beneath his calm exterior. Use a deep, authoritative tone with deliberate pauses that make subordinates hang on every threatening syllable. His speech patterns should convey absolute certainty in his own superiority, occasionally letting slip a cruel satisfaction when discussing his enemies\' suffering."\n\nCRITICAL RULES:\n- Output ONLY the voice direction prompt - no analysis, no headers, no explanations\n- Write in English only\n- Be SPECIFIC and VIVID - avoid generic descriptions\n- Make every word count toward creating a unique vocal portrait'
TONE_ANALYSIS_USER_PROMPT_WITH_CHARACTER = "## Character Profile (USE THIS AS THE FOUNDATION)\n- **Name**: {speaker}\n- **Age**: {age}\n- **Gender**: {gender}\n- **Appearance**: {appearance}\n- **Personality/Profile**: {profile}\n\n## Sample Dialogues (analyze for emotional delivery and speech patterns)\n{dialogues}\n\nCreate a detailed, vivid voice direction prompt (3-5 sentences, 80-150 words) that:\n1. Perfectly matches this character's age and gender\n2. Reflects their personality traits\n3. Captures their unique vocal identity based on both profile and dialogue patterns"
TONE_ANALYSIS_USER_PROMPT = "Character name: {speaker}\n\nSample dialogues from this character (analyze the subtext, emotional undertones, and what these lines reveal about the speaker's personality):\n{dialogues}\n\nCreate a detailed, vivid voice direction prompt that would allow a voice actor to perfectly embody this character's unique vocal identity."

class ToneAnalysisService:
    '''화자 톤 분석 서비스 - Gemini 2.5를 활용한 캐릭터 음성 톤 분석

    Enhancement v2:
    - 나이대별 음성 특성 상세화
    - 대인 관계 태도 분석
    - 캐릭터 정보 없을 때 대사에서 자동 추론
    '''
    
    def __init__(self = None, api_key = None):
        '''
        Args:
            api_key: Google API 키
        '''
        self.api_key = api_key
        self.genai = configure_legacy_genai(api_key)
        self.model = self.genai.GenerativeModel('gemini-2.5-flash')
        logger.info('ToneAnalysisService 초기화 완료 (gemini-2.5-flash)')

    
    def analyze_speaker_tone(self = None, speaker = None, dialogues = None, character_info = (None,)):
        '''
        화자의 대사를 분석하여 Gemini TTS용 톤 프롬프트 생성

        Enhancement v2:
        - 캐릭터 정보가 있을 때: 나이별 음성 특성 + 대인관계 분석 적용
        - 캐릭터 정보가 없을 때: 대사에서 성별/나이/분위기 자동 추론

        Args:
            speaker: 화자 이름 (예: "민수", "나레이션")
            dialogues: 화자의 대사 목록
            character_info: 캐릭터 정보 (선택사항)
                - ageRange: 나이대 (예: "40대 중반")
                - gender: 성별 ("male", "female", "unknown")
                - appearance: 외모 설명
                - profile: 인적사항 (직업, 성격 등)

        Returns:
            영어 톤 프롬프트 (예: "Speak as a warm grandmother with gentle...")
        '''
        if not dialogues:
            return self._get_default_prompt(speaker)
        sample_dialogues = None[:10]
        dialogues_text = (lambda .0: [ f'''- "{d}"''' for d in .0 ])(sample_dialogues())
        
        try:
            response = self.model.generate_content(full_prompt, generation_config = {
                'max_output_tokens': 500,
                'temperature': 0.8 })
            result = response.text.strip()
            logger.info(f'''[Tone Analysis] Speaker: {speaker}, Result length: {len(result)}''')
            return result
        except Exception:
            e = None
            logger.error(f'''Tone analysis failed for {speaker}: {e}''')
            del e
            return None
            None = 
            del e


    
    def _has_meaningful_character_info(self = None, character_info = None):
