# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grok_automation_service.pyc (Python 3.11)

'''
Grok Automation Service

Automates Grok web interface for image-to-video conversion using undetected-chromedriver.
Handles X (Twitter) OAuth login, image upload, video generation, and download.
'''
import os
import time
import json
import logging
import ssl
import base64
import hashlib
import atexit
import threading
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

def setup_grok_file_logger():
    '''Set up or reuse the Grok automation file logger for this process.'''
    get_data_path = get_data_path
    import app.config.paths
    log_dir = get_data_path() / 'logs'
    log_dir.mkdir(parents = True, exist_ok = True)
    log_file = log_dir / 'grok_automation.log'
    existing_logger = logging.getLogger(__name__)
    log_file_str = str(log_file)
    for handler in existing_logger.handlers:
        if isinstance(handler, logging.FileHandler) and handler.baseFilename == log_file_str:
            
            return None, (handler, log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s', datefmt = '%Y-%m-%d %H:%M:%S'))
        existing_logger.addHandler(file_handler)
        return (file_handler, log_file)

(_file_handler, GROK_LOG_FILE) = setup_grok_file_logger()

try:
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    SELENIUM_AVAILABLE = True
    uc_logger = logging.getLogger('undetected_chromedriver')
    uc_logger.setLevel(logging.ERROR)
    uc_patcher_logger = logging.getLogger('uc')
    uc_patcher_logger.setLevel(logging.ERROR)
except ImportError:
    SELENIUM_AVAILABLE = False


try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

from app import db
from app.models.grok_automation import GrokAutomationTask, GrokCredentials
from app.config.paths import get_data_path, get_default_appdata_path, get_projects_path, get_relative_data_path
from app.services.automation_humanization import AutomationHumanizer, describe_automation_humanization_settings, get_persisted_automation_humanization_settings, normalize_automation_humanization_settings
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if _file_handler not in logger.handlers:
    logger.addHandler(_file_handler)
_CERTIFI_CA_CONFIGURED = False
_CERTIFICATE_ERROR_HINTS = ('certificate_verify_failed', 'unable to get local issuer certificate', 'self signed certificate', 'tlsv1 alert unknown ca', 'sslv3 alert bad certificate', 'urlopen error [ssl')

def _is_tls_certificate_error(error = None):
    '''Return True if an exception message indicates TLS certificate verification failure.'''
    pass
# WARNING: Decompyle incomplete


def _configure_certifi_ca_bundle(force = None):
    '''Configure urllib TLS verification to use certifi CA bundle (verification remains enabled).'''
    pass
# WARNING: Decompyle incomplete


def get_grok_log_file():
    '''Return path to Grok log file for external access.'''
    return str(GROK_LOG_FILE)

GROK_URL = 'https://grok.com'
GROK_IMAGINE_URL = 'https://grok.com/imagine'
X_LOGIN_URL = 'https://x.com/i/flow/login'
GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_LOGIN_HOST_TOKENS = ('accounts.google.com', 'accounts.youtube.com')
GROK_LOGIN_HOST_TOKENS = ('grok.com', 'x.com', 'twitter.com')
GOOGLE_ACCOUNT_CHOOSER_TOKENS = ('chooser', 'chooseaccount', 'accountchooser', 'selectaccount')
PENDING_AUTH_TOKENS = ('signin', 'identifier', 'challenge', 'oauth', 'consent', 'servicelogin', 'login', 'auth', '/i/flow')
SELENIUM_SCRIPT_TIMEOUT_SECONDS = 180
DOWNLOAD_START_DETECTION_TIMEOUT_SECONDS = 30
DOWNLOAD_COMPLETION_TIMEOUT_SECONDS = 180
SELENIUM_DOWNLOAD_SCRIPT_TIMEOUT_SCHEDULE = (120, 180)
CHROME_DRIVER_INIT_TIMEOUT_SCHEDULE_SECONDS = (150, 60, 60)
GROK_VIDEO_MODE_TOGGLE_BUTTON_XPATHS = ('/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/form/div/div/div/div[2]/div[1]/button', '/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/button[1]')
GROK_GENERATE_BUTTON_XPATHS = ('/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/form/div/div/div/div[2]/div[2]/button', '/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/button[2]', "//button[@type='submit']", "//button[@aria-label='제출']", "//button[@aria-label='Submit']", "//form//button[@type='submit']")
GROK_VIDEO_DOWNLOAD_BUTTON_XPATHS = ('/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[2]', "//button[contains(@aria-label, '다운로드')]", "//button[contains(@aria-label, 'Download')]", "//button[contains(normalize-space(.), 'Download')]")
GROK_VIDEO_RADIO_BUTTON_XPATHS = ("//button[@role='radio'][.//span[normalize-space()='비디오']]", "//button[@role='radio'][contains(normalize-space(.), '비디오')]", "//button[@role='radio'][contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'video')]", "//button[@role='radio'][contains(normalize-space(.), '動画')]", "(//div[@role='radiogroup']//button[@role='radio'])[2]")
_stop_requested = False
_stop_mode: Optional[str] = None
_active_service = None
_active_service_project_id: Optional[str] = None
_active_service_lock = threading.Lock()
_login_flow_lock = threading.Lock()
_login_service: Optional['GrokAutomationService'] = None
_cached_chrome_version: Optional[int] = None
_chrome_version_detected: bool = False

def _parse_major_version(version_str = None):
    '''Extract Chrome major version from a version string.'''
    if not version_str:
        normalized = ''.strip()
        if not normalized:
            return None
        parts = None.split('.', 1)
        major_str = parts[0].strip()
        if not major_str.isdigit():
            return None
        major = None(major_str)
    return major if major > 0 else None


def get_login_service():
    '''Get or create the singleton login service instance.'''
    pass
# WARNING: Decompyle incomplete


def clear_login_service():
    '''Clear the login service singleton (after complete or error).'''
    global _login_service
    _login_service = None


def request_stop(mode = None):
    """Request to stop/pause the current generation process.

    Args:
        mode: 'stop' closes browser immediately, 'pause' keeps browser open for resume.
    """
    global _stop_requested, _stop_mode
    _stop_requested = True
    _stop_mode = 'pause' if mode == 'pause' else 'stop'
    if _stop_mode == 'pause':
        logger.info('Pause requested - keeping browser open for resume')
        return None
    None.info('Stop requested - closing browser immediately')
    (service, _, is_alive) = get_active_service_snapshot()
    if service or is_alive:
        
        try:
            logger.info('Forcefully closing browser...')
            service.close_browser()
            logger.info('Browser closed successfully')
            return None
        except Exception:
            e = None
            logger.warning(f'''Error closing browser during stop: {e}''')
            e = None
            del e
            return None
            e = None
            del e
            return None
            return None



def clear_stop_flag():
    '''Clear the stop flag (call at start of generation).'''
    global _stop_requested, _stop_mode
    _stop_requested = False
    _stop_mode = None


def set_active_service(service = None, project_id = None):
    '''Set the currently active service instance for stop handling.'''
    global _active_service, _active_service_project_id
    _active_service_lock
    _active_service = service
    _active_service_project_id = project_id
    None(None, None)
    return None
    with None:
        if not None:
            pass


def get_active_service():
    '''Get the currently active generation service (if any).'''
    (service, _, _) = get_active_service_snapshot()
    return service


def get_active_service_snapshot():
    '''Return the active service, reserved project ID, and browser liveness.'''
    _active_service_lock
    service = _active_service
    project_id = _active_service_project_id
# WARNING: Decompyle incomplete


def clear_active_service():
    '''Clear the active service reference.'''
    global _active_service, _active_service_project_id
    _active_service_lock
    _active_service = None
    _active_service_project_id = None
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _cleanup_chrome_drivers():
    '''Cleanup Chrome drivers on process exit (Flask reload, shutdown).'''
    global _active_service, _active_service_project_id, _login_service
    for name, service in (('active', _active_service), ('login', _login_service)):
        if service and hasattr(service, 'driver') and service.driver:
            if hasattr(service.driver, 'service'):
                service.driver.service = None
            service.driver.quit()
        else:
            except Exception:
                pass
            service.driver = None
            if hasattr(service, 'wait'):
                service.wait = None
        service.driver = None
        if hasattr(service, 'wait'):
            service.wait = None
        _active_service = None
        _active_service_project_id = None
        _login_service = None
        return None

atexit.register(_cleanup_chrome_drivers)

def is_stop_requested():
    '''Check if stop has been requested.'''
    return _stop_requested


def get_stop_mode():
    """Get current stop mode: None | 'pause' | 'stop'."""
    return _stop_mode


def is_pause_requested():
    '''Check whether current stop request is a pause request.'''
    if _stop_requested:
        pass
    return _stop_mode == 'pause'


def interruptible_sleep(seconds = None, check_interval = None):
    '''
    Sleep for the specified duration but check for stop request frequently.

    Args:
        seconds: Total time to sleep
        check_interval: How often to check for stop (default 0.5s)

    Returns:
        True if sleep completed normally, False if interrupted by stop request
    '''
    elapsed = 0
# WARNING: Decompyle incomplete


def get_encryption_key():
    '''Get installation-specific encryption key.'''
    _get_key = get_encryption_key
    import app.utils.secret_key
    return _get_key()


class GrokAutomationService:
    '''
    Service for automating Grok web interface.

    Workflow:
    1. Initialize browser (undetected-chromedriver)
    2. Authenticate via X OAuth
    3. Upload image to Grok
    4. Monitor video generation
    5. Download generated video
    '''
    
    def __init__(self):
        self.driver = None
        self.wait = None
        self.fernet = None
        self.download_dir = None
        self._active_humanization_task_id = None
        self._active_humanization_settings = get_persisted_automation_humanization_settings()
        self._humanizer = AutomationHumanizer(self._active_humanization_settings, logger_instance = logger, should_stop = is_stop_requested)
        if not SELENIUM_AVAILABLE:
            raise ImportError('undetected-chromedriver is not installed. Install with: pip install undetected-chromedriver')
        if CRYPTO_AVAILABLE:
            self.fernet = Fernet(get_encryption_key())
            return None

    
    def _get_humanization_config(self = None, task = None):
        task_settings = task.generation_settings if task and isinstance(task.generation_settings, dict) else { }
        if not task_settings:
            return dict(self._active_humanization_settings)
        normalized = None(task_settings)
    # WARNING: Decompyle incomplete

    
    def _activate_task_humanization(self = None, task = None):
        config = self._get_humanization_config(task)
        task_id = task.id if task else 'runtime'
        if not self._active_humanization_task_id != task_id:
            changed = self._active_humanization_settings != config
            self._active_humanization_task_id = task_id
            self._active_humanization_settings = dict(config)
            self._humanizer.set_settings(config, source = f'''grok-task:{task_id}''')
            if changed:
                logger.info('[GrokHumanization] Loaded config for task=%s: %s', task_id, describe_automation_humanization_settings(config))
        return dict(config)

    
    def _log_humanization(self, action = None, applied_delay_ms = None, reason = None, context = (None, 'manual'), delay_kind = ('action', str, 'applied_delay_ms', int, 'reason', str, 'context', Optional[Dict[(str, Any)]], 'delay_kind', str, 'return', None)):
        self._humanizer.log_manual(action, applied_delay_ms, reason, context, delay_kind = delay_kind)

    
    def _stable_wait(self = None, seconds_or_ms = None, reason = None, context = None, *, unit):
        return self._humanizer.stable_wait(seconds_or_ms, reason, context, unit = unit)

    
    def _randomized_wait(self = None, min_ms = None, max_ms = None, reason = (None,), context = ('min_ms', int, 'max_ms', int, 'reason', str, 'context', Optional[Dict[(str, Any)]], 'return', int)):
        return self._humanizer.randomized_wait(min_ms, max_ms, reason, context)

    
    def _human_pause(self = None, action_type = None, task = None, context = None, *, phase):
        pass
    # WARNING: Decompyle incomplete

    
    def _human_click(self = None, element = None, reason = None, task = None, context = (None, None), *, pre_delay, post_delay):
        pass
    # WARNING: Decompyle incomplete

    
    def _human_move_and_click(self = None, element = None, reason = None, task = (None, None), context = ('element', Any, 'reason', str, 'task', Optional[GrokAutomationTask], 'context', Optional[Dict[(str, Any)]], 'return', str)):
        return self._human_click(element, reason, task = task, context = context)

    
    def _human_retry_pause(self = None, attempt_idx = None, reason = None, task = (None, None), context = ('attempt_idx', int, 'reason', str, 'task', Optional[GrokAutomationTask], 'context', Optional[Dict[(str, Any)]], 'return', int)):
        pass
    # WARNING: Decompyle incomplete

    _kill_orphaned_chrome_processes = (lambda : if os.name != 'nt':
Noneimport subprocessrun_kwargs = {
'capture_output': True,
'text': True,
'timeout': 5,
'stdin': subprocess.DEVNULL }run_kwargs['creationflags'] = subprocess.CREATE_NO_WINDOWprofile_dir = GrokAutomationService._get_grok_profile_dir()profile_dir_str = str(profile_dir).replace('/', '\\').lower()killed_count = 0# WARNING: Decompyle incomplete
)()
    
    def _create_chrome_options(self = None, headless = None, user_data_dir = None):
        '''Create a fresh ChromeOptions instance.

        IMPORTANT: ChromeOptions cannot be reused after uc.Chrome() call.
        Must create a new instance for each driver initialization attempt.
        '''
        options = uc.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-first-run')
        options.add_argument('--no-default-browser-check')
        options.add_argument('--disable-session-crashed-bubble')
        options.add_argument('--window-size=1920,1080')
        if not headless:
            options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-features=VizDisplayCompositor')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--lang=ko-KR')
        options.add_argument('--disable-background-timer-throttling')
        options.add_argument('--disable-backgrounding-occluded-windows')
        options.add_argument('--disable-renderer-backgrounding')
        if headless:
            options.add_argument('--headless=new')
        if user_data_dir:
            options.add_argument(f'''--user-data-dir={user_data_dir}''')
        prefs = {
            'download.default_directory': self.download_dir,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True,
            'profile.default_content_settings.popups': 0,
            'profile.default_content_setting_values.automatic_downloads': 1 }
        options.add_experimental_option('prefs', prefs)
        return options

    
    def _create_driver_with_timeout(self, chrome_version = None, driver_exe_path = None, options = None, timeout_seconds = ('chrome_version', Optional[int], 'driver_exe_path', Optional[str], 'options', 'uc.ChromeOptions', 'timeout_seconds', int, 'return', Any)):
        '''Create uc.Chrome() with timeout and late-driver cleanup.

        uc.Chrome() can hang intermittently. If timeout happens, the worker thread
        cannot be force-killed, so we set a cancellation flag and make sure any
        late-created driver quits immediately to avoid blank window accumulation.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _init_driver(self = None, headless = None):
        '''Initialize Chrome driver with anti-detection measures.'''
        if self.driver:
            logger.info('Driver already initialized, reusing existing instance')
            return None
        None.info(f'''Initializing Chrome driver (headless={headless})...''')
        self._kill_orphaned_chrome_processes()
        user_data_dir = self._get_user_data_dir()
        if user_data_dir:
            logger.info(f'''Using Chrome profile: {user_data_dir}''')
            self._repair_chrome_profile(Path(user_data_dir))
        self.download_dir = self._get_download_dir()
        logger.info(f'''Download directory: {self.download_dir}''')
        chrome_version = self._detect_chrome_version()
        driver_exe_path = self._ensure_correct_chromedriver(chrome_version)
        timeout_schedule = list(CHROME_DRIVER_INIT_TIMEOUT_SCHEDULE_SECONDS)
        max_attempts = 3
        last_error = None
        for attempt_idx in range(max_attempts):
            if is_stop_requested():
                logger.info('Stop requested during driver initialization, aborting')
                raise RuntimeError('Generation stopped by user during browser initialization')
            if driver_exe_path:
                logger.info(f'''Attempt {attempt_idx + 1}/{max_attempts}: driver_executable_path={driver_exe_path}''')
            else:
                logger.info(f'''Attempt {attempt_idx + 1}/{max_attempts}: auto-detect''')
            options = self._create_chrome_options(headless, user_data_dir)
            current_timeout = timeout_schedule[min(attempt_idx, len(timeout_schedule) - 1)]
            self.driver = self._create_driver_with_timeout(chrome_version = chrome_version, driver_exe_path = driver_exe_path, options = options, timeout_seconds = current_timeout)
            self.wait = WebDriverWait(self.driver, 60)
            self.driver.set_script_timeout(SELENIUM_SCRIPT_TIMEOUT_SECONDS)
        except Exception:
            timeout_error = None
            logger.warning(f'''Failed to set Selenium script timeout: {timeout_error}''')
            timeout_error = None
            del timeout_error
        except:
            timeout_error = None
            del timeout_error
        logger.info('Chrome driver initialized successfully')
        logger.info(f'''Chrome version: {self.driver.capabilities.get('browserVersion', 'unknown')}''')

    _cleanup_stale_session_restore_files = (lambda user_data_dir = None: if not user_data_dir:
Nonedefault_dir = None.path.join(user_data_dir, 'Default')sessions_dir = os.path.join(default_dir, 'Sessions')restore_files = [
'Current Session',
'Current Tabs',
'Last Session',
'Last Tabs',
'Current Session-journal',
'Current Tabs-journal',
'Last Session-journal',
'Last Tabs-journal']removed_count = 0for base_dir in (default_dir, sessions_dir):
if not os.path.exists(base_dir):
continuefor file_name in restore_files:
file_path = os.path.join(base_dir, file_name)if not os.path.exists(file_path):
continueos.remove(file_path)removed_count += 1except PermissionError:
logger.debug(f'''Session restore file in use, skipping: {file_path}''')continueexcept Exception:
e = Nonelogger.debug(f'''Failed to remove session restore file {file_path}: {e}''')e = Nonedel econtinuee = Nonedel eif removed_count > 0:
logger.info(f'''Removed {removed_count} stale Chrome session restore files''')NoneNone)()
    _ensure_correct_chromedriver = (lambda chrome_version = None: if not chrome_version:
logger.info('Chrome version unknown, skipping pre-patch')None# WARNING: Decompyle incomplete
)()
    _detect_chrome_version = (lambda : if _chrome_version_detected:
_cached_chrome_version# WARNING: Decompyle incomplete
)()
    _get_chromedriver_cache_paths = (lambda : cache_dirs = []if os.name == 'nt':
appdata = os.environ.get('APPDATA', '')localappdata = os.environ.get('LOCALAPPDATA', '')home = os.path.expanduser('~')cache_dirs = [
os.path.join(appdata, 'undetected_chromedriver'),
os.path.join(localappdata, 'undetected_chromedriver'),
os.path.join(home, '.local', 'share', 'undetected_chromedriver')]else:
home = os.path.expanduser('~')cache_dirs = [
os.path.join(home, '.local', 'share', 'undetected_chromedriver')]cache_dirs)()
    _clear_chromedriver_cache = (lambda : import shutilfor cache_dir in GrokAutomationService._get_chromedriver_cache_paths():
if os.path.exists(cache_dir):
shutil.rmtree(cache_dir)logger.info(f'''Cleared chromedriver cache: {cache_dir}''')continueexcept Exception:
e = Nonelogger.warning(f'''Failed to clear cache {cache_dir}: {e}''')e = Nonedel econtinuee = Nonedel eNone)()
    _clear_chrome_profile = (lambda : import shutilprofile_dir = str(GrokAutomationService._get_grok_profile_dir())if os.path.exists(profile_dir):
try:
shutil.rmtree(profile_dir)logger.info(f'''Cleared Chrome profile: {profile_dir}''')Noneexcept PermissionError:
e = Noneif getattr(e, 'winerror', None) == 32 or 'WinError 32' in str(e):
error_msg = "Chrome 프로필이 다른 프로세스에 의해 잠겨 있습니다. 'Grok 프로필 삭제' 버튼을 눌러보시고, 안 되면 컴퓨터를 재부팅한 후 다시 시도해주세요."logger.error(f'''Chrome profile locked: {e}''')logger.error(error_msg)raise RuntimeError(error_msg), elogger.warning(f'''Failed to clear Chrome profile {profile_dir}: {e}''')e = Nonedel eNonee = Nonedel eexcept Exception:
e = Nonelogger.warning(f'''Failed to clear Chrome profile {profile_dir}: {e}''')for lock_file in ('SingletonLock', 'SingletonSocket', 'SingletonCookie', 'lockfile'):
lock_path = os.path.join(profile_dir, lock_file)if os.path.exists(lock_path):
os.remove(lock_path)logger.info(f'''Removed lock file: {lock_file}''')continueexcept Exception:
continuee = Nonedel eNonee = Nonedel eNone)()
    _get_grok_appdata_dir = (lambda : get_default_appdata_path())()
    _get_grok_profile_dir = (lambda : profile_dir = GrokAutomationService._get_grok_appdata_dir() / 'chrome_profile'profile_dir.mkdir(parents = True, exist_ok = True)profile_dir)()
    _repair_chrome_profile = (lambda profile_dir = None: if not profile_dir.exists():
NoneNone._cleanup_stale_session_restore_files(str(profile_dir))for lock_name in ('SingletonLock', 'SingletonSocket', 'SingletonCookie', 'lockfile'):
lock_path = profile_dir / lock_nameif not lock_path.exists() or lock_path.is_file():
continuelock_path.unlink()logger.info(f'''Removed Chrome profile lock file: {lock_path.name}''')except PermissionError:
logger.debug(f'''Chrome profile lock file still in use: {lock_path}''')continueexcept Exception:
e = Nonelogger.debug(f'''Failed to remove Chrome profile lock file {lock_path}: {e}''')e = Nonedel econtinuee = Nonedel eprefs_files = [
profile_dir / 'Default' / 'Preferences',
profile_dir / 'Preferences']for prefs_path in prefs_files:
if not prefs_path.exists() or prefs_path.is_file():
continuefile_size = prefs_path.stat().st_sizeif file_size > 10485760:
logger.warning(f'''Corrupted Preferences file detected ({file_size / 1024 / 1024:.1f}MB): {prefs_path}''')prefs_path.unlink()continueprefs_file = open(prefs_path, 'r', encoding = 'utf-8')prefix = prefs_file.read(1024).lstrip()None(None, None)with None:
if not None:
passif not prefix and prefix.startswith('{'):
logger.warning(f'''Invalid Preferences file detected (not JSON): {prefs_path}''')prefs_path.unlink()continueexcept Exception:
e = Nonelogger.warning(f'''Failed to inspect/repair Chrome Preferences {prefs_path}: {e}''')e = Nonedel econtinuee = Nonedel e)()
    
    def _get_download_dir(self = None):
        '''Get download directory for Grok videos.'''
        download_dir = str(self._get_grok_appdata_dir() / 'grok_downloads')
        os.makedirs(download_dir, exist_ok = True)
        return download_dir

    
    def _get_user_data_dir(self = None):
        '''Get user data directory for Chrome profile.'''
        user_data_dir = str(self._get_grok_profile_dir())
        os.makedirs(user_data_dir, exist_ok = True)
        return user_data_dir

    
    def _is_driver_alive(self = None):
        '''Return True if current WebDriver session is still responsive.'''
        if not self.driver:
            return False
        
        try:
            _ = self.driver.window_handles
            _ = self.driver.current_url
            return True
        except Exception:
            return False


    
    def _close_driver(self = None):
        '''Close the browser driver and kill any leftover processes.'''
        had_driver = self.driver is not None
        if self.driver:
            
            try:
                if hasattr(self.driver, 'service'):
                    self.driver.service = None
                self.driver.quit()
                
                try:
                    pass
                except Exception:
                    
                    try:
                        pass
                    try:
                        self.driver = None
                        self.wait = None
                    except:
                        self.driver = None
                        self.wait = None

                    if not had_driver:
                        self.wait = None


        if had_driver:
            self._kill_orphaned_chrome_processes()
            return None

    
    def _clear_grok_cookies(self = None):
        '''
        Clear Grok-related cookies from Chrome profile.
        Used when switching accounts to prevent old session from being loaded.

        Returns:
            bool: True if cookies were cleared successfully
        '''
        user_data_dir = self._get_user_data_dir()
        if not user_data_dir:
            logger.warning('No user data directory found for clearing cookies')
            return False
        
        try:
            stats = self.clear_login_traces_for_profile(Path(user_data_dir), include_google = False, reset_account_state = False)
            logger.info(f'''Cleared Grok-only cookies/session traces: cookies={stats['cookiesDeleted']}, storage_files={stats['storageFilesDeleted']}''')
            return True
        except Exception:
            e = None
            logger.error(f'''Failed to clear Grok cookies: {e}''')
            e = None
            del e
            return False
            e = None
            del e


    _normalize_browser_url = (lambda url = None:
