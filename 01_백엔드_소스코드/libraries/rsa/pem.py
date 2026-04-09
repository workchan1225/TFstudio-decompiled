# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pem.pyc (Python 3.11)

'''Functions that load and write PEM-encoded files.'''
import base64
import typing
FlexiText = typing.Union[(str, bytes)]

def _markers(pem_marker = None):
    '''
    Returns the start and end PEM markers, as bytes.
    '''
    if not isinstance(pem_marker, bytes):
        pem_marker = pem_marker.encode('ascii')
    return (b'-----BEGIN ' + pem_marker + b'-----', b'-----END ' + pem_marker + b'-----')


def _pem_lines(contents = None, pem_start = None, pem_end = None):
    '''Generator over PEM lines between pem_start and pem_end.'''
    pass
# WARNING: Decompyle incomplete


def load_pem(contents = None, pem_marker = None):
    """Loads a PEM file.

    :param contents: the contents of the file to interpret
    :param pem_marker: the marker of the PEM content, such as 'RSA PRIVATE KEY'
        when your file has '-----BEGIN RSA PRIVATE KEY-----' and
        '-----END RSA PRIVATE KEY-----' markers.

    :return: the base64-decoded content between the start and end markers.

    @raise ValueError: when the content is invalid, for example when the start
        marker cannot be found.

    """
    if not isinstance(contents, bytes):
        contents = contents.encode('ascii')
    (pem_start, pem_end) = _markers(pem_marker)
    pem_lines = _pem_lines(contents, pem_start, pem_end)()
    pem = b''.join(pem_lines)
    return base64.standard_b64decode(pem)


def save_pem(contents = None, pem_marker = None):
    """Saves a PEM file.

    :param contents: the contents to encode in PEM format
    :param pem_marker: the marker of the PEM content, such as 'RSA PRIVATE KEY'
        when your file has '-----BEGIN RSA PRIVATE KEY-----' and
        '-----END RSA PRIVATE KEY-----' markers.

    :return: the base64-encoded content between the start and end markers, as bytes.

    """
    (pem_start, pem_end) = _markers(pem_marker)
    b64 = base64.standard_b64encode(contents).replace(b'\n', b'')
    pem_lines = [
        pem_start]
    for block_start in range(0, len(b64), 64):
        block = b64[block_start:block_start + 64]
        pem_lines.append(block)
        pem_lines.append(pem_end)
        pem_lines.append(b'')
        return b'\n'.join(pem_lines)
