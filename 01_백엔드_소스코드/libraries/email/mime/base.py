# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Base class for MIME specializations.'''
__all__ = [
    'MIMEBase']
import email.policy as email
from email import message

class MIMEBase(message.Message):
    '''Base class for MIME specializations.'''
    
    def __init__(self, _maintype = None, _subtype = {
        'policy': None }, *, policy, **_params):
        '''This constructor adds a Content-Type: and a MIME-Version: header.

        The Content-Type: header is taken from the _maintype and _subtype
        arguments.  Additional parameters for this header are taken from the
        keyword arguments.
        '''
        pass
    # WARNING: Decompyle incomplete
