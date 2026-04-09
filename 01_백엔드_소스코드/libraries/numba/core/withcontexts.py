# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: withcontexts.pyc (Python 3.11)

import numba
from numba.core import errors, ir, ir_utils, sigutils, types
from numba.core.ir_utils import build_definitions
from numba.core.transforms import find_region_inout_vars
from numba.core.typing.typeof import typeof_impl

class WithContext(object):
    '''A dummy object for use as contextmanager.
    This can be used as a contextmanager.
    '''
    is_callable = False
    
    def __enter__(self):
        pass

    
    def __exit__(self, typ, val, tb):
        pass

    
    def mutate_with_body(self, func_ir, blocks, blk_start, blk_end, body_blocks, dispatcher_factory, extra):
        """Mutate the *blocks* to implement this contextmanager.

        Parameters
        ----------
        func_ir : FunctionIR
        blocks : dict[ir.Block]
        blk_start, blk_end : int
            labels of the starting and ending block of the context-manager.
        body_block: sequence[int]
            A sequence of int's representing labels of the with-body
        dispatcher_factory : callable
            A callable that takes a `FunctionIR` and returns a `Dispatcher`.
        """
        raise NotImplementedError


typeof_contextmanager = (lambda val, c: types.ContextManager(val))()

def _get_var_parent(name):
    '''Get parent of the variable given its name'''
    if not name.startswith('$'):
        return name.split('.')[0]


def _clear_blocks(blocks, to_clear):
    '''Remove keys in *to_clear* from *blocks*.'''
    for b in to_clear:
        del blocks[b]
        return None


class _ByPassContextType(WithContext):
    '''A simple context-manager that tells the compiler to bypass the body
    of the with-block.
    '''
    
    def mutate_with_body(self, func_ir, blocks, blk_start, blk_end, body_blocks, dispatcher_factory, extra):
        pass
    # WARNING: Decompyle incomplete


bypass_context = _ByPassContextType()

class _CallContextType(WithContext):
    '''A simple context-manager that tells the compiler to lift the body of the
    with-block as another function.
    '''
    
    def mutate_with_body(self, func_ir, blocks, blk_start, blk_end, body_blocks, dispatcher_factory, extra):
        pass
    # WARNING: Decompyle incomplete


call_context = _CallContextType()

class _ObjModeContextType(WithContext):
    '''Creates a contextmanager to be used inside jitted functions to enter
    *object-mode* for using interpreter features.  The body of the with-context
    is lifted into a function that is compiled in *object-mode*.  This
    transformation process is limited and cannot process all possible
    Python code.  However, users can wrap complicated logic in another
    Python function, which will then be executed by the interpreter.

    Use this as a function that takes keyword arguments only.
    The argument names must correspond to the output variables from the
    with-block.  Their respective values can be:

    1. strings representing the expected types; i.e. ``"float32"``.
    2. compile-time bound global or nonlocal variables referring to the
       expected type. The variables are read at compile time.

    When exiting the with-context, the output variables are converted
    to the expected nopython types according to the annotation.  This process
    is the same as passing Python objects into arguments of a nopython
    function.

    Example::

        import numpy as np
        from numba import njit, objmode, types

        def bar(x):
            # This code is executed by the interpreter.
            return np.asarray(list(reversed(x.tolist())))

        # Output type as global variable
        out_ty = types.intp[:]

        @njit
        def foo():
            x = np.arange(5)
            y = np.zeros_like(x)
            with objmode(y=\'intp[:]\', z=out_ty):  # annotate return type
                # this region is executed by object-mode.
                y += bar(x)
                z = y
            return y, z

    .. note:: Known limitations:

        - with-block cannot use incoming list objects.
        - with-block cannot use incoming function objects.
        - with-block cannot ``yield``, ``break``, ``return`` or ``raise``           such that the execution will leave the with-block immediately.
        - with-block cannot contain `with` statements.
        - random number generator states do not synchronize; i.e.           nopython-mode and object-mode uses different RNG states.

    .. note:: When used outside of no-python mode, the context-manager has no
        effect.

    .. warning:: This feature is experimental.  The supported features may
        change with or without notice.

    '''
    is_callable = True
    
    def _legalize_args(self, func_ir, args, kwargs, loc, func_globals, func_closures):
        '''
        Legalize arguments to the context-manager

        Parameters
        ----------
        func_ir: FunctionIR
        args: tuple
            Positional arguments to the with-context call as IR nodes.
        kwargs: dict
            Keyword arguments to the with-context call as IR nodes.
        loc: numba.core.ir.Loc
            Source location of the with-context call.
        func_globals: dict
            The globals dictionary of the calling function.
        func_closures: dict
            The resolved closure variables of the calling function.
        '''
        if args:
            raise errors.CompilerError("objectmode context doesn't take any positional arguments")
        typeanns = { }
        
        def report_error(varname, msg, loc):
            raise errors.CompilerError(f'''Error handling objmode argument {varname!r}. {msg}''', loc = loc)

        for k, v in kwargs.items():
            if isinstance(v, ir.Const) and isinstance(v.value, str):
                typeanns[k] = sigutils._parse_signature_string(v.value)
                continue
            if isinstance(v, ir.FreeVar):
                v = func_closures[v.name]
            else:
                except KeyError:
                    report_error(varname = k, msg = f'''Freevar {v.name!r} is not defined.''', loc = loc)
                typeanns[k] = v
            if isinstance(v, ir.Global):
                v = func_globals[v.name]
            else:
                except KeyError:
                    report_error(varname = k, msg = f'''Global {v.name!r} is not defined.''', loc = loc)
                typeanns[k] = v
            if isinstance(v, ir.Expr) and v.op == 'getattr':
                base_obj = func_ir.infer_constant(v.value)
                typ = getattr(base_obj, v.attr)
                typeanns[k] = typ
                continue
                except (errors.ConstantInferenceError, AttributeError):
                    report_error(varname = k, msg = 'Getattr cannot be resolved at compile-time.', loc = loc)
                    continue
            report_error(varname = k, msg = 'The value must be a compile-time constant either as a non-local variable or a getattr expression that refers to a Numba type.', loc = loc)
            for name, typ in typeanns.items():
                self._legalize_arg_type(name, typ, loc)
                return typeanns

    
    def _legalize_arg_type(self, name, typ, loc):
        '''Legalize the argument type

        Parameters
        ----------
        name: str
            argument name.
        typ: numba.core.types.Type
            argument type.
        loc: numba.core.ir.Loc
            source location for error reporting.
        '''
        if getattr(typ, 'reflected', False):
            msgbuf = [
                'Objmode context failed.',
                f'''Argument {name!r} is declared as an unsupported type: {typ}.''',
                'Reflected types are not supported.']
            raise errors.CompilerError(' '.join(msgbuf), loc = loc)

    
    def mutate_with_body(self, func_ir, blocks, blk_start, blk_end, body_blocks, dispatcher_factory, extra):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, *args, **kwargs):
        return self


