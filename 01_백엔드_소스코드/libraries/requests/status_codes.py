# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: status_codes.pyc (Python 3.11)

__doc__ = "\nThe ``codes`` object defines a mapping from common names for HTTP statuses\nto their numerical codes, accessible either as attributes or as dictionary\nitems.\n\nExample::\n\n    >>> import requests\n    >>> requests.codes['temporary_redirect']\n    307\n    >>> requests.codes.teapot\n    418\n    >>> requests.codes['\\o/']\n    200\n\nSome codes have multiple names, and both upper- and lower-case versions of\nthe names are allowed. For example, ``codes.ok``, ``codes.OK``, and\n``codes.okay`` all correspond to the HTTP status code 200.\n"
from structures import LookupDict
# WARNING: Decompyle incomplete
