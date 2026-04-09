# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _logs.pyc (Python 3.11)

import os
import logging
from typing_extensions import override
from _utils import is_dict
logger: logging.Logger = logging.getLogger('openai')
httpx_logger: logging.Logger = logging.getLogger('httpx')
SENSITIVE_HEADERS = {
    'api-key',
    'authorization'}

def _basic_config():
    logging.basicConfig(format = '[%(asctime)s - %(name)s:%(lineno)d - %(levelname)s] %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')


def setup_logging():
    env = os.environ.get('OPENAI_LOG')
    if env == 'debug':
        _basic_config()
        logger.setLevel(logging.DEBUG)
        httpx_logger.setLevel(logging.DEBUG)
        return None
    if None == 'info':
        _basic_config()
        logger.setLevel(logging.INFO)
        httpx_logger.setLevel(logging.INFO)
        return None


class SensitiveHeadersFilter(logging.Filter):
    filter = (lambda self = None, record = None: pass# WARNING: Decompyle incomplete
)()
