# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _main.pyc (Python 3.11)

from __future__ import annotations
import functools
import json
import sys
import typing
import click
import pygments.lexers as pygments
import pygments.util as pygments
import rich.console as rich
import rich.markup as rich
import rich.progress as rich
import rich.syntax as rich
import rich.table as rich
from _client import Client
from _exceptions import RequestError
from _models import Response
from _status_codes import codes
if typing.TYPE_CHECKING:
    import httpcore

def print_help():
    console = rich.console.Console()
    console.print('[bold]HTTPX :butterfly:', justify = 'center')
    console.print()
    console.print('A next generation HTTP client.', justify = 'center')
    console.print()
    console.print('Usage: [bold]httpx[/bold] [cyan]<URL> [OPTIONS][/cyan] ', justify = 'left')
    console.print()
    table = rich.table.Table.grid(padding = 1, pad_edge = True)
    table.add_column('Parameter', no_wrap = True, justify = 'left', style = 'bold')
    table.add_column('Description')
    table.add_row('-m, --method [cyan]METHOD', 'Request method, such as GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD.\n[Default: GET, or POST if a request body is included]')
    table.add_row('-p, --params [cyan]<NAME VALUE> ...', 'Query parameters to include in the request URL.')
    table.add_row('-c, --content [cyan]TEXT', 'Byte content to include in the request body.')
    table.add_row('-d, --data [cyan]<NAME VALUE> ...', 'Form data to include in the request body.')
    table.add_row('-f, --files [cyan]<NAME FILENAME> ...', 'Form files to include in the request body.')
    table.add_row('-j, --json [cyan]TEXT', 'JSON data to include in the request body.')
    table.add_row('-h, --headers [cyan]<NAME VALUE> ...', 'Include additional HTTP headers in the request.')
    table.add_row('--cookies [cyan]<NAME VALUE> ...', 'Cookies to include in the request.')
    table.add_row('--auth [cyan]<USER PASS>', "Username and password to include in the request. Specify '-' for the password to use a password prompt. Note that using --verbose/-v will expose the Authorization header, including the password encoding in a trivially reversible format.")
    table.add_row('--proxy [cyan]URL', 'Send the request via a proxy. Should be the URL giving the proxy address.')
    table.add_row('--timeout [cyan]FLOAT', 'Timeout value to use for network operations, such as establishing the connection, reading some data, etc... [Default: 5.0]')
    table.add_row('--follow-redirects', 'Automatically follow redirects.')
    table.add_row('--no-verify', 'Disable SSL verification.')
    table.add_row('--http2', 'Send the request using HTTP/2, if the remote server supports it.')
    table.add_row('--download [cyan]FILE', 'Save the response content as a file, rather than displaying it.')
    table.add_row('-v, --verbose', 'Verbose output. Show request as well as response.')
    table.add_row('--help', 'Show this message and exit.')
    console.print(table)


def get_lexer_for_response(response = None):
    content_type = response.headers.get('Content-Type')
# WARNING: Decompyle incomplete


def format_request_headers(request = None, http2 = None):
    pass
# WARNING: Decompyle incomplete


def format_response_headers(http_version = None, status = None, reason_phrase = None, headers = ('http_version', 'bytes', 'status', 'int', 'reason_phrase', 'bytes | None', 'headers', 'list[tuple[bytes, bytes]]', 'return', 'str')):
    version = http_version.decode('ascii')
# WARNING: Decompyle incomplete


def print_request_headers(request = None, http2 = None):
    console = rich.console.Console()
    http_text = format_request_headers(request, http2 = http2)
    syntax = rich.syntax.Syntax(http_text, 'http', theme = 'ansi_dark', word_wrap = True)
    console.print(syntax)
    syntax = rich.syntax.Syntax('', 'http', theme = 'ansi_dark', word_wrap = True)
    console.print(syntax)


def print_response_headers(http_version = None, status = None, reason_phrase = None, headers = ('http_version', 'bytes', 'status', 'int', 'reason_phrase', 'bytes | None', 'headers', 'list[tuple[bytes, bytes]]', 'return', 'None')):
    console = rich.console.Console()
    http_text = format_response_headers(http_version, status, reason_phrase, headers)
    syntax = rich.syntax.Syntax(http_text, 'http', theme = 'ansi_dark', word_wrap = True)
    console.print(syntax)
    syntax = rich.syntax.Syntax('', 'http', theme = 'ansi_dark', word_wrap = True)
    console.print(syntax)


def print_response(response = None):
    console = rich.console.Console()
    lexer_name = get_lexer_for_response(response)
    if lexer_name:
        if lexer_name.lower() == 'json':
            
            try:
                data = response.json()
                text = json.dumps(data, indent = 4)
            except ValueError:
                text = response.text
            except:
                text = response.text

            syntax = rich.syntax.Syntax(text, lexer_name, theme = 'ansi_dark', word_wrap = True)
            console.print(syntax)
            return None
        None.print(f'''<{len(response.content)} bytes of binary data>''')
        return None

