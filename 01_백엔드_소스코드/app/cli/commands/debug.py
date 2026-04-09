# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: debug.pyc (Python 3.11)

'''디버그 및 진단 CLI 명령.'''
import json as _json
import click
from app.cli import with_app_context
from app.cli.formatters import output, section_header, status_line
debug_group = (lambda : pass)()
debug_env = (lambda ctx, show_keys, check: collect_runtime_diagnostics = collect_runtime_diagnosticsimport app.services.runtime_diagnostics_servicediag = collect_runtime_diagnostics()if ctx.obj['json']:
diag['apiKeys'] = _collect_api_key_info(show_keys)diag['featureFlags'] = _collect_feature_flags()output(diag, True)NoneNone.echo('\n=== TFstudio Environment Diagnostics ===')click.echo(section_header('PATHS'))click.echo(status_line('IS_FROZEN', str(diag['isFrozen']), 'OK'))click.echo(status_line('data_path_source', str(diag['dataPathSource']), 'OK'))for key, path_str in diag['paths'].items():
writable_info = diag['writableChecks'].get(key, { })if writable_info:
is_ok = writable_info.get('writable', False)stat = 'OK' if is_ok else 'ERROR'if check and is_ok:
continueclick.echo(status_line(key, path_str, stat))continueclick.echo(status_line(key, path_str, 'OK'))click.echo(section_header('API KEYS'))key_info = _collect_api_key_info(show_keys)for name, info in key_info.items():
stat = 'SET' if info['set'] else 'MISSING'if check and info['set']:
continueclick.echo(status_line(name, info['display'], stat))click.echo(section_header('BINARIES'))for binary_name in ('ffmpeg', 'ffprobe'):
bdata = diag[binary_name]available = bdata.get('available', False)source = bdata.get('source', 'unknown')path = bdata.get('resolvedPath', bdata.get('bundledPath', ''))if check and available:
continueclick.echo(status_line(binary_name, f'''{path} ({source})''', 'OK' if available else 'MISSING'))click.echo(section_header('FEATURE FLAGS'))flags = _collect_feature_flags()for name, value in flags.items():
click.echo(status_line(name, str(value), 'OK'))errors = diag.get('criticalErrors', [])if errors:
click.echo(section_header('CRITICAL ERRORS'))for err in errors:
click.echo(f'''  ** {err}''')Noneif not check:
click.echo(section_header('CRITICAL ERRORS'))click.echo('  (none)')NoneNone)()()()()()

def _collect_api_key_info(show_keys = click.option('--check', is_flag = True, help = '문제 항목만 출력')):
    '''API 키 설정 상태 수집.'''
    Settings = Settings
    import app.models.settings
    is_google_ai_configured = is_google_ai_configured
    resolve_google_auth_config = resolve_google_auth_config
    import app.services.google_auth_service
    settings = Settings.get_or_create()
    google_auth = resolve_google_auth_config(settings = settings)
    key_fields = {
        'openai': 'openai_api_key',
        'google': 'google_api_key',
        'anthropic': 'claude_api_key',
        'elevenlabs': 'elevenlabs_api_key',
        'nanobanana': 'nanobanana_api_key',
        'typecast': 'typecast_api_key' }
    result = { }
    for name, attr in key_fields.items():
        if name == 'google':
            value = google_auth.api_key if google_auth.auth_mode == 'api_key' else google_auth.auth_mode
            is_set = is_google_ai_configured(settings = settings)
        else:
            value = getattr(settings, attr, None)
            if value:
                is_set = bool(str(value).strip())
                if show_keys and is_set:
                    display = str(value)
                elif is_set:
                    v = str(value)
                    display = f'''{v[:8]}***{v[-4:]}''' if len(v) > 12 else '***'
                else:
                    display = '(not set)'
        result[name] = {
            'set': is_set,
            'display': display }
        return result


def _collect_feature_flags():
    '''Feature flags 수집.'''
    
    try:
        FeatureFlags = FeatureFlags
        import app.config.feature_flags
        return FeatureFlags.get_all_flags()
    except Exception:
        return 


