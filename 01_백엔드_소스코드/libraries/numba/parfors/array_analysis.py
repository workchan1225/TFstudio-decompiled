# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: array_analysis.pyc (Python 3.11)

import numpy
import operator
from numba.core import types, ir, config, cgutils, errors
from numba.core.ir_utils import mk_unique_var, find_topo_order, dprint_func_ir, get_global_func_typ, guard, require, get_definition, find_callname, find_build_sequence, find_const, is_namedtuple_class, build_definitions, find_potential_aliases, get_canonical_alias, GuardException
from numba.core.analysis import compute_cfg_from_blocks
from numba.core.typing import npydecl, signature
import copy
from numba.core.extending import intrinsic
import llvmlite
UNKNOWN_CLASS = -1
CONST_CLASS = 0
MAP_TYPES = [
    numpy.ufunc]
array_analysis_extensions = { }
array_creation = [
    'empty',
    'zeros',
    'ones',
    'full']
random_int_args = [
    'rand',
    'randn']
random_1arg_size = [
    'ranf',
    'random_sample',
    'sample',
    'random',
    'standard_normal']
random_2arg_sizelast = [
    'chisquare',
    'weibull',
    'power',
    'geometric',
    'exponential',
    'poisson',
    'rayleigh']
random_3arg_sizelast = [
    'normal',
    'uniform',
    'beta',
    'binomial',
    'f',
    'gamma',
    'lognormal',
    'laplace']
random_calls = random_int_args + random_1arg_size + random_2arg_sizelast + random_3arg_sizelast + [
    'randint',
    'triangular']
wrap_index = (lambda typingctx, idx, size: pass# WARNING: Decompyle incomplete
)()

def wrap_index_literal(idx, size):
    if idx < 0:
        if idx <= -size:
            return 0
        return None + size
    if None >= size:
        return size

assert_equiv = (lambda typingctx: if len(val) > 1:
val = (types.StarArgTuple(val),)# WARNING: Decompyle incomplete
)()

class EquivSet(object):
    '''EquivSet keeps track of equivalence relations between
    a set of objects.
    '''
    
    def __init__(self, obj_to_ind, ind_to_obj, next_ind = (None, None, 0)):
        '''Create a new EquivSet object. Optional keyword arguments are for
        internal use only.
        '''
        self.obj_to_ind = obj_to_ind if obj_to_ind else { }
        self.ind_to_obj = ind_to_obj if ind_to_obj else { }
        self.next_ind = next_ind

    
    def empty(self):
        '''Return an empty EquivSet object.
        '''
        return EquivSet()

    
    def clone(self):
        '''Return a new copy.
        '''
        return EquivSet(obj_to_ind = copy.deepcopy(self.obj_to_ind), ind_to_obj = copy.deepcopy(self.ind_to_obj), next_id = self.next_ind)

    
    def __repr__(self):
        return 'EquivSet({})'.format(self.ind_to_obj)

    
    def is_empty(self):
        '''Return true if the set is empty, or false otherwise.
        '''
        return self.obj_to_ind == { }

    
    def _get_ind(self, x):
        '''Return the internal index (greater or equal to 0) of the given
        object, or -1 if not found.
        '''
        return self.obj_to_ind.get(x, -1)

    
    def _get_or_add_ind(self, x):
        '''Return the internal index (greater or equal to 0) of the given
        object, or create a new one if not found.
        '''
        return i

    
    def _insert(self, objs):
        '''Base method that inserts a set of equivalent objects by modifying
        self.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def is_equiv(self, *objs):
        '''Try to derive if given objects are equivalent, return true
        if so, or false otherwise.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_equiv_const(self, obj):
        '''Check if obj is equivalent to some int constant, and return
        the constant if found, or None otherwise.
        '''
        ind = self._get_ind(obj)
        if ind >= 0:
            objs = self.ind_to_obj[ind]
            for x in objs:
                if isinstance(x, int):
                    
                    return None, x
                return None

    
    def get_equiv_set(self, obj):
        '''Return the set of equivalent objects.
        '''
        ind = self._get_ind(obj)
        if ind >= 0:
            return set(self.ind_to_obj[ind])
        return None()

    
    def insert_equiv(self, *objs):
        '''Insert a set of equivalent objects by modifying self. This
        method can be overloaded to transform object type before insertion.
        '''
        return self._insert(objs)

    
    def intersect(self, equiv_set):
        ''' Return the intersection of self and the given equiv_set,
        without modifying either of them. The result will also keep
        old equivalence indices unchanged.
        '''
        pass
    # WARNING: Decompyle incomplete



