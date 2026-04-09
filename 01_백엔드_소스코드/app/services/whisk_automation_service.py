# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: whisk_automation_service.pyc (Python 3.11)

'''
Whisk Automation Service

Google Whisk 웹 인터페이스 자동화를 위한 서비스.
Google 계정 로그인 및 세션 관리를 담당합니다.
'''
import os
import time
import json
import logging
import base64
import hashlib
import atexit
from pathlib import Path
from typing import Optional, Dict, Any

def setup_whisk_file_logger():
    '''Setup file logger for Whisk automation.'''
    get_data_path = get_data_path
    import app.config.paths
    log_dir = get_data_path() / 'logs'
    log_dir.mkdir(parents = True, exist_ok = True)
    log_file = log_dir / 'whisk_automation.log'
    file_handler = logging.FileHandler(log_file, mode = 'a', encoding = 'utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s', datefmt = '%Y-%m-%d %H:%M:%S'))
    return (file_handler, log_file)

(_file_handler, WHISK_LOG_FILE) = setup_whisk_file_logger()

try:
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
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
from app.models.whisk_automation import WhiskCredentials, WhiskGenerationTask

try:
    from app.utils.whisk_prompt_optimizer import optimize_whisk_prompt, quick_optimize
    WHISK_OPTIMIZER_AVAILABLE = True
except ImportError:
    WHISK_OPTIMIZER_AVAILABLE = False

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(_file_handler)

def get_whisk_log_file():
    '''Return path to Whisk log file for external access.'''
    return str(WHISK_LOG_FILE)


def whisk_log(message = None, level = None):
    """
    Write log to Whisk log file.
    Use this function from any module to write to the shared Whisk log file.

    Args:
        message: Log message
        level: Log level ('debug', 'info', 'warning', 'error')
    """
    if level == 'debug':
        logger.debug(message)
        return None
    if None == 'warning':
        logger.warning(message)
        return None
    if None == 'error':
        logger.error(message)
        return None
    None.info(message)


def whisk_event(event_type = None, details = None):
    """
    Log user interaction events (button clicks, navigation, etc.)

    Args:
        event_type: Type of event (e.g., 'CLICK', 'NAVIGATE', 'INPUT')
        details: Additional details about the event
    """
    logger.info(f'''[EVENT] {event_type}: {details}''')


def reset_whisk_log():
    '''Reset (clear) the Whisk log file for a new session.'''
    global _file_handler
    
    try:
        if _file_handler:
            _file_handler.close()
            logger.removeHandler(_file_handler)
        _file_handler = logging.FileHandler(WHISK_LOG_FILE, mode = 'w', encoding = 'utf-8')
        _file_handler.setLevel(logging.DEBUG)
        _file_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s', datefmt = '%Y-%m-%d %H:%M:%S'))
        logger.addHandler(_file_handler)
        logger.info('============================================================')
        logger.info('Whisk Automation Session Started')
        logger.info(f'''Log file: {WHISK_LOG_FILE}''')
        logger.info('============================================================')
        return None
    except Exception:
        e = None
        print(f'''Error resetting log: {e}''')
        e = None
        del e
        return None
        e = None
        del e


WHISK_URL = 'https://labs.google/fx/tools/whisk'
LABS_GOOGLE_URL = 'https://labs.google/fx'
GOOGLE_LOGIN_URL = 'https://accounts.google.com/ServiceLogin'
WHISK_CSS = {
    'prompt_textarea': 'textarea[placeholder]',
    'generate_button': 'button[aria-label="프롬프트 제출"], button[aria-label="Submit prompt"]',
    'download_buttons': 'button i.google-symbols' }
_login_service: Optional['WhiskAutomationService'] = None

def get_login_service():
    '''Get or create the singleton login service instance.'''
    pass
# WARNING: Decompyle incomplete


def clear_login_service():
    '''Clear the login service singleton (after complete or error).'''
    pass