debug_paths = (lambda ctx: p = pathsimport app.configpath_fns = [
('get_base_path', p.get_base_path),
('get_data_path', p.get_data_path),
('get_database_path', p.get_database_path),
('get_projects_path', p.get_projects_path),
('get_outputs_path', p.get_outputs_path),
('get_temp_path', p.get_temp_path),
('get_static_path', p.get_static_path),
('get_fonts_path', p.get_fonts_path),
('get_env_path', p.get_env_path)]optional_fns = [
'get_ffmpeg_path',
'get_scene_data_path',
'get_assistant_data_path',
'get_overlay_assets_path',
'get_thumbnail_references_path',
'get_default_style_samples_path',
'get_custom_style_templates_dir',
'get_supertonic_helper_path',
'get_supertonic_onnx_path',
'get_supertonic_voice_styles_path']for fn_name in optional_fns:
fn = getattr(p, fn_name, None)if fn:
path_fns.append((fn_name, fn))rows = []for name, fn in path_fns:
result = fn()rows.append({
'function': f'''{name}()''',
'path': str(result),
'exists': result.exists() if hasattr(result, 'exists') else 'N/A' })except Exception:
e = Nonerows.append({
'function': f'''{name}()''',
'path': f'''ERROR: {e}''',
'exists': False })e = Nonedel econtinuee = Nonedel eoutput(rows, ctx.obj['json'])None)()()()
debug_project_health = (lambda ctx, project_id, section, all_projects: Project = Projectimport app.models.projectif all_projects:
projects = Project.query.all()summaries = []for proj in projects:
issues = _check_project_health(proj, 'all')total_issues = (lambda .0: pass# WARNING: Decompyle incomplete
)(issues.values()())
            summaries.append({
                'id': proj.id,
                'title': proj.title,
                'issues': total_issues })
            output(summaries, ctx.obj['json'])
            return None
            if not project_id:
                click.echo('project_id 또는 --all-projects 옵션이 필요합니다.', err = True)
                raise SystemExit(1)
            project = Project.query.get(project_id)
            if not project:
                click.echo(f'''Project not found: {project_id}''', err = True)
                raise SystemExit(1)
            issues = _check_project_health(project, section)
            if ctx.obj['json']:
                output(issues, True)
                return None
            sum.echo(f'''\n=== Project Health: "{project.title}" ({project.id}) ===''')
            for sect_name, sect_issues in issues.items():
                if not sect_issues:
                    click.echo(f'''\n[{sect_name.upper()}] OK''')
                    continue
                click.echo(f'''\n[{sect_name.upper()}] {len(sect_issues)} issue(s)''')
                for issue in sect_issues:
                    click.echo(f'''  {issue['severity']}: {issue['message']}''')
                    return None
)()()()()()()

def _check_project_health(project = click.option('--all-projects', is_flag = True, help = '전체 프로젝트 요약'), section = click.pass_context):
    '''프로젝트 무결성 검사 실행.'''
    Path = Path
    import pathlib
    get_data_path = get_data_path
    import app.config.paths
    data_path = get_data_path()
    issues = { }
    if section in ('all', 'images'):
        issues['images'] = _check_images(project, data_path)
    if section in ('all', 'tts'):
        issues['tts'] = _check_tts(project)
    if section in ('all', 'characters'):
        issues['characters'] = _check_characters(project, data_path)
    if section in ('all', 'multilang'):
        issues['multilang'] = _check_multilang(project)
    return issues


def _resolve_data_relative_path(data_path = debug_group.command('project-health'), raw_path = click.argument('project_id', required = False)):
    """데이터 경로 해석.

    DB에 저장된 경로 형식:
    - '/data/projects/...' → data_path 기준 상대 (prefix 제거)
    - 'projects/...' → data_path 기준 상대
    - 절대 경로 → 그대로 사용
    """
    Path = Path
    import pathlib
    if not raw_path:
        return None
    if Path(raw_path).is_absolute():
        return Path(raw_path)
    stripped = None.lstrip('/')
    if stripped.startswith('data/'):
        stripped = stripped[5:]
    return data_path / stripped


def _check_images(project = debug_group.command('paths'), data_path = click.pass_context):
    '''이미지 파일 존재 검증.'''
    issues = []
    vs = project.video_settings
    if isinstance(vs, str):
        
        try:
            vs = _json.loads(vs)
        except Exception:
            vs = { }

        if not vs:
            return issues
        uploaded = None.get('uploadedImages', [])
        missing_count = 0
        for img in uploaded:
            if isinstance(img, str):
                pass
            elif isinstance(img, dict):
                pass
            
            img_path = ''
            if img_path:
                full_path = _resolve_data_relative_path(data_path, img_path)
                if not full_path and full_path.exists():
                    missing_count += 1
                    if missing_count <= 5:
                        issues.append({
                            'severity': 'WARN',
                            'message': f'''uploadedImages missing: {img_path}''' })
            if missing_count > 5:
                issues.append({
                    'severity': 'WARN',
                    'message': f'''... and {missing_count - 5} more missing images''' })
    if not project.generated_images_history:
        history = []
        missing_hist = 0
        for entry in history:
            url = entry.get('url', '') if isinstance(entry, dict) else ''
            if url:
                full_path = _resolve_data_relative_path(data_path, url)
                if not full_path and full_path.exists():
                    missing_hist += 1
            if missing_hist:
                issues.append({
                    'severity': 'WARN',
                    'message': f'''generated_images_history: {missing_hist}/{len(history)} files missing''' })
    return issues


