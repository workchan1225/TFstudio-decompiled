# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _compression.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
import grpc
from grpc._cython import cygrpc
from grpc._typing import MetadataType
NoCompression = cygrpc.CompressionAlgorithm.none
Deflate = cygrpc.CompressionAlgorithm.deflate
Gzip = cygrpc.CompressionAlgorithm.gzip
_METADATA_STRING_MAPPING = {
    Gzip: 'gzip',
    Deflate: 'deflate',
    NoCompression: 'identity' }

def _compression_algorithm_to_metadata_value(compression = None):
    return _METADATA_STRING_MAPPING[compression]


def compression_algorithm_to_metadata(compression = None):
    return (cygrpc.GRPC_COMPRESSION_REQUEST_ALGORITHM_MD_KEY, _compression_algorithm_to_metadata_value(compression))


def create_channel_option(compression = None):
    return ((cygrpc.GRPC_COMPRESSION_CHANNEL_DEFAULT_ALGORITHM, int(compression)),) if compression else ()


def augment_metadata(metadata = None, compression = None):
    if not metadata and compression:
        return None
    base_metadata = tuple(metadata) if None else ()
    compression_metadata = (compression_algorithm_to_metadata(compression),) if compression else ()
    return base_metadata + compression_metadata

__all__ = ('NoCompression', 'Deflate', 'Gzip')
