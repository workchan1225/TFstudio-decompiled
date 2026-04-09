# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nonmultipart.pyc (Python 3.11)

'''Base class for MIME type messages that are not multipart.'''
__all__ = [
    'MIMENonMultipart']
from email import errors
from email.mime.base import MIMEBase

class MIMENonMultipart(MIMEBase):
    '''Base class for MIME non-multipart type messages.'''
    
    def attach(self, payload):
        raise errors.MultipartConversionError('Cannot attach additional subparts to non-multipart/*')
