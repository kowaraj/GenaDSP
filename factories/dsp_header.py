print 'dsp_header is being imported'
import os
import datetime
import getpass




### ---- log2file.py

def log(str):
    if log.file:
        log.file.write(str+'\n')
log.fullpath = '/Users/kowaraj/usr/src/Gena/TestMaps/DSP/dsp_header_debug_log.c'
if os.path.isdir(os.path.split(log.fullpath)[0]) != True:
    print 'dsp_header: no logging'
    log.file = None
else:
    log.file = open(log.fullpath, 'w')
    log('log file opened on: {0}'.format(datetime.datetime.now()))
    print 'dsp_header: logging to {0}'.format(log.fullpath)





### ---- multimethod.py 

def mm(type1, type2):
    # print 'multimethod for types: ', type1, type2
    def f_decorator(f):

            # print 'f_decorator: types = ', (type1, type2)
            # print 'f_decorator: cache = ', mm.cache
            # print 'f_decorator: f = ', f
            mm.cache[(type1, type2)] = f
            # print 'f_decorator: cache = ', mm.cache
            
            def decorated_f(arg1, arg2, *args):
                # print 'decorated_f: args = ', args
###                types_tuple = (type(arg1), type(arg2))
                types_tuple = (arg1.type, type(arg2))
                # print 'decorated_f: types_tuple = ', types_tuple
                # print 'decorated_f: mm.cache = ', mm.cache

                if types_tuple not in mm.cache:
                    raise RuntimeError, 'mm: unknown tuple: {0}'.format(types_tuple)
                
                f_ret = mm.cache[types_tuple]
                # print 'decorated_f: f_ret = ', f_ret
                return f_ret(arg1, arg2, *args)
            
 
            return decorated_f
    return f_decorator
mm.cache = {}




### ---- code_file.py 

class code_file(object):
    def __init__(self, opath, projname):
        pass

    @staticmethod
    def assure_opath(opath):
        if os.path.isdir(opath) != True:
            os.mkdir(opath)
        return opath

    @staticmethod
    def append_path(path, name):
        path = code_file.assure_opath(os.path.join(path,name))
        return path

    def get_fullpath(self):
        return os.path.join(self.opath, self.filename)

    def _open(self):
        # print '_open: ', self.ofullpath
        return open(self.ofullpath, 'w')

    def close(self):
        self.f.write('\n'.join(self.out))
        self.f.close()

    def append(self, text):
        lines = [text]
        self.out.extend(lines)

    def extend(self, lines):
        self.out.extend(lines)

class code_file_vmeh(code_file):
    def __init__(self, opath, projname):
        self.opath = code_file.append_path(opath, 'include')
        self.filename = 'vmeacc_' + projname + '.h'
        self.ofullpath = self.get_fullpath()
        self.f = self._open()
        self.out = []
        #print 'dbg: code_file_vmeh.init: ofullpath = ', self.ofullpath

class code_file_vmec(code_file):
    def __init__(self, opath, projname):
        self.opath = opath
        self.filename = 'vmeacc_' + projname + '.c'
        self.ofullpath = self.get_fullpath()
        self.f = self._open()
        self.out = []
        #print 'dbg: code_file_vmec.init: ofullpath = ', self.ofullpath

class code_file_mmh(code_file):
    def __init__(self, opath, projname):
        self.opath = code_file.append_path(opath, 'include')
        self.filename = 'MemMapDSP_' + projname + '.h'
        self.ofullpath = self.get_fullpath()
        self.f = self._open()
        self.out = []





### ---- cheb_data.py 

