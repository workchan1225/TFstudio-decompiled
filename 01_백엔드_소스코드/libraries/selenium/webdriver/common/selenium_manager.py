# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: selenium_manager.pyc (Python 3.11)

import json
import logging
import os
import platform
import subprocess
import sys
import sysconfig
from pathlib import Path
from selenium.common import WebDriverException
logger = logging.getLogger(__name__)

class SeleniumManager:
    '''Wrapper for getting information from the Selenium Manager binaries.

    This implementation is still in beta, and may change.
    '''
    
    def binary_paths(self = None, args = None):
        '''Determines the locations of the requested assets.

        Args:
            args: the commands to send to the selenium manager binary.

        Returns:
            Dictionary of assets and their path.
        '''
        args = [
            str(self._get_binary())] + args
        if logger.getEffectiveLevel() == logging.DEBUG:
            args.append('--debug')
        args.append('--language-binding')
        args.append('python')
        args.append('--output')
        args.append('json')
        return self._run(args)

    _get_binary = (lambda : compiled_path = Path(__file__).parent.joinpath('selenium-manager')exe = sysconfig.get_config_var('EXE')# WARNING: Decompyle incomplete
)()
    _run = (lambda args = None: command = ' '.join(args)logger.debug('Executing process: %s', command)try:
if sys.platform == 'win32':
completed_proc = subprocess.run(args, capture_output = True, creationflags = subprocess.CREATE_NO_WINDOW)else:
completed_proc = subprocess.run(args, capture_output = True)stdout = completed_proc.stdout.decode('utf-8').rstrip('\n')stderr = completed_proc.stderr.decode('utf-8').rstrip('\n')output = json.loads(stdout) if stdout != '' else {
'logs': [],
'result': { } }except Exception:
err = Noneraise WebDriverException(f'''Unsuccessful command executed: {command}'''), errerr = Nonedel errSeleniumManager._process_logs(output['logs'])result = output['result']if completed_proc.returncode:
raise WebDriverException(f'''Unsuccessful command executed: {command}; code: {completed_proc.returncode}\n{result}\n{stderr}''')result)()
    _process_logs = (lambda log_items = None: for item in log_items:
if item['level'] == 'WARN':
logger.warning(item['message'])continueif item['level'] in ('DEBUG', 'INFO'):
logger.debug(item['message'])None)()
