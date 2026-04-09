# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webhdfs.pyc (Python 3.11)

import logging
import os
import secrets
import shutil
import tempfile
import uuid
from contextlib import suppress
from urllib.parse import quote
import requests
from spec import AbstractBufferedFile, AbstractFileSystem
from utils import infer_storage_options, tokenize
logger = logging.getLogger('webhdfs')

class WebHDFS(AbstractFileSystem):
    pass
# WARNING: Decompyle incomplete


class WebHDFile(AbstractBufferedFile):
    pass
# WARNING: Decompyle incomplete
