# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _service_account_info.pyc (Python 3.11)

'''Helper functions for loading data from a Google service account file.'''
import io
import json
from google.auth import crypt
from google.auth import exceptions

def from_dict(data, require, use_rsa_signer = (None, True)):
    '''Validates a dictionary containing Google service account data.

    Creates and returns a :class:`google.auth.crypt.Signer` instance from the
    private key specified in the data.

    Args:
        data (Mapping[str, str]): The service account data
        require (Sequence[str]): List of keys required to be present in the
            info.
        use_rsa_signer (Optional[bool]): Whether to use RSA signer or EC signer.
            We use RSA signer by default.

    Returns:
        google.auth.crypt.Signer: A signer created from the private key in the
            service account file.

    Raises:
        MalformedError: if the data was in the wrong format, or if one of the
            required keys is missing.
    '''
    pass
# WARNING: Decompyle incomplete


def from_filename(filename, require, use_rsa_signer = (None, True)):
    '''Reads a Google service account JSON file and returns its parsed info.

    Args:
        filename (str): The path to the service account .json file.
        require (Sequence[str]): List of keys required to be present in the
            info.
        use_rsa_signer (Optional[bool]): Whether to use RSA signer or EC signer.
            We use RSA signer by default.

    Returns:
        Tuple[ Mapping[str, str], google.auth.crypt.Signer ]: The verified
            info and a signer instance.
    '''
    json_file = io.open(filename, 'r', encoding = 'utf-8')
    data = json.load(json_file)
    None(None, None)
    return 
    with None:
        if not None, (data, from_dict(data, require = require, use_rsa_signer = use_rsa_signer)):
            pass