class ShapeEquivSet(EquivSet):
    pass
# WARNING: Decompyle incomplete


class SymbolicEquivSet(ShapeEquivSet):
    pass
# WARNING: Decompyle incomplete


class WrapIndexMeta(object):
    """
      Array analysis should be able to analyze all the function
      calls that it adds to the IR.  That way, array analysis can
      be run as often as needed and you should get the same
      equivalencies.  One modification to the IR that array analysis
      makes is the insertion of wrap_index calls.  Thus, repeated
      array analysis passes should be able to analyze these wrap_index
      calls.  The difficulty of these calls is that the equivalence
      class of the left-hand side of the assignment is not present in
      the arguments to wrap_index in the right-hand side.  Instead,
      the equivalence class of the wrap_index output is a combination
      of the wrap_index args.  The important thing to
      note is that if the equivalence classes of the slice size
      and the dimension's size are the same for two wrap index
      calls then we can be assured of the answer being the same.
      So, we maintain the wrap_map dict that maps from a tuple
      of equivalence class ids for the slice and dimension size
      to some new equivalence class id for the output size.
      However, when we are analyzing the first such wrap_index
      call we don't have a variable there to associate to the
      size since we're in the process of analyzing the instruction
      that creates that mapping.  So, instead we return an object
      of this special class and analyze_inst will establish the
      connection between a tuple of the parts of this object
      below and the left-hand side variable.
    """
    
    def __init__(self, slice_size, dim_size):
        self.slice_size = slice_size
        self.dim_size = dim_size



