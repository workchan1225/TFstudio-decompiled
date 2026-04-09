# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: service.pyc (Python 3.11)

import errno
import logging
import os
import subprocess
import sys
from abc import ABC, abstractmethod
from collections.abc import Mapping
from io import IOBase
from subprocess import PIPE
from time import sleep
from typing import IO, Any
from urllib import request
from urllib.error import URLError
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import utils
logger = logging.getLogger(__name__)

class Service(ABC):
    '''Abstract base class for all service objects that manage driver processes.

    Services typically launch a child program in a new process as an interim process to
    communicate with a browser.

    Args:
        executable_path: (Optional) Install path of the executable.
        port: (Optional) Port for the service to run on, defaults to 0 where the operating system will decide.
        log_output: (Optional) int representation of STDOUT/DEVNULL, any IO instance or String path to file.
        env: (Optional) Mapping of environment variables for the new process, defaults to `os.environ`.
        driver_path_env_key: (Optional) Environment variable to use to get the path to the driver executable.
    '''
    
    def __init__(self, executable_path = None, port = None, log_output = None, env = (None, 0, None, None, None), driver_path_env_key = ('executable_path', str | None, 'port', int, 'log_output', int | str | IO[Any] | None, 'env', Mapping[(Any, Any)] | None, 'driver_path_env_key', str | None, 'return', None), **kwargs):
        self
        if isinstance(log_output, str):
            self.log_output = open(log_output, 'a+', encoding = 'utf-8')
        elif log_output == subprocess.STDOUT:
            self.log_output = None
    # WARNING: Decompyle incomplete

    service_url = (lambda self = None: f'''http://{utils.join_host_port('localhost', self.port)}''')()
    command_line_args = (lambda self = None: raise NotImplementedError('This method needs to be implemented in a sub class'))()
    path = (lambda self = None:
