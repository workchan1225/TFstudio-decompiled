# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sftp.pyc (Python 3.11)

import datetime
import logging
import os
import types
import uuid
from stat import S_ISDIR, S_ISLNK
import paramiko
from  import AbstractFileSystem
from utils import infer_storage_options
logger = logging.getLogger('fsspec.sftp')

class SFTPFileSystem(AbstractFileSystem):
    pass
# WARNING: Decompyle incomplete


def commit_a_file(self):
    self.fs.mv(self.temppath, self.targetpath)


def discard_a_file(self):
    self.fs._rm(self.temppath)
