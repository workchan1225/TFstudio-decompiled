# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: premiere_export_service.pyc (Python 3.11)

'''
Premiere Pro Export Service

TFstudio 프로젝트를 Adobe Premiere Pro 호환 형식으로 내보내기
- 네이티브 .prproj (PremiereData XML Version 3)
- FCP XML (XMEML Version 5) + SRT 자막 파일

호환 프로그램:
- Adobe Premiere Pro CC 2019+ (native .prproj)
- Adobe Premiere Pro (FCP XML)
- DaVinci Resolve (FCP XML)
- Final Cut Pro (FCP XML)
'''
import gzip
import logging
import os
import shutil
import uuid
import zipfile

ElementTree
from datetime import datetime
import xml.etree.ElementTree, etree
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from xml.dom import minidom
from app.models.project import Project
from app.utils.file_paths import ProjectPaths
from app.config.paths import get_data_path
logger = logging.getLogger(__name__)

class PremiereExportService:
    '''TFstudio 프로젝트를 Premiere Pro 형식으로 내보내기'''
    XMEML_VERSION = '5'
    DEFAULT_TIMEBASE = 30
    DEFAULT_SAMPLE_RATE = 48000
    export_to_premiere = (lambda project = None, include_images = None, include_srt = staticmethod, export_format = (True, True, 'prproj', 30), timebase = ('project', Project, 'include_images', bool, 'include_srt', bool, 'export_format', str, 'timebase', int, 'return', str): logger.info(f'''[PremiereExport] Starting export for project: {project.id}, format: {export_format}''')if export_format == 'prproj':
PremiereExportService._export_native_prproj(project, include_images)None._export_fcp_xml(project, include_images, include_srt, timebase))()
    _export_native_prproj = (lambda project = None, include_images = None: logger.info(f'''[PremiereExport] Generating native .prproj for project: {project.id}''')PremiereExportService._validate_project(project)paths = ProjectPaths(project.id)data_dir = get_data_path()timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')if not project.title:
safe_title = (lambda .0: pass# WARNING: Decompyle incomplete
)('project'()).strip()[:30]
            export_folder_name = f'''{safe_title}_premiere_{timestamp}'''
            export_dir = paths.project_base / 'exports' / export_folder_name
            export_dir.mkdir(parents = True, exist_ok = True)
            media_dir = export_dir / 'media'
            media_dir.mkdir(exist_ok = True)
            segments = PremiereExportService._get_subtitle_segments(project)
            audio_info_orig = PremiereExportService._prepare_audio(project, data_dir)
        images_info_orig = PremiereExportService._prepare_images(project, data_dir) if include_images else []
        audio_src = Path(audio_info_orig['path'])
        audio_dst = media_dir / audio_src.name
        shutil.copy2(audio_src, audio_dst)
    # WARNING: Decompyle incomplete
)()
    _export_fcp_xml = (lambda project = None, include_images = None, include_srt = staticmethod, timebase = (True, True, 30): logger.info(f'''[PremiereExport] Generating FCP XML for project: {project.id}''')PremiereExportService._validate_project(project)paths = ProjectPaths(project.id)data_dir = get_data_path()export_dir = paths.project_base / 'exports'export_dir.mkdir(parents = True, exist_ok = True)temp_dir = paths.project_base / 'premiere_export_temp'try:
if temp_dir.exists():
shutil.rmtree(temp_dir)temp_dir.mkdir(parents = True)segments = PremiereExportService._get_subtitle_segments(project)audio_info = PremiereExportService._prepare_audio(project, data_dir)images_info = PremiereExportService._prepare_images(project, data_dir) if include_images else []xml_content = PremiereExportService._generate_fcp_xml(project = project, audio_info = audio_info, images_info = images_info, segments = segments, timebase = timebase)xml_path = temp_dir / 'project.xml'f = open(xml_path, 'w', encoding = 'utf-8')f.write(xml_content)try:
None(None, None)with None:
if not None:
try:
try:
if include_srt and segments:
srt_content = PremiereExportService._generate_srt(segments)srt_path = temp_dir / 'subtitles.srt'f = open(srt_path, 'w', encoding = 'utf-8')f.write(srt_content)try:
None(None, None)with None:
if not None:
try:
try:
readme_content = PremiereExportService._generate_readme(project_title = 'TFstudio Project', segment_count = len(segments), total_duration = segments[-1].get('end', 0) if project.title or segments else 0, include_srt = include_srt)readme_path = temp_dir / 'README.txt'f = open(readme_path, 'w', encoding = 'utf-8')f.write(readme_content)try:
None(None, None)with None:
if not None:
try:
try:
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')if not project.title:
safe_title = (lambda .0: pass# WARNING: Decompyle incomplete
)('project'()).strip()[:30]
                                                                    output_filename = f'''{safe_title}_premiere_{timestamp}.zip'''
                                                                    output_path = export_dir / output_filename
                                                                    PremiereExportService._create_zip(temp_dir, output_path)
                                                                    logger.info(f'''[PremiereExport] FCP XML export completed: {output_path}''')
                                                                    if temp_dir.exists():
                                                                        shutil.rmtree(temp_dir)
                                                                        return str(output_path)
                                                                    except Exception:
                                                                        e = ''.join
                                                                        logger.warning(f'''[PremiereExport] Failed to cleanup temp dir: {e}''')
                                                                        e = None
                                                                        del e
                                                                        return None
                                                                        e = None
                                                                        del e
                                                                    return None
                                                                if temp_dir.exists():
                                                                    shutil.rmtree(temp_dir)
                                                                    except Exception:
                                                                        
                                                                        def e(.0):
                                                                            pass
                                                                        # WARNING: Decompyle incomplete

                                                                        logger.warning(f'''[PremiereExport] Failed to cleanup temp dir: {e}''')
                                                                        e = None
                                                                        del e
                                                                        e = None
                                                                        del e










)()
    _validate_project = (lambda project = None: segments = PremiereExportService._get_subtitle_segments(project)if not segments:
raise ValueError('자막이 생성되지 않았습니다.\n\nPremiere Pro 내보내기를 위해 먼저 자막을 생성해주세요.')audio_url = project.get_final_audio_url()if not audio_url:
raise ValueError('오디오가 생성되지 않았습니다.\n\nTTS 탭에서 음성을 먼저 생성해주세요.'))()
    _validate_segments_quality = (lambda segments = None: if not segments:
FalseMAX_SEGMENT_DURATION = Noneinvalid_count = 0for seg in segments:
if not seg.get('start', 0):
start = 0if not seg.get('end', 0):
end = 0duration = end - startif duration > MAX_SEGMENT_DURATION:
logger.warning(f'''[PremiereExport] Segment too long: {duration:.2f}s''')Falseif None == 0 and end == 0:
invalid_count += 1if invalid_count > len(segments) * 0.5:
logger.warning(f'''[PremiereExport] Too many invalid segments: {invalid_count}/{len(segments)}''')FalseNone)()
    _get_subtitle_segments = (lambda project = None:
