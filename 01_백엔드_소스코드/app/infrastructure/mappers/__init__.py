# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Infrastructure Mappers

Mappers convert between ORM models and Domain entities.
These mappers ensure clean separation between the database layer and domain layer.
'''
from typing import Optional, List
from datetime import datetime
from app.domain.entities import Project as ProjectEntity, Character as CharacterEntity, Media as MediaEntity
from app.domain.enums import ProjectType, ProjectStatus, TTSMethod, MediaType, YouTubeUploadStatus
from app.domain.value_objects import AudioUrl, VideoSettings, DependencyMetadata, SubtitleLayer, BGMTrack
from app.models.project import Project as ProjectORM, Character as CharacterORM, Media as MediaORM

class CharacterMapper:
    '''Mapper for Character entity <-> ORM model'''
    to_domain = (lambda orm = None: if not orm.created_at:
entity = CharacterEntity(id = orm.id, name = orm.name, description = orm.description, created_at = datetime.utcnow())if orm.image_url:
entity.set_image_url(orm.image_url)entity)()
    to_orm = (lambda entity = None, project_id = None: CharacterORM(id = entity.id, project_id = project_id, name = entity.name, description = entity.description, image_url = entity.image_url, created_at = entity.created_at))()


class MediaMapper:
    '''Mapper for Media entity <-> ORM model'''
    to_domain = (lambda orm = None: pass# WARNING: Decompyle incomplete
)()
    to_orm = (lambda entity = None: pass# WARNING: Decompyle incomplete
)()


class ProjectMapper:
    '''Mapper for Project entity <-> ORM model'''
    _extract_supertonic_audio_url = (lambda orm = None: tts_audio_by_language = orm.tts_audio_by_languageif not isinstance(tts_audio_by_language, dict):
Noneif not None.active_script_language:
language = '한국어'language_audio = tts_audio_by_language.get(language)if not isinstance(language_audio, dict):
language_audio = tts_audio_by_language.get('한국어')if not isinstance(language_audio, dict):
Nonesupertonic_url = None.get('supertonicTts')supertonic_url if isinstance(supertonic_url, str) and supertonic_url else None)()
    _set_supertonic_audio_url = (lambda orm = None, url = None: tts_audio_by_language = orm.tts_audio_by_language if isinstance(orm.tts_audio_by_language, dict) else { }if not orm.active_script_language:
language = '한국어'language_audio = tts_audio_by_language.get(language)if not isinstance(language_audio, dict):
language_audio = { }language_audio['supertonicTts'] = url.valuetts_audio_by_language[language] = language_audioorm.tts_audio_by_language = tts_audio_by_language)()
    to_domain = (lambda orm = None: audio_urls = { }if orm.typecast_audio_url:
audio_urls[TTSMethod.TYPECAST] = AudioUrl(orm.typecast_audio_url)if orm.web_tts_audio_url:
audio_urls[TTSMethod.WEB_TTS] = AudioUrl(orm.web_tts_audio_url)if orm.local_audio_url:
audio_urls[TTSMethod.LOCAL_UPLOAD] = AudioUrl(orm.local_audio_url)if orm.google_cloud_tts_audio_url:
audio_urls[TTSMethod.GOOGLE_VOICE] = AudioUrl(orm.google_cloud_tts_audio_url)if orm.gemini_tts_audio_url:
audio_urls[TTSMethod.GEMINI_VOICE] = AudioUrl(orm.gemini_tts_audio_url)if orm.gemini_native_tts_audio_url:
audio_urls[TTSMethod.GEMINI_NATIVE] = AudioUrl(orm.gemini_native_tts_audio_url)if orm.edge_tts_audio_url:
audio_urls[TTSMethod.EDGE_TTS] = AudioUrl(orm.edge_tts_audio_url)if orm.qwen3_tts_audio_url:
audio_urls[TTSMethod.QWEN3] = AudioUrl(orm.qwen3_tts_audio_url)if orm.elevenlabs_tts_audio_url:
audio_urls[TTSMethod.ELEVENLABS] = AudioUrl(orm.elevenlabs_tts_audio_url)supertonic_url = ProjectMapper._extract_supertonic_audio_url(orm)if supertonic_url:
audio_urls[TTSMethod.SUPERTONIC] = AudioUrl(supertonic_url)subtitle_layers = []# WARNING: Decompyle incomplete
)()
    to_orm = (lambda entity = None: pass# WARNING: Decompyle incomplete
)()
    update_orm = (lambda orm = None, entity = None: orm.title = entity.titleorm.type = entity.project_type.valueorm.status = entity.status.valueorm.thumbnail = entity.thumbnailorm.current_step = entity.current_steporm.topic = entity.topicorm.outline = entity.outlineorm.script = entity.scriptorm.selected_tts_method = entity.selected_tts_method.value if entity.selected_tts_method else Noneorm.mixed_audio_url = entity.mixed_audio_url.value if entity.mixed_audio_url else Noneorm.subtitle_url = entity.subtitle_urlorm.subtitle_layers = entity.subtitle_layers()orm.youtube_title = entity.youtube_titleorm.youtube_description = entity.youtube_descriptionorm.youtube_video_id = entity.youtube_video_idorm.youtube_upload_status = entity.youtube_upload_status.valueorm.youtube_upload_date = entity.youtube_upload_dateorm.youtube_scheduled_time = entity.youtube_scheduled_timeorm.youtube_metadata = entity.youtube_metadataorm.video_url = entity.video_urlorm.video_settings = entity.video_settings.to_dict()orm.uploaded_script_path = entity.uploaded_script_pathorm.script_path = entity.script_pathorm.script_version = entity.script_versionorm.direct_progress = entity.direct_progressorm.simple_progress = entity.simple_progressorm.dependency_metadata = entity.dependency_metadata.to_dict()orm.bgm_tracks = entity.bgm_tracks()orm.llm_generation_metadata = entity.llm_generation_metadataorm.script_expansion_history = entity.script_expansion_historyorm.editor_state = entity.editor_stateorm.use_speaker_separation = entity.use_speaker_separationorm.speaker_tts_data = entity.speaker_tts_dataorm.speaker_merged_audio_url = entity.speaker_merged_audio_url.value if entity.speaker_merged_audio_url else Noneorm.updated_at = entity.updated_atfor method, url in entity.audio_urls.items():
if method == TTSMethod.TYPECAST:
orm.typecast_audio_url = url.valuecontinueif method == TTSMethod.WEB_TTS:
orm.web_tts_audio_url = url.valuecontinueif method == TTSMethod.LOCAL_UPLOAD:
orm.local_audio_url = url.valuecontinueif method == TTSMethod.GOOGLE_VOICE:
orm.google_cloud_tts_audio_url = url.valuecontinueif method == TTSMethod.GEMINI_VOICE:
orm.gemini_tts_audio_url = url.valuecontinueif method == TTSMethod.GEMINI_NATIVE:
orm.gemini_native_tts_audio_url = url.valuecontinueif method == TTSMethod.EDGE_TTS:
orm.edge_tts_audio_url = url.valuecontinueif method == TTSMethod.QWEN3:
orm.qwen3_tts_audio_url = url.valuecontinueif method == TTSMethod.ELEVENLABS:
orm.elevenlabs_tts_audio_url = url.valuecontinueif method == TTSMethod.SUPERTONIC:
ProjectMapper._set_supertonic_audio_url(orm, url)None)()
