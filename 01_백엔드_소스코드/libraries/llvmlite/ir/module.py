# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: module.pyc (Python 3.11)

import collections
from llvmlite.ir import context, values, types, _utils

class Module(object):
    
    def __init__(self, name, context = ('', context.global_context)):
        self.context = context
        self.name = name
        self.data_layout = ''
        self.scope = _utils.NameScope()
        self.triple = 'unknown-unknown-unknown'
        self.globals = collections.OrderedDict()
        self.metadata = []
        self.namedmetadata = { }
        self._metadatacache = { }

    
    def _fix_metadata_operands(self, operands):
        fixed_ops = []
    # WARNING: Decompyle incomplete

    
    def _fix_di_operands(self, operands):
        fixed_ops = []
        for name, op in operands:
            if isinstance(op, (list, tuple)):
                op = self.add_metadata(op)
            fixed_ops.append((name, op))
            return fixed_ops

    
    def str_ditok_operands(self, operands):
        str_ops = []
        for name, op in operands:
            if name == 'encoding' and isinstance(op, values.DIToken):
                op = op.value
            str_ops.append((name, op))
            return str_ops

    
    def add_metadata(self, operands):
        '''
        Add an unnamed metadata to the module with the given *operands*
        (a sequence of values) or return a previous equivalent metadata.
        A MDValue instance is returned, it can then be associated to
        e.g. an instruction.
        '''
        if not isinstance(operands, (list, tuple)):
            raise TypeError(f'''expected a list or tuple of metadata values, got {operands!r}''')
        operands = self._fix_metadata_operands(operands)
        key = tuple(operands)
        if key not in self._metadatacache:
            n = len(self.metadata)
            md = values.MDValue(self, operands, name = str(n))
            self._metadatacache[key] = md
        else:
            md = self._metadatacache[key]
        return md

    
    def add_debug_info(self, kind, operands, is_distinct = (False,)):
        '''
        Add debug information metadata to the module with the given
        *operands* (a dict of values with string keys) or return
        a previous equivalent metadata.  *kind* is a string of the
        debug information kind (e.g. "DICompileUnit").

        A DIValue instance is returned, it can then be associated to e.g.
        an instruction.
        '''
        operands = tuple(sorted(self._fix_di_operands(operands.items())))
        str_op_key = tuple(sorted(self.str_ditok_operands(operands)))
        key = (kind, str_op_key, is_distinct)
        if key not in self._metadatacache:
            n = len(self.metadata)
            di = values.DIValue(self, is_distinct, kind, operands, name = str(n))
            self._metadatacache[key] = di
        else:
            di = self._metadatacache[key]
        return di

    
    def add_named_metadata(self, name, element = (None,)):
        '''
        Add a named metadata node to the module, if it doesn\'t exist,
        or return the existing node.
        If *element* is given, it will append a new element to
        the named metadata node.  If *element* is a sequence of values
        (rather than a metadata value), a new unnamed node will first be
        created.

        Example::
            module.add_named_metadata("llvm.ident", ["llvmlite/1.0"])
        '''
        if name in self.namedmetadata:
            nmd = self.namedmetadata[name]
        else:
            nmd = values.NamedMetaData(self)
            self.namedmetadata[name] = values.NamedMetaData(self)
    # WARNING: Decompyle incomplete

    
    def get_named_metadata(self, name):
        '''
        Return the metadata node with the given *name*.  KeyError is raised
        if no such node exists (contrast with add_named_metadata()).
        '''
        return self.namedmetadata[name]

    functions = (lambda self: self.globals.values()())()
    global_values = (lambda self: self.globals.values())()
    
    def get_global(self, name):
        '''
        Get a global value by name.
        '''
        return self.globals[name]

    
    def add_global(self, globalvalue):
        '''
        Add a new global value.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_unique_name(self, name = ('',)):
        '''
        Get a unique global name with the following *name* hint.
        '''
        return self.scope.deduplicate(name)

    
    def declare_intrinsic(self, intrinsic, tys, fnty = ((), None)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_identified_types(self):
        return self.context.identified_types

    
    def _get_body_lines(self):
        lines = self.get_identified_types().values()()
        (lambda .0: [ str(v) for v in .0 ]) += self.globals.values()()
        return lines

    
    def _get_metadata_lines(self):
        mdbuf = []
        for k, v in self.namedmetadata.items():
            '!{name} = !{{ {operands} }}'.format(k(name = ', '.join, operands = (lambda .0: pass# WARNING: Decompyle incomplete
)(v.operands())))
            for md in self.metadata:
                mdbuf.append(str(md))
                return mdbuf

    
    def _stringify_body(self):
        return '\n'.join(self._get_body_lines())

    
    def _stringify_metadata(self):
        return '\n'.join(self._get_metadata_lines())

    
    def __repr__(self):
        lines = []
        lines += [
            f'''; ModuleID = "{self.name!s}"''',
            f'''target triple = "{self.triple!s}"''',
            f'''target datalayout = "{self.data_layout!s}"''',
            '']
        lines += self._get_body_lines()
        lines += self._get_metadata_lines()
        return '\n'.join(lines)
