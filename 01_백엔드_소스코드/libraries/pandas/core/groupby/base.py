# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''
Provide basic components for groupby.
'''
from __future__ import annotations
import dataclasses
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Hashable
OutputKey = <NODE:12>()
plotting_methods = frozenset([
    'plot',
    'hist'])
cythonized_kernels = frozenset([
    'cumprod',
    'cumsum',
    'shift',
    'cummin',
    'cummax'])
reduction_kernels = frozenset([
    'all',
    'any',
    'corrwith',
    'count',
    'first',
    'idxmax',
    'idxmin',
    'last',
    'max',
    'mean',
    'median',
    'min',
    'nunique',
    'prod',
    'quantile',
    'sem',
    'size',
    'skew',
    'kurt',
    'std',
    'sum',
    'var'])
transformation_kernels = frozenset([
    'bfill',
    'cumcount',
    'cummax',
    'cummin',
    'cumprod',
    'cumsum',
    'diff',
    'ffill',
    'ngroup',
    'pct_change',
    'rank',
    'shift'])
groupby_other_methods = frozenset([
    'agg',
    'aggregate',
    'apply',
    'boxplot',
    'corr',
    'cov',
    'describe',
    'expanding',
    'ewm',
    'filter',
    'get_group',
    'groups',
    'head',
    'hist',
    'indices',
    'ndim',
    'ngroups',
    'nth',
    'ohlc',
    'pipe',
    'plot',
    'resample',
    'rolling',
    'tail',
    'take',
    'transform',
    'sample',
    'value_counts'])
transform_kernel_allowlist = reduction_kernels | transformation_kernels
