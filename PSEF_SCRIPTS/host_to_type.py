'''
Administrator has to describe the equipment of psefabric.
In this realisation of psefabric the words 'cisco'  and 'juniper' are essential.
The mul_cfg.py script uses them in the deciding how to process the data.
'''

def host_to_type():
    host = {}
    host['192.168.31.133'] = 'cisco_l3sw'
    host['192.168.31.134'] = 'juniper_srx'
    host['192.168.31.138'] = 'cisco_asa'
    host['192.168.31.139'] = 'cisco_l3sw'
    host['192.168.31.137'] = 'cisco_l2sw'
    host['192.168.31.136'] = 'cisco_router'
    return host
