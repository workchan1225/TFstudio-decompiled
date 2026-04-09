# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _default.pyc (Python 3.11)

'''Application default credentials.

Implements application default credentials and project ID detection.
'''
import io
import json
import logging
import os
import warnings
from google.auth import environment_vars
from google.auth import exceptions
import google.auth.transport._http_client as google
_LOGGER = logging.getLogger(__name__)
_AUTHORIZED_USER_TYPE = 'authorized_user'
_SERVICE_ACCOUNT_TYPE = 'service_account'
_EXTERNAL_ACCOUNT_TYPE = 'external_account'
_EXTERNAL_ACCOUNT_AUTHORIZED_USER_TYPE = 'external_account_authorized_user'
_IMPERSONATED_SERVICE_ACCOUNT_TYPE = 'impersonated_service_account'
_GDCH_SERVICE_ACCOUNT_TYPE = 'gdch_service_account'
_VALID_TYPES = (_AUTHORIZED_USER_TYPE, _SERVICE_ACCOUNT_TYPE, _EXTERNAL_ACCOUNT_TYPE, _EXTERNAL_ACCOUNT_AUTHORIZED_USER_TYPE, _IMPERSONATED_SERVICE_ACCOUNT_TYPE, _GDCH_SERVICE_ACCOUNT_TYPE)
_CLOUD_SDK_MISSING_CREDENTIALS = 'Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.'
_CLOUD_SDK_CREDENTIALS_WARNING = 'Your application has authenticated using end user credentials from Google Cloud SDK without a quota project. You might receive a "quota exceeded" or "API not enabled" error. See the following page for troubleshooting: https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds. '
_GENERIC_LOAD_METHOD_WARNING = 'The {} method is deprecated because of a potential security risk.\n\nThis method does not validate the credential configuration. The security\nrisk occurs when a credential configuration is accepted from a source that\nis not under your control and used without validation on your side.\n\nIf you know that you will be loading credential configurations of a\nspecific type, it is recommended to use a credential-type-specific\nload method.\nThis will ensure that an unexpected credential type with potential for\nmalicious intent is not loaded unintentionally. You might still have to do\nvalidation for certain credential types. Please follow the recommendations\nfor that method. For example, if you want to load only service accounts,\nyou can create the service account credentials explicitly:\n\n```\nfrom google.oauth2 import service_account\ncreds = service_account.Credentials.from_service_account_file(filename)\n```\n\nIf you are loading your credential configuration from an untrusted source and have\nnot mitigated the risks (e.g. by validating the configuration yourself), make\nthese changes as soon as possible to prevent security risks to your environment.\n\nRegardless of the method used, it is always your responsibility to validate\nconfigurations received from external sources.\n\nRefer to https://cloud.google.com/docs/authentication/external/externally-sourced-credentials\nfor more details.\n'
_AWS_SUBJECT_TOKEN_TYPE = 'urn:ietf:params:aws:token-type:aws4_request'

def _warn_about_problematic_credentials(credentials):
    """Determines if the credentials are problematic.

    Credentials from the Cloud SDK that are associated with Cloud SDK's project
    are problematic because they may not have APIs enabled and have limited
    quota. If this is the case, warn about it.
    """
    _cloud_sdk = _cloud_sdk
    import google.auth
    if credentials.client_id == _cloud_sdk.CLOUD_SDK_CLIENT_ID:
        warnings.warn(_CLOUD_SDK_CREDENTIALS_WARNING)
        return None


def _warn_about_generic_load_method(method_name):
    '''Warns that a generic load method is being used.

    This is to discourage use of the generic load methods in favor of
    more specific methods. The generic methods are more likely to lead to
    security issues if the input is not validated.

    Args:
        method_name (str): The name of the method being used.
    '''
    warnings.warn(_GENERIC_LOAD_METHOD_WARNING.format(method_name), DeprecationWarning)