class ArrayAnalysis(object):
    aa_count = 0
    
    def __init__(self, context, func_ir, typemap, calltypes):
        self.context = context
        self.func_ir = func_ir
        self.typemap = typemap
        self.calltypes = calltypes
        self.equiv_sets = { }
        self.array_attr_calls = { }
        self.object_attrs = { }
        self.prepends = { }
        self.pruned_predecessors = { }

    
    def get_equiv_set(self, block_label):
        '''Return the equiv_set object of an block given its label.
        '''
        return self.equiv_sets[block_label]

    
    def remove_redefineds(self, redefineds):
        '''Take a set of variables in redefineds and go through all
        the currently existing equivalence sets (created in topo order)
        and remove that variable from all of them since it is multiply
        defined within the function.
        '''
        unused = set()
        for r in redefineds:
            for eslabel in self.equiv_sets:
                es = self.equiv_sets[eslabel]
                es.define(r, unused)
                return None

    
    def run(self, blocks, equiv_set = (None, None)):
        '''run array shape analysis on the given IR blocks, resulting in
        modified IR and finalized EquivSet for each block.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _run_on_blocks(self, topo_order, blocks, cfg, init_equiv_set):
        for label in topo_order:
            if config.DEBUG_ARRAY_OPT >= 2:
                print('Processing block:', label)
            block = blocks[label]
            scope = block.scope
            pending_transforms = self._determine_transform(cfg, block, label, scope, init_equiv_set)
            self._combine_to_new_block(block, pending_transforms)
            return None

    
    def _combine_to_new_block(self, block, pending_transforms):
        '''Combine the new instructions from previous pass into a new block
        body.
        '''
        new_body = []
        for inst, pre, post in pending_transforms:
            for instr in pre:
                new_body.append(instr)
                new_body.append(inst)
                for instr in post:
                    new_body.append(instr)
                    block.body = new_body
                    return None

    
    def _determine_transform(self, cfg, block, label, scope, init_equiv_set):
        '''Determine the transformation for each instruction in the block
        '''
        equiv_set = None
        preds = cfg.predecessors(label)
        if label in self.pruned_predecessors:
            pruned = self.pruned_predecessors[label]
        else:
            pruned = []
        if config.DEBUG_ARRAY_OPT >= 2:
            print('preds:', preds)
    # WARNING: Decompyle incomplete

    
    def dump(self):
        '''dump per-block equivalence sets for debugging purposes.
        '''
        print('Array Analysis: ', self.equiv_sets)

    
    def _define(self, equiv_set, var, typ, value):
        self.typemap[var.name] = typ
        self.func_ir._definitions[var.name] = [
            value]
        redefineds = set()
        equiv_set.define(var, redefineds, self.func_ir, typ)

    
    class AnalyzeResult(object):
        
        def __init__(self, **kwargs):
            self.kwargs = kwargs


    
    def _analyze_inst(self, label, scope, equiv_set, inst, redefined):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_expr(self, scope, equiv_set, expr, lhs):
        fname = '_analyze_op_{}'.format(expr.op)
        
        try:
            fn = getattr(self, fname)
        except AttributeError:
            return None

        return guard(fn, scope, equiv_set, expr, lhs)

    
    def _analyze_op_getattr(self, scope, equiv_set, expr, lhs):
        if expr.attr == 'T' and self._isarray(expr.value.name):
            return self._analyze_op_call_numpy_transpose(scope, equiv_set, expr.loc, [
                expr.value], { })
        if None.attr == 'shape':
            shape = equiv_set.get_shape(expr.value)
            return ArrayAnalysis.AnalyzeResult(shape = shape)
        if None.attr in ('real', 'imag') and self._isarray(expr.value.name):
            return ArrayAnalysis.AnalyzeResult(shape = expr.value)
        if None._isarray(lhs.name):
            canonical_value = get_canonical_alias(expr.value.name, self.alias_map)
            if (canonical_value, expr.attr) in self.object_attrs:
                return ArrayAnalysis.AnalyzeResult(shape = self.object_attrs[(canonical_value, expr.attr)])
            typ = None.typemap[lhs.name]
            post = []
            shape = self._gen_shape_call(equiv_set, lhs, typ.ndim, None, post)
            self.object_attrs[(canonical_value, expr.attr)] = shape
            return ArrayAnalysis.AnalyzeResult(shape = shape, post = post)

    
    def _analyze_op_cast(self, scope, equiv_set, expr, lhs):
        return ArrayAnalysis.AnalyzeResult(shape = expr.value)

    
    def _analyze_op_exhaust_iter(self, scope, equiv_set, expr, lhs):
        var = expr.value
        typ = self.typemap[var.name]
        if isinstance(typ, types.BaseTuple):
            require(len(typ) == expr.count)
            require(equiv_set.has_shape(var))
            return ArrayAnalysis.AnalyzeResult(shape = var)

    
    def gen_literal_slice_part(self, arg_val, loc, scope, stmts, equiv_set, name = ('static_literal_slice_part',)):
        static_literal_slice_part_var = ir.Var(scope, mk_unique_var(name), loc)
        static_literal_slice_part_val = ir.Const(arg_val, loc)
        static_literal_slice_part_typ = types.IntegerLiteral(arg_val)
        stmts.append(ir.Assign(value = static_literal_slice_part_val, target = static_literal_slice_part_var, loc = loc))
        self._define(equiv_set, static_literal_slice_part_var, static_literal_slice_part_typ, static_literal_slice_part_val)
        return (static_literal_slice_part_var, static_literal_slice_part_typ)

    
    def gen_static_slice_size(self, lhs_rel, rhs_rel, loc, scope, stmts, equiv_set):
        pass
    # WARNING: Decompyle incomplete

    
    def gen_explicit_neg(self, arg, arg_rel, arg_typ, size_typ, loc, scope, dsize, stmts, equiv_set):
        pass
    # WARNING: Decompyle incomplete

    
    def update_replacement_slice(self, lhs, lhs_typ, lhs_rel, dsize_rel, replacement_slice, slice_index, need_replacement, loc, scope, stmts, equiv_set, size_typ, dsize):
        known = False
    # WARNING: Decompyle incomplete

    
    def slice_size(self, index, dsize, equiv_set, scope, stmts):
        '''Reason about the size of a slice represented by the "index"
        variable, and return a variable that has this size data, or
        raise GuardException if it cannot reason about it.

        The computation takes care of negative values used in the slice
        with respect to the given dimensional size ("dsize").

        Extra statements required to produce the result are appended
        to parent function\'s stmts list.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _index_to_shape(self, scope, equiv_set, var, ind_var):
        '''For indexing like var[index] (either write or read), see if
        the index corresponds to a range/slice shape.
        Returns a 2-tuple where the first item is either None or a ir.Var
        to be used to replace the index variable in the outer getitem or
        setitem instruction.  The second item is also a tuple returning
        the shape and prepending instructions.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_getitem(self, scope, equiv_set, expr, lhs):
        result = self._index_to_shape(scope, equiv_set, expr.value, expr.index)
    # WARNING: Decompyle incomplete

    
    def _analyze_op_static_getitem(self, scope, equiv_set, expr, lhs):
        var = expr.value
        typ = self.typemap[var.name]
    # WARNING: Decompyle incomplete

    
    def _analyze_op_unary(self, scope, equiv_set, expr, lhs):
        require(expr.fn in UNARY_MAP_OP)
        if self._isarray(expr.value.name) or expr.fn == operator.add:
            return ArrayAnalysis.AnalyzeResult(shape = expr.value)

    
    def _analyze_op_binop(self, scope, equiv_set, expr, lhs):
        require(expr.fn in BINARY_MAP_OP)
        return self._analyze_broadcast(scope, equiv_set, expr.loc, [
            expr.lhs,
            expr.rhs], expr.fn)

    
    def _analyze_op_inplace_binop(self, scope, equiv_set, expr, lhs):
        require(expr.fn in INPLACE_BINARY_MAP_OP)
        return self._analyze_broadcast(scope, equiv_set, expr.loc, [
            expr.lhs,
            expr.rhs], expr.fn)

    
    def _analyze_op_arrayexpr(self, scope, equiv_set, expr, lhs):
        return self._analyze_broadcast(scope, equiv_set, expr.loc, expr.list_vars(), None)

    
    def _analyze_op_build_tuple(self, scope, equiv_set, expr, lhs):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call(self, scope, equiv_set, expr, lhs):
        StencilFunc = StencilFunc
        import numba.stencils.stencil
        callee = expr.func
        callee_def = get_definition(self.func_ir, callee)
        if isinstance(callee_def, (ir.Global, ir.FreeVar)) and is_namedtuple_class(callee_def.value):
            return ArrayAnalysis.AnalyzeResult(shape = tuple(expr.args))
        if None(callee_def, (ir.Global, ir.FreeVar)) and isinstance(callee_def.value, StencilFunc):
            args = expr.args
            return self._analyze_stencil(scope, equiv_set, callee_def.value, expr.loc, args, dict(expr.kws))
        (fname, mod_name) = None(self.func_ir, expr, typemap = self.typemap)
        added_mod_name = False
        if isinstance(mod_name, ir.Var) and isinstance(self.typemap[mod_name.name], types.ArrayCompatible):
            args = [
                mod_name] + expr.args
            mod_name = 'numpy'
            added_mod_name = True
        else:
            args = expr.args
        fname = '_analyze_op_call_{}_{}'.format(mod_name, fname).replace('.', '_')
        if fname in UFUNC_MAP_OP:
            return self._analyze_broadcast(scope, equiv_set, expr.loc, args, None)
        
        try:
            fn = getattr(self, fname)
        except AttributeError:
            return None

        result = guard(fn, scope = scope, equiv_set = equiv_set, loc = expr.loc, args = args, kws = dict(expr.kws))
        if added_mod_name:
            expr.args = args[1:]
        return result

    
    def _analyze_op_call_builtins_len(self, scope, equiv_set, loc, args, kws):
        require(len(args) == 1)
        var = args[0]
        typ = self.typemap[var.name]
        require(isinstance(typ, types.ArrayCompatible))
        shape = equiv_set._get_shape(var)
        return ArrayAnalysis.AnalyzeResult(shape = shape[0], rhs = shape[0])

    
    def _analyze_op_call_numba_parfors_array_analysis_assert_equiv(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numba_parfors_array_analysis_wrap_index(self, scope, equiv_set, loc, args, kws):
        ''' Analyze wrap_index calls added by a previous run of
            Array Analysis
        '''
        require(len(args) == 2)
        slice_size = args[0].name
        dim_size = args[1].name
        slice_eq = equiv_set._get_or_add_ind(slice_size)
        dim_eq = equiv_set._get_or_add_ind(dim_size)
        if (slice_eq, dim_eq) in equiv_set.wrap_map:
            wrap_ind = equiv_set.wrap_map[(slice_eq, dim_eq)]
            require(wrap_ind in equiv_set.ind_to_var)
            vs = equiv_set.ind_to_var[wrap_ind]
            require(vs != [])
            return ArrayAnalysis.AnalyzeResult(shape = (vs[0],))
        return None.AnalyzeResult(shape = WrapIndexMeta(slice_eq, dim_eq))

    
    def _analyze_numpy_create_array(self, scope, equiv_set, loc, args, kws):
        shape_var = None
        if len(args) > 0:
            shape_var = args[0]
        elif 'shape' in kws:
            shape_var = kws['shape']
        if shape_var:
            return ArrayAnalysis.AnalyzeResult(shape = shape_var)
        raise None.UnsupportedRewriteError('Must specify a shape for array creation', loc = loc)

    
    def _analyze_op_call_numpy_empty(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_create_array(scope, equiv_set, loc, args, kws)

    
    def _analyze_op_call_numba_np_unsafe_ndarray_empty_inferred(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_create_array(scope, equiv_set, loc, args, kws)

    
    def _analyze_op_call_numpy_zeros(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_create_array(scope, equiv_set, loc, args, kws)

    
    def _analyze_op_call_numpy_ones(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_create_array(scope, equiv_set, loc, args, kws)

    
    def _analyze_op_call_numpy_eye(self, scope, equiv_set, loc, args, kws):
        if len(args) > 0:
            N = args[0]
        elif 'N' in kws:
            N = kws['N']
        else:
            raise errors.UnsupportedRewriteError("Expect one argument (or 'N') to eye function", loc = loc)
        if 'M' in kws:
            M = kws['M']
        else:
            M = N
        return ArrayAnalysis.AnalyzeResult(shape = (N, M))

    
    def _analyze_op_call_numpy_identity(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_diag(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_numpy_array_like(self, scope, equiv_set, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_ravel(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_copy(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_array_like(scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_empty_like(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_array_like(scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_zeros_like(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_array_like(scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_ones_like(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_array_like(scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_full_like(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_array_like(scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_asfortranarray(self, scope, equiv_set, loc, args, kws):
        return self._analyze_numpy_array_like(scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_reshape(self, scope, equiv_set, loc, args, kws):
        n = len(args)
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_transpose(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_random_rand(self, scope, equiv_set, loc, args, kws):
        if len(args) > 0:
            return ArrayAnalysis.AnalyzeResult(shape = tuple(args))

    
    def _analyze_op_call_numpy_random_randn(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_call_numpy_random_rand(scope, equiv_set, loc, args, kws)

    
    def _analyze_op_numpy_random_with_size(self, pos, scope, equiv_set, args, kws):
        if 'size' in kws:
            return ArrayAnalysis.AnalyzeResult(shape = kws['size'])
        if None(args) > pos:
            return ArrayAnalysis.AnalyzeResult(shape = args[pos])

    
    def _analyze_op_call_numpy_random_ranf(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(0, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_random_sample(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(0, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_sample(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(0, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_random(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(0, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_standard_normal(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(0, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_chisquare(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(1, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_weibull(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(1, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_power(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(1, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_geometric(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(1, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_exponential(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(1, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_poisson(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(1, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_rayleigh(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(1, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_normal(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_uniform(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_beta(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_binomial(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_f(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_gamma(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_lognormal(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_laplace(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_randint(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(2, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_random_triangular(self, scope, equiv_set, loc, args, kws):
        return self._analyze_op_numpy_random_with_size(3, scope, equiv_set, args, kws)

    
    def _analyze_op_call_numpy_concatenate(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_stack(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_vstack(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_hstack(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_dstack(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_cumsum(self, scope, equiv_set, loc, args, kws):
        pass

    
    def _analyze_op_call_numpy_cumprod(self, scope, equiv_set, loc, args, kws):
        pass

    
    def _analyze_op_call_numpy_linspace(self, scope, equiv_set, loc, args, kws):
        n = len(args)
        num = 50
        if n > 2:
            num = args[2]
        elif 'num' in kws:
            num = kws['num']
        return ArrayAnalysis.AnalyzeResult(shape = (num,))

    
    def _analyze_op_call_numpy_dot(self, scope, equiv_set, loc, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _analyze_stencil(self, scope, equiv_set, stencil_func, loc, args, kws):
        std_idx_arrs = stencil_func.options.get('standard_indexing', ())
        kernel_arg_names = stencil_func.kernel_ir.arg_names
        if isinstance(std_idx_arrs, str):
            std_idx_arrs = (std_idx_arrs,)
        rel_idx_arrs = []
    # WARNING: Decompyle incomplete

    
    def _analyze_op_call_numpy_linalg_inv(self, scope, equiv_set, loc, args, kws):
        require(len(args) >= 1)
        return ArrayAnalysis.AnalyzeResult(shape = equiv_set._get_shape(args[0]))

    
    def _analyze_broadcast(self, scope, equiv_set, loc, args, fn):
        '''Infer shape equivalence of arguments based on Numpy broadcast rules
        and return shape of output
        https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _broadcast_assert_shapes(self, scope, equiv_set, loc, shapes, names):
        '''Produce assert_equiv for sizes in each dimension, taking into
        account of dimension coercion and constant size of 1.
        '''
        asserts = []
        new_shape = []
        max_dim = (lambda .0: [ len(shape) for shape in .0 ])(shapes())
        const_size_one = None
    # WARNING: Decompyle incomplete

    
    def _call_assert_equiv(self, scope, loc, equiv_set, args, names = (None,)):
        insts = self._make_assert_equiv(scope, loc, equiv_set, args, names = names)
    # WARNING: Decompyle incomplete

    
    def _make_assert_equiv(self, scope, loc, equiv_set, _args, names = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _gen_shape_call(self, equiv_set, var, ndims, shape, post):
        if isinstance(shape, ir.Var):
            shape = equiv_set.get_shape(shape)
        if isinstance(shape, ir.Var):
            attr_var = shape
            shape_attr_call = None
            shape = None
        elif isinstance(shape, ir.Arg):
            attr_var = var
            shape_attr_call = None
            shape = None
        else:
            shape_attr_call = ir.Expr.getattr(var, 'shape', var.loc)
            attr_var = ir.Var(var.scope, mk_unique_var('{}_shape'.format(var.name)), var.loc)
            shape_attr_typ = types.containers.UniTuple(types.intp, ndims)
        size_vars = []
        use_attr_var = False
        if shape:
            nshapes = len(shape)
            if ndims < nshapes:
                shape = shape[nshapes - ndims:]
    # WARNING: Decompyle incomplete

    
    def _isarray(self, varname):