class cheb_data(object):
    
    def _gen_bfd_sr_vmeh(self):
        return ['// Not implemented yet: no {0} accessors'.format(self.type)]

    def _gen_bfd_sr_vmec(self):
        l = []
        l.extend([
                self.ctype + ' get_' + self.name + '() {',
                '\t' + self.ctype + '* preg = (' + self.ctype + '*)' + self.name + ';',
                '\tunsigned int bmask = ' + self.bmask + ';',
                '\tunsigned int b_lsb = ' + '{0:d}'.format(self.b_lsb) + ';',
                '\t' + self.ctype + ' bval = ( (*preg & bmask) >> b_lsb );',
                '\treturn bval;',
                '}'
                ])
        
        l.extend([
                'void set_' + self.name + '(' + self.ctype + ' bval) {',
                '\t' + self.ctype + '* preg = (' + self.ctype + '*)' + self.name + ';',
                '\t' + self.ctype + ' oldval = *preg;',
                '\tunsigned int bmask = ' + self.bmask + ';',
                '\tunsigned int b_lsb = ' + '{0:d}'.format(self.b_lsb) + ';',
                '\t' + self.ctype + ' newval = (oldval & ~bmask) | (bval << b_lsb);',
                '\t*preg = newval;',
                '}'
                ])

        return l
        
        
class register_data(object):

    known_types = dict([(('float', 32), 'float'), (('float', 64), 'double'), (('unsigned', 16), 'unsigned short'), (('unsigned', 32), 'unsigned int'), (('signed', 16), 'short'), (('signed', 32), 'int')])

    def __init__(self, ch, prefix=''):
        self.el = ch
        self.name = prefix+ch.name
        self.type = ch.type
        self.mode = ch.access_mode
        self.addr = ch.address
        ctype = self.known_types[(self.el.bit_encoding, self.el.element_width)]
        self.ctype = ctype
        
    def gen_mmh(self):
        return ['#define {0:30} (0x{1:0>8X})// {4}, {2:3}, {3}'.format(self.name, self.addr, self.mode, self.ctype, self.type)]

    def gen_vmeh(self):
        log('gen_vmeh')
        l = []
        l.extend([self.ctype + ' get_' + self.name + '(void);'])
        if self.mode == 'rw' or self.mode == 'w':
            l.extend(['void set_' + self.name + '(' + self.ctype + ' val);'])
        return l

    def gen_vmec(self):
        # getter
        l = []
        l.extend([
                self.ctype + ' get_' + self.name + '() {',
                '\t' + self.ctype + '* preg = (' + self.ctype + '*)' + self.name + ';',
                '\t' + 'return (' + self.ctype + ') *preg;',
                '}'
                ])
        # setter
        if self.mode == 'rw' or self.mode == 'w':
            l.extend([
                    'void set_' + self.name + '(' + self.ctype + ' val) {',
                    '\t' + self.ctype + '* preg = (' + self.ctype + '*)' + self.name + ';',
                    '\t' + '*preg = val;',
                    '}'
                    ])
        return l

class sub_reg(cheb_data):

    def __init__(self, ch, prefix, ctype):
        self.el = ch
        self.name = prefix+ch.name
        self.type = ch.type
        self.mode = ch.access_mode
        self.ctype = ctype

        self.b_lsb = b._attr['lsb']
        self.b_msb = b._attr['msb']

        if b_lsb == None:
            raise RuntimeError, 'b_lsb of a sub-reg could be None'
        self.bmask = '0x{0:0>8X}'.format( ((1 << (b_msb-b_lsb+1))-1) << b_lsb) 

    def gen_mmh(self):
        return ['#define {0:30} ({1}) // {2}'.format(self.name, self.bitmask, self.type)]

    def gen_vmec(self):
        return self._gen_bfd_sr_vmec()

    def gen_vmeh(self):
        return self._gen_bfd_sr_vmeh()

class bit_field_data(cheb_data):

    def __init__(self, ch, prefix, ctype):
        self.el = ch
        self.name = prefix+ch.name
        self.type = ch.type
        self.mode = ch.access_mode
        self.bit = ch.bit
        self.bmask = '0x{0:0>8X}'.format(1<< ch.bit)
        self.ctype = ctype
        self.b_lsb = self.bit
                        
    def gen_mmh(self):
        return ['#define {0:30} ({1}) // {2}'.format(self.name, self.bmask, self.type)]

    def gen_vmec(self):
        return self._gen_bfd_sr_vmec()

    def gen_vmeh(self):
        return self._gen_bfd_sr_vmeh()

