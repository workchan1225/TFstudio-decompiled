# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: content.pyc (Python 3.11)

__all__ = ('Context',)
from jnius import JavaClass, JavaStaticField, MetaJavaClass

def Context():
    '''Context'''
    __doc__ = '\n    Represents the Android Context Java class providing access to application-specific\n    resources and services.\n\n    This class serves as a bridge to interact with the Android framework and various\n    system services provided by the Android operating system. It holds functionality\n    for accessing application environments, managing resources, and invoking system:\n    defined services.\n\n    Attributes:\n        __javaclass__ (str): The fully qualified Java class name representation of the Context class.\n        DOWNLOAD_SERVICE (JavaStaticField): A static field representing the Java constant\n            for the download service.\n    '
    __javaclass__ = 'android/content/Context'
    DOWNLOAD_SERVICE = JavaStaticField('Ljava/lang/String;')

Context = <NODE:27>(Context, 'Context', JavaClass, metaclass = MetaJavaClass)
