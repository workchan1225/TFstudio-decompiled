# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: patcher.pyc (Python 3.11)

from distutils.version import LooseVersion
import io
import json
import logging
import os
import pathlib
import platform
import random
import re
import shutil
import string
import sys
import time
from urllib.request import urlopen
from urllib.request import urlretrieve
import zipfile
from multiprocessing import Lock
logger = logging.getLogger(__name__)
IS_POSIX = sys.platform.startswith(('darwin', 'cygwin', 'linux', 'linux2'))

class Patcher(object):
    lock = Lock()
    exe_name = 'chromedriver%s'
    platform = sys.platform
    if platform.endswith('win32'):
        d = '~/appdata/roaming/undetected_chromedriver'
    elif 'LAMBDA_TASK_ROOT' in os.environ:
        d = '/tmp/undetected_chromedriver'
    elif platform.startswith(('linux', 'linux2')):
        d = '~/.local/share/undetected_chromedriver'
    elif platform.endswith('darwin'):
        d = '~/Library/Application Support/undetected_chromedriver'
    else:
        d = '~/.undetected_chromedriver'
    data_path = os.path.abspath(os.path.expanduser(d))
    
    def __init__(self = None, executable_path = None, force = None, version_main = (None, False, 0, False), user_multi_procs = ('version_main', int)):
        '''
        Args:
            executable_path: None = automatic
                             a full file path to the chromedriver executable
            force: False
                    terminate processes which are holding lock
            version_main: 0 = auto
                specify main chrome version (rounded, ex: 82)
        '''
        self.force = force
        self._custom_exe_path = False
        prefix = 'undetected'
        self.user_multi_procs = user_multi_procs
        if version_main:
            self.is_old_chromedriver = version_main <= 114
            self._set_platform_name()
            if not os.path.exists(self.data_path):
                os.makedirs(self.data_path, exist_ok = True)
        if not executable_path:
            self.executable_path = os.path.join(self.data_path, '_'.join([
                prefix,
                self.exe_name]))
        if not IS_POSIX and executable_path and executable_path[-4:] == '.exe':
            executable_path += '.exe'
        self.zip_path = os.path.join(self.data_path, prefix)
        if not executable_path and self.user_multi_procs:
            self.executable_path = os.path.abspath(os.path.join('.', self.executable_path))
        if executable_path:
            self._custom_exe_path = True
            self.executable_path = executable_path
        if self.is_old_chromedriver:
            self.url_repo = 'https://chromedriver.storage.googleapis.com'
        else:
            self.url_repo = 'https://googlechromelabs.github.io/chrome-for-testing'
        self.version_main = version_main
        self.version_full = None

    
    def _set_platform_name(self):
        '''
        Set the platform and exe name based on the platform undetected_chromedriver is running on
        in order to download the correct chromedriver.
        '''
        if self.platform.endswith('win32'):
            self.platform_name = 'win32'
        if self.platform.endswith(('linux', 'linux2')):
            'linux64' = self, self.exe_name %= '.exe', .exe_name
        if self.platform.endswith('darwin'):
            return None
        return self, self.exe_name %= '', .exe_name

    
    def auto(self, executable_path, force, version_main, _ = (None, False, None, None)):
        '''

        Args:
            executable_path:
            force:
            version_main:

        Returns:

        '''
        p = pathlib.Path(self.data_path)
        if self.user_multi_procs:
            Lock()
            files = list(p.rglob('*chromedriver*'))
            most_recent = max(files, key = (lambda f: f.stat().st_mtime))
            files.remove(most_recent)
            list(map((lambda f: f.unlink()), files))
            if self.is_binary_patched(most_recent):
                self.executable_path = str(most_recent)
                None(None, None)
                return True
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        if executable_path:
            self.executable_path = executable_path
            self._custom_exe_path = True
        if self._custom_exe_path:
            ispatched = self.is_binary_patched(self.executable_path)
            if not ispatched:
                return self.patch_exe()
            return None
        if None:
            self.version_main = version_main
        if force is True:
            self.force = force
        
        try:
            os.unlink(self.executable_path)
        except PermissionError:
            if self.force:
                self.force_kill_instances(self.executable_path)
                return 
            if self.is_binary_patched():
                return True
            except PermissionError:
                pass
        except FileNotFoundError:
            pass

        release.version[0] = self.fetch_release_number()
        self.version_full = release
        self.unzip_package(self.fetch_package())
        return self.patch()

    
    def driver_binary_in_use(self = None, path = None):
        """
        naive test to check if a found chromedriver binary is
        currently in use

        Args:
            path: a string or PathLike object to the binary to check.
                  if not specified, we check use this object's executable_path
        """
        if not path:
            path = self.executable_path
        p = pathlib.Path(path)
        if not p.exists():
            raise OSError('file does not exist: %s' % p)
        
        try:
            fs = open(p, mode = 'a+b')
            exc = []
            fs.seek(0, 0)
        except PermissionError:
            e = None
            exc.append(e)
            e = None
            del e
        except:
            e = None
            del e

        fs.readline()

    
    def cleanup_unused_files(self):
        p = pathlib.Path(self.data_path)
        items = list(p.glob('*undetected*'))
        for item in items:
            item.unlink()
            return None

    
    def patch(self):
        self.patch_exe()
        return self.is_binary_patched()

    
    def fetch_release_number(self):
        '''
        Gets the latest major version available, or the latest major version of self.target_version if set explicitly.
        :return: version string
        :rtype: LooseVersion
        '''
        if self.is_old_chromedriver:
            path = f'''/latest_release_{self.version_main}'''
            path = path.upper()
            logger.debug('getting release number from %s' % path)
            return LooseVersion(urlopen(self.url_repo + path).read().decode())
        if not None.version_main:
            path = '/last-known-good-versions-with-downloads.json'
            logger.debug('getting release number from %s' % path)
            conn = urlopen(self.url_repo + path)
            response = conn.read().decode()
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        last_versions = json.loads(response)
        return LooseVersion(last_versions['channels']['Stable']['version'])
        path = '/latest-versions-per-milestone-with-downloads.json'
        logger.debug('getting release number from %s' % path)
        conn = urlopen(self.url_repo + path)
        response = conn.read().decode()
        None(None, None)

    
    def parse_exe_version(self):
        pass
    # WARNING: Decompyle incomplete

    
    def fetch_package(self):
        '''
        Downloads ChromeDriver from source

        :return: path to downloaded file
        '''
        zip_name = f'''chromedriver_{self.platform_name}.zip'''
        if self.is_old_chromedriver:
            download_url = f'''{self.url_repo!s}/{self.version_full.vstring!s}/{zip_name!s}'''
        else:
            zip_name = zip_name.replace('_', '-', 1)
            download_url = 'https://storage.googleapis.com/chrome-for-testing-public/%s/%s/%s'
            download_url %= (self.version_full.vstring, self.platform_name, zip_name)
        logger.debug('downloading from %s' % download_url)
        return urlretrieve(download_url)[0]

    
    def unzip_package(self, fp):
        '''
        Does what it says

        :return: path to unpacked executable
        '''
        exe_path = self.exe_name
        if not self.is_old_chromedriver:
            zip_name = f'''chromedriver-{self.platform_name}'''
            exe_path = os.path.join(zip_name, self.exe_name)
        logger.debug('unzipping %s' % fp)
        
        try:
            os.unlink(self.zip_path)
        except (FileNotFoundError, OSError):
            pass

        os.makedirs(self.zip_path, mode = 493, exist_ok = True)
        zf = zipfile.ZipFile(fp, mode = 'r')
        zf.extractall(self.zip_path)
        None(None, None)

    force_kill_instances = (lambda exe_name: exe_name = os.path.basename(exe_name)if IS_POSIX:
r = os.system('kill -f -9 $(pidof %s)' % exe_name)else:
r = os.system('taskkill /f /im %s' % exe_name)not r)()
    gen_random_cdc = (lambda : cdc = random.choices(string.ascii_letters, k = 27)''.join(cdc).encode())()
    
    def is_binary_patched(self, executable_path = (None,)):
        if not executable_path:
            pass
        executable_path = self.executable_path
        
        try:
            fh = io.open(executable_path, 'rb')
            
            try:
                None(None, None)
                return 
                with None:
                    if not None, fh.read().find(b'undetected chromedriver') != -1:
                        
                        try:
                            
                            try:
                                return None
                            except FileNotFoundError:
                                return False





    
    def patch_exe(self):
        start = time.perf_counter()
        logger.info('patching driver executable %s' % self.executable_path)
        fh = io.open(self.executable_path, 'r+b')
        content = fh.read()
        match_injected_codeblock = re.search(b'\\{window\\.cdc.*?;\\}', content)
        if match_injected_codeblock:
            target_bytes = match_injected_codeblock[0]
            new_target_bytes = b'{console.log("undetected chromedriver 1337!")}'.ljust(len(target_bytes), b' ')
            new_content = content.replace(target_bytes, new_target_bytes)
            if new_content == content:
                logger.warning('something went wrong patching the driver binary. could not find injection code block')
            else:
                logger.debug(f'''found block:\n{target_bytes!s}\nreplacing with:\n{new_target_bytes!s}''')
            fh.seek(0)
            fh.write(new_content)
        None(None, None)

    
    def __repr__(self):
        return '{0:s}({1:s})'.format(self.__class__.__name__, self.executable_path)

    
    def __del__(self):
        if self._custom_exe_path:
            return None
        timeout = None
        t = time.monotonic()
        
        now = lambda : time.monotonic()
        if now() - t > timeout:
            
            try:
                if self.user_multi_procs:
                    return None
                None.unlink(self.executable_path)
                logger.debug('successfully unlinked %s' % self.executable_path)
                return None
            except (OSError, RuntimeError, PermissionError):
                time.sleep(0.01)
                continue
                except FileNotFoundError:
                    return None
                return None
