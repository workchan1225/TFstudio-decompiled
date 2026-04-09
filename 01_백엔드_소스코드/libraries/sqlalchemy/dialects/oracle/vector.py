# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector.pyc (Python 3.11)

from __future__ import annotations
import array
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from typing import Union
from sqlalchemy.types import types
from sqlalchemy.types import Float

class VectorIndexType(Enum):
    '''Enum representing different types of VECTOR index structures.

    See :ref:`oracle_vector_datatype` for background.

    .. versionadded:: 2.0.41

    '''
    HNSW = 'HNSW'
    IVF = 'IVF'


class VectorDistanceType(Enum):
    '''Enum representing different types of vector distance metrics.

    See :ref:`oracle_vector_datatype` for background.

    .. versionadded:: 2.0.41

    '''
    EUCLIDEAN = 'EUCLIDEAN'
    DOT = 'DOT'
    COSINE = 'COSINE'
    MANHATTAN = 'MANHATTAN'


class VectorStorageFormat(Enum):
    '''Enum representing the data format used to store vector components.

    See :ref:`oracle_vector_datatype` for background.

    .. versionadded:: 2.0.41

    '''
    INT8 = 'INT8'
    BINARY = 'BINARY'
    FLOAT32 = 'FLOAT32'
    FLOAT64 = 'FLOAT64'


class VectorStorageType(Enum):
    '''Enum representing the vector type,

    See :ref:`oracle_vector_datatype` for background.

    .. versionadded:: 2.0.43

    '''
    SPARSE = 'SPARSE'
    DENSE = 'DENSE'

VectorIndexConfig = <NODE:12>()

class SparseVector:
    '''
    Lightweight SQLAlchemy-side version of SparseVector.
    This mimics oracledb.SparseVector.

    .. versionadded:: 2.0.43

    '''
    
    def __init__(self = None, num_dimensions = None, indices = None, values = ('num_dimensions', 'int', 'indices', 'Union[list, array.array]', 'values', 'Union[list, array.array]')):
        if isinstance(indices, array.array) or indices.typecode != 'I':
            indices = array.array('I', indices)
        if not isinstance(values, array.array):
            values = array.array('d', values)
        if len(indices) != len(values):
            raise TypeError('indices and values must be of the same length!')
        self.num_dimensions = num_dimensions
        self.indices = indices
        self.values = values

    
    def __str__(self):
        return f'''SparseVector(num_dimensions={self.num_dimensions}, size={len(self.indices)}, typecode={self.values.typecode})'''



class VECTOR(types.TypeEngine):
    '''Oracle VECTOR datatype.

    For complete background on using this type, see
    :ref:`oracle_vector_datatype`.

    .. versionadded:: 2.0.41

    '''
    cache_ok = True
    __visit_name__ = 'VECTOR'
    _typecode_map = {
        VectorStorageFormat.FLOAT64: 'd',
        VectorStorageFormat.FLOAT32: 'f',
        VectorStorageFormat.BINARY: 'B',
        VectorStorageFormat.INT8: 'b' }
    
    def __init__(self, dim, storage_format, storage_type = (None, None, None)):
        '''Construct a VECTOR.

        :param dim: integer. The dimension of the VECTOR datatype. This
         should be an integer value.

        :param storage_format: VectorStorageFormat. The VECTOR storage
         type format. This should be Enum values form
         :class:`.VectorStorageFormat` INT8, BINARY, FLOAT32, or FLOAT64.

        :param storage_type: VectorStorageType. The Vector storage type. This
         should be Enum values from :class:`.VectorStorageType` SPARSE or
         DENSE.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _cached_bind_processor(self, dialect):
        '''
        Converts a Python-side SparseVector instance into an
        oracledb.SparseVectormor a compatible array format before
        binding it to the database.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _cached_result_processor(self, dialect, coltype):
        '''
        Converts database-returned values into Python-native representations.
        If the value is an oracledb.SparseVector, it is converted into the
        SQLAlchemy-side SparseVector class.
        If the value is a array.array, it is converted to a plain Python list.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _array_typecode(self, typecode):
        '''
        Map storage format to array typecode.
        '''
        return self._typecode_map.get(typecode, 'd')

    
    class comparator_factory(types.TypeEngine.Comparator):
        
        def l2_distance(self, other):
            return self.op('<->', return_type = Float)(other)

        
        def inner_product(self, other):
            return self.op('<#>', return_type = Float)(other)

        
        def cosine_distance(self, other):
            return self.op('<=>', return_type = Float)(other)
