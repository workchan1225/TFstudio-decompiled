# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multipart.pyc (Python 3.11)

'''Base class for MIME multipart/* type messages.'''
__all__ = [
    'MIMEMultipart']
from email.mime.base import MIMEBase

class MIMEMultipart(MIMEBase):
    '''Base class for MIME multipart/* type messages.'''
    
    def __init__(self, _subtype = None, boundary = ('mixed', None, None), _subparts = {
        'policy': None }, *, policy, **_params):
        """Creates a multipart/* type message.

        By default, creates a multipart/mixed message, with proper
        Content-Type and MIME-Version headers.

        _subtype is the subtype of the multipart content type, defaulting to
        `mixed'.

        boundary is the multipart boundary string.  By default it is
        calculated as needed.

        _subparts is a sequence of initial subparts for the payload.  It
        must be an iterable object, such as a list.  You can always
        attach new subparts to the message by using the attach() method.

        Additional parameters for the Content-Type header are taken from the
        keyword arguments (or passed into the _params argument).
        """
        pass
    # WARNING: Decompyle incomplete