def load_credentials_from_file(filename, scopes, default_scopes, quota_project_id, request = (None, None, None, None)):
    """Loads Google credentials from a file.

    The credentials file must be a service account key, stored authorized
    user credentials, external account credentials, or impersonated service
    account credentials.

    .. warning::
        Important: If you accept a credential configuration (credential JSON/File/Stream)
        from an external source for authentication to Google Cloud Platform, you must
        validate it before providing it to any Google API or client library. Providing an
        unvalidated credential configuration to Google APIs or libraries can compromise
        the security of your systems and data. For more information, refer to
        `Validate credential configurations from external sources`_.

        .. _Validate credential configurations from external sources:
            https://cloud.google.com/docs/authentication/external/externally-sourced-credentials

    Args:
        filename (str): The full path to the credentials file.
        scopes (Optional[Sequence[str]]): The list of scopes for the credentials. If
            specified, the credentials will automatically be scoped if
            necessary
        default_scopes (Optional[Sequence[str]]): Default scopes passed by a
            Google client library. Use 'scopes' for user-defined scopes.
        quota_project_id (Optional[str]):  The project ID used for
            quota and billing.
        request (Optional[google.auth.transport.Request]): An object used to make
            HTTP requests. This is used to determine the associated project ID
            for a workload identity pool resource (external account credentials).
            If not specified, then it will use a
            google.auth.transport.requests.Request client to make requests.

    Returns:
        Tuple[google.auth.credentials.Credentials, Optional[str]]: Loaded
            credentials and the project ID. Authorized user credentials do not
            have the project ID information. External account credentials project
            IDs may not always be determined.

    Raises:
        google.auth.exceptions.DefaultCredentialsError: if the file is in the
            wrong format or is missing.
    """
    _warn_about_generic_load_method('load_credentials_from_file')
    if not os.path.exists(filename):
        raise exceptions.DefaultCredentialsError('File {} was not found.'.format(filename))
    file_obj = io.open(filename, 'r')
    info = json.load(file_obj)


def load_credentials_from_dict(info, scopes, default_scopes, quota_project_id, request = (None, None, None, None)):
    """Loads Google credentials from a dict.

    The credentials file must be a service account key, stored authorized
    user credentials, external account credentials, or impersonated service
    account credentials.

    .. warning::
        Important: If you accept a credential configuration (credential JSON/File/Stream)
        from an external source for authentication to Google Cloud Platform, you must
        validate it before providing it to any Google API or client library. Providing an
        unvalidated credential configuration to Google APIs or libraries can compromise
        the security of your systems and data. For more information, refer to
        `Validate credential configurations from external sources`_.

    .. _Validate credential configurations from external sources:
        https://cloud.google.com/docs/authentication/external/externally-sourced-credentials

    Args:
        info (Dict[str, Any]): A dict object containing the credentials
        scopes (Optional[Sequence[str]]): The list of scopes for the credentials. If
            specified, the credentials will automatically be scoped if
            necessary
        default_scopes (Optional[Sequence[str]]): Default scopes passed by a
            Google client library. Use 'scopes' for user-defined scopes.
        quota_project_id (Optional[str]):  The project ID used for
            quota and billing.
        request (Optional[google.auth.transport.Request]): An object used to make
            HTTP requests. This is used to determine the associated project ID
            for a workload identity pool resource (external account credentials).
            If not specified, then it will use a
            google.auth.transport.requests.Request client to make requests.

    Returns:
        Tuple[google.auth.credentials.Credentials, Optional[str]]: Loaded
            credentials and the project ID. Authorized user credentials do not
            have the project ID information. External account credentials project
            IDs may not always be determined.

    Raises:
        google.auth.exceptions.DefaultCredentialsError: if the file is in the
            wrong format or is missing.
    """
    _warn_about_generic_load_method('load_credentials_from_dict')
    if not isinstance(info, dict):
        raise exceptions.DefaultCredentialsError('info object was of type {} but dict type was expected.'.format(type(info)))
    return _load_credentials_from_info('dict object', info, scopes, default_scopes, quota_project_id, request)


