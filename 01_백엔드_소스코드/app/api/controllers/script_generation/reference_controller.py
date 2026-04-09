# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reference_controller.pyc (Python 3.11)

'''
Reference Script Generation Controller

레퍼런스 기반 대본 생성 API 엔드포인트
'''
import logging
from flask import Blueprint, request, jsonify
from app.api.controllers.ai_utils import get_api_key_from_settings
from app.services.google_auth_service import get_google_configuration_error_message
from app.utils.google_sdk import configure_legacy_genai
logger = logging.getLogger(__name__)
reference_bp = Blueprint('reference', __name__)
SCRIPT_UPLOAD_TAB_REFERENCE_MODEL = 'gemini-2.5-flash'

def _get_genai_and_model():
    '''Google Generative AI 인스턴스 및 모델 가져오기'''
    api_key = get_api_key_from_settings('google')
    if not api_key:
        raise ValueError(get_google_configuration_error_message())
    genai = configure_legacy_genai(api_key)
    model_name = SCRIPT_UPLOAD_TAB_REFERENCE_MODEL
    model = genai.GenerativeModel(model_name)
    return (genai, model)

extract_transcript = (lambda : try:
data = request.get_json()youtube_url = data.get('youtubeUrl', '').strip()if not youtube_url:
(jsonify({
'success': False,
'error': 'YouTube URL이 필요합니다.' }), 400)None.info(f'''Extracting transcript from: {youtube_url}''')TranscriptExtractor = TranscriptExtractorimport app.services.script_generation.youtubeextractor = TranscriptExtractor()result = extractor.extract(youtube_url)if not result.success:
(jsonify({
'success': False,
'error': result.error }), 400)response_data = {
'success': (lambda .0: [ {
'text': seg.text,
'start': seg.start,
'duration': seg.duration } for seg in .0 ]),
            'transcript': result.transcript(),
            'fullText': result.full_text,
            'videoInfo': {
                'videoId': result.video_info.video_id if result.video_info else '',
                'title': result.video_info.title if result.video_info else '',
                'channelName': result.video_info.channel_name if result.video_info else '',
                'duration': result.video_info.duration if result.video_info else 0 },
            'language': result.language }
        if result.video_info and result.video_info.video_id:
            video_info = extractor.get_video_info_from_api(result.video_info.video_id)
            if video_info:
                response_data['videoInfo']['title'] = video_info.title
                response_data['videoInfo']['channelName'] = video_info.channel_name
                if video_info.duration > 0:
                    response_data['videoInfo']['duration'] = video_info.duration
        return (jsonify(response_data), 200)
    except Exception:
        e = None
        logger.error(f'''Failed to extract transcript: {e}''')
        del e
        return None
        None = 
        del e

)()
analyze_pattern = (lambda : try:
data = request.get_json()transcript = data.get('transcript', '').strip()video_info = data.get('videoInfo', { })if not transcript:
(jsonify({
'success': False,
'error': '자막 텍스트가 필요합니다.' }), 400)None.info(f'''Analyzing pattern for: {video_info.get('title', 'Unknown')}''')(genai, model) = _get_genai_and_model()PatternAnalyzer = PatternAnalyzerimport app.services.script_generation.youtubeanalyzer = PatternAnalyzer(genai, model)result = analyzer.analyze(transcript, video_info)if not result.success:
(jsonify({
'success': False,
'error': result.error }), 400)(None({
'success': True,
'analysis': result.analysis.to_dict() if result.analysis else None }), 200)except ValueError:
e = Nonelogger.error(f'''Configuration error: {e}''')del eNoneNone = del eexcept Exception:
e = Nonelogger.error(f'''Failed to analyze pattern: {e}''')del eNoneNone = del e)()
generate_titles = (lambda : try:
data = request.get_json()analysis = data.get('analysis')topic_direction = data.get('topicDirection', '').strip()language = data.get('language', '한국어')count = data.get('count', 10)include_characters = data.get('includeCharacters', True)exclude_characters = not include_charactersif not analysis:
(jsonify({
'success': False,
'error': '레퍼런스 분석 결과가 필요합니다.' }), 400)if not topic_direction:
None.info(f'''Generating reference titles, topic: {'(auto)'}''')(genai, model) = _get_genai_and_model()ReferenceMode = ReferenceModeimport app.services.script_generation.modesTitleConfig = TitleConfigimport app.services.script_generation.typesmode = ReferenceMode(genai, model)if not topic_direction:
config = TitleConfig(topic = '', language = language, count = count, content_format = 'reference', reference_analysis = analysis, topic_direction = topic_direction, exclude_character_analysis = exclude_characters)titles = mode.generate_titles(config)(True({
'success': (lambda .0: [ {
'title': t.title,
'description': t.description,
'hooks': t.hooks } for t in .0 ]),
                    'titles': titles() }), 200)
            except ValueError:
                e = TitleConfig
                logger.error(f'''Validation error: {e}''')
                del e
                return None
                None = 
                del e
            except Exception:
                e = None
                logger.error(f'''Failed to generate titles: {e}''')
                del e
                return None
                None = 
                del e

)()
generate_synopses = (lambda : try:
data = request.get_json()analysis = data.get('analysis')selected_title = data.get('selectedTitle', '').strip()topic_direction = data.get('topicDirection', '').strip()pattern_intensity = data.get('patternIntensity', 'moderate')language = data.get('language', '한국어')count = data.get('count', 5)include_characters = data.get('includeCharacters', True)exclude_characters = not include_charactersif not analysis:
(jsonify({
'success': False,
'error': '레퍼런스 분석 결과가 필요합니다.' }), 400)if not None:
(jsonify({
'success': False,
'error': '제목을 선택해주세요.' }), 400)None.info(f'''Generating reference synopses for: {selected_title}''')(genai, model) = _get_genai_and_model()ReferenceMode = ReferenceModeimport app.services.script_generation.modesSynopsisConfig = SynopsisConfigimport app.services.script_generation.typesmode = ReferenceMode(genai, model)config = SynopsisConfig(title = selected_title, language = language, count = count, content_format = 'reference', reference_analysis = analysis, topic_direction = topic_direction, pattern_intensity = pattern_intensity, exclude_character_analysis = exclude_characters)synopses = mode.generate_synopses(config)(True({
'success': (lambda .0: [ {
'synopsis': s.synopsis,
'characters': s.characters } for s in .0 ]),
            'synopses': synopses() }), 200)
    except ValueError:
        e = None
        logger.error(f'''Validation error: {e}''')
        del e
        return None
        None = 
        del e
        except Exception:
            e = None
            logger.error(f'''Failed to generate synopses: {e}''')
            del e
            return None
            None = 
            del e

)()
generate_script = (lambda :