# WARNING: Decompyle incomplete

_generation_service: Optional['WhiskAutomationService'] = None
_stop_requested: bool = False
_cached_chrome_version: Optional[int] = None
_chrome_version_detected: bool = False
_generation_progress: Dict[(str, Any)] = {
    'project_id': None,
    'total': 0,
    'current': 0,
    'completed_results': [],
    'is_running': False,
    'last_update': None }
_progress_lock = None

def _cleanup_whisk_chrome_drivers():
    '''Cleanup Chrome drivers on process exit (Flask reload, shutdown).'''
    global _login_service, _generation_service
    for name, service in (('login', _login_service), ('generation', _generation_service)):
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
        _login_service = None
        _generation_service = None
        return None

atexit.register(_cleanup_whisk_chrome_drivers)

def get_generation_progress():
    '''Get current generation progress for SSE streaming.'''
    return _generation_progress.copy()


def update_generation_progress(project_id, total = None, current = None, result = None, is_running = (None, None, None, None, None, False), reset = ('project_id', str, 'total', int, 'current', int, 'result', Dict, 'is_running', bool, 'reset', bool)):
    '''Update generation progress for SSE streaming.'''
    global _generation_progress
    import time
# WARNING: Decompyle incomplete


def get_generation_service():
    '''Get or create the singleton generation service instance.'''
    pass
# WARNING: Decompyle incomplete


def clear_generation_service():
    '''Clear the generation service singleton.'''
    global _stop_requested
    _stop_requested = True
# WARNING: Decompyle incomplete


def is_generation_browser_open():
    '''
    Check if generation browser is currently open and responsive.
    Used by frontend to sync browser state on page load/refresh.

    Returns:
        bool: True if browser is open and responsive, False otherwise
    '''
    pass
# WARNING: Decompyle incomplete


def request_stop():
    '''Request stop for generation - called from stop endpoint.'''
    global _stop_requested, _stop_requested
    logger.info('Stop requested for Whisk generation')
    _stop_requested = True
    if _generation_service:
        
        try:
            _generation_service._close_driver()
        except Exception:
            e = None
            logger.warning(f'''Error closing driver on stop: {e}''')
            e = None
            del e
        except:
            e = None
            del e

        _stop_requested = False
        return None


def is_stop_requested():
    '''Check if stop has been requested.'''
    return _stop_requested


def reset_stop_flag():
    '''Reset the stop flag.'''
    global _stop_requested
    _stop_requested = False


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


