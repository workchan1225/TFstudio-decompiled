# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _logs.pyc (Python 3.11)

import os
import logging
logger: logging.Logger = logging.getLogger('anthropic')
httpx_logger: logging.Logger = logging.getLogger('httpx')

def _basic_config():
    logging.basicConfig(format = '[%(asctime)s - %(name)s:%(lineno)d - %(levelname)s] %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')


def setup_logging():
    env = os.environ.get('ANTHROPIC_LOG')
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
