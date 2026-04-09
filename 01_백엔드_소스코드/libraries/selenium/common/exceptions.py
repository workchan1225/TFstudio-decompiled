# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

'''Exceptions that may happen in all the webdriver code.'''
from collections.abc import Sequence
from typing import Any
SUPPORT_MSG = 'For documentation on this error, please visit:'
ERROR_URL = 'https://www.selenium.dev/documentation/webdriver/troubleshooting/errors'

class WebDriverException(Exception):
    pass
# WARNING: Decompyle incomplete


class InvalidSwitchToTargetException(WebDriverException):
    """Thrown when frame or window target to be switched doesn't exist."""
    pass


class NoSuchFrameException(InvalidSwitchToTargetException):
    """Thrown when frame target to be switched doesn't exist."""
    pass


class NoSuchWindowException(InvalidSwitchToTargetException):
    """Thrown when window target to be switched doesn't exist.

    To find the current set of active window handles, you can get a list
    of the active window handles in the following way::

        print driver.window_handles
    """
    pass


class NoSuchElementException(WebDriverException):
    pass
# WARNING: Decompyle incomplete


class NoSuchAttributeException(WebDriverException):
    """Thrown when the attribute of element could not be found.

    You may want to check if the attribute exists in the particular
    browser you are testing against.  Some browsers may have different
    property names for the same property.  (IE8's .innerText vs. Firefox
    .textContent)
    """
    pass


class NoSuchShadowRootException(WebDriverException):
    '''Thrown when trying to access the shadow root of an element when it does not have a shadow root attached.'''
    pass


class StaleElementReferenceException(WebDriverException):
    pass
# WARNING: Decompyle incomplete


class InvalidElementStateException(WebDriverException):
    """Thrown when a command could not be completed because the element is in an invalid state.

    This can be caused by attempting to clear an element that isn't both editable and resettable.
    """
    pass


class UnexpectedAlertPresentException(WebDriverException):
    pass
# WARNING: Decompyle incomplete


class NoAlertPresentException(WebDriverException):
    '''Thrown when switching to no presented alert.

    This can be caused by calling an operation on the Alert() class when
    an alert is not yet on the screen.
    '''
    pass


class ElementNotVisibleException(InvalidElementStateException):
    pass
# WARNING: Decompyle incomplete


class ElementNotInteractableException(InvalidElementStateException):
    pass
# WARNING: Decompyle incomplete


class ElementNotSelectableException(InvalidElementStateException):
    """Thrown when trying to select an unselectable element.

    For example, selecting a 'script' element.
    """
    pass


class InvalidCookieDomainException(WebDriverException):
    '''Thrown when attempting to add a cookie under a different domain.'''
    pass


class UnableToSetCookieException(WebDriverException):
    '''Thrown when a driver fails to set a cookie.'''
    pass


class TimeoutException(WebDriverException):
    '''Thrown when a command does not complete in enough time.'''
    pass


class MoveTargetOutOfBoundsException(WebDriverException):
    '''Thrown when the target provided to the `ActionsChains` move() method is invalid, i.e. out of document.'''
    pass


class UnexpectedTagNameException(WebDriverException):
    '''Thrown when a support class did not get an expected web element.'''
    pass


class InvalidSelectorException(WebDriverException):
    pass
# WARNING: Decompyle incomplete


class ImeNotAvailableException(WebDriverException):
    '''Thrown when IME support is not available.

    This exception is thrown for every IME-related method call if IME
    support is not available on the machine.
    '''
    pass


class ImeActivationFailedException(WebDriverException):
    '''Thrown when activating an IME engine has failed.'''
    pass


class InvalidArgumentException(WebDriverException):
    '''The arguments passed to a command are either invalid or malformed.'''
    pass


class JavascriptException(WebDriverException):
    '''An error occurred while executing JavaScript supplied by the user.'''
    pass


class NoSuchCookieException(WebDriverException):
    '''Thrown when no cookie matching the given path name was found.'''
    pass


class ScreenshotException(WebDriverException):
    '''A screen capture was made impossible.'''
    pass


class ElementClickInterceptedException(WebDriverException):
    pass
# WARNING: Decompyle incomplete


class InsecureCertificateException(WebDriverException):
    '''Thrown when the user agent hits a certificate warning (expired or invalid TLS certificate).'''
    pass


class InvalidCoordinatesException(WebDriverException):
    """The coordinates provided to an interaction's operation are invalid."""
    pass


class InvalidSessionIdException(WebDriverException):
    pass
# WARNING: Decompyle incomplete


class SessionNotCreatedException(WebDriverException):
    pass
# WARNING: Decompyle incomplete


class UnknownMethodException(WebDriverException):
    '''The requested command matched a known URL but did not match any methods for that URL.'''
    pass


class NoSuchDriverException(WebDriverException):
    pass
# WARNING: Decompyle incomplete


class DetachedShadowRootException(WebDriverException):
    '''Raised when referenced shadow root is no longer attached to the DOM.'''
    pass
