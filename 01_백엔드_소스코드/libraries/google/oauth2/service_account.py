# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: service_account.pyc (Python 3.11)

'''Service Accounts: JSON Web Token (JWT) Profile for OAuth 2.0

This module implements the JWT Profile for OAuth 2.0 Authorization Grants
as defined by `RFC 7523`_ with particular support for how this RFC is
implemented in Google\'s infrastructure. Google refers to these credentials
as *Service Accounts*.

Service accounts are used for server-to-server communication, such as
interactions between a web application server and a Google service. The
service account belongs to your application instead of to an individual end
user. In contrast to other OAuth 2.0 profiles, no users are involved and your
application "acts" as the service account.

Typically an application uses a service account when the application uses
Google APIs to work with its own data rather than a user\'s data. For example,
an application that uses Google Cloud Datastore for data persistence would use
a service account to authenticate its calls to the Google Cloud Datastore API.
However, an application that needs to access a user\'s Drive documents would
use the normal OAuth 2.0 profile.

Additionally, Google Apps domain administrators can grant service accounts
`domain-wide delegation`_ authority to access user data on behalf of users in
the domain.

This profile uses a JWT to acquire an OAuth 2.0 access token. The JWT is used
in place of the usual authorization token returned during the standard
OAuth 2.0 Authorization Code grant. The JWT is only used for this purpose, as
the acquired access token is used as the bearer token when making requests
using these credentials.

This profile differs from normal OAuth 2.0 profile because no user consent
step is required. The use of the private key allows this profile to assert
identity directly.

This profile also differs from the :mod:`google.auth.jwt` authentication
because the JWT credentials use the JWT directly as the bearer token. This
profile instead only uses the JWT to obtain an OAuth 2.0 access token. The
obtained OAuth 2.0 access token is used as the bearer token.

Domain-wide delegation
----------------------

Domain-wide delegation allows a service account to access user data on
behalf of any user in a Google Apps domain without consent from the user.
For example, an application that uses the Google Calendar API to add events to
the calendars of all users in a Google Apps domain would use a service account
to access the Google Calendar API on behalf of users.

The Google Apps administrator must explicitly authorize the service account to
do this. This authorization step is referred to as "delegating domain-wide
authority" to a service account.

You can use domain-wise delegation by creating a set of credentials with a
specific subject using :meth:`~Credentials.with_subject`.

.. _RFC 7523: https://tools.ietf.org/html/rfc7523
'''
import copy
import datetime
from google.auth import _helpers
from google.auth import _service_account_info
from google.auth import credentials
from google.auth import exceptions
from google.auth import iam
from google.auth import jwt
from google.auth import metrics
from google.oauth2 import _client
_DEFAULT_TOKEN_LIFETIME_SECS = 3600
_GOOGLE_OAUTH2_TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token'
_TRUST_BOUNDARY_LOOKUP_ENDPOINT = 'https://iamcredentials.{}/v1/projects/-/serviceAccounts/{}/allowedLocations'

class Credentials(credentials.CredentialsWithTrustBoundary, credentials.CredentialsWithTokenUri, credentials.CredentialsWithQuotaProject, credentials.Scoped, credentials.Signing):
    pass
# WARNING: Decompyle incomplete


class IDTokenCredentials(credentials.CredentialsWithTokenUri, credentials.CredentialsWithQuotaProject, credentials.Signing):
    pass
# WARNING: Decompyle incomplete
