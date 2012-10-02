# py.test test file for dsp_header.py
# apashnin@20120928
# 

def test_import_all():
    import sys

    print 'dsp_header_test is being imported'

    if sys.modules.has_key('dsp_header'):
        print 'del d'
        del sys.modules['dsp_header']
    if sys.modules.has_key('dsp_header.dsp_header'):
        print 'del d.d'
        del sys.modules['dsp_header.dsp_header']
    # if sys.modules.has_key('factories'):
    #     print 'del factories'
    #     del sys.modules['factories']


    import factories
    reload(factories)
    from PyCheb import *
    from dsp_header import *
    import dsp_header
# def test_dsp_header_has_ctor_taking_2args():
#     arg1_root = ''
#     arg2_fullpath = ''
#     #assert( dsp_header(arg1_root, arg2_fullpath) == 'self + two arguments')
    
# def test_dsp_header_temp():
#    fullpath = '/Users/kowaraj/usr/src/20120928_Gena/Gena/TestMaps/spsFreqProgDSP.xml'
    fullpath = '/Users/kowaraj/usr/src/Gena/TestMaps/spsFreqProgDSP_areatest2.xml'
    root = PyCheb(fullpath, False).get()
    #print 'root = ', root
    #print 'dir(root) = ', dir(root)
    #print 'root.__dict__ = ', root.__dict__
    #print 'name = ', root.__dict__['_attr']['name']
    #print 'gen_dsp = ', root.__dict__['_attr']['gen']

    # root is a class
    assert('__class__' in dir(root))
    # root has '_attr' which contains a 'name'
    assert(root.__dict__['_attr']['name'])
    # root should contain 'dsp' in 'gen'
    assert(root.__dict__['_attr']['gen']['dsp'] == True)


    # preview...
    
    f = factories.dsp_header(root, fullpath)
    













