# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: translation_service.pyc (Python 3.11)

'''
Translation Service - 대본 번역 서비스 (Gemini AI 사용)

다국어 대본 지원을 위한 번역 서비스.
화자 태그 형식을 유지하면서 대본을 번역합니다.

일본어의 경우 TTS용(히라가나)과 자막용(한자) 버전을 분리하여 생성합니다.
'''
import logging
from typing import Optional, TypedDict
from app.utils.google_sdk import configure_legacy_genai
from app.models.settings import Settings
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
logger = logging.getLogger(__name__)

class JapaneseTranslation(TypedDict):
    mapping: str = '일본어 번역 결과 (TTS/자막 분리 + 매핑)'


class TranslationService:
    '''대본 번역 서비스 (Gemini AI 사용)'''
    SUPPORTED_LANGUAGES = [
        '한국어',
        '영어',
        '일본어']
    LANGUAGE_CODES = {
        '한국어': 'ko',
        '영어': 'en',
        '일본어': 'ja' }
    LANGUAGE_NAMES = {
        '한국어': 'Korean',
        '영어': 'English',
        '일본어': 'Japanese' }
    
    def __init__(self = None, api_key = None):
        '''Initialize translation service with API key.'''
        if not api_key:
            settings = Settings.get_or_create()
            api_key = get_google_api_key_or_runtime_token(settings = settings)
        if not api_key:
            raise ValueError(get_google_configuration_error_message())
        self.genai = configure_legacy_genai(api_key)
        self.model = self.genai.GenerativeModel('gemini-2.5-flash')

    
    def translate_script(self = None, script = None, target_language = None, source_language = ('한국어',)):
        """
        대본 번역 (화자명 포함)

        Args:
            script: 원본 대본 (한국어)
            target_language: 대상 언어 ('영어' | '일본어')
            source_language: 원본 언어 (기본값: '한국어')

        Returns:
            번역된 대본 (화자 태그 형식 유지)
        """
        if target_language not in self.SUPPORTED_LANGUAGES:
            raise ValueError(f'''Unsupported target language: {target_language}''')
        if target_language == source_language:
            return script
        target_lang_name = None.LANGUAGE_NAMES.get(target_language, target_language)
        source_lang_name = self.LANGUAGE_NAMES.get(source_language, source_language)
        prompt = self._build_translation_prompt(script = script, source_language = source_lang_name, target_language = target_lang_name)
        
        try:
            response = self.model.generate_content(prompt, generation_config = {
                'temperature': 0.3,
                'max_output_tokens': 40000 })
            if response.text:
                translated = response.text.strip()
                if translated.startswith('```'):
                    lines = translated.split('\n')
                    if lines[0].startswith('```'):
                        lines = lines[1:]
                    if lines and lines[-1].strip() == '```':
                        lines = lines[:-1]
                    translated = '\n'.join(lines)
                return translated.strip()
            None.error('Empty response from translation model')
            raise ValueError('Translation failed: empty response')
        except Exception:
            e = None
            logger.error(f'''Translation failed: {e}''')
            raise 
            e = None
            del e


    
    def _build_translation_prompt(self = None, script = None, source_language = None, target_language = ('script', str, 'source_language', str, 'target_language', str, 'return', str)):
        '''번역 프롬프트 생성'''
        return f'''You are a professional script translator for video content.\n\n## Task\nTranslate the following {source_language} script to {target_language}.\nIMPORTANT: Translate the ENTIRE script completely. Do not omit or summarize any part.\n\n## Critical Rules\n1. TRANSLATE speaker tags: [나레이션] → [Narration] (English) / [ナレーション] (Japanese)\n2. Preserve the [Speaker]: format exactly - each speaker tag must be on a new line\n3. Maintain emotional tone and dramatic effect\n4. Keep ALL paragraph structures and line breaks EXACTLY as in the original\n5. Adapt cultural references appropriately for the target audience\n6. Translate character names to natural target language equivalents or romanize them\n\n## Chapter/Section Title Rules (CRITICAL)\n- Chapter titles marked with ##, ###, or similar headers MUST be preserved and translated\n- Section dividers (like "---", "***", "===") MUST be kept exactly as-is\n- If there\'s a title line like "## 챕터 1: 시작" → "## Chapter 1: Beginning" (English) / "## 第1章: 始まり" (Japanese)\n- NEVER skip or remove chapter headers\n- Keep the exact same heading level (## stays ##, ### stays ###)\n\n## Speaker Tag Translations (Korean → English / Japanese)\n- 나레이션 → Narration / ナレーション\n- 나레이터 → Narrator / ナレーター\n- Other Korean names: Romanize (e.g., 민수 → Minsu / ミンス)\n\n## Format Rules\n- Keep the [Speaker]: format on each line\n- Preserve empty lines between paragraphs\n- Preserve ALL chapter/section headers\n- Do not add any explanations or notes\n- Output ONLY the translated script, nothing else\n- Do NOT truncate or summarize - translate EVERY line\n\n## Example\nInput (Korean):\n## 챕터 1: 운명의 밤\n\n[나레이션]: 어둠이 내려앉은 밤, 그는 선택의 기로에 섰다.\n[민수]: 정말 여기가 맞아?\n[수진]: 확신할 수 없어... 하지만 갈 수밖에 없어.\n\n---\n\n## 챕터 2: 결정\n\n[나레이션]: 시간이 흘렀다.\n\nOutput (English):\n## Chapter 1: Night of Destiny\n\n[Narration]: On a night when darkness had fallen, he stood at a crossroads.\n[Minsu]: Is this really the right place?\n[Sujin]: I can\'t be sure... but we have no choice but to go.\n\n---\n\n## Chapter 2: Decision\n\n[Narration]: Time passed.\n\nOutput (Japanese):\n## 第1章: 運命の夜\n\n[ナレーション]: 闇が降りた夜、彼は選択の岐路に立っていた。\n[ミンス]: 本当にここで合ってる?\n[スジン]: 確信は持てない...でも行くしかない。\n\n---\n\n## 第2章: 決定\n\n[ナレーション]: 時が流れた。\n\n---\n\n## Script to Translate ({source_language} → {target_language})\nTotal lines to translate: {len(script.splitlines())} lines\nYou MUST translate ALL {len(script.splitlines())} lines completely.\n\n{script}\n\n---\n\n## Translated Script ({target_language})\nTranslate the ENTIRE script above. Do not skip any line.\n'''

    
    def translate_script_japanese_dual(self = None, script = None, source_language = None):
        """
        일본어 번역 (TTS/자막 분리) - 2단계 방식

        한자를 사용하는 일본어 특성상:
        - 자막용: 한자 포함 (시청자가 읽기 편하도록)
        - TTS용: 히라가나/가타카나 위주 (음성 합성기가 제대로 읽도록)

        2단계 방식으로 안정적인 분리 보장:
        1단계: 한국어 → 일본어 자막용 (한자 포함)
        2단계: 자막용 → TTS용 (히라가나 변환)

        Args:
            script: 원본 대본 (한국어)
            source_language: 원본 언어 (기본값: '한국어')

        Returns:
            JapaneseTranslation: {'tts': '...', 'subtitle': '...'}
        """
        source_lang_name = self.LANGUAGE_NAMES.get(source_language, source_language)
        
        try:
            logger.info('Japanese translation step 1: Translating to subtitle version (with kanji)')
            subtitle_version = self._translate_to_japanese_subtitle(script, source_lang_name)
            if not subtitle_version:
                raise ValueError('Step 1 failed: Empty subtitle translation')
            logger.info('Japanese translation step 2: Converting to TTS version (hiragana)')
            tts_version = self._convert_to_hiragana_for_tts(subtitle_version)
            if not tts_version:
                logger.warning('Step 2 failed: Using subtitle version for TTS')
                tts_version = subtitle_version
            logger.info('Japanese translation step 3: Generating mapping version (punctuation-based)')
            mapping_version = self._generate_mapping_version(tts_version, subtitle_version)
            logger.info(f'''Japanese dual translation completed. Subtitle: {len(subtitle_version)} chars, TTS: {len(tts_version)} chars, Mapping: {len(mapping_version)} chars''')
            return JapaneseTranslation(tts = tts_version, subtitle = subtitle_version, mapping = mapping_version)
        except Exception:
            e = None
            logger.error(f'''Japanese dual translation failed: {e}''')
            raise 
            e = None
            del e


    
    def _translate_to_japanese_subtitle(self = None, script = None, source_language = None):
        '''1단계: 한국어 → 일본어 자막용 번역 (한자 포함, 읽기 편함)'''
        prompt = f'''# Role\nYou are a professional translator who localizes Korean content for the Japanese market.\n\n## Task\nTranslate the following {source_language} script to Japanese for SUBTITLE display.\n\n## Guidelines\n- Use natural kanji-kana mixture for readability on screen\n- Translate Korean names to katakana (민수 → ミンス, 수진 → スジン)\n- Preserve chapter markers format (## 챕터 1 → ## 第1章)\n- Keep speaker tags format ([나레이션] → [ナレーション])\n- Maintain dramatic tone and emotional arc\n- Translate the ENTIRE script - do not skip any line\n\n## Speaker Tag Translations\n- 나레이션 → ナレーション\n- 나레이터 → ナレーター\n- Korean names → Katakana\n\n## Chapter/Section Rules\n- Keep ## and ### markers\n- Translate chapter titles: 챕터 1: 시작 → 第1章: 始まり\n- Keep dividers (---, ***) as-is\n\n## Script to Translate\nTotal lines: {len(script.splitlines())}\n\n{script}\n\n## Japanese Translation (subtitle version with kanji)\nOutput ONLY the translated script. No explanations.\n'''
        response = self.model.generate_content(prompt, generation_config = {
            'temperature': 0.3,
            'max_output_tokens': 40000 })
        if response.text:
            return self._clean_response(response.text)

    
    def _convert_to_hiragana_for_tts(self = None, japanese_text = None):
        '''2단계: 자막용 → TTS용 변환 (한자 → 히라가나)'''
        prompt = f'''# Role\nYou are a Japanese text processor for TTS (text-to-speech) systems.\n\n## Task\nConvert the following Japanese text to a TTS-friendly version:\n- Convert kanji to hiragana for clear pronunciation\n- Keep katakana as-is (foreign words, names, emphasis)\n- Keep proper nouns in katakana (ミンス, スジン, etc.)\n- Preserve all formatting (chapter markers, speaker tags, line breaks)\n\n## Important Rules\n- Do NOT change the meaning or translate again\n- Only convert kanji → hiragana for pronunciation clarity\n- Output the ENTIRE text - do not skip any line\n- Keep [ナレーション]: format exactly\n\n## Example\nInput: 今日は良い日だ。彼は選択の岐路に立っていた。\nOutput: きょうはいいひだ。かれはせんたくのきろにたっていた。\n\n## Japanese Text (subtitle version)\nTotal lines: {len(japanese_text.splitlines())}\n\n{japanese_text}\n\n## TTS Version (hiragana conversion)\nOutput ONLY the converted text. No explanations.\n'''
        response = self.model.generate_content(prompt, generation_config = {
            'temperature': 0.2,
            'max_output_tokens': 40000 })
        if response.text:
            return self._clean_response(response.text)

    
    def _clean_response(self = None, text = None):
        '''응답 텍스트 정리 (코드 블록 제거 등)'''
        text = text.strip()
        if text.startswith('```'):
            lines = text.split('\n')
            if lines[0].startswith('```'):
                lines = lines[1:]
            if lines and lines[-1].strip() == '```':
                lines = lines[:-1]
            text = '\n'.join(lines)
        return text.strip()

    
    def _generate_mapping_version(self = None, tts_text = None, subtitle_text = None):
        '''
        구두점 기반으로 자막용과 TTS용 텍스트를 매핑

        Args:
            tts_text: TTS용 텍스트 (히라가나 위주)
            subtitle_text: 자막용 텍스트 (한자 포함)

        Returns:
            매핑용 텍스트: "자막(TTS)구두점자막(TTS)구두점..."
        '''
        import re
        PUNCTUATION_PATTERN = '([。、！？!?])'
        tts_lines = tts_text.split('\n')
        sub_lines = subtitle_text.split('\n')
        result_lines = []
        min_lines = min(len(tts_lines), len(sub_lines))
        for i in range(min_lines):
            tts_line = tts_lines[i].strip()
            sub_line = sub_lines[i].strip()
            if sub_line and sub_line.startswith('##') and sub_line.startswith('---') or sub_line.startswith('***'):
                result_lines.append(sub_line)
                continue
            speaker_match = re.match('^(\\[[^\\]]+\\]:\\s*)', sub_line)
            speaker_tag = ''
            if speaker_match:
                speaker_tag = speaker_match.group(1)
                sub_line = sub_line[len(speaker_tag):]
                tts_speaker_match = re.match('^(\\[[^\\]]+\\]:\\s*)', tts_line)
                if tts_speaker_match:
                    tts_line = tts_line[len(tts_speaker_match.group(1)):]
            if not sub_line.strip():
                result_lines.append(speaker_tag.strip() if speaker_tag else '')
                continue
            sub_segments = re.split(PUNCTUATION_PATTERN, sub_line)
            tts_segments = re.split(PUNCTUATION_PATTERN, tts_line)
            sub_pairs = self._pair_segments_with_punctuation(sub_segments)
            tts_pairs = self._pair_segments_with_punctuation(tts_segments)
            if len(sub_pairs) == len(tts_pairs) and len(sub_pairs) > 0:
                mapped_parts = []
                for sub_text, sub_punc in zip(sub_pairs, tts_pairs):
                    (tts_text_seg, _) = None
                    if sub_text.strip() or tts_text_seg.strip():
                        mapped_parts.append(f'''{sub_text}({tts_text_seg}){sub_punc}''')
                        continue
                    mapped_parts.append(sub_punc)
                    result_lines.append(speaker_tag + ''.join(mapped_parts))
                    if sub_line.strip() and tts_line.strip():
                        result_lines.append(f'''{speaker_tag}{sub_line}({tts_line})''')
                        continue
            result_lines.append(speaker_tag + sub_line)
            for i in range(min_lines, len(sub_lines)):
                result_lines.append(sub_lines[i])
                return '\n'.join(result_lines)

    
    def _pair_segments_with_punctuation(self = None, segments = None):
        '''
        분할된 세그먼트를 (텍스트, 구두점) 쌍으로 재구성

        Args:
            segments: re.split 결과 (텍스트와 구두점이 번갈아 나옴)

        Returns:
            [(텍스트, 구두점), ...] 리스트
        '''
        import re
        PUNCTUATION_CHARS = {
            '、',
            '。',
            '！',
            '？',
            '?',
            '!'}
        pairs = []
        current_text = ''
        for seg in segments:
            if seg in PUNCTUATION_CHARS:
                pairs.append((current_text, seg))
                current_text = ''
                continue
            current_text += seg
            if current_text.strip():
                pairs.append((current_text, ''))
        return pairs

    
    def _build_japanese_dual_prompt(self = None, script = None, source_language = None):
        '''일본어 TTS/자막 분리 번역 프롬프트 생성 (전문 현지화 가이드라인 적용)'''
        return f'''# Role\nYou are a professional translator and scenario writer who localizes Korean content (drama, information/education, news) for the Japanese market. You don\'t just replace words - you perform "transcreation" that maximizes genre characteristics and viewer immersion.\n\n## Task\nTranslate the following {source_language} script to Japanese, providing TWO versions:\n1. **TTS version**: For text-to-speech - use appropriate kanji mixture for TTS engine to read context correctly\n2. **Subtitle version**: For on-screen display - minimize kanji constraints for smartphone readability, use strategic punctuation\n\nIMPORTANT: Translate the ENTIRE script completely. Do not omit or summarize any part.\n\n## Core Guidelines (Must Follow)\n\n### 1. Genre-specific Speaking Style Optimization\n- **Revenge/Thriller**: Cold, decisive tone. Male protagonist uses \'俺(ore)\', villains use arrogant \'私(watashi)\' or \'俺\'. Use weighty words like 代償(daishou), 因果応報(inga ouhou).\n- **Romance/Family**: Warm, soft tone. Women use \'私(watashi)\', use soft endings (~ね, ~よ) as appropriate.\n- **Information/Tips**: Use trustworthy \'です/ます\' style. Friendly tone as if speaking directly to the viewer.\n- **Historical/Period**: Use archaic/honorific speech. Reflect Japanese period drama (時代劇) feel with \'拙者(sessha)\', \'~でござる\' etc.\n- **Power Fantasy/SF**: Confident, modern feel. Technical terms clearly written in katakana.\n\n### 2. Honorific and Pronoun Localization\n- Korean \'너(you)\' by context: friend(君/お前), enemy(貴様/あんた), subordinate(君)\n- Korean titles (팀장, 대표) → Japanese business customs: \'チーム長\', \'代表\' etc.\n- \'형/누나/오빠/언니\' if not actual relatives → \'~さん\', \'~くん\' after name, or omit based on intimacy\n\n### 3. Natural Phrasing (Korean → Japanese idioms)\n- 예민하다 → 敏感だ / 神経質だ / 苛立っている\n- 대가를 치르다 → 報いを受ける / 代償を払う\n- 말이 안 되다 → ありえない / 話にならない\n- 뒤통수를 치다 → 裏切る / 寝首をかく\n- 눈에 불을 켜다 → 目を光らせる / 血眼になる\n\n### 4. Constraints\n- Do NOT damage the emotional arc of the original\n- Keep character personality consistent throughout - maintain dialogue tone\n- Preserve dramatic tension and pacing\n\n## Critical Rules for TTS Version\n- Use appropriate kanji mixture so TTS engine understands context correctly\n- Keep katakana for foreign words and emphasis\n- Numbers in natural reading: 3人 → 3人(さんにん)\n- Proper nouns can stay in kanji/katakana\n\n## Critical Rules for Subtitle Version\n- Minimize kanji for easy reading on smartphone screens\n- Strategic use of punctuation (、。) and spacing for readability\n- Write naturally as a native Japanese speaker would\n\n## Chapter/Section Title Rules (CRITICAL)\n- Chapter titles (##, ###) MUST be preserved and translated in BOTH versions\n- Section dividers (---, ***, ===) MUST be kept exactly as-is\n- NEVER skip or remove chapter headers\n\n## Speaker Tag Translations\n- 나레이션 → ナレーション\n- 나레이터 → ナレーター\n- Korean names: Convert to katakana (e.g., 민수 → ミンス, 수진 → スジン)\n\n## Output Format (CRITICAL - Follow Exactly)\nYou MUST output in this EXACT format with these EXACT markers:\n\n===TTS_VERSION_START===\n[ナレーション]: 今日は学校に行きました。\n[ミンス]: 本当にここで合ってる?\n===TTS_VERSION_END===\n\n===SUBTITLE_VERSION_START===\n[ナレーション]: きょうは学校に行きました。\n[ミンス]: ほんとうにここで合ってる?\n===SUBTITLE_VERSION_END===\n\n## Example with Chapters\nInput (Korean):\n## 챕터 1: 시작\n\n[나레이션]: 오늘은 좋은 날이다.\n[민수]: 드디어 복수할 때가 왔군.\n\nOutput:\n===TTS_VERSION_START===\n## 第1章: 始まり\n\n[ナレーション]: 今日は良い日だ。\n[ミンス]: ついに報いを受けさせる時が来た。\n===TTS_VERSION_END===\n\n===SUBTITLE_VERSION_START===\n## だい1しょう: はじまり\n\n[ナレーション]: きょうはいいひだ。\n[ミンス]: ついにむくいを受けさせるときがきた。\n===SUBTITLE_VERSION_END===\n\n---\n\n## Script to Translate ({source_language} → Japanese)\nTotal lines: {len(script.splitlines())} lines\nYou MUST translate ALL lines completely in BOTH versions.\n\n{script}\n\n---\n\n## Japanese Translation (provide BOTH versions in the exact format above)\n'''

    
    def _parse_japanese_dual_response(self = None, response_text = None):
        '''일본어 TTS/자막 응답 파싱'''
        text = response_text.strip()
        if text.startswith('```'):
            lines = text.split('\n')
            if lines[0].startswith('```'):
                lines = lines[1:]
            if lines and lines[-1].strip() == '```':
                lines = lines[:-1]
            text = '\n'.join(lines)
        tts_version = ''
        subtitle_version = ''
        tts_start = text.find('===TTS_VERSION_START===')
        tts_end = text.find('===TTS_VERSION_END===')
        if tts_start != -1 and tts_end != -1:
            tts_version = text[tts_start + len('===TTS_VERSION_START==='):tts_end].strip()
        subtitle_start = text.find('===SUBTITLE_VERSION_START===')
        subtitle_end = text.find('===SUBTITLE_VERSION_END===')
        if subtitle_start != -1 and subtitle_end != -1:
            subtitle_version = text[subtitle_start + len('===SUBTITLE_VERSION_START==='):subtitle_end].strip()
        if not tts_version and subtitle_version:
            logger.warning('Failed to parse Japanese dual format, using full response for both')
            tts_version = text
            subtitle_version = text
        return JapaneseTranslation(tts = tts_version, subtitle = subtitle_version)

    get_language_code = (lambda language = None: TranslationService.LANGUAGE_CODES.get(language, 'ko'))()
    get_supported_languages = (lambda : TranslationService.SUPPORTED_LANGUAGES.copy())()

_translation_service: Optional[TranslationService] = None

def get_translation_service():
    '''Get or create translation service singleton'''
    pass
# WARNING: Decompyle incomplete
