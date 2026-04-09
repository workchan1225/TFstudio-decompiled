# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sts.pyc (Python 3.11)

'''OAuth 2.0 Token Exchange Spec.

This module defines a token exchange utility based on the `OAuth 2.0 Token
Exchange`_ spec. This will be mainly used to exchange external credentials
for GCP access tokens in workload identity pools to access Google APIs.

The implementation will support various types of client authentication as
allowed in the spec.

A deviation on the spec will be for additional Google specific options that
cannot be easily mapped to parameters defined in the RFC.

The returned dictionary response will be based on the `rfc8693 section 2.2.1`_
spec JSON response.

.. _OAuth 2.0 Token Exchange: https://tools.ietf.org/html/rfc8693
.. _rfc8693 section 2.2.1: https://tools.ietf.org/html/rfc8693#section-2.2.1
'''
from http.client import client as http_client
import json
import urllib
from google.oauth2 import utils
_URLENCODED_HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded' }

class Client(utils.OAuthClientAuthHandler):
    pass
# WARNING: Decompyle incomplete
