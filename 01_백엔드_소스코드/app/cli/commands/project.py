# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: project.pyc (Python 3.11)

'''프로젝트 관리 CLI 명령.'''
import click
from app.cli import with_app_context
from app.cli.formatters import output
project_group = (lambda : pass)()
list_projects = (lambda ctx, status, limit: Project = Projectimport app.models.projectquery = Project.query.order_by(Project.created_at.desc())if status:
query = query.filter_by(status = status)projects = query.limit(limit).all()data = projects()output(data, ctx.obj['json']))()()()()()
get_project = (lambda ctx, project_id, include_characters, include_script: Project = Projectimport app.models.projectproject = Project.query.get(project_id)if not project:
click.echo(f'''Project not found: {project_id}''', err = True)raise SystemExit(1)data = {
'id': project.id,
'title': project.title,
'type': project.type,
'status': project.status,
'content_format': project.content_format,
'current_step': project.current_step,
'selected_tts_method': project.selected_tts_method,
'active_script_language': project.active_script_language,
'created_at': str(project.created_at) if project.created_at else None,
'updated_at': str(project.updated_at) if project.updated_at else None }if include_script and project.script:
data['script'] = project.script[:2000]data['script_truncated'] = len(project.script) > 2000if include_characters:
characters = project.charactersdata['characters'] = characters()output(data, ctx.obj['json']))()()()()()()
project_stats = (lambda ctx: Character = CharacterProject = Projectimport app.models.projecttotal = Project.query.count()by_status = { }for status_val in ('draft', 'in-progress', 'completed'):
by_status[status_val] = Project.query.filter_by(status = status_val).count()by_type = { }for type_val in ('direct', 'simple'):
by_type[type_val] = Project.query.filter_by(type = type_val).count()total_characters = Character.query.count()data = {
'total_projects': total,
'by_status': by_status,
'by_type': by_type,
'total_characters': total_characters }output(data, ctx.obj['json'])None)()()()
