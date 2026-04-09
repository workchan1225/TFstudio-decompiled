# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: analytics_service.pyc (Python 3.11)

'''
Analytics Service - 분석 통계 계산 서비스
'''
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple, Optional
from sqlalchemy import func, and_
from collections import defaultdict
from app import db
from app.models.project import Project, Media
TTS_COST_PER_1K_CHARS = {
    'typecast': 0.015,
    'web-tts': 0,
    'google-voice': 0.016,
    'gemini-voice': 0,
    'local-upload': 0 }
AI_COST_PER_1K_TOKENS = {
    'openai/gpt-4': {
        'input': 0.03,
        'output': 0.06 },
    'openai/gpt-4o': {
        'input': 0.0025,
        'output': 0.01 },
    'openai/gpt-4o-mini': {
        'input': 0.00015,
        'output': 0.0006 },
    'anthropic/claude-3-opus': {
        'input': 0.015,
        'output': 0.075 },
    'anthropic/claude-3-5-sonnet': {
        'input': 0.003,
        'output': 0.015 },
    'anthropic/claude-3-haiku': {
        'input': 0.00025,
        'output': 0.00125 },
    'google/gemini-pro': {
        'input': 0.00125,
        'output': 0.005 },
    'google/gemini-flash': {
        'input': 7.5e-05,
        'output': 0.0003 } }
DIRECT_STEPS = [
    'hasScript',
    'hasImages',
    'hasTTS',
    'hasSubtitles',
    'hasSubtitleStyle',
    'hasImageTimeline',
    'hasVideo']
SIMPLE_STEPS = [
    'hasTopic',
    'hasOutline',
    'hasScript',
    'hasScene',
    'hasAudio',
    'hasCharacter',
    'hasVideo',
    'hasTitle',
    'hasDescription']

