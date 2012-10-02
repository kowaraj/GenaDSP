'''

    DSP Memory Map & Getters.. 


@author:    Andrey Pashnin <apashnin@cern.ch>
            CERN, BE-RF-CS

@change:    
            2012-08-16
            --  bugfix: register address is divided by (self.dataSize/8) now.

            2012-08-14
            --  Basic functionality. 
            
            2012-08-09         
            --  Initial revision.


@todo:
            --  
@func:
            Generates the following file tree:
                ./DSP
                ./DSP/include/MemMapDSP_<name>.h    = memory map file
                ./DSP/include/vmeacc_<name>.h       = vme access functions declaration
                ./DSP/vmeacc_<name>.c               = vme access functions definitions

            root's nodes:
                - register-data
                    width:
                    - 16, 32 for unsigned and signed
                        children:
                        - bit-field-data
                        - sub-reg
                    - 32, 64 for float


'''

from gena_factory import gena_factory
import os
from math import log, floor, ceil
import datetime
import getpass

import inspect #grab line number

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

class dsp_header(gena_factory):

    info = {
        'name': 'DSP Header',
        'version': 'v2012-08-09',
        'author': 'Andrey Pashnin <apashnin@cern.ch>, CERN BE-RF-CS'
    }
    
    def __parse_register(self, ch, prefix):
            
            
            #1.memory map
            
            #
            # Bits...
            #

            if len(ch) > 0:
                for b in ch._children:

                    bmask = []
                    b_name = ''
                    if b.type == 'bit-field-data':
                        b_name = b._attr['name']
                        b_bit = b._attr['bit']
                        bmask = '0x{0:0>8X}'.format(1<< b_bit)
                        
                        #5. getter, bits
                        self.__gen_GetBFD_uint32(c_type, ch_name, b_name, bmask, b_bit)
                        #6. setter, bits
                        self.__gen_SetBFD_uint32(c_type, ch_name, b_name, bmask, b_bit)
                    
                    elif b.type == 'sub-reg':
                        b_name = b._attr['name']
                        b_lsb = b._attr['lsb']
                        b_msb = b._attr['msb']

                        if b_lsb == None:
                            bmask = '0x{0:0>8X}'.format(1<< b_msb)
                        else:
                            bmask = '0x{0:0>8X}'.format( ((1 << (b_msb-b_lsb+1))-1) << b_lsb) 
                        
                        #5. getter, bits
                        self.__gen_GetSubreg_uint32(c_type, ch_name, b_name, bmask, b_lsb)
                        #6. setter, bits
                        self.__gen_SetSubreg_uint32(c_type, ch_name, b_name, bmask, b_lsb)
                    
                    else:
                        raise RuntimeError, 'Unknown type. Not implemented yet.'
                
                    #4. memorty map, bits
                    l = '#define {0:30} ({1}) // bitmask'.format(ch_name+'_'+b_name, bmask)
                    self.out_mm.append(l)
                    
                    self.out_h.extend([''])
                    self.out_c.extend([''])
        

    def __parse_area(self, root, prefix=''):

        #print '__parse_area: name = {0}, type = {1}, prefix = {2}'.format(root._attr['name'], root.type, prefix)
        if root.type not in  {'area', 'memory-map'}:
            raise RuntimeError, 'Not implemented yet. Expected type: {area | memory-map}'
        
        self.out_mm.extend([
            '',
            '//    -- Register interface{0}'.format(4)
        ])

        for ch in sorted(root._children, key=lambda x: x._attr['address']):

            ch_name = ch._attr['name']
            ch_addr = ch._attr['address']
            #print 'ch_name = {0}, ch_type = {1}, ch_addr = {2}'.format(ch_name, ch.type, ch_addr)
            if ch.type == 'area':
                self.__parse_area(ch, prefix + ch_name + '_')

            elif ch.type == 'register-data':
                self.__parse_register(ch, prefix)

            else:
                raise RuntimeError, 'Not implemented yet. Expected {area | register-data}'


    def __init__(self, root, fullpath, prefix=''):

        #raise RuntimeError, 'file:{0}, line:{1}'.format(__file__, lineno())

        print 'dsp_header __init__, fullpath = {0}'.format(fullpath)


        # Split out file path and file name, ofilepath will be used as the 
        # output directory
        ifilepath, filename = os.path.split(fullpath)
        name = root.name
        mapVersion = root.map_version
        identCode = root.ident_code
        accessMode = root.mem_map_access_mode
        self.dataSize = root.data_size
        self.dspBaseAddr = 0x2000000
        mapDepth = root.area_depth
        addrSize = root.addr_size

        #input parameters:
        ## 0. ifilepath = path of the xml memory map file

        #temporal parameters:
        ## 0. ofilepath = root folder for the DSP code
        ## 1. ofilepath_inc = 'include' directory

        ## 2. ofilename_c = definitions
        ## 3. ofilename_h = declarations
        ## 4. ofilename_mm = memory map header

        # File reading complete! Let's get on with making some C!
        ofilepath = os.path.join(ifilepath, 'DSP')
        ofilepath_inc = os.path.join(ofilepath, 'include')

        if os.path.isdir(ofilepath) != True:
            os.mkdir(ofilepath)
        if os.path.isdir(ofilepath_inc) != True:
            os.mkdir(ofilepath_inc)

        # Open file for writing
        ofilename_mm = 'MemMapDSP_{0}.h'.format(name)
        f_mm = open(os.path.join(ofilepath_inc, ofilename_mm), 'w')
        f_c = open(os.path.join(ofilepath, 'vmeacc_{0}.c'.format(name)), 'w')
        f_h = open(os.path.join(ofilepath_inc, 'vmeacc_{0}.h'.format(name)), 'w')

        addrMSB = addrSize - 1
        addrLSB = int(log(self.dataSize // 8, 2))
        dataMSB = self.dataSize - 1

        readableTypes = ('r', 'rw', 'rmw')
        writableTypes = ('w', 'rw', 'rmw')

        # Write preamble, comments and standard bits of the entity
        # memory map header
        
        d = datetime.datetime.now()
        dsp_version = '0x' + d.strftime("%y%m%d%M") + ' // format: 0xyymmddMM'
        #print 'dsp_version = {0}'.format(dsp_version)

        self.out_mm = [
            '// DSP Memory map for {0}'.format(name),
            '// Generated from: {0}, version {1}'.format(filename, mapVersion),
            '// Generated on: {0:%Y-%m-%d %H:%M:%S} by {1} using {2[name]} ({2[version]})'.format(datetime.datetime.now(), getpass.getuser(), dsp_header.info),
            '// ',
            '',
            '#define DSP_VERSION {0}'.format(dsp_version), 
            ''
        ]
        f_mm.write('\n'.join(self.out_mm))
        
        # vme access code
        self.out_c = [
            '// VME access for {0}'.format(name),
            '// Generated from: {0}, version {1}'.format(filename, mapVersion),
            '// Generated on: {0:%Y-%m-%d %H:%M:%S} by {1} using {2[name]} ({2[version]})'.format(datetime.datetime.now(), getpass.getuser(), dsp_header.info),
            '// ',
            '',
            '#include "include\{0}"'.format(ofilename_mm),
            '\n'
        ]
        F_c.write('\n'.join(self.out_c))

        # vme access header
        self.out_h = [
            '// VME access header for {0}'.format(name),
            '// Generated from: {0}, version {1}'.format(filename, mapVersion),
            '// Generated on: {0:%Y-%m-%d %H:%M:%S} by {1} using {2[name]} ({2[version]})'.format(datetime.datetime.now(), getpass.getuser(), dsp_header.info),
            '// ',
            ''
        ]
        f_h.write('\n'.join(self.out_h))

        self.out_mm = []
        self.out_c = []
        self.out_h = []
           
        # root == memory-map
        print 'root attrs = {0}'.format(root._attr)
        self.__parse_area(root)
        
        '''
        for o in self.out_mm:
            print '{0}'.format(o)
        for o in self.out_c:
            print '{0}'.format(o)
        for o in self.out_h:
            print '{0}'.format(o)
        '''

        self.out_mm.extend([''])
        self.out_h.extend([''])
        self.out_c.extend([''])
       
        f_mm.write('\n'.join(self.out_mm))
        f_c.write('\n'.join(self.out_c))
        f_h.write('\n'.join(self.out_h))

        f_mm.close()
        f_c.close()
        f_h.close()


# EOF