class code_field(object):

    def __init__(self, ch, prefix):
        self.el = ch
        self.name = prefix+ch.name
        self.type = ch.type
                        
    def gen_mmh(self):
        # debug_output.append('cf = {0}'.format(self.el.__dict__))
        return ['#define {0:30} {1} // {2}'.format(self.name, self.el.code, self.type)]

    def gen_vmeh(self):
        return ['// Not implemented yet: no {0} accessors'.format(self.type)]
    
    def gen_vmec(self):
        return ['// Not implemented yet: no {0} accessors'.format(self.type)]

@mm("register-data", code_file_vmeh)
def print_rec_to_file(rec, file, prefix, parent):
    file.extend(register_data(rec, prefix).gen_vmeh())

@mm("register-data", code_file_vmec)
def print_rec_to_file(rec, file, prefix, parent):
    file.extend(register_data(rec, prefix).gen_vmec())

@mm("register-data", code_file_mmh)
def print_rec_to_file(rec, file, prefix, parent):
    file.extend(register_data(rec, prefix).gen_mmh())

@mm("bit-field-data", code_file_vmeh)
def print_rec_to_file(rec, file, prefix, parent):
    ctype = register_data(parent).ctype
    file.extend(bit_field_data(rec, prefix, ctype).gen_vmeh())

@mm("bit-field-data", code_file_vmec)
def print_rec_to_file(rec, file, prefix, parent):
    ctype = register_data(parent).ctype
    file.extend(bit_field_data(rec, prefix, ctype).gen_vmec())

@mm("bit-field-data", code_file_mmh)
def print_rec_to_file(rec, file, prefix, parent):
    ctype = register_data(parent).ctype
    file.extend(bit_field_data(rec, prefix, ctype).gen_mmh())

@mm("sub-reg", code_file_mmh)
def print_rec_to_file(rec, file, prefix, parent):
    ctype = register_data(parent).ctype
    file.extend(sub_reg(rec, prefix, ctype).gen_mmh())

@mm("sub-reg", code_file_vmec)
def print_rec_to_file(rec, file, prefix, parent):
    ctype = register_data(parent).ctype
    file.extend(sub_reg(rec, prefix, ctype).gen_vmec())

@mm("sub-reg", code_file_vmeh)
def print_rec_to_file(rec, file, prefix, parent):
    ctype = register_data(parent).ctype
    file.extend(sub_reg(rec, prefix, ctype).gen_vmeh())

@mm("code-field", code_file_mmh)
def print_rec_to_file(rec, file, prefix, parent):
    file.extend(code_field(rec, prefix).gen_mmh())

@mm("code-field", code_file_vmec)
def print_rec_to_file(rec, file, prefix, parent):
    file.extend(code_field(rec, prefix).gen_vmec())

@mm("code-field", code_file_vmeh)
def print_rec_to_file(rec, file, prefix, parent):
    file.extend(code_field(rec, prefix).gen_vmeh())





### ---- code_generator.py 

