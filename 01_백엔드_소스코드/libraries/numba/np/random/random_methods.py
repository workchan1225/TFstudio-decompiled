# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: random_methods.pyc (Python 3.11)

import numpy as np
from numba import uint64, uint32, uint16, uint8
from numba.core.extending import register_jitable
from numba.np.random._constants import UINT32_MAX, UINT64_MAX, UINT16_MAX, UINT8_MAX
from numba.np.random.generator_core import next_uint32, next_uint64
gen_mask = (lambda max: mask = uint64(max)mask |= mask >> 1mask |= mask >> 2mask |= mask >> 4mask |= mask >> 8mask |= mask >> 16mask |= mask >> 32mask)()
buffered_bounded_bool = (lambda bitgen, off, rng, bcnt, buf: if rng == 0:
(off, bcnt, buf)if not None:
buf = next_uint32(bitgen)bcnt = 31else:
buf >>= 1bcnt -= 1(buf & 1 != 0, bcnt, buf))()
buffered_uint8 = (lambda bitgen, bcnt, buf: if not bcnt:
buf = next_uint32(bitgen)bcnt = 3else:
buf >>= 8bcnt -= 1(uint8(buf), bcnt, buf))()
buffered_uint16 = (lambda bitgen, bcnt, buf: if not bcnt:
buf = next_uint32(bitgen)bcnt = 1else:
buf >>= 16bcnt -= 1(uint16(buf), bcnt, buf))()
buffered_bounded_lemire_uint8 = (lambda bitgen, rng, bcnt, buf: rng_excl = uint8(rng) + uint8(1)# WARNING: Decompyle incomplete
)()
buffered_bounded_lemire_uint16 = (lambda bitgen, rng, bcnt, buf: rng_excl = uint16(rng) + uint16(1)# WARNING: Decompyle incomplete
)()
buffered_bounded_lemire_uint32 = (lambda bitgen, rng: rng_excl = uint32(rng) + uint32(1)# WARNING: Decompyle incomplete
)()
bounded_lemire_uint64 = (lambda bitgen, rng: rng_excl = uint64(rng) + uint64(1)# WARNING: Decompyle incomplete
)()
random_bounded_uint64_fill = (lambda bitgen, low, rng, size, dtype: out = np.empty(size, dtype = dtype)if rng == 0:
for i in np.ndindex(size):
out[i] = lowif rng <= 0xFFFFFFFF:
if rng == 0xFFFFFFFF:
for i in np.ndindex(size):
out[i] = low + next_uint32(bitgen)for i in np.ndindex(size):
out[i] = low + buffered_bounded_lemire_uint32(bitgen, rng)if rng == 0xFFFFFFFFFFFFFFFF:
for i in np.ndindex(size):
out[i] = low + next_uint64(bitgen)for i in np.ndindex(size):
out[i] = low + bounded_lemire_uint64(bitgen, rng)out)()
random_bounded_uint32_fill = (lambda bitgen, low, rng, size, dtype: out = np.empty(size, dtype = dtype)if rng == 0:
for i in np.ndindex(size):
out[i] = lowif rng == 0xFFFFFFFF:
for i in np.ndindex(size):
out[i] = low + next_uint32(bitgen)for i in np.ndindex(size):
out[i] = low + buffered_bounded_lemire_uint32(bitgen, rng)out)()
random_bounded_uint16_fill = (lambda bitgen, low, rng, size, dtype: buf = 0bcnt = 0out = np.empty(size, dtype = dtype)if rng == 0:
for i in np.ndindex(size):
out[i] = lowif rng == 65535:
for i in np.ndindex(size):
(val, bcnt, buf) = buffered_uint16(bitgen, bcnt, buf)out[i] = low + valfor i in np.ndindex(size):
(val, bcnt, buf) = buffered_bounded_lemire_uint16(bitgen, rng, bcnt, buf)out[i] = low + valout)()
random_bounded_uint8_fill = (lambda bitgen, low, rng, size, dtype: buf = 0bcnt = 0out = np.empty(size, dtype = dtype)if rng == 0:
for i in np.ndindex(size):
out[i] = lowif rng == 255:
for i in np.ndindex(size):
(val, bcnt, buf) = buffered_uint8(bitgen, bcnt, buf)out[i] = low + valfor i in np.ndindex(size):
(val, bcnt, buf) = buffered_bounded_lemire_uint8(bitgen, rng, bcnt, buf)out[i] = low + valout)()
random_bounded_bool_fill = (lambda bitgen, low, rng, size, dtype: buf = 0bcnt = 0out = np.empty(size, dtype = dtype)for i in np.ndindex(size):
(val, bcnt, buf) = buffered_bounded_bool(bitgen, low, rng, bcnt, buf)out[i] = low + valout)()
_randint_arg_check = (lambda low, high, endpoint, lower_bound, upper_bound: if low < lower_bound:
raise ValueError('low is out of bounds')if high > 0:
high = uint64(high)if not endpoint:
high -= uint64(1)upper_bound = uint64(upper_bound)if low > 0:
low = uint64(low)if high > upper_bound:
raise ValueError('high is out of bounds')if low > high:
raise ValueError('low is greater than high in given interval')Noneif None > upper_bound:
raise ValueError('high is out of bounds')if low > high:
raise ValueError('low is greater than high in given interval'))()
random_interval = (lambda bitgen, max_val: if max_val == 0:
0max_val = None(max_val)mask = uint64(gen_mask(max_val))# WARNING: Decompyle incomplete
)()