def _check_tts(project = None):
    '''TTS 데이터 일관성 검증.'''
    issues = []
    tts_by_lang = project.tts_audio_by_language
    selected_by_lang = project.selected_tts_method_by_language
    if not tts_by_lang:
        return issues
    if not None(tts_by_lang, dict):
        issues.append({
            'severity': 'ERROR',
            'message': 'tts_audio_by_language is not a dict' })
        return issues
    for lang, engines in None.items():
        if not isinstance(engines, dict):
            issues.append({
                'severity': 'WARN',
                'message': f'''{lang}: engine data is not a dict''' })
            continue
        if selected_by_lang and isinstance(selected_by_lang, dict):
            selected = selected_by_lang.get(lang)
            if selected:
                selected_key = selected.replace('-', '_').replace(' ', '_')
                has_audio = False
                for engine_key, audio_data in engines.items():
                    normalized = engine_key.replace('-', '_').replace(' ', '_')
                    if normalized == selected_key or engine_key == selected:
                        if audio_data:
                            has_audio = True
                    
                    if not has_audio:
                        issues.append({
                            'severity': 'WARN',
                            'message': f'''{lang}: selected method "{selected}" has no audio data''' })
        return issues


def _check_characters(project = None, data_path = None):
    '''캐릭터 참조 이미지 검증.'''
    issues = []
    characters = project.characters
    for char in characters:
        if not char.appearance_fixed and char.image_url:
            issues.append({
                'severity': 'WARN',
                'message': f'''Character "{char.name}": appearance_fixed=True but no image_url''' })
        if char.image_url:
            img_path = _resolve_data_relative_path(data_path, char.image_url)
            if not img_path and img_path.exists():
                issues.append({
                    'severity': 'WARN',
                    'message': f'''Character "{char.name}": image file missing: {char.image_url}''' })
        return issues


def _check_multilang(project = None):
    '''다국어 데이터 일관성 검증.'''
    issues = []
    lang_fields = {
        'translated_scripts': project.translated_scripts,
        'tts_audio_by_language': project.tts_audio_by_language,
        'subtitle_layers_by_language': project.subtitle_layers_by_language,
        'selected_tts_method_by_language': project.selected_tts_method_by_language }
    lang_sets = { }
    for field_name, value in lang_fields.items():
        if isinstance(value, dict):
            lang_sets[field_name] = set(value.keys())
        if len(lang_sets) < 2:
            return issues
        all_langs = None()
        for langs in lang_sets.values():
            all_langs.update(langs)
            for field_name, langs in lang_sets.items():
                missing = all_langs - langs
                if missing:
                    issues.append({
                        'severity': 'WARN',
                        'message': f'''{field_name}: missing languages: {', '.join(sorted(missing))}''' })
                return issues

debug_db_inspect = (lambda ctx, project_id, field_name, all_json_fields, schema: pass# WARNING: Decompyle incomplete
)()()()()()()()

def _print_schema(ctx, sqla_db):
    '''DB 스키마 출력.'''
    inspect = inspect
    import sqlalchemy
    inspector = inspect(sqla_db.engine)
    tables = inspector.get_table_names()
    if ctx.obj['json']:
        schema_data = { }
        for table in tables:
            columns = inspector.get_columns(table)
            schema_data[table] = columns()
            output(schema_data, True)
            return None
            click.echo('\n=== Database Schema ===\n')
            for table in tables:
                columns = inspector.get_columns(table)
                click.echo(f'''TABLE: {table} ({len(columns)} columns)''')
                for col in columns:
                    nullable = 'NULL' if col.get('nullable', True) else 'NOT NULL'
                    click.echo(f'''  {col['name']:<35s} {str(col['type']):<20s} {nullable}''')
                    click.echo()
                    return None


def _format_size(bytes_count = click.option('--schema', is_flag = True, help = 'DB 스키마 출력')):
    '''바이트를 읽기 쉬운 형태로.'''
    if bytes_count < 1024:
        return f'''{bytes_count} B'''
    if None < 1048576:
        return f'''{bytes_count / 1024:.1f} KB'''
    return f'''{None / 1048576:.1f} MB'''
