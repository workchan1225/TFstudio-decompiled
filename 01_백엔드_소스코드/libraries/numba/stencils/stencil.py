# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stencil.pyc (Python 3.11)

import copy
import numpy as np
from llvmlite import ir as lir
from numba.core import types, typing, utils, ir, config, ir_utils, registry
from numba.core.typing.templates import CallableTemplate, signature, infer_global, AbstractTemplate
from numba.core.imputils import lower_builtin
from numba.core.extending import register_jitable
from numba.core.errors import NumbaValueError
from numba.misc.special import literal_unroll
import numba
import operator
from numba.np import numpy_support

class StencilFuncLowerer(object):
    '''Callable class responsible for lowering calls to a specific StencilFunc.
    '''
    
    def __init__(self, sf):
        self.stencilFunc = sf

    
    def __call__(self, context, builder, sig, args):
        cres = self.stencilFunc.compile_for_argtys(sig.args, { }, sig.return_type, None)
        res = context.call_internal(builder, cres.fndesc, sig, args)
        context.add_linking_libs([
            cres.library])
        return res


raise_if_incompatible_array_sizes = (lambda a: ashape = a.shapefor arg in literal_unroll(args):
if a.ndim != arg.ndim:
raise ValueError('Secondary stencil array does not have same number  of dimensions as the first stencil input.')argshape = arg.shapefor i in range(len(ashape)):
if ashape[i] > argshape[i]:
raise ValueError('Secondary stencil array has some dimension smaller the same dimension in the first stencil input.')None)()

def slice_addition(the_slice, addend):
    ''' Called by stencil in Python mode to add the loop index to a
        user-specified slice.
    '''
    return slice(the_slice.start + addend, the_slice.stop + addend)


class StencilFunc(object):
    '''
    A special type to hold stencil information for the IR.
    '''
    id_counter = 0
    
    def __init__(self, kernel_ir, mode, options):
        self.id = type(self).id_counter
        kernel_ir = type(self), type(self).id_counter += 1, .id_counter
        self.mode = mode
        self.options = options
        self.kws = []
        self._typingctx = registry.cpu_target.typing_context
        self._targetctx = registry.cpu_target.target_context
        self._install_type(self._typingctx)
        self.neighborhood = self.options.get('neighborhood')
        self._type_cache = { }
        self._lower_me = StencilFuncLowerer(self)

    
    def replace_return_with_setitem(self, blocks, index_vars, out_name):
        '''
        Find return statements in the IR and replace them with a SetItem
        call of the value "returned" by the kernel into the result array.
        Returns the block labels that contained return statements.
        '''
        ret_blocks = []
        for label, block in blocks.items():
            scope = block.scope
            loc = block.loc
            new_body = []
            for stmt in block.body:
                if isinstance(stmt, ir.Return):
                    ret_blocks.append(label)
                    if len(index_vars) == 1:
                        rvar = ir.Var(scope, out_name, loc)
                        ivar = ir.Var(scope, index_vars[0], loc)
                        new_body.append(ir.SetItem(rvar, ivar, stmt.value, loc))
                        continue
                    var_index_vars = []
                    for one_var in index_vars:
                        index_var = ir.Var(scope, one_var, loc)
                        var_index_vars += [
                            index_var]
                        s_index_var = scope.redefine('stencil_index', loc)
                        tuple_call = ir.Expr.build_tuple(var_index_vars, loc)
                        new_body.append(ir.Assign(tuple_call, s_index_var, loc))
                        rvar = ir.Var(scope, out_name, loc)
                        si = ir.SetItem(rvar, s_index_var, stmt.value, loc)
                        new_body.append(si)
                        new_body.append(stmt)
                        block.body = new_body
                        return ret_blocks

    
    def add_indices_to_kernel(self, kernel, index_names, ndim, neighborhood, standard_indexed, typemap, calltypes):
        """
        Transforms the stencil kernel as specified by the user into one
        that includes each dimension's index variable as part of the getitem
        calls.  So, in effect array[-1] becomes array[index0-1].
        """
        const_dict = { }
        kernel_consts = []
        if config.DEBUG_ARRAY_OPT >= 1:
            print('add_indices_to_kernel', ndim, neighborhood)
            ir_utils.dump_blocks(kernel.blocks)
    # WARNING: Decompyle incomplete

    
    def get_return_type(self, argtys):
        if config.DEBUG_ARRAY_OPT >= 1:
            print('get_return_type', argtys)
            ir_utils.dump_blocks(self.kernel_ir.blocks)
        if not isinstance(argtys[0], types.npytypes.Array):
            raise NumbaValueError('The first argument to a stencil kernel must be the primary input array.')
        typed_passes = typed_passes
        import numba.core
        (typemap, return_type, calltypes, _) = typed_passes.type_inference_stage(self._typingctx, self._targetctx, self.kernel_ir, argtys, None, { })
        if isinstance(return_type, types.npytypes.Array):
            raise NumbaValueError('Stencil kernel must return a scalar and not a numpy array.')
        real_ret = types.npytypes.Array(return_type, argtys[0].ndim, argtys[0].layout)
        return (real_ret, typemap, calltypes)

    
    def _install_type(self, typingctx):
        '''Constructs and installs a typing class for a StencilFunc object in
        the input typing context.
        '''
        _ty_cls = type('StencilFuncTyping_' + str(self.id), (AbstractTemplate,), dict(key = self, generic = self._type_me))
        typingctx.insert_user_function(self, _ty_cls)

    
    def compile_for_argtys(self, argtys, kwtys, return_type, sigret):
        (_, result, typemap, calltypes) = self._type_cache[argtys]
    # WARNING: Decompyle incomplete

    
    def _type_me(self, argtys, kwtys):
        '''
        Implement AbstractTemplate.generic() for the typing class
        built by StencilFunc._install_type().
        Return the call-site signature.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def copy_ir_with_calltypes(self, ir, calltypes):
        '''
        Create a copy of a given IR along with its calltype information.
        We need a copy of the calltypes because copy propagation applied
        to the copied IR will change the calltypes and make subsequent
        uses of the original IR invalid.
        '''
        copy_calltypes = { }
        kernel_copy = ir.copy()
        kernel_copy.blocks = { }
        for block_label, block in ir.blocks.items():
            new_block = copy.deepcopy(ir.blocks[block_label])
            new_block.body = []
            for stmt in ir.blocks[block_label].body:
                scopy = copy.deepcopy(stmt)
                new_block.body.append(scopy)
                if stmt in calltypes:
                    copy_calltypes[scopy] = calltypes[stmt]
                kernel_copy.blocks[block_label] = new_block
                return (kernel_copy, copy_calltypes)

    
    def _stencil_wrapper(self, result, sigret, return_type, typemap, calltypes, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, *args, **kwargs):
        self._typingctx.refresh()
    # WARNING: Decompyle incomplete



def stencil(func_or_mode = ('constant',), **options):
    if not isinstance(func_or_mode, str):
        mode = 'constant'
        func = func_or_mode
    else:
        mode = func_or_mode
        func = None
# WARNING: Decompyle incomplete


def _stencil(mode, options):
    pass
# WARNING: Decompyle incomplete

stencil_dummy_lower = (lambda context, builder, sig, args: lir.Constant(lir.IntType(types.intp.bitwidth), 0))()