class code_generator(object):
    

    class Info(object): pass
    info = Info()
    
    def _set_info(self, root):
        self.info.GenaDSP = { 'name': 'GenaDSP', 'version': 'v2012-10-02', 'author = ': 'Andrey Pashnin <apashnin@cern.ch>, CERN BE-RF-CS' }
        self.info.memmap_ver = root.map_version
        self.info.ts = datetime.datetime.now()
        self.info.user = getpass.getuser()
        self.info.dsp_ver = '0x' + self.info.ts.strftime("%y%m%d%M") + ' // format: 0xyymmddMM'

    def _make_common_header(self):
        l = [
            '// Generated from: {0}, '.format(self.ifilename),
            '//           memory map version: {0}'.format(self.info.memmap_ver),
            '// Generated on: {0:%Y-%m-%d %H:%M:%S},'.format(self.info.ts),
            '//           by: {0},'.format(self.info.user),
            '//           using: {0[name]} ({0[version]})'.format(self.info.GenaDSP),
            '// '
            ]
        return l

    def _make_mmh_header(self, h_common):
        l = []
        l.extend([
                '// DSP Memory map for {0}'.format(self.projname)
                ])
        l.extend(h_common)
        l.extend([
                '',
                '#define DSP_VERSION {0}'.format(self.info.dsp_ver), 
                ''
                ])
        return l

    def _make_vmeh_header(self, h_common):
        l = []
        l.extend([
                '// VME accessors .h for {0}'.format(self.projname)
                ])
        l.extend(h_common)
        l.extend([
                ''
                ])
        return l

    def _make_vmec_header(self, h_common):
        l = []
        l.extend([
                '// VME accessors .c for {0}'.format(self.projname)
                ])
        l.extend(h_common)
        l.extend([
                ''
                ])
        return l
        
    def __init__(self, root, fullpath):

        self.root = root
        self.projname = root.name
        filepath, filename = os.path.split(fullpath)
        self.ifilename = filename
        self.ipath = filepath
        self.opath = code_file.append_path(filepath, 'DSP')
        self.files = list()
        self._set_info(root)

        # make the list of files
        vme_acc_h = code_file_vmeh(self.opath, self.projname)
        self.add_file(vme_acc_h)
        vme_acc_c = code_file_vmec(self.opath, self.projname)
        self.add_file(vme_acc_c)
        mm_h = code_file_mmh(self.opath, self.projname)
        self.add_file(mm_h)

        # add headers
        h_common = self._make_common_header()
        h_mmh = self._make_mmh_header(h_common)
        h_vmeh = self._make_vmeh_header(h_common)
        h_vmec = self._make_vmec_header(h_common)

        mm_h.extend(h_mmh)
        vme_acc_h.extend(h_vmeh)
        vme_acc_c.extend(h_vmec)


    def add_file(self, file):
        self.files.append(file)

    def _parse_root(self, root, prefix=''):
        # print '___ root.type = ', root.type
        # print '___ root.__dict__ = ', root.__dict__
        # print '___ ch.__dict__ = ', root._children[0].__dict__
        # print '___ root.name = ', root.name, ', root.type = ', root.type
        
        def sort_key(x):
            # print '__ x.name = ', x.name, ', x.type = ', x.type
            # print '__ x = ', x.__dict__
            if x._attr.has_key('address'):
                return x._attr['address']
            elif x._attr.has_key('bit'):
                return x._attr['bit']
            elif x._attr.has_key('range'):
                return x._attr['range']
            elif x._attr.has_key('code'):
                return x._attr['code']
            else:
                raise RuntimeError, "sorting key not found"

        for ch in sorted(root._children, key=sort_key):
            if len(ch) > 0:
                log('_parse_root: recur({0})... '.format(prefix + ch.name + '_'))
                self._parse_root(ch, prefix + ch.name + '_')
            else:
                if ch.type == 'area':
                    log('_parse_root: empty area found')
                else:
                    log('_parse_root: ch = ({0},{1})'.format(ch.name, ch.type))
                    # log('_parse_root: ch.__dict__ = {0} '.format(ch.__dict__))
                    print 'parse_child'
                    for f in self.files:
                        print_rec_to_file(ch, f, prefix, root)

    def _do(self):
        self._parse_root(self.root)

        for f in self.files:
            f.close()


### ---- dsp_header.py 

class dsp_header(object):
    
    def __init__(self, root, fullpath):
        gen = code_generator(root, fullpath)
        gen._do()

        log.file.close()


#EOF
