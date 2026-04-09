# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: os.pyc (Python 3.11)

__all__ = ('Environment',)
from jnius import JavaClass, JavaStaticField, MetaJavaClass

def Environment():
    '''Environment'''
    __doc__ = "\n    Represents the Android environment class for interacting with the external storage and system paths.\n\n    This class provides access to system-defined constants and methods for\n    interacting with the device's file and directory management environment.\n    Acts as a proxy to the Android's Java environment class. Use its attributes\n    and methods to access critical file paths or configurations within the\n    Android operating system.\n\n    Attributes:\n        __javaclass__ (str): Represents the Java class path being bridged.\n        DIRECTORY_DOWNLOADS (JavaStaticField): Static field representing the\n            path for storing user downloads, defined in the Android\n            environment.\n    "
    __javaclass__ = 'android/os/Environment'
    DIRECTORY_DOWNLOADS = JavaStaticField('Ljava/lang/String;')

Environment = <NODE:27>(Environment, 'Environment', JavaClass, metaclass = MetaJavaClass)