objmode_context = _ObjModeContextType()

def _bypass_with_context(blocks, blk_start, blk_end, forwardvars):
    '''Given the starting and ending block of the with-context,
    replaces the head block with a new block that jumps to the end.

    *blocks* is modified inplace.
    '''
    sblk = blocks[blk_start]
    scope = sblk.scope
    loc = sblk.loc
    newblk = ir.Block(scope = scope, loc = loc)
    for k, v in forwardvars.items():
        newblk.append(ir.Assign(value = scope.get_exact(k), target = scope.get_exact(v), loc = loc))
        newblk.append(ir.Jump(target = blk_end, loc = loc))
        blocks[blk_start] = newblk
        return None


def _mutate_with_block_caller(dispatcher, blocks, blk_start, blk_end, inputs, outputs):
    '''Make a new block that calls into the lifeted with-context.

    Parameters
    ----------
    dispatcher : Dispatcher
    blocks : dict[ir.Block]
    blk_start, blk_end : int
        labels of the starting and ending block of the context-manager.
    inputs: sequence[str]
        Input variable names
    outputs: sequence[str]
        Output variable names
    '''
    sblk = blocks[blk_start]
    scope = sblk.scope
    loc = sblk.loc
    newblock = ir.Block(scope = scope, loc = loc)
    ir_utils.fill_block_with_call(newblock = newblock, callee = dispatcher, label_next = blk_end, inputs = inputs, outputs = outputs)
    return newblock


def _mutate_with_block_callee(blocks, blk_start, blk_end, inputs, outputs):
    '''Mutate *blocks* for the callee of a with-context.

    Parameters
    ----------
    blocks : dict[ir.Block]
    blk_start, blk_end : int
        labels of the starting and ending block of the context-manager.
    inputs: sequence[str]
        Input variable names
    outputs: sequence[str]
        Output variable names
    '''
    if not blocks:
        raise errors.NumbaValueError('No blocks in with-context block')
    head_blk = min(blocks)
    temp_blk = blocks[head_blk]
    scope = temp_blk.scope
    loc = temp_blk.loc
    blocks[blk_start] = ir_utils.fill_callee_prologue(block = ir.Block(scope = scope, loc = loc), inputs = inputs, label_next = head_blk)
    blocks[blk_end] = ir_utils.fill_callee_epilogue(block = ir.Block(scope = scope, loc = loc), outputs = outputs)


class _ParallelChunksize(WithContext):
    is_callable = True
    
    def mutate_with_body(self, func_ir, blocks, blk_start, blk_end, body_blocks, dispatcher_factory, extra):
        ir_utils.dprint_func_ir(func_ir, 'Before with changes', blocks = blocks)
    # WARNING: Decompyle incomplete

    
    def __call__(self, *args, **kwargs):
        '''Act like a function and enforce the contract that
        setting the chunksize takes only one integer input.
        '''
        if not len(args) != 1 and kwargs or isinstance(args[0], int):
            raise ValueError('parallel_chunksize takes only a single integer argument.')
        self.chunksize = args[0]
        return self

    
    def __enter__(self):
        self.orig_chunksize = numba.get_parallel_chunksize()
        numba.set_parallel_chunksize(self.chunksize)

    
    def __exit__(self, typ, val, tb):
        numba.set_parallel_chunksize(self.orig_chunksize)


parallel_chunksize = _ParallelChunksize()
