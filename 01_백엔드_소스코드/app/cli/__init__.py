# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''TFstudio CLI - 개발 및 디버깅 도구.'''
import functools
import click

def _create_cli_app():
    '''CLI용 Flask 앱 생성 (서버 미시작).'''
    create_app = create_app
    import app
    return create_app()


def with_app_context(f):
    '''Click 명령을 Flask app context 내에서 실행하는 데코레이터.'''
    pass
# WARNING: Decompyle incomplete


class _JsonGroup(click.Group):
    pass
# WARNING: Decompyle incomplete

cli = (lambda ctx: ctx.ensure_object(dict)ctx.obj.setdefault('json', False))()()

def _register_commands():
    project_group = project_group
    import app.cli.commands.project
    pipeline_group = pipeline_group
    import app.cli.commands.pipeline
    tts_group = tts_group
    import app.cli.commands.tts
    debug_group = debug_group
    import app.cli.commands.debug
    cli.add_command(project_group, 'project')
    cli.add_command(pipeline_group, 'pipeline')
    cli.add_command(tts_group, 'tts')
    cli.add_command(debug_group, 'debug')

_register_commands()
