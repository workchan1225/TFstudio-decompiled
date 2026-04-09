# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: type_annotations.pyc (Python 3.11)

from collections import defaultdict, OrderedDict
from collections.abc import Mapping
from contextlib import closing
import copy
import inspect
import os
import re
import sys
import textwrap
from io import StringIO
import numba.core.dispatcher as numba
from numba.core import ir

class SourceLines(Mapping):
    
    def __init__(self, func):
        
        try:
            (lines, startno) = inspect.getsourcelines(func)
            self.lines = textwrap.dedent(''.join(lines)).splitlines()
            self.startno = startno
            return None
        except OSError:
            self.lines = ()
            self.startno = 0
            return None


    
    def __getitem__(self, lineno):
        
        try:
            return self.lines[lineno - self.startno].rstrip()
        except IndexError:
            return ''


    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        return len(self.lines)

    avail = (lambda self: bool(self.lines))()


class TypeAnnotation(object):
    func_data = OrderedDict()
    
    def __init__(self, func_ir, typemap, calltypes, lifted, lifted_from, args, return_type, html_output = (None,)):
        self.func_id = func_ir.func_id
        self.blocks = func_ir.blocks
        self.typemap = typemap
        self.calltypes = calltypes
        self.filename = func_ir.loc.filename
        self.linenum = str(func_ir.loc.line)
        self.signature = str(args) + ' -> ' + str(return_type)
        self.lifted = lifted
        self.num_lifted_loops = len(lifted)
        self.lifted_from = lifted_from

    
    def prepare_annotations(self):
        groupedinst = defaultdict(list)
        found_lifted_loop = False
        for blkid in sorted(self.blocks.keys()):
            blk = self.blocks[blkid]
            groupedinst[blk.loc.line].append('label %s' % blkid)
            for inst in blk.body:
                lineno = inst.loc.line
                if isinstance(inst, ir.Assign):
                    if found_lifted_loop:
                        atype = 'XXX Lifted Loop XXX'
                        found_lifted_loop = False
                    elif isinstance(inst.value, ir.Expr) and inst.value.op == 'call':
                        atype = self.calltypes[inst.value]
                    elif isinstance(inst.value, ir.Const) and isinstance(inst.value.value, numba.core.dispatcher.LiftedLoop):
                        atype = 'XXX Lifted Loop XXX'
                        found_lifted_loop = True
                    else:
                        atype = self.typemap.get(inst.target.name, '<missing>')
                    aline = f'''{inst.target!s} = {inst.value!s}  :: {atype!s}'''
                elif isinstance(inst, ir.SetItem):
                    atype = self.calltypes[inst]
                    aline = f'''{inst!s}  :: {atype!s}'''
                else:
                    aline = '%s' % inst
                groupedinst[lineno].append('  %s' % aline)
                return groupedinst

    
    def annotate(self):
        source = SourceLines(self.func_id.func)
        groupedinst = self.prepare_annotations()
        io = StringIO()
        closing(io)
        if source.avail:
            print('# File: %s' % self.filename, file = io)
            for num in source:
                srcline = source[num]
                ind = _getindent(srcline)
                print('%s# --- LINE %d --- ' % (ind, num), file = io)
                for inst in groupedinst[num]:
                    print(f'''{ind!s}# {inst!s}''', file = io)
                    print(file = io)
                    print(srcline, file = io)
                    print(file = io)
                    if self.lifted:
                        print('# The function contains lifted loops', file = io)
                        for loop in self.lifted:
                            print('# Loop at line %d' % loop.get_source_location(), file = io)
                            print('# Has %d overloads' % len(loop.overloads), file = io)
                            for cres in loop.overloads.values():
                                print(cres.type_annotation, file = io)
                            print('# Source code unavailable', file = io)
                            for num in groupedinst:
                                for inst in groupedinst[num]:
                                    print(f'''{inst!s}''', file = io)
                                    print(file = io)
                                    None(None, None)
                                    return 
                                    with None:
                                        if not None, io.getvalue():
                                            pass

    
    def html_annotate(self, outfile):
        self.annotate_raw()
        func_data = copy.deepcopy(self.func_data)
        key = 'python_indent'
        for this_func in func_data.values():
            if key in this_func:
                idents = { }
                for line, amount in this_func[key].items():
                    idents[line] = '&nbsp;' * amount
                    this_func[key] = idents
                    key = 'ir_indent'
                    for this_func in func_data.values():
                        if key in this_func:
                            idents = { }
                            for line, ir_id in this_func[key].items():
                                idents[line] = ir_id()
                                this_func[key] = idents
                                
                                try:
                                    Template = Template
                                    import jinja2
                                except ImportError:
                                    raise ImportError("please install the 'jinja2' package")

                                root = os.path.join(os.path.dirname(__file__))
                                template_filename = os.path.join(root, 'template.html')
                                template = open(template_filename, 'r')
                                html = template.read()
                                None(None, None)
                            with None:
                                if not None:
                                    pass
        template = Template(html)
        rendered = template.render(func_data = func_data)
        outfile.write(rendered)

    
    def annotate_raw(self):
        '''
        This returns "raw" annotation information i.e. it has no output format
        specific markup included.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return self.annotate()


re_longest_white_prefix = re.compile('^\\s*')

def _getindent(text):
    m = re_longest_white_prefix.match(text)
    if not m:
        return ''
    return None * len(m.group(0))
