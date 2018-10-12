'''
Administrator has to describe the equipment of psefabric.
In this realisation of psefabric the words 'cisco'  and 'juniper' are essential.
The mul_cfg.py script uses them in the deciding how to process the data.
'''

def host_to_type():
    host = {}
    host['panorama'] = 'pa_panorama'
    host['OSS_AA'] = 'pa_panorama'
    host['OSS_INTERNET'] = 'pa_panorama'
    host['INTERNAL_AA'] = 'pa_panorama'
    host['EXTERNAL_AA'] = 'pa_panorama'
    host['CORPO_INTERNET'] = 'pa_panorama'
    host['shared'] = 'pa_panorama'
    return host

def map():
    map = {}
    map['pan'] = {}
    map['pan']['area'] = {}
    map['pan']['area']['EXTERNAL_AA'] = 'EXTERNAL_AA'
    map['pan']['area']['INTERNAL_AA'] = 'INTERNAL_AA'
    map['pan']['area']['OSS_AA'] = 'OSS_AA'
    map['pan']['eq']['EXTERNAL_AA'] = 'panorama'
    map['pan']['eq']['INTERNAL_AA'] = 'panorama'
    map['pan']['eq']['OSS_AA'] = 'panorama'

    map['aci'] = {}
    map['aci']['area'] = {}
    map['aci']['area']['EXTERNAL_AA'] = 'ext-stg'
    map['aci']['area']['INTERNAL_AA'] = 'int-stg'
    map['aci']['area']['OSS_AA'] = 'oss-stg'
    
    map['aci']['eq']['EXTERNAL_AA'] = 'panorama'
    map['aci']['eq']['INTERNAL_AA'] = 'panorama'
    map['aci']['eq']['OSS_AA'] = 'panorama'