_PCTRTT = typing.Tuple[(typing.Tuple[(str, str)], ...)]
_PCTRTTT = typing.Tuple[(_PCTRTT, ...)]
_PeerCertRetDictType = typing.Dict[(str, typing.Union[(str, _PCTRTTT, _PCTRTT)])]

def format_certificate(cert = None):
    lines = []
    for key, value in cert.items():
        if isinstance(value, (list, tuple)):
            lines.append(f'''*   {key}:''')
            for item in value:
                if key in ('subject', 'issuer'):
                    for sub_item in item:
                        lines.append(f'''*     {sub_item[0]}: {sub_item[1]!r}''')
                        if isinstance(item, tuple) and len(item) == 2:
                            lines.append(f'''*     {item[0]}: {item[1]!r}''')
                            continue
                lines.append(f'''*     {item!r}''')
                lines.append(f'''*   {key}: {value!r}''')
                return '\n'.join(lines)


def trace(name = None, info = None, verbose = None):
    console = rich.console.Console()
    if name == 'connection.connect_tcp.started' and verbose:
        host = info['host']
        console.print(f'''* Connecting to {host!r}''')
        return None
    if None == 'connection.connect_tcp.complete' and verbose:
        stream = info['return_value']
        server_addr = stream.get_extra_info('server_addr')
        console.print(f'''* Connected to {server_addr[0]!r} on port {server_addr[1]}''')
        return None
    if None == 'connection.start_tls.complete' and verbose:
        stream = info['return_value']
        ssl_object = stream.get_extra_info('ssl_object')
        version = ssl_object.version()
        cipher = ssl_object.cipher()
        server_cert = ssl_object.getpeercert()
        alpn = ssl_object.selected_alpn_protocol()
        console.print(f'''* SSL established using {version!r} / {cipher[0]!r}''')
        console.print(f'''* Selected ALPN protocol: {alpn!r}''')
        if server_cert:
            console.print('* Server certificate:')
            console.print(format_certificate(server_cert))
            return None
        return None
    if None == 'http11.send_request_headers.started' and verbose:
        request = info['request']
        print_request_headers(request, http2 = False)
        return None
    if None == 'http2.send_request_headers.started' and verbose:
        request = info['request']
        print_request_headers(request, http2 = True)
        return None
    if None == 'http11.receive_response_headers.complete':
        (http_version, status, reason_phrase, headers) = info['return_value']
        print_response_headers(http_version, status, reason_phrase, headers)
        return None
    if None == 'http2.receive_response_headers.complete':
        (status, headers) = info['return_value']
        http_version = b'HTTP/2'
        reason_phrase = None
        print_response_headers(http_version, status, reason_phrase, headers)
        return None


def download_response(response = None, download = None):
    console = rich.console.Console()
    console.print()
    content_length = response.headers.get('Content-Length')
    progress = rich.progress.Progress('[progress.description]{task.description}', '[progress.percentage]{task.percentage:>3.0f}%', rich.progress.BarColumn(bar_width = None), rich.progress.DownloadColumn(), rich.progress.TransferSpeedColumn())
    description = f'''Downloading [bold]{rich.markup.escape(download.name)}'''
    if not content_length:
        download_task = progress.add_task(description, total = int(0), start = content_length is not None)
        for chunk in response.iter_bytes():
            download.write(chunk)
            progress.update(download_task, completed = response.num_bytes_downloaded)
            None(None, None)
            return None
            with None:
                if not None:
                    pass


def validate_json(ctx = None, param = None, value = None):
    pass
# WARNING: Decompyle incomplete


def validate_auth(ctx = None, param = None, value = None):
    if value == (None, None):
        return None
    (username, password) = None
    if password == '-':
        password = click.prompt('Password', hide_input = True)
    return (username, password)


def handle_help(ctx = None, param = None, value = None):
    if value or ctx.resilient_parsing:
        return None
    None()
    ctx.exit()

main = (lambda url, method, params, content, data, files, json, headers, cookies, auth, proxy, timeout, follow_redirects, verify = click.option('--download', type = click.File('wb'), help = 'Save the response content as a file, rather than displaying it.'), http2 = click.option('--verbose', '-v', type = bool, is_flag = True, default = False, help = 'Verbose. Show request as well as response.'), download = click.option('--help', is_flag = True, is_eager = True, expose_value = False, callback = handle_help, help = 'Show this message and exit.'), verbose = ('url', 'str', 'method', 'str', 'params', 'list[tuple[str, str]]', 'content', 'str', 'data', 'list[tuple[str, str]]', 'files', 'list[tuple[str, click.File]]', 'json', 'str', 'headers', 'list[tuple[str, str]]', 'cookies', 'list[tuple[str, str]]', 'auth', 'tuple[str, str] | None', 'proxy', 'str', 'timeout', 'float', 'follow_redirects', 'bool', 'verify', 'bool', 'http2', 'bool', 'download', 'typing.BinaryIO | None', 'verbose', 'bool', 'return', 'None'): if not method:
method = 'POST' if content and data and files or json else 'GET'# WARNING: Decompyle incomplete
)()()()()()()()()()()()()()()()()()()()
