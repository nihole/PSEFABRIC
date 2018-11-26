'''
Adminstrator has to describe the equipment of psefabric.
The mult_cfg.py script uses these dicts in the deciding of how to process the data.
'''

def host_to_type():
    host = {}
    host['panorama'] = 'pa_panorama'
    host['apic_aci_dc1'] = 'cisco_aci'
    host['apic_aci_dc2'] = 'cisco_aci'
    return host

def area_to_eq_aci():
    
    map_apic_host = {}
    map_apic_host['dc1'] = 'apic_aci_dc1'
    map_apic_host['dc2'] = 'apic_aci_dc2'

    
    map_aci_tenant = {}
    map_aci_tenant['dc1'] = {}
    map_aci_tenant['dc2'] = {}
    map_aci_tenant['dc1']['a1'] = 't1'
    map_aci_tenant['dc1']['a2'] = 't2'
    map_aci_tenant['dc2']['a1'] = 't1'
    map_aci_tenant['dc2']['a2'] = 't2'

    return (map_apic_host, map_aci_tenant)

def area_to_eq_pa():

    '''
    Maps areas to panorama device-groups
    '''
    
    map_pa_device_group = {}
    map_pa_device_group['dc1'] = {}
    map_pa_device_group['dc2'] = {}
    map_pa_device_group['dc1']['a1'] = 'dc1_a1'
    map_pa_device_group['dc1']['a2'] = 'dc1_a2'
    map_pa_device_group['dc2']['a1'] = 'dc2_a1'
    map_pa_device_group['dc2']['a2'] = 'dc2_a2'

    return map_pa_device_group
