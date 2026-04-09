# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Data embedding techniques.'''
from sklearn.manifold._classical_mds import ClassicalMDS
from sklearn.manifold._isomap import Isomap
from sklearn.manifold._locally_linear import LocallyLinearEmbedding, locally_linear_embedding
from sklearn.manifold._mds import MDS, smacof
from sklearn.manifold._spectral_embedding import SpectralEmbedding, spectral_embedding
from sklearn.manifold._t_sne import TSNE, trustworthiness
__all__ = [
    'MDS',
    'TSNE',
    'ClassicalMDS',
    'Isomap',
    'LocallyLinearEmbedding',
    'SpectralEmbedding',
    'locally_linear_embedding',
    'smacof',
    'spectral_embedding',
    'trustworthiness']
