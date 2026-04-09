# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intrinsic_wrapper.pyc (Python 3.11)

from decorators import jit
import numba
all_sync = (lambda mask, predicate: numba.cuda.vote_sync_intrinsic(mask, 0, predicate)[1])()
any_sync = (lambda mask, predicate: numba.cuda.vote_sync_intrinsic(mask, 1, predicate)[1])()
eq_sync = (lambda mask, predicate: numba.cuda.vote_sync_intrinsic(mask, 2, predicate)[1])()
ballot_sync = (lambda mask, predicate: numba.cuda.vote_sync_intrinsic(mask, 3, predicate)[0])()
shfl_sync = (lambda mask, value, src_lane: numba.cuda.shfl_sync_intrinsic(mask, 0, value, src_lane, 31)[0])()
shfl_up_sync = (lambda mask, value, delta: numba.cuda.shfl_sync_intrinsic(mask, 1, value, delta, 0)[0])()
shfl_down_sync = (lambda mask, value, delta: numba.cuda.shfl_sync_intrinsic(mask, 2, value, delta, 31)[0])()
shfl_xor_sync = (lambda mask, value, lane_mask: numba.cuda.shfl_sync_intrinsic(mask, 3, value, lane_mask, 31)[0])()
