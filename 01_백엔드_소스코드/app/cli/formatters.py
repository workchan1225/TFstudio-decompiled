# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: formatters.pyc (Python 3.11)

'''CLI 출력 포매터 - JSON/테이블/상태라인.'''
import json as _json
from typing import Any, List
import click

def output(data = None, json_mode = None):
    '''통합 출력 함수.

    json_mode=True → JSON 구조화 출력
    json_mode=False → 사람용 테이블/dict 출력
    '''
    if json_mode:
        click.echo(_json.dumps(data, ensure_ascii = False, indent = 2, default = str))
        return None
    if None(data, list):
        print_table(data)
        return None
    if None(data, dict):
        print_dict(data)
        return None
    None.echo(str(data))


def print_table(rows = None):
    '''dict 리스트를 정렬된 테이블로 출력.'''
    pass
# WARNING: Decompyle incomplete


def print_dict(d = None, indent = None):
    '''중첩 dict를 들여쓰기 형태로 출력.'''
    prefix = '  ' * indent
    for k, v in d.items():
        if isinstance(v, dict):
            click.echo(f'''{prefix}{k}:''')
            print_dict(v, indent + 1)
            continue
        if isinstance(v, list) and v and isinstance(v[0], dict):
            click.echo(f'''{prefix}{k}:''')
            print_table(v)
            continue
        click.echo(f'''{prefix}{k}: {v}''')
        return None


def status_line(label = None, value = None, status = None):
    '''상태 라인 포매팅.

    Returns:
        "  label                value                    OK"
    '''
    marks = {
        'OK': 'OK',
        'WARN': '!! WARN',
        'MISSING': '** MISSING',
        'ERROR': '** ERROR',
        'SET': 'SET',
        'EMPTY': 'EMPTY' }
    mark = marks.get(status, status)
    return f'''  {label:<30s} {value:<50s} {mark}'''


def section_header(title = None):
    '''섹션 헤더 포매팅.'''
    return f'''\n[{title}]'''
