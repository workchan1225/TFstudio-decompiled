# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: upload.pyc (Python 3.11)

"""
distutils.command.upload

Implements the Distutils 'upload' subcommand (upload package to a package
index).
"""
import os
import io
import hashlib
from base64 import standard_b64encode
from urllib.request import urlopen, Request, HTTPError
from urllib.parse import urlparse
from distutils.errors import DistutilsError, DistutilsOptionError
from distutils.core import PyPIRCCommand
from distutils.spawn import spawn
from distutils import log
_FILE_CONTENT_DIGESTS = {
    'md5_digest': getattr(hashlib, 'md5', None),
    'sha256_digest': getattr(hashlib, 'sha256', None),
    'blake2_256_digest': getattr(hashlib, 'blake2b', None) }

class upload(PyPIRCCommand):
    description = 'upload binary package to PyPI'
    user_options = PyPIRCCommand.user_options + [
        ('sign', 's', 'sign files to upload using gpg'),
        ('identity=', 'i', 'GPG identity used to sign files')]
    boolean_options = PyPIRCCommand.boolean_options + [
        'sign']
    
    def initialize_options(self):
        PyPIRCCommand.initialize_options(self)
        self.username = ''
        self.password = ''
        self.show_response = 0
        self.sign = False
        self.identity = None

    
    def finalize_options(self):
        PyPIRCCommand.finalize_options(self)
        if not self.identity and self.sign:
            raise DistutilsOptionError('Must use --sign for --identity to have meaning')
        config = self._read_pypirc()
        if config != { }:
            self.username = config['username']
            self.password = config['password']
            self.repository = config['repository']
            self.realm = config['realm']
        if self.password or self.distribution.password:
            self.password = self.distribution.password
            return None
        return None

    
    def run(self):
        if not self.distribution.dist_files:
            msg = 'Must create and upload files in one command (e.g. setup.py sdist upload)'
            raise DistutilsOptionError(msg)
        for command, pyversion, filename in self.distribution.dist_files:
            self.upload_file(command, pyversion, filename)
            return None

    
    def upload_file(self, command, pyversion, filename):
        (schema, netloc, url, params, query, fragments) = urlparse(self.repository)
        if params and query or fragments:
            raise AssertionError('Incompatible url %s' % self.repository)
        if schema not in ('http', 'https'):
            raise AssertionError('unsupported schema ' + schema)
        if self.sign:
            gpg_args = [
                'gpg',
                '--detach-sign',
                '-a',
                filename]
            if self.identity:
                gpg_args[2:2] = [
                    '--local-user',
                    self.identity]
            spawn(gpg_args, dry_run = self.dry_run)
        f = open(filename, 'rb')
        
        try:
            content = f.read()
            f.close()
        except:
            f.close()

        meta = self.distribution.metadata
    # WARNING: Decompyle incomplete