def _load_credentials_from_info(filename, info, scopes, default_scopes, quota_project_id, request):
    CredentialsWithQuotaProject = CredentialsWithQuotaProject
    import google.auth.credentials
    credential_type = info.get('type')
    if credential_type == _AUTHORIZED_USER_TYPE:
        (credentials, project_id) = _get_authorized_user_credentials(filename, info, scopes)
    elif credential_type == _SERVICE_ACCOUNT_TYPE:
        (credentials, project_id) = _get_service_account_credentials(filename, info, scopes, default_scopes)
    elif credential_type == _EXTERNAL_ACCOUNT_TYPE:
        (credentials, project_id) = _get_external_account_credentials(info, filename, scopes = scopes, default_scopes = default_scopes, request = request)
    elif credential_type == _EXTERNAL_ACCOUNT_AUTHORIZED_USER_TYPE:
        (credentials, project_id) = _get_external_account_authorized_user_credentials(filename, info, request)
    elif credential_type == _IMPERSONATED_SERVICE_ACCOUNT_TYPE:
        (credentials, project_id) = _get_impersonated_service_account_credentials(filename, info, scopes)
    elif credential_type == _GDCH_SERVICE_ACCOUNT_TYPE:
        (credentials, project_id) = _get_gdch_service_account_credentials(filename, info)
    else:
        raise exceptions.DefaultCredentialsError('The file {file} does not have a valid type. Type is {type}, expected one of {valid_types}.'.format(file = filename, type = credential_type, valid_types = _VALID_TYPES))
    if isinstance(credentials, CredentialsWithQuotaProject):
        credentials = _apply_quota_project_id(credentials, quota_project_id)
    return (credentials, project_id)


def _get_gcloud_sdk_credentials(quota_project_id = (None,)):
    '''Gets the credentials and project ID from the Cloud SDK.'''
    _cloud_sdk = _cloud_sdk
    import google.auth
    _LOGGER.debug('Checking Cloud SDK credentials as part of auth process...')
    credentials_filename = _cloud_sdk.get_application_default_credentials_path()
    if not os.path.isfile(credentials_filename):
        _LOGGER.debug('Cloud SDK credentials not found on disk; not using them')
        return (None, None)
    None.catch_warnings()
    warnings.simplefilter('ignore', DeprecationWarning)
    (credentials, project_id) = load_credentials_from_file(credentials_filename, quota_project_id = quota_project_id)
    credentials._cred_file_path = credentials_filename
    if not project_id:
        project_id = _cloud_sdk.get_project_id()
    None(None, None)
    return 
    with None:
        if not None, (credentials, project_id):
            pass


def _get_explicit_environ_credentials(quota_project_id = (None,)):
    '''Gets credentials from the GOOGLE_APPLICATION_CREDENTIALS environment
    variable.'''
    _cloud_sdk = _cloud_sdk
    import google.auth
    cloud_sdk_adc_path = _cloud_sdk.get_application_default_credentials_path()
    explicit_file = os.environ.get(environment_vars.CREDENTIALS)
    _LOGGER.debug('Checking %s for explicit credentials as part of auth process...', explicit_file)
# WARNING: Decompyle incomplete


def _get_gae_credentials():
    '''Gets Google App Engine App Identity credentials and project ID.'''
    if os.environ.get(environment_vars.LEGACY_APPENGINE_RUNTIME) != 'python27':
        return (None, None)
    
    try:
        _LOGGER.debug('Checking for App Engine runtime as part of auth process...')
        
        app_engine
    except ImportError:
        _LOGGER.warning('Import of App Engine auth library failed.')
        return (None, None)

    
    try:
        app_engine.Credentials() = import google.auth.app_engine, auth
        project_id = app_engine.get_project_id()
        return (credentials, project_id)
    except EnvironmentError:
        _LOGGER.debug('No App Engine library was found so cannot authentication via App Engine Identity Credentials.')
        return (None, None)



def _get_gce_credentials(request, quota_project_id = (None, None)):
    '''Gets credentials and project ID from the GCE Metadata Service.'''
    
    try:
        compute_engine = compute_engine
        import google.auth
        _metadata = _metadata
        import google.auth.compute_engine
    except ImportError:
        _LOGGER.warning('Import of Compute Engine auth library failed.')
        return (None, None)

# WARNING: Decompyle incomplete


