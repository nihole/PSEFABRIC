'''
Adminstrator has to describe the equipment of psefabric.
The mult_cfg.py script uses these dicts in the deciding of how to process the data.
'''

def host_to_type():
    host = {}
    host['dc1_sw1'] = 'cisco_l3sw'
    host['dc1_fw1'] = 'juniper_srx'
    host['dc2_fw1'] = 'cisco_asa'
    host['dc2_sw1'] = 'cisco_l3sw'
    host['dc3_sw1'] = 'cisco_l2sw'
    host['dc3_r1'] = 'cisco_router'
    return host

# Also may be some mapping dictionaries here (for mapping some logical network  area to physical entities, for example areas -> aci tenants and palo alto VSYSes)  