class AnalyticsService:
    '''분석 통계 서비스'''
    _get_period_range = (lambda period = None: now = datetime.utcnow()if period == 'week':
start = now - timedelta(days = 7)elif period == 'year':
start = now - timedelta(days = 365)else:
start = now - timedelta(days = 30)(start, now))()
    _get_previous_period_range = (lambda period = None: now = datetime.utcnow()if period == 'week':
end = now - timedelta(days = 7)start = now - timedelta(days = 14)elif period == 'year':
end = now - timedelta(days = 365)start = now - timedelta(days = 730)else:
end = now - timedelta(days = 30)start = now - timedelta(days = 60)(start, end))()
    _calculate_progress = (lambda project = None: pass# WARNING: Decompyle incomplete
)()
    get_overview_stats = (lambda period = None: (start, end) = AnalyticsService._get_period_range(period)(prev_start, prev_end) = AnalyticsService._get_previous_period_range(period)total_projects = Project.query.count()completed_projects = Project.query.filter(Project.video_url.isnot(None)).count()draft_projects = Project.query.filter(Project.status == 'draft').count()in_progress_projects = Project.query.filter(Project.status == 'in-progress').count()period_projects = Project.query.filter(Project.created_at >= start, Project.created_at <= end).count()prev_period_projects = Project.query.filter(Project.created_at >= prev_start, Project.created_at <= prev_end).count()period_completed = 0prev_period_completed = 0all_completed = Project.query.filter(Project.video_url.isnot(None)).all()for project in all_completed:
generated_at = Noneif project.video_settings and 'generatedAt' in project.video_settings:
generated_at = datetime.fromisoformat(project.video_settings['generatedAt'])else:
except (ValueError, TypeError):
passif not generated_at:
generated_at = project.updated_atif generated_at:
if  <= start, generated_at or start, generated_at <= end:
passif  <= prev_start, generated_at or prev_start, generated_at <= prev_end:
passprev_period_completed += 1if total_projects > 0:
avg_completion_rate = round((completed_projects / total_projects) * 100, 1)else:
avg_completion_rate = 0
def calc_change(current = None, previous = None):
if previous == 0:
100 if current > 0 else 0None(((current - previous) / previous) * 100, 1)projects_change = calc_change(period_projects, prev_period_projects)videos_change = calc_change(period_completed, prev_period_completed)direct_count = Project.query.filter(Project.type == 'direct').count()simple_count = Project.query.filter(Project.type == 'simple').count(){
'totalProjects': total_projects,
'completedVideos': completed_projects,
'draftProjects': draft_projects,
'inProgressProjects': in_progress_projects,
'totalMediaCount': total_media,
'avgCompletionRate': avg_completion_rate,
'periodComparison': {
'projectsChange': projects_change,
'videosChange': videos_change },
'projectsByType': {
'direct': direct_count,
'simple': simple_count } })()
    get_projects_timeline = (lambda period = None: (start, end) = AnalyticsService._get_period_range(period)if period == 'year':
date_format = func.strftime('%Y-%m', Project.created_at)date_format_str = '%Y-%m'else:
date_format = func.date(Project.created_at)date_format_str = '%Y-%m-%d'created_query = db.session.query(date_format.label('date'), func.count(Project.id).label('count')).filter(Project.created_at >= start, Project.created_at <= end).group_by('date').all()completed_dict = { }completed_projects = Project.query.filter(Project.video_url.isnot(None)).all()for project in completed_projects:
generated_at = Noneif project.video_settings and 'generatedAt' in project.video_settings:
generated_at = datetime.fromisoformat(project.video_settings['generatedAt'])else:
except (ValueError, TypeError):
passif not generated_at:
generated_at = project.updated_atif generated_at:
if  <= start, generated_at or start, generated_at <= end:
passif period == 'year':
passelse:
generated_at.strftime('%Y-%m-%d') = generated_at.strftime('%Y-%m')completed_dict[date_key] = completed_dict.get(date_key, 0) + 1created_dict = created_query()all_dates = sorted(set(created_dict.keys()) | set(completed_dict.keys()))timeline = []for date in all_dates:
timeline.append({
'date': date,
'created': created_dict.get(date, 0),
'completed': completed_dict.get(date, 0) })timeline)()
    get_recent_projects = (lambda limit = None: projects = Project.query.order_by(Project.updated_at.desc()).limit(limit).all()result = []for project in projects:
(completed, total) = AnalyticsService._calculate_progress(project)progress_percent = round((completed / total) * 100) if total > 0 else 0if not bool(project.video_url):
if not project.direct_progress or { }.get('hasVideo'):
if not project.simple_progress:
has_video = bool({ }.get('hasVideo'))result.append({
'id': project.id,
'name': project.title,
'status': project.status,
'type': 'direct',
'progress': progress_percent,
'updatedAt': project.updated_at.isoformat() if project.type or project.updated_at else None,
'hasVideo': has_video })result)()
    get_top_projects = (lambda limit = None: projects = Project.query.order_by((Project.status == 'completed').desc(), Project.updated_at.desc()).limit(limit * 2).all()project_ids = projects()media_counts_query = db.session.query(Media.project_id, func.count(Media.id).label('count')).filter(Media.project_id.in_(project_ids)).group_by(Media.project_id).all()media_count_dict = media_counts_query()result = []for project in projects:
(completed, total) = AnalyticsService._calculate_progress(project)media_count = media_count_dict.get(project.id, 0)result.append({
'id': project.id,
'title': project.title,
'status': project.status,
'type': 'direct',
'mediaCount': media_count,
'completedSteps': completed,
'totalSteps': total,
'progress': round((completed / total) * 100) if project.type or total > 0 else 0 })result.sort(key = (lambda x: (x['progress'], x['mediaCount'])), reverse = True)
            return result[:limit]
)()
    get_project_analytics = (lambda project_id = None: project = Project.query.get(project_id)if not project:
Noneif None.type == 'direct':
steps = DIRECT_STEPSif not bool(project.video_url):
has_completed_video = progress_data.get('hasVideo', False)if has_completed_video and media_stats['videoCount'] == 0:
media_stats['videoCount'] = 1completed_count = (lambda .0: pass# WARNING: Decompyle incomplete
)(step_details())
        total_count = len(step_details)
        generated_at = None
        if project.video_settings and 'generatedAt' in project.video_settings:
            generated_at = project.video_settings['generatedAt']
        return {
            'project': {
                'id': project.id,
                'title': project.title,
                'type': 'direct',
                'status': project.status,
                'createdAt': project.created_at.isoformat() if project.type or project.created_at else None,
                'updatedAt': project.updated_at.isoformat() if project.updated_at else None,
                'videoGeneratedAt': generated_at,
                'hasVideo': bool(project.video_url) },
            'progress': {
                'current': completed_count,
                'total': total_count,
                'percent': round((completed_count / total_count) * 100) if total_count > 0 else 0,
                'steps': step_details },
            'stats': {
                'imageCount': media_stats['imageCount'],
                'audioCount': media_stats['audioCount'],
                'videoCount': media_stats['videoCount'],
                'totalMedia': sum(media_stats.values()) } }
)()
    get_resource_usage = (lambda period = None: (start, end) = AnalyticsService._get_period_range(period)tts_usage = defaultdict(int)tts_char_count = defaultdict(int)projects = Project.query.filter(Project.created_at >= start, Project.created_at <= end).all()for project in projects:
method = project.selected_tts_methodif method and project.script:
passdefaultdict((lambda : {
'count': 0,
'inputTokens': 0,
'outputTokens': 0 })) = None
            for project in projects:
                if project.llm_generation_metadata:
                    metadata = project.llm_generation_metadata
                    for key in ('topicGeneration', 'outlineGeneration', 'scriptGeneration', 'titleGeneration'):
                        if key in metadata and 'model' in metadata[key]:
                            model = metadata[key].get('model', 'unknown')
                        [] = None
                        for project in projects:
                            date_key = project.created_at.strftime('%Y-%m-%d') if period != 'year' else project.created_at.strftime('%Y-%m')
                            usage_timeline.append({
                                'date': date_key,
                                'ttsMethod': project.selected_tts_method,
                                'hasAI': bool(project.llm_generation_metadata) })
                            timeline_data = defaultdict((lambda : {
'ttsCount': 0,
'aiCount': 0 }))
                            for item in usage_timeline:
                                
                                def sorted(timeline_data.items())()(.0):
                                    '''ttsCount'''
                                    return [ {
                                        'date': date,
                                        'ttsCount': data['ttsCount'],
                                        'aiCount': data['aiCount'] } for date, data in .0 ]

                                tts_cost = (lambda .0: pass# WARNING: Decompyle incomplete
)(tts_char_count.items()())
                                ai_cost = (lambda .0: pass# WARNING: Decompyle incomplete
)(ai_usage.items()())
                                video_stats = {
                                    'totalVideos': 0,
                                    'byResolution': defaultdict(int),
                                    'byFps': defaultdict(int),
                                    'byQuality': defaultdict(int) }
                                for project in projects:
                                    if project.video_url and project.video_settings:
                                        project.video_settings = sum
                                        if vs.get('resolution'):
                                            pass
                                        if vs.get('fps'):
                                            pass
                                        if vs.get('quality'):
                                            pass
                                    return {
                                        'tts': sum,
                                        'ai': {
                                            'byModel': (lambda .0: pass# WARNING: Decompyle incomplete
)(ai_usage.values()()),
                                            'totalRequests': None,
                                            'totalInputTokens': sum,
                                            'totalOutputTokens': (lambda .0: pass# WARNING: Decompyle incomplete
)(ai_usage.values()()),
                                            'estimatedCost': round(ai_cost, 4) },
                                        'video': {
                                            'totalVideos': video_stats['totalVideos'],
                                            'byResolution': dict(video_stats['byResolution']),
                                            'byFps': dict(video_stats['byFps']),
                                            'byQuality': dict(video_stats['byQuality']) },
                                        'timeline': timeline_list,
                                        'period': period }
)()
    get_productivity_stats = (lambda period = None: (start, end) = AnalyticsService._get_period_range(period)projects = Project.query.filter(Project.created_at >= start, Project.created_at <= end).all()completion_times = []step_durations = defaultdict(list)for project in projects:
if project.video_url and project.updated_at and project.created_at:
duration_hours = (project.updated_at - project.created_at).total_seconds() / 3600completion_times.append({
'id': project.id,
'title': project.title,
'hours': round(duration_hours, 2) })if project.dependency_metadata and 'lastCompletedAt' in project.dependency_metadata:
completed_at = project.dependency_metadata['lastCompletedAt']sorted_steps = sorted(completed_at.items(), key = (lambda x: x[1]))
                prev_time = project.created_at
                for step, time_str in sorted_steps:
                    step_time = datetime.fromisoformat(time_str)
                    duration_mins = (step_time - prev_time).total_seconds() / 60
                    if duration_mins > 0:
                        step_durations[step].append(duration_mins)
                    prev_time = step_time
                    except (ValueError, TypeError):
                        continue
                    avg_step_durations = step_durations.items()()
                    total_projects = len(projects)
                    completed_projects = (lambda .0: pass# WARNING: Decompyle incomplete
)(projects())
        completion_rate = (completed_projects / total_projects) * 100 if total_projects > 0 else 0
        avg_completion_hours = (lambda .0: pass# WARNING: Decompyle incomplete
)(completion_times()) / len(completion_times) if completion_times else 0
        speed_score = max(0, 100 - avg_completion_hours * 5)
        productivity_score = round(completion_rate * 0.6 + speed_score * 0.4)
        daily_completions = defaultdict(int)
        for project in projects:
            if project.video_url and project.updated_at:
                date_key = project.updated_at.strftime('%Y-%m-%d') if period != 'year' else project.updated_at.strftime('%Y-%m')
            
            def sorted(daily_completions.items())()(.0):
                return [ {
                    'date': date,
                    'completed': count } for date, count in .0 ]

            return {
                'summary': {
                    'totalProjects': total_projects,
                    'completedProjects': completed_projects,
                    'completionRate': round(completion_rate, 1),
                    'avgCompletionHours': round(avg_completion_hours, 2),
                    'productivityScore': productivity_score },
                'completionTimes': completion_times[:20],
                'avgStepDurations': avg_step_durations,
                'efficiencyTimeline': efficiency_timeline,
                'period': period }
)()
    get_project_media_details = (lambda project_id = None: project = Project.query.get(project_id)if not project:
Nonemedia_list = None.query.filter(Media.project_id == project_id).all()images = media_list()audios = media_list()videos = media_list()image_analysis = {
'count': None,
'totalSize': round,
'avgSize': sum((lambda .0: pass# WARNING: Decompyle incomplete
)(images()) / len(images)) if images else 0,
            'resolutions': { },
            'formats': { } }
        for img in images:
            if img.width and img.height:
                res_key = f'''{img.width}x{img.height}'''
                image_analysis['resolutions'][res_key] = image_analysis['resolutions'].get(res_key, 0) + 1
            if img.mime_type:
                fmt = img.mime_type.split('/')[-1]
                image_analysis['formats'][fmt] = image_analysis['formats'].get(fmt, 0) + 1
            audio_analysis = {
                'count': None,
                'totalDuration': sum,
                'totalSize': (lambda .0: pass# WARNING: Decompyle incomplete
)(audios()),
                'formats': { } }
            for aud in audios:
                if aud.mime_type:
                    fmt = aud.mime_type.split('/')[-1]
                    audio_analysis['formats'][fmt] = audio_analysis['formats'].get(fmt, 0) + 1
                if not project.script and project.script and project.selected_tts_method:
                    tts_info = {
                        'method': project.selected_tts_method,
                        'hasAudio': bool(project.get_final_audio_url()),
                        'scriptLength': len(''),
                        'estimatedCost': round((len('') / 1000) * TTS_COST_PER_1K_CHARS.get('', 0), 4) }
                    video_analysis = {
                        'count': None,
                        'totalDuration': sum,
                        'totalSize': (lambda .0: pass# WARNING: Decompyle incomplete
)(videos()),
                        'resolutions': { },
                        'videoUrl': project.video_url,
                        'sampleVideoUrl': project.sample_video_url,
                        'hasVideo': bool(project.video_url) }
                    for vid in videos:
                        if vid.width and vid.height:
                            res_key = f'''{vid.width}x{vid.height}'''
                            video_analysis['resolutions'][res_key] = video_analysis['resolutions'].get(res_key, 0) + 1
        return {
            'projectId': image_analysis,
            'projectTitle': audio_analysis,
            'images': tts_info,
            'audios': video_analysis,
            'tts': len(media_list),
            'videos': None,
            'totalMedia': sum,
            'totalSize': (lambda .0: pass# WARNING: Decompyle incomplete
)(media_list()) }
)()
    get_project_history = (lambda project_id = None: project = Project.query.get(project_id)if not project:
Nonehistory = Nonehistory.append({
'event': 'project_created',
'label': '프로젝트 생성',
'timestamp': project.created_at.isoformat() if project.created_at else None,
'details': {
'title': project.title,
'type': project.type } })if project.dependency_metadata and 'lastCompletedAt' in project.dependency_metadata:
step_labels = {
'script': '스크립트 작성',
'tts': 'TTS 생성',
'subtitles': '자막 생성',
'subtitle_style': '자막 스타일 설정',
'images': '이미지 추가',
'image_timeline': '이미지 타임라인',
'video': '영상 생성' }for step, time_str in project.dependency_metadata['lastCompletedAt'].items():
history.append({
'event': f'''step_{step}_completed''',
'label': step_labels.get(step, f'''{step} 완료'''),
'timestamp': time_str,
'details': {
'step': step } })except (ValueError, TypeError):
continueif project.script_expansion_history:
for expansion in project.script_expansion_history:
history.append({
'event': 'script_expanded',
'label': '스크립트 확장',
'timestamp': expansion.get('timestamp'),
'details': {
'beforeLength': expansion.get('beforeLength'),
'afterLength': expansion.get('afterLength') } })if project.video_settings and 'generatedAt' in project.video_settings:
history.append({
'event': 'video_generated',
'label': '영상 생성 완료',
'timestamp': project.video_settings['generatedAt'],
'details': { } })history.sort(key = (lambda x:
