'''
Adminstrator has to describe the equipment of psefabric.
The mult_cfg.py script uses these dicts in the deciding of how to process the data.
'''

def host_to_type():
    host = {}
    host['example_device1'] = 'example_vendor'
    host['example_device2'] = 'example_vendor'
    return host

# Also may be some mapping dictionaries here (for mapping some logical network  area to physical entities, for example areas -> aci tenants and palo alto VSYSes)  