def _get_external_account_credentials(info, filename, scopes, default_scopes, request = (None, None, None)):
    """Loads external account Credentials from the parsed external account info.

    The credentials information must correspond to a supported external account
    credentials.

    Args:
        info (Mapping[str, str]): The external account info in Google format.
        filename (str): The full path to the credentials file.
        scopes (Optional[Sequence[str]]): The list of scopes for the credentials. If
            specified, the credentials will automatically be scoped if
            necessary.
        default_scopes (Optional[Sequence[str]]): Default scopes passed by a
            Google client library. Use 'scopes' for user-defined scopes.
        request (Optional[google.auth.transport.Request]): An object used to make
            HTTP requests. This is used to determine the associated project ID
            for a workload identity pool resource (external account credentials).
            If not specified, then it will use a
            google.auth.transport.requests.Request client to make requests.

    Returns:
        Tuple[google.auth.credentials.Credentials, Optional[str]]: Loaded
            credentials and the project ID. External account credentials project
            IDs may not always be determined.

    Raises:
        google.auth.exceptions.DefaultCredentialsError: if the info dictionary
            is in the wrong format or is missing required information.
    """
    if info.get('subject_token_type') == _AWS_SUBJECT_TOKEN_TYPE:
        aws = aws
        import google.auth
        credentials = aws.Credentials.from_info(info, scopes = scopes, default_scopes = default_scopes)
# WARNING: Decompyle incomplete


def _get_external_account_authorized_user_credentials(filename, info, scopes, default_scopes, request = (None, None, None)):
    
    try:
        external_account_authorized_user = external_account_authorized_user
        import google.auth
        credentials = external_account_authorized_user.Credentials.from_info(info)
    except ValueError:
        raise exceptions.DefaultCredentialsError('Failed to load external account authorized user credentials from {}'.format(filename))

    return (credentials, None)


def _get_authorized_user_credentials(filename, info, scopes = (None,)):
    credentials = credentials
    import google.oauth2
    
    try:
        credentials = credentials.Credentials.from_authorized_user_info(info, scopes = scopes)
    except ValueError:
        caught_exc = None
        msg = 'Failed to load authorized user credentials from {}'.format(filename)
        new_exc = exceptions.DefaultCredentialsError(msg, caught_exc)
        raise new_exc, caught_exc
        caught_exc = None
        del caught_exc

    return (credentials, None)


def _get_service_account_credentials(filename, info, scopes, default_scopes = (None, None)):
    service_account = service_account
    import google.oauth2
    
    try:
        credentials = service_account.Credentials.from_service_account_info(info, scopes = scopes, default_scopes = default_scopes)
    except ValueError:
        caught_exc = None
        msg = 'Failed to load service account credentials from {}'.format(filename)
        new_exc = exceptions.DefaultCredentialsError(msg, caught_exc)
        raise new_exc, caught_exc
        caught_exc = None
        del caught_exc

    return (credentials, info.get('project_id'))


def _get_impersonated_service_account_credentials(filename, info, scopes):
    impersonated_credentials = impersonated_credentials
    import google.auth
    
    try:
        credentials = impersonated_credentials.Credentials.from_impersonated_service_account_info(info, scopes = scopes)
    except ValueError:
        caught_exc = None
        msg = 'Failed to load impersonated service account credentials from {}'.format(filename)
        new_exc = exceptions.DefaultCredentialsError(msg, caught_exc)
        raise new_exc, caught_exc
        caught_exc = None
        del caught_exc

    return (credentials, None)


def _get_gdch_service_account_credentials(filename, info):
    gdch_credentials = gdch_credentials
    import google.oauth2
    
    try:
        credentials = gdch_credentials.ServiceAccountCredentials.from_service_account_info(info)
    except ValueError:
        caught_exc = None
        msg = 'Failed to load GDCH service account credentials from {}'.format(filename)
        new_exc = exceptions.DefaultCredentialsError(msg, caught_exc)
        raise new_exc, caught_exc
        caught_exc = None
        del caught_exc

    return (credentials, info.get('project'))


def get_api_key_credentials(key):
    '''Return credentials with the given API key.'''
    api_key = api_key
    import google.auth
    return api_key.Credentials(key)


