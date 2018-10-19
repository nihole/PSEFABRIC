'''
Adminstrator has to describe the equipment of psefabric.
The mult_cfg.py script uses these dicts in the deciding of how to process the data.
'''

def host_to_type():
    host = {}
    host['panorama'] = 'pa_panorama'
    host['aci_dc1_oss'] = 'cisco_aci'
    host['aci_dc1_corpo'] = 'cisco_aci'
    host['aci_dc2_oss'] = 'cisco_aci'
    host['aci_dc2_corpo'] = 'cisco_aci'
    return host

def area_to_eq_aci():
    
    map_aci = {}

    map_aci['dc1'] = {}
    map_aci['dc2'] = {}
    map_aci['dc1']['oss_aa'] = 'aci_dc1_oss'
    map_aci['dc1']['int_aa'] = 'aci_dc1_corpo'
    map_aci['dc1']['ext_aa'] = 'aci_dc1_corpo'
    map_aci['dc1']['corpo_internet'] = 'aci_dc1_corpo'
    map_aci['dc1']['oss_internet'] = 'aci_dc1_oss'
    map_aci['dc2']['oss_aa'] = 'aci_dc2_oss'
    map_aci['dc2']['int_aa'] = 'aci_dc2_corpo'
    map_aci['dc2']['ext_aa'] = 'aci_dc2_corpo'
    map_aci['dc2']['corpo_internet'] = 'aci_dc2_corpo'
    map_aci['dc2']['oss_internet'] = 'aci_dc2_oss'
    return map_aci
