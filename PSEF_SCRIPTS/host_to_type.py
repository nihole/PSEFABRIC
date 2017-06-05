'''
Administrator has to describe the equipment of psefabric.
In this realisation of psefabric the words 'cisco'  and 'juniper' are essential.
The mul_cfg.py script uses them in the deciding how to process the data.
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

