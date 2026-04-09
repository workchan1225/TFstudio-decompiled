# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webkit.pyc (Python 3.11)

__all__ = ('ValueCallback', 'DownloadListener')
from jnius import PythonJavaClass, java_method

class ValueCallback(PythonJavaClass):
    """
    Represents a callback to receive a value from Java code.

    This class implements the Android ValueCallback interface in order to receive
    values from a Java environment. It's particularly useful when working with
    Android-related tasks where results from Java methods are passed back to Python.

    Attributes:
    on_receive_value: Callable function to handle the received value from the Java
    environment.

    Methods:
    onReceiveValue: This method is invoked when a value is received from Java,
    passing the value to the Python callback function.
    """
    __javacontext__ = 'app'
    __javainterfaces__ = [
        'android/webkit/ValueCallback']
    
    def __init__(self, on_receive_value):
        self.on_receive_value = on_receive_value

    onReceiveValue = (lambda self, value: self.on_receive_value(value))()


class DownloadListener(PythonJavaClass):
    '''
    Handles download events initiated through a WebView in an Android application.

    This class serves as a bridge for the Android `DownloadListener` interface,
    facilitating the handling of download requests generated during WebView interactions.
    By implementing this interface, it allows the developer to intercept and handle
    download events directly using the provided callback.

    Attributes:
    on_download_start (callable): A callback function that is triggered when a download
        starts. The function should accept five parameters: url, user_agent, content_disposition,
        mimetype, and content_length.
    '''
    __javacontext__ = 'app'
    __javainterfaces__ = [
        'android/webkit/DownloadListener']
    
    def __init__(self, on_download_start):
        self.on_download_start = on_download_start

    onDownloadStart = (lambda self, url, user_agent, content_disposition, mimetype, content_length: self.on_download_start(url, user_agent, content_disposition, mimetype, content_length))()