class WhiskAutomationService:
    '''
    Service for automating Whisk web interface login.

    Workflow:
    1. Initialize browser (undetected-chromedriver)
    2. Authenticate via Google account
    3. Save session for future use
    '''
    
    def __init__(self):
        self.driver = None
        self.wait = None
        self.fernet = None
        self._download_dir = None
        if not SELENIUM_AVAILABLE:
            raise ImportError('undetected-chromedriver is not installed. Install with: pip install undetected-chromedriver')
        if CRYPTO_AVAILABLE:
            self.fernet = Fernet(get_encryption_key())
            return None

    
    def capture_browser_logs(self = None, context = None):
        '''
        Capture and log browser console messages and errors.
        Call this after important actions to record any JS errors or warnings.

        Args:
            context: Description of when/why logs are being captured
        '''
        if not self.driver:
            return None
        
        try:
            browser_logs = self.driver.get_log('browser')
            if browser_logs:
                logger.info(f'''[BROWSER_LOG] === {context} ===''')
                for entry in browser_logs:
                    level = entry.get('level', 'INFO')
                    message = entry.get('message', '')
                    timestamp = entry.get('timestamp', 0)
                    if timestamp:
                        datetime = datetime
                        import datetime
                        dt = datetime.fromtimestamp(timestamp / 1000)
                        time_str = dt.strftime('%H:%M:%S.%f')[:-3]
                    else:
                        time_str = '??:??:??.???'
                    logger.info(f'''[BROWSER_LOG] [{time_str}] [{level}] {message}''')
                    return None
                    return None
                    except Exception:
                        e = None
                        logger.debug(f'''Could not capture browser logs: {e}''')
                        e = None
                        del e
                        return None
                        e = None
                        del e


    
    def capture_page_errors(self = None, context = None):
        '''
        Capture JavaScript errors from the page.

        Args:
            context: Description of when/why errors are being captured
        '''
        if not self.driver:
            return None
        
        try:
            errors = self.driver.execute_script('\n                if (window.__whiskErrors) {\n                    var errors = window.__whiskErrors;\n                    window.__whiskErrors = [];\n                    return errors;\n                }\n                return [];\n            ')
            if errors:
                logger.info(f'''[PAGE_ERROR] === {context} ===''')
                for err in errors:
                    logger.error(f'''[PAGE_ERROR] {err}''')
                    return None
                    return None
                    except Exception:
                        e = None
                        logger.debug(f'''Could not capture page errors: {e}''')
                        e = None
                        del e
                        return None
                        e = None
                        del e


    
    def inject_error_listener(self = None):
        '''
        Inject JavaScript error listener to capture runtime errors.
        Call this after page load.
        '''
        if not self.driver:
            return None
        
        try:
            self.driver.execute_script("\n                if (!window.__whiskErrorListenerInstalled) {\n                    window.__whiskErrors = [];\n                    window.addEventListener('error', function(e) {\n                        window.__whiskErrors.push({\n                            type: 'error',\n                            message: e.message,\n                            filename: e.filename,\n                            lineno: e.lineno,\n                            colno: e.colno,\n                            timestamp: Date.now()\n                        });\n                    });\n                    window.addEventListener('unhandledrejection', function(e) {\n                        window.__whiskErrors.push({\n                            type: 'unhandledrejection',\n                            reason: String(e.reason),\n                            timestamp: Date.now()\n                        });\n                    });\n                    window.__whiskErrorListenerInstalled = true;\n                    console.log('[Whisk] Error listener installed');\n                }\n            ")
            logger.info('[SERVICE] Error listener injected into page')
            return None
        except Exception:
            e = None
            logger.debug(f'''Could not inject error listener: {e}''')
            e = None
            del e
            return None
            e = None
            del e


    _kill_orphaned_chrome_processes = (lambda : if os.name != 'nt':
Noneimport subprocessrun_kwargs = {
'capture_output': True,
'text': True,
'timeout': 5,
'stdin': subprocess.DEVNULL }run_kwargs['creationflags'] = subprocess.CREATE_NO_WINDOWkilled_count = 0# WARNING: Decompyle incomplete
)()
    
    def _create_chrome_options(self = None, headless = None):
        """Create fresh ChromeOptions for each driver initialization attempt.

        Note: undetected_chromedriver's ChromeOptions cannot be reused.
        This method creates a new options object for each attempt.
        """
        options = uc.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
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
        options.set_capability('goog:loggingPrefs', {
            'browser': 'ALL',
            'performance': 'ALL' })
        self._download_dir = self._get_whisk_download_dir()
        prefs = {
            'download.default_directory': self._download_dir,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True,
            'profile.default_content_settings.popups': 0,
            'profile.default_content_setting_values.automatic_downloads': 1 }
        options.add_experimental_option('prefs', prefs)
        if headless:
            options.add_argument('--headless=new')
        return options

    
    def _init_driver(self = None, headless = None, download_dir = None, use_profile = (False, None, True)):
        '''Initialize Chrome driver with anti-detection measures.

        Args:
            headless: Run browser in headless mode
            download_dir: Custom download directory
            use_profile: If True, use saved Chrome profile (preserves login state).
                        If False, use temporary profile (fresh session, no saved cookies).
        '''
        pass
    # WARNING: Decompyle incomplete

    _detect_chrome_version = (lambda :
