# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _mtls_helper.pyc (Python 3.11)

'''Helper functions for getting mTLS cert and key.'''
import json
import logging
from os import environ, path
import re
import subprocess
from google.auth import exceptions
CONTEXT_AWARE_METADATA_PATH = '~/.secureConnect/context_aware_metadata.json'
CERTIFICATE_CONFIGURATION_DEFAULT_PATH = '~/.config/gcloud/certificate_config.json'
_CERTIFICATE_CONFIGURATION_ENV = 'GOOGLE_API_CERTIFICATE_CONFIG'
_CERT_PROVIDER_COMMAND = 'cert_provider_command'
_CERT_REGEX = re.compile(b'-----BEGIN CERTIFICATE-----.+-----END CERTIFICATE-----\r?\n?', re.DOTALL)
_KEY_REGEX = re.compile(b'-----BEGIN [A-Z ]*PRIVATE KEY-----.+-----END [A-Z ]*PRIVATE KEY-----\r?\n?', re.DOTALL)
_LOGGER = logging.getLogger(__name__)
_PASSPHRASE_REGEX = re.compile(b'-----BEGIN PASSPHRASE-----(.+)-----END PASSPHRASE-----', re.DOTALL)

def _check_config_path(config_path):
    '''Checks for config file path. If it exists, returns the absolute path with user expansion;
    otherwise returns None.

    Args:
        config_path (str): The config file path for either context_aware_metadata.json or certificate_config.json for example

    Returns:
        str: absolute path if exists and None otherwise.
    '''
    config_path = path.expanduser(config_path)
    if not path.exists(config_path):
        _LOGGER.debug('%s is not found.', config_path)
        return None


def _load_json_file(path):
    '''Reads and loads JSON from the given path. Used to read both X509 workload certificate and
    secure connect configurations.

    Args:
        path (str): the path to read from.

    Returns:
        Dict[str, str]: The JSON stored at the file.

    Raises:
        google.auth.exceptions.ClientCertError: If failed to parse the file as JSON.
    '''
    
    try:
        f = open(path)
        json_data = json.load(f)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except ValueError:
                        caught_exc = None
                        new_exc = exceptions.ClientCertError(caught_exc)
                        raise new_exc, caught_exc
                        caught_exc = None
                        del caught_exc

                    return json_data





def _get_workload_cert_and_key(certificate_config_path = (None,)):
    '''Read the workload identity cert and key files specified in the certificate config provided.
    If no config path is provided, check the environment variable: "GOOGLE_API_CERTIFICATE_CONFIG"
    first, then the well known gcloud location: "~/.config/gcloud/certificate_config.json".

    Args:
        certificate_config_path (string): The certificate config path. If no path is provided,
        the environment variable will be checked first, then the well known gcloud location.

    Returns:
        Tuple[Optional[bytes], Optional[bytes]]: client certificate bytes in PEM format and key
            bytes in PEM format.

    Raises:
        google.auth.exceptions.ClientCertError: if problems occurs when retrieving
        the certificate or key information.
    '''
    (cert_path, key_path) = _get_workload_cert_and_key_paths(certificate_config_path)
# WARNING: Decompyle incomplete


def _get_cert_config_path(certificate_config_path = (None,)):
    '''Get the certificate configuration path based on the following order:

    1: Explicit override, if set
    2: Environment variable, if set
    3: Well-known location

    Returns "None" if the selected config file does not exist.

    Args:
        certificate_config_path (string): The certificate config path. If provided, the well known
        location and environment variable will be ignored.

    Returns:
        The absolute path of the certificate config file, and None if the file does not exist.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_workload_cert_and_key_paths(config_path):
    absolute_path = _get_cert_config_path(config_path)
# WARNING: Decompyle incomplete


def _read_cert_and_key_files(cert_path, key_path):
    cert_data = _read_cert_file(cert_path)
    key_data = _read_key_file(key_path)
    return (cert_data, key_data)


def _read_cert_file(cert_path):