def _apply_quota_project_id(credentials, quota_project_id):
    if quota_project_id:
        credentials = credentials.with_quota_project(quota_project_id)
    else:
        credentials = credentials.with_quota_project_from_environment()
    authorized_user_credentials = credentials
    import google.oauth2
    if not isinstance(credentials, authorized_user_credentials.Credentials) and credentials.quota_project_id:
        _warn_about_problematic_credentials(credentials)
    return credentials


def default(scopes, request, quota_project_id, default_scopes = (None, None, None, None)):
    """Gets the default credentials for the current environment.

    `Application Default Credentials`_ provides an easy way to obtain
    credentials to call Google APIs for server-to-server or local applications.
    This function acquires credentials from the environment in the following
    order:

    1. If the environment variable ``GOOGLE_APPLICATION_CREDENTIALS`` is set
       to the path of a valid service account JSON private key file, then it is
       loaded and returned. The project ID returned is the project ID defined
       in the service account file if available (some older files do not
       contain project ID information).

       If the environment variable is set to the path of a valid external
       account JSON configuration file (workload identity federation), then the
       configuration file is used to determine and retrieve the external
       credentials from the current environment (AWS, Azure, etc).
       These will then be exchanged for Google access tokens via the Google STS
       endpoint.
       The project ID returned in this case is the one corresponding to the
       underlying workload identity pool resource if determinable.

       If the environment variable is set to the path of a valid GDCH service
       account JSON file (`Google Distributed Cloud Hosted`_), then a GDCH
       credential will be returned. The project ID returned is the project
       specified in the JSON file.
    2. If the `Google Cloud SDK`_ is installed and has application default
       credentials set they are loaded and returned.

       To enable application default credentials with the Cloud SDK run::

            gcloud auth application-default login

       If the Cloud SDK has an active project, the project ID is returned. The
       active project can be set using::

            gcloud config set project

    3. If the application is running in the `App Engine standard environment`_
       (first generation) then the credentials and project ID from the
       `App Identity Service`_ are used.
    4. If the application is running in `Compute Engine`_ or `Cloud Run`_ or
       the `App Engine flexible environment`_ or the `App Engine standard
       environment`_ (second generation) then the credentials and project ID
       are obtained from the `Metadata Service`_.
    5. If no credentials are found,
       :class:`~google.auth.exceptions.DefaultCredentialsError` will be raised.

    .. _Application Default Credentials: https://developers.google.com            /identity/protocols/application-default-credentials
    .. _Google Cloud SDK: https://cloud.google.com/sdk
    .. _App Engine standard environment: https://cloud.google.com/appengine
    .. _App Identity Service: https://cloud.google.com/appengine/docs/python            /appidentity/
    .. _Compute Engine: https://cloud.google.com/compute
    .. _App Engine flexible environment: https://cloud.google.com            /appengine/flexible
    .. _Metadata Service: https://cloud.google.com/compute/docs            /storing-retrieving-metadata
    .. _Cloud Run: https://cloud.google.com/run
    .. _Google Distributed Cloud Hosted: https://cloud.google.com/blog/topics            /hybrid-cloud/announcing-google-distributed-cloud-edge-and-hosted

    Example::

        import google.auth

        credentials, project_id = google.auth.default()

    Args:
        scopes (Sequence[str]): The list of scopes for the credentials. If
            specified, the credentials will automatically be scoped if
            necessary.
        request (Optional[google.auth.transport.Request]): An object used to make
            HTTP requests. This is used to either detect whether the application
            is running on Compute Engine or to determine the associated project
            ID for a workload identity pool resource (external account
            credentials). If not specified, then it will either use the standard
            library http client to make requests for Compute Engine credentials
            or a google.auth.transport.requests.Request client for external
            account credentials.
        quota_project_id (Optional[str]): The project ID used for
            quota and billing.
        default_scopes (Optional[Sequence[str]]): Default scopes passed by a
            Google client library. Use 'scopes' for user-defined scopes.
    Returns:
        Tuple[~google.auth.credentials.Credentials, Optional[str]]:
            the current environment's credentials and project ID. Project ID
            may be None, which indicates that the Project ID could not be
            ascertained from the environment.

    Raises:
        ~google.auth.exceptions.DefaultCredentialsError:
            If no credentials were found, or if the credentials found were
            invalid.
    """
    pass
# WARNING: Decompyle incomplete
