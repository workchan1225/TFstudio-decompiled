# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _wavelet_packets.pyc (Python 3.11)

'''1D and 2D Wavelet packet transform module.'''
__all__ = [
    'BaseNode',
    'Node',
    'WaveletPacket',
    'Node2D',
    'WaveletPacket2D',
    'NodeND',
    'WaveletPacketND']
from collections import OrderedDict
from itertools import product
import numpy as np
from _dwt import dwt, dwt_max_level, idwt
from _extensions._pywt import Wavelet, _check_dtype
from _multidim import dwt2, dwtn, idwt2, idwtn

def get_graycode_order(level, x, y = ('a', 'd')):
    pass
# WARNING: Decompyle incomplete


class BaseNode:
    '''
    BaseNode for wavelet packet 1D and 2D tree nodes.

    The BaseNode is a base class for `Node` and `Node2D`.
    It should not be used directly unless creating a new transformation
    type. It is included here to document the common interface of 1D
    and 2D node and wavelet packet transform classes.

    Parameters
    ----------
    parent :
        Parent node. If parent is None then the node is considered detached
        (ie root).
    data : 1D or 2D array
        Data associated with the node. 1D or 2D numeric array, depending on the
        transform type.
    node_name :
        A name identifying the coefficients type.
        See `Node.node_name` and `Node2D.node_name`
        for information on the accepted subnodes names.
    '''
    PART_LEN = None
    PARTS = None
    
    def __init__(self, parent, data, node_name):
        self.parent = parent
    # WARNING: Decompyle incomplete

    
    def _init_subnodes(self):
        for part in self.PARTS:
            self._set_node(part, None)
            return None

    
    def _create_subnode(self, part, data, overwrite = (None, True)):
        raise NotImplementedError()

    
    def _create_subnode_base(self, node_cls, part, data, overwrite = (None, True), **kwargs):
        self._validate_node_name(part)
    # WARNING: Decompyle incomplete

    
    def _get_node(self, part):
        return getattr(self, part)

    
    def _set_node(self, part, node):
        setattr(self, part, node)

    
    def _delete_node(self, part):
        self._set_node(part, None)

    
    def _validate_node_name(self, part):
        if part not in self.PARTS:
            raise "Subnode name must be in [{}], not '{}'.".format(', '.join((lambda .0: pass# WARNING: Decompyle incomplete
)(self.PARTS()), part))

    path_tuple = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def _evaluate_maxlevel(self, evaluate_from = ('parent',)):
        """
        Try to find the value of maximum decomposition level if it is not
        specified explicitly.

        Parameters
        ----------
        evaluate_from : {'parent', 'subnodes'}
        """
        pass
    # WARNING: Decompyle incomplete

    maxlevel = (lambda self: pass# WARNING: Decompyle incomplete
)()
    node_name = (lambda self: self.path[-(self.PART_LEN):])()
    
    def decompose(self):
        '''
        Decompose node data creating DWT coefficients subnodes.

        Performs Discrete Wavelet Transform on the `~BaseNode.data` and
        returns transform coefficients.

        Note
        ----
        Descends to subnodes and recursively
        calls `~BaseNode.reconstruct` on them.

        '''
        if self.level < self.maxlevel:
            return self._decompose()
        raise None('Maximum decomposition level reached.')

    
    def _decompose(self):
        raise NotImplementedError()

    
    def reconstruct(self, update = (False,)):
        '''
        Reconstruct node from subnodes.

        Parameters
        ----------
        update : bool, optional
            If True, then reconstructed data replaces the current
            node data (default: False).

        Returns:
            - original node data if subnodes do not exist
            - IDWT of subnodes otherwise.
        '''
        if not self.has_any_subnode:
            return self.data
        return None._reconstruct(update)

    
    def _reconstruct(self):
        raise NotImplementedError()

    
    def get_subnode(self, part, decompose = (True,)):
        '''
        Returns subnode or None (see `decomposition` flag description).

        Parameters
        ----------
        part :
            Subnode name
        decompose : bool, optional
            If the param is True and corresponding subnode does not
            exist, the subnode will be created using coefficients
            from the DWT decomposition of the current node.
            (default: True)
        '''
        self._validate_node_name(part)
        subnode = self._get_node(part)
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, path):
        '''
        Find node represented by the given path.

        Similar to `~BaseNode.get_subnode` method with `decompose=True`, but
        can access nodes on any level in the decomposition tree.

        Parameters
        ----------
        path : str
            String composed of node names. See `Node.node_name` and
            `Node2D.node_name` for node naming convention.

        Notes
        -----
        If node does not exist yet, it will be created by decomposition of its
        parent node.
        '''
        errmsg = 'Invalid path parameter type - expected string or tuple of strings but got %s.' % type(path)
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, path, data):
        """
        Set node or node's data in the decomposition tree. Nodes are
        identified by string `path`.

        Parameters
        ----------
        path : str
            String composed of node names.
        data : array or BaseNode subclass.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, path):
        '''
        Remove node from the tree.

        Parameters
        ----------
        path : str
            String composed of node names.
        '''
        node = self[path]
        parent = node.parent
        node.parent = None
        if parent or node.node_name:
            parent._delete_node(node.node_name)
            return None
        return None

    is_empty = (lambda self: self.data is None)()
    has_any_subnode = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def get_leaf_nodes(self, decompose = (False,)):
        '''
        Returns leaf nodes.

        Parameters
        ----------
        decompose : bool, optional
            (default: True)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def walk(self, func, args, kwargs, decompose = ((), None, True)):
        '''
        Traverses the decomposition tree and calls
        ``func(node, *args, **kwargs)`` on every node. If `func` returns True,
        descending to subnodes will continue.

        Parameters
        ----------
        func : callable
            Callable accepting `BaseNode` as the first param and
            optional positional and keyword arguments
        args :
            func params
        kwargs :
            func keyword params
        decompose : bool, optional
            If True (default), the method will also try to decompose the tree
            up to the `maximum level <BaseNode.maxlevel>`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def walk_depth(self, func, args, kwargs, decompose = ((), None, True)):
        '''
        Walk tree and call func on every node starting from the bottom-most
        nodes.

        Parameters
        ----------
        func : callable
            Callable accepting :class:`BaseNode` as the first param and
            optional positional and keyword arguments
        args :
            func params
        kwargs :
            func keyword params
        decompose : bool, optional
            (default: False)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return self.path + ': ' + str(self.data)



class Node(BaseNode):
    '''
    WaveletPacket tree node.

    Subnodes are called `a` and `d`, just like approximation
    and detail coefficients in the Discrete Wavelet Transform.
    '''
    A = 'a'
    D = 'd'
    PARTS = (A, D)
    PART_LEN = 1
    
    def _create_subnode(self, part, data, overwrite = (None, True)):
        return self._create_subnode_base(node_cls = Node, part = part, data = data, overwrite = overwrite)

    
    def _decompose(self):
        '''

        See also
        --------
        dwt : for 1D Discrete Wavelet Transform output coefficients.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _reconstruct(self, update):
        (data_a, data_d) = (None, None)
        node_d = self._get_node(self.D)
        node_a = self._get_node(self.A)
    # WARNING: Decompyle incomplete



class Node2D(BaseNode):
    """
    WaveletPacket tree node.

    Subnodes are called 'a' (LL), 'h' (HL), 'v' (LH) and  'd' (HH), like
    approximation and detail coefficients in the 2D Discrete Wavelet Transform
    """
    LL = 'a'
    HL = 'h'
    LH = 'v'
    HH = 'd'
    PARTS = (LL, HL, LH, HH)
    PART_LEN = 1
    
    def _create_subnode(self, part, data, overwrite = (None, True)):
        return self._create_subnode_base(node_cls = Node2D, part = part, data = data, overwrite = overwrite)

    
    def _decompose(self):
        '''
        See also
        --------
        dwt2 : for 2D Discrete Wavelet Transform output coefficients.
        '''
        self._create_subnode(self.LL, data_ll)
        self._create_subnode(self.LH, data_lh)
        self._create_subnode(self.HL, data_hl)
        self._create_subnode(self.HH, data_hh)
        return (self._get_node(self.LL), self._get_node(self.HL), self._get_node(self.LH), self._get_node(self.HH))

    
    def _reconstruct(self, update):
        (data_ll, data_lh, data_hl, data_hh) = (None, None, None, None)
        (node_ll, node_lh, node_hl, node_hh) = (self._get_node(self.LL), self._get_node(self.LH), self._get_node(self.HL), self._get_node(self.HH))
    # WARNING: Decompyle incomplete

    
    def expand_2d_path(self, path):
        pass
    # WARNING: Decompyle incomplete



class NodeND(BaseNode):
    pass
# WARNING: Decompyle incomplete


class WaveletPacket(Node):
    pass
# WARNING: Decompyle incomplete


class WaveletPacket2D(Node2D):
    pass
# WARNING: Decompyle incomplete


class WaveletPacketND(NodeND):
    pass
# WARNING: Decompyle incomplete
