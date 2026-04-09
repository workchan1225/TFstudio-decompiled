# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_options.pyc (Python 3.11)

'''Client options class.

Client options provide a consistent interface for user options to be defined
across clients.

You can pass a client options object to a client.

.. code-block:: python

    from google.api_core.client_options import ClientOptions
    from google.cloud.vision_v1 import ImageAnnotatorClient

    def get_client_cert():
        # code to load client certificate and private key.
        return client_cert_bytes, client_private_key_bytes

    options = ClientOptions(api_endpoint="foo.googleapis.com",
        client_cert_source=get_client_cert)

    client = ImageAnnotatorClient(client_options=options)

You can also pass a mapping object.

.. code-block:: python

    from google.cloud.vision_v1 import ImageAnnotatorClient

    client = ImageAnnotatorClient(
        client_options={
            "api_endpoint": "foo.googleapis.com",
            "client_cert_source" : get_client_cert
        })


'''
from typing import Callable, Mapping, Optional, Sequence, Tuple
import warnings
from google.api_core import general_helpers

class ClientOptions(object):
    '''Client Options used to set options on clients.

    Args:
        api_endpoint (Optional[str]): The desired API endpoint, e.g.,
            compute.googleapis.com
        client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]): A callback
            which returns client certificate bytes and private key bytes both in
            PEM format. ``client_cert_source`` and ``client_encrypted_cert_source``
            are mutually exclusive.
        client_encrypted_cert_source (Optional[Callable[[], Tuple[str, str, bytes]]]):
            A callback which returns client certificate file path, encrypted
            private key file path, and the passphrase bytes.``client_cert_source``
            and ``client_encrypted_cert_source`` are mutually exclusive.
        quota_project_id (Optional[str]): A project name that a client\'s
            quota belongs to.
        credentials_file (Optional[str]): Deprecated. A path to a file storing credentials.
            ``credentials_file` and ``api_key`` are mutually exclusive. This argument will be
            removed in the next major version of `google-api-core`.

            .. warning::
                Important: If you accept a credential configuration (credential JSON/File/Stream)
                from an external source for authentication to Google Cloud Platform, you must
                validate it before providing it to any Google API or client library. Providing an
                unvalidated credential configuration to Google APIs or libraries can compromise
                the security of your systems and data. For more information, refer to
                `Validate credential configurations from external sources`_.

            .. _Validate credential configurations from external sources:

            https://cloud.google.com/docs/authentication/external/externally-sourced-credentials
        scopes (Optional[Sequence[str]]): OAuth access token override scopes.
        api_key (Optional[str]): Google API key. ``credentials_file`` and
            ``api_key`` are mutually exclusive.
        api_audience (Optional[str]): The intended audience for the API calls
            to the service that will be set when using certain 3rd party
            authentication flows. Audience is typically a resource identifier.
            If not set, the service endpoint value will be used as a default.
            An example of a valid ``api_audience`` is: "https://language.googleapis.com".
        universe_domain (Optional[str]): The desired universe domain. This must match
            the one in credentials. If not set, the default universe domain is
            `googleapis.com`. If both `api_endpoint` and `universe_domain` are set,
            then `api_endpoint` is used as the service endpoint. If `api_endpoint` is
            not specified, the format will be `{service}.{universe_domain}`.

    Raises:
        ValueError: If both ``client_cert_source`` and ``client_encrypted_cert_source``
            are provided, or both ``credentials_file`` and ``api_key`` are provided.
    '''
    
    def __init__(self, api_endpoint, client_cert_source, client_encrypted_cert_source, quota_project_id, credentials_file = None, scopes = None, api_key = None, api_audience = (None, None, None, None, None, None, None, None, None), universe_domain = ('api_endpoint', Optional[str], 'client_cert_source', Optional[Callable[([], Tuple[(bytes, bytes)])]], 'client_encrypted_cert_source', Optional[Callable[([], Tuple[(str, str, bytes)])]], 'quota_project_id', Optional[str], 'credentials_file', Optional[str], 'scopes', Optional[Sequence[str]], 'api_key', Optional[str], 'api_audience', Optional[str], 'universe_domain', Optional[str])):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return 'ClientOptions: ' + repr(self.__dict__)



def from_dict(options = None):
    '''Construct a client options object from a mapping object.

    Args:
        options (collections.abc.Mapping): A mapping object with client options.
            See the docstring for ClientOptions for details on valid arguments.
    '''
    client_options = ClientOptions()
    for key, value in options.items():
        if hasattr(client_options, key):
            setattr(client_options, key, value)
            continue
        raise ValueError("ClientOptions does not accept an option '" + key + "'")
        return client_options
