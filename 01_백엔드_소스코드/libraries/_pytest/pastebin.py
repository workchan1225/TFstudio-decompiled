# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pastebin.pyc (Python 3.11)

'''Submit failure or test session information to a pastebin service.'''
from __future__ import annotations
from io import StringIO
import tempfile
from typing import IO
from _pytest.config import Config
from _pytest.config import create_terminal_writer
from _pytest.config.argparsing import Parser
from _pytest.stash import StashKey
from _pytest.terminal import TerminalReporter
import pytest
pastebinfile_key = StashKey[IO[bytes]]()

def pytest_addoption(parser = None):
    group = parser.getgroup('terminal reporting')
    group.addoption('--pastebin', metavar = 'mode', action = 'store', dest = 'pastebin', default = None, choices = [
        'failed',
        'all'], help = 'Send failed|all info to bpaste.net pastebin service')

pytest_configure = (lambda config = None: pass# WARNING: Decompyle incomplete
)()

def pytest_unconfigure(config = None):
    if pastebinfile_key in config.stash:
        pastebinfile = config.stash[pastebinfile_key]
        pastebinfile.seek(0)
        sessionlog = pastebinfile.read()
        pastebinfile.close()
        del config.stash[pastebinfile_key]
        tr = config.pluginmanager.getplugin('terminalreporter')
        del tr._tw.__dict__['write']
        tr.write_sep('=', 'Sending information to Paste Service')
        pastebinurl = create_new_paste(sessionlog)
        tr.write_line(f'''pastebin session-log: {pastebinurl}\n''')
        return None


def create_new_paste(contents = None):
    '''Create a new paste using the bpaste.net service.

    :contents: Paste contents string.
    :returns: URL to the pasted contents, or an error message.
    '''
    import re
    HTTPError = HTTPError
    import urllib.error
    urlencode = urlencode
    import urllib.parse
    urlopen = urlopen
    import urllib.request
    params = {
        'code': contents,
        'lexer': 'text',
        'expiry': '1week' }
    url = 'https://bpa.st'
    
    try:
        response = urlopen(url, data = urlencode(params).encode('ascii')).read().decode('utf-8')
    except HTTPError:
        e = None
        e
        None(None, None)
        del e
        return None
        with None:
            if not :
                pass
        None, f'''bad response: {e}''', 
        None = None
        del e
    except OSError:
        e = None
        del e
        return None
        None = 
        del e

    m = re.search('href="/raw/(\\w+)"', response)
    if m:
        return f'''{url}/show/{m.group(1)}'''
    return None + response + "')"


def pytest_terminal_summary(terminalreporter = None):
    if terminalreporter.config.option.pastebin != 'failed':
        return None
# WARNING: Decompyle incomplete
