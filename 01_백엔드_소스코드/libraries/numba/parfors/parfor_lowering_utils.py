# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parfor_lowering_utils.pyc (Python 3.11)

from collections import namedtuple
from numba.core import types, ir
from numba.core.typing import signature
_CallableNode = namedtuple('BoundFunc', [
    'func',
    'sig'])

class ParforLoweringBuilder:
    '''Helper class for building Numba-IR and lowering for Parfor.
    '''
    
    def __init__(self, lowerer, scope, loc):
        self._lowerer = lowerer
        self._scope = scope
        self._loc = loc

    _context = (lambda self: self._lowerer.context)()
    _typingctx = (lambda self: self._context.typing_context)()
    _typemap = (lambda self: self._lowerer.fndesc.typemap)()
    _calltypes = (lambda self: self._lowerer.fndesc.calltypes)()
    
    def bind_global_function(self, fobj, ftype, args, kws = (None,)):
        '''Binds a global function to a variable.

        Parameters
        ----------
        fobj : object
            The function to be bound.
        ftype : types.Type
        args : Sequence[types.Type]
        kws : Mapping[str, types.Type]

        Returns
        -------
        callable: _CallableNode
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def make_const_variable(self = property, cval = property, typ = property, name = ('pf_const',)):
        '''Makes a constant variable

        Parameters
        ----------
        cval : object
            The constant value
        typ : types.Type
            type of the value
        name : str
            variable name to store to

        Returns
        -------
        res : ir.Var
        '''
        return self.assign(rhs = ir.Const(cval, loc = self._loc), typ = typ, name = name)

    
    def make_tuple_variable(self = None, varlist = None, name = property):
        '''Makes a tuple variable

        Parameters
        ----------
        varlist : Sequence[ir.Var]
            Variables containing the values to be stored.
        name : str
            variable name to store to

        Returns
        -------
        res : ir.Var
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def assign(self = None, rhs = None, typ = None, name = ('pf_assign',)):
        '''Assign a value to a new variable

        Parameters
        ----------
        rhs : object
            The value
        typ : types.Type
            type of the value
        name : str
            variable name to store to

        Returns
        -------
        res : ir.Var
        '''
        loc = self._loc
        var = self._scope.redefine(name, loc)
        self._typemap[var.name] = typ
        assign = ir.Assign(rhs, var, loc)
        self._lowerer.lower_inst(assign)
        return var

    
    def assign_inplace(self = None, rhs = None, typ = None, name = ('return', ir.Var)):
        '''Assign a value to a new variable or inplace if it already exist

        Parameters
        ----------
        rhs : object
            The value
        typ : types.Type
            type of the value
        name : str
            variable name to store to

        Returns
        -------
        res : ir.Var
        '''
        loc = self._loc
        var = ir.Var(self._scope, name, loc)
        assign = ir.Assign(rhs, var, loc)
        self._typemap.setdefault(var.name, typ)
        self._lowerer.lower_inst(assign)
        return var

    
    def call(self = None, callable_node = None, args = None, kws = (None,)):
        '''Call a bound callable

        Parameters
        ----------
        callable_node : _CallableNode
            The callee
        args : Sequence[ir.Var]
        kws : Mapping[str, ir.Var]

        Returns
        -------
        res : ir.Expr
            The expression node for the return value of the call
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def setitem(self = None, obj = None, index = None, val = ('return', ir.SetItem)):
        '''Makes a setitem call

        Parameters
        ----------
        obj : ir.Var
            the object being indexed
        index : ir.Var
            the index
        val : ir.Var
            the value to be stored

        Returns
        -------
        res : ir.SetItem
        '''
        loc = self._loc
        tm = self._typemap
        setitem = ir.SetItem(obj, index, val, loc = loc)
        self._lowerer.fndesc.calltypes[setitem] = signature(types.none, tm[obj.name], tm[index.name], tm[val.name])
        self._lowerer.lower_inst(setitem)
        return setitem

    
    def getitem(self = None, obj = None, index = None, typ = ('return', ir.Expr)):
        '''Makes a getitem call

        Parameters
        ----------
        obj : ir.Var
            the object being indexed
        index : ir.Var
            the index
        val : ir.Var
            the ty

        Returns
        -------
        res : ir.Expr
            the retrieved value
        '''
        tm = self._typemap
        getitem = ir.Expr.getitem(obj, index, loc = self._loc)
        self._lowerer.fndesc.calltypes[getitem] = signature(typ, tm[obj.name], tm[index.name])
        return getitem
