# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pipeline.pyc (Python 3.11)

'''이미지 생성 파이프라인 디버깅 CLI 명령.'''
import json as _json
from dataclasses import asdict
import click
from app.cli import with_app_context
from app.cli.formatters import output, section_header
pipeline_group = (lambda : pass)()
pipeline_trace = (lambda ctx, project_id, scene_index, stage: Project = Projectimport app.models.projectproject = Project.query.get(project_id)if not project:
click.echo(f'''Project not found: {project_id}''', err = True)raise SystemExit(1)scene_data = _extract_scene_data(project, scene_index)if not scene_data:
click.echo(f'''Scene index {scene_index} not found or no script data.''', err = True)raise SystemExit(1)SceneImageGenerationPipelineRequest = SceneImageGenerationPipelineRequestimport app.services.scene.scene_image_generation_typesrequest = SceneImageGenerationPipelineRequest(entrypoint = scene_data.get('entrypoint', 'scene_single'), payload = scene_data.get('payload', { }), preserve_reference_character_style = scene_data.get('preserve_reference_character_style', False), informational_realistic_background = scene_data.get('informational_realistic_background', False), style_visual_category = scene_data.get('style_visual_category', ''), content_category = scene_data.get('content_category', ''), speaker_mode = scene_data.get('speaker_mode', 'multi_speaker'))trace_result = { }if stage in ('all', 'normalize'):
try:
normalize_pipeline_request = normalize_pipeline_requestimport app.services.scene.scene_image_generation_normalizernormalized = normalize_pipeline_request(request)trace_result['normalize'] = _safe_asdict(normalized)except Exception:
e = Nonetrace_result['normalize'] = {
'error': str(e) }e = Nonedel eexcept:
e = Nonedel eif stage in ('all', 'resolve'):
try:
resolve_scene_image_generation_mode = resolve_scene_image_generation_modeimport app.services.scene.scene_image_generation_mode_resolvernormalize_pipeline_request = normalize_pipeline_requestimport app.services.scene.scene_image_generation_normalizernormalized = normalize_pipeline_request(request)resolution = resolve_scene_image_generation_mode(normalized)trace_result['resolve'] = _safe_asdict(resolution)except Exception:
e = Nonetrace_result['resolve'] = {
'error': str(e) }e = Nonedel eexcept:
e = Nonedel eif stage in ('all', 'contract'):
try:
normalize_pipeline_request = normalize_pipeline_requestimport app.services.scene.scene_image_generation_normalizerresolve_scene_image_generation_style_contract = resolve_scene_image_generation_style_contractimport app.services.scene.scene_image_generation_style_contractnormalized = normalize_pipeline_request(request)contract = resolve_scene_image_generation_style_contract(normalized)trace_result['contract'] = _safe_asdict(contract)except Exception:
e = Nonetrace_result['contract'] = {
'error': str(e) }e = Nonedel eexcept:
e = Nonedel eif ctx.obj['json']:
output(trace_result, True)NoneNone.echo(f'''\n=== Pipeline Trace: Project {project_id} / Scene {scene_index} ===''')if 'normalize' in trace_result:
_print_normalize_stage(trace_result['normalize'])if 'resolve' in trace_result:
_print_resolve_stage(trace_result['resolve'])if 'contract' in trace_result:
_print_contract_stage(trace_result['contract'])_print_warnings(trace_result))()()()()()()
pipeline_resolve = (lambda ctx, entrypoint, style_visual_category, content_category, preserve_ref_style: resolve_scene_image_generation_mode = resolve_scene_image_generation_modeimport app.services.scene.scene_image_generation_mode_resolvernormalize_pipeline_request = normalize_pipeline_requestimport app.services.scene.scene_image_generation_normalizerSceneImageGenerationPipelineRequest = SceneImageGenerationPipelineRequestimport app.services.scene.scene_image_generation_typesrequest = SceneImageGenerationPipelineRequest(entrypoint = entrypoint, payload = { }, preserve_reference_character_style = preserve_ref_style, style_visual_category = style_visual_category, content_category = content_category)try:
normalized = normalize_pipeline_request(request)resolution = resolve_scene_image_generation_mode(normalized)result = _safe_asdict(resolution)except Exception:
e = Noneresult = {
'error': str(e) }e = Nonedel eexcept:
e = Nonedel eoutput(result, ctx.obj['json']))()()()()()()()

def _extract_scene_data(project = click.option('--preserve-ref-style', is_flag = True, help = '참조 스타일 잠금'), scene_index = click.pass_context):
