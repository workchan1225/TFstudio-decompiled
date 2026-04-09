# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: net.pyc (Python 3.11)

__all__ = ('Uri',)
from jnius import JavaClass, JavaMethod, JavaStaticMethod, MetaJavaClass

def Uri():
    '''Uri'''
    __doc__ = "\n    Represents a URI reference as defined in RFC 2396, composed of components such as\n    scheme, authority, path, query, and fragment.\n\n    The Uri class provides methods to work with uniform resource identifiers (URI). It\n    facilitates parsing, retrieving specific parts of the URI, and performing a variety\n    of URI-related manipulations. Typically used in Android development for handling\n    URI-based resources.\n\n    Attributes:\n        __javaclass__ : str\n            Specifies the associated Java class for this Python wrapper.\n        parse : JavaMethod\n            Represents the Java method 'parse' to convert a string to a Uri instance.\n        getLastPathSegment : JavaMethod\n            Represents the Java method 'getLastPathSegment' to retrieve the last\n            segment of the URI's path.\n    "
    __javaclass__ = 'android/net/Uri'
    parse = JavaStaticMethod('(Ljava/lang/String;)Landroid/net/Uri;')
    getLastPathSegment = JavaMethod('()Ljava/lang/String;')

Uri = <NODE:27>(Uri, 'Uri', JavaClass, metaclass = MetaJavaClass)
