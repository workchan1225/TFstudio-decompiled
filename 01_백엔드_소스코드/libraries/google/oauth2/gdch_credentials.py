# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gdch_credentials.pyc (Python 3.11)

'''Experimental GDCH credentials support.
'''
import datetime
from google.auth import _helpers
from google.auth import _service_account_info
from google.auth import credentials
from google.auth import exceptions
from google.auth import jwt
from google.oauth2 import _client
TOKEN_EXCHANGE_TYPE = 'urn:ietf:params:oauth:token-type:token-exchange'
ACCESS_TOKEN_TOKEN_TYPE = 'urn:ietf:params:oauth:token-type:access_token'
SERVICE_ACCOUNT_TOKEN_TYPE = 'urn:k8s:params:oauth:token-type:serviceaccount'
JWT_LIFETIME = datetime.timedelta(seconds = 3600)

class ServiceAccountCredentials(credentials.Credentials):
    pass
# WARNING: Decompyle incomplete
