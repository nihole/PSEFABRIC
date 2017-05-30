'''
This is essential element of the demultiplexer layes of Psefabric Dataflow Model and one of the key elements of the psefabric concept.
The python dictionaries created here are used in multiplexer.py.
The matter is that depending on the values of the structural elements (for networks in this realization) we have to program a specific set of commands for different MOs.
And we need some algorithm for that. So these dictionaries describe this logic.

We need to program logic for the adding/removal of addresses, address-sets, applications, application-sets, policies. So we have:

def mult_dict_address()
def mult_dict_address_set()
def mult_dict_application()
def mult_dict_application_set()
def mult_dict_policy()
'''

import copy
import host_to_type

def mult_dict_address():

##########  Description  #######
    '''
    key 'DC' meens any dc.
    key 'no_vlan' corresponds vlan = 0
    key 'vlan' meens any vlan not equal 0
    '''
#############  BODY ############

    mult = {}
    mult[('DC', 'no_vlan')]=[]
    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][0]['eq_addr'] = '192.168.31.134'
    mult[('DC', 'no_vlan')][0]['cmd'] = {}
    mult[('DC', 'no_vlan')][0]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][0]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][0]['cmd']['ad'].append('jtemplates.srx_create_address')
    mult[('DC', 'no_vlan')][0]['cmd']['rm'].append('jtemplates.srx_delete_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][1]['eq_addr'] = '192.168.31.133'
    mult[('DC', 'no_vlan')][1]['cmd'] = {}
    mult[('DC', 'no_vlan')][1]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][1]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][1]['cmd']['rm'].append('ctemplates.cisco_delete_address')
    mult[('DC', 'no_vlan')][1]['cmd']['ad'].append('ctemplates.cisco_create_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][2]['eq_addr'] = '192.168.31.138'
    mult[('DC', 'no_vlan')][2]['cmd'] = {}
    mult[('DC', 'no_vlan')][2]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][2]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][2]['cmd']['rm'].append('ctemplates.asa_delete_address')
    mult[('DC', 'no_vlan')][2]['cmd']['ad'].append('ctemplates.asa_create_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][3]['eq_addr'] = '192.168.31.136'
    mult[('DC', 'no_vlan')][3]['cmd'] = {}
    mult[('DC', 'no_vlan')][3]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][3]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][3]['cmd']['rm'].append('ctemplates.cisco_delete_address')
    mult[('DC', 'no_vlan')][3]['cmd']['ad'].append('ctemplates.cisco_create_address')
    mult_ = copy.deepcopy(mult)

    mult[('DC1', 'vlan')]=[]
    mult[('DC1', 'vlan')].append({})
    mult[('DC1', 'vlan')][0]['eq_addr'] = '192.168.31.133'
    mult[('DC1', 'vlan')][0]['cmd'] = {}
    mult[('DC1', 'vlan')][0]['cmd']['ad'] = []
    mult[('DC1', 'vlan')][0]['cmd']['rm'] = []
    mult[('DC1', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_remove_vlan_to_trunk')
    mult[('DC1', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_svi')
    mult[('DC1', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_vlan')
    mult[('DC1', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_address')
    mult[('DC1', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_vlan')
    mult[('DC1', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_svi')
    mult[('DC1', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_address')
    mult[('DC1', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_add_vlan_to_trunk')
    
    for mult_el in mult_[('DC', 'no_vlan')]:
        if not (mult_el['eq_addr'] == '192.168.31.133'):
            mult[('DC1', 'vlan')].append(mult_el)

    mult[('DC2', 'vlan')]=[]
    mult[('DC2', 'vlan')].append({})
    mult[('DC2', 'vlan')][0]['eq_addr'] = '192.168.31.139'
    mult[('DC2', 'vlan')][0]['cmd'] = {}
    mult[('DC2', 'vlan')][0]['cmd']['ad'] = []
    mult[('DC2', 'vlan')][0]['cmd']['rm'] = []
    mult[('DC2', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_remove_vlan_to_trunk')
    mult[('DC2', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_svi')
    mult[('DC2', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_vlan')
    mult[('DC2', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_address')
    mult[('DC2', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_vlan')
    mult[('DC2', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_svi')
    mult[('DC2', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_address')
    mult[('DC2', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_add_vlan_to_trunk')
    for mult_el in mult_[('DC', 'no_vlan')]:
        if not (mult_el['eq_addr'] == '192.168.31.139'):
            mult[('DC2', 'vlan')].append(mult_el) 

    mult[('DC3', 'vlan')]=[]
    mult[('DC3', 'vlan')].append({})
    mult[('DC3', 'vlan')][0]['eq_addr'] = '192.168.31.137'
    mult[('DC3', 'vlan')][0]['cmd'] = {}
    mult[('DC3', 'vlan')][0]['cmd']['ad'] = []
    mult[('DC3', 'vlan')][0]['cmd']['rm'] = []
    mult[('DC3', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_remove_vlan_to_trunk')
    mult[('DC3', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_svi')
    mult[('DC3', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_vlan')
    mult[('DC3', 'vlan')][0]['cmd']['rm'].append('ctemplates.cisco_delete_address')
    mult[('DC3', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_vlan')
    mult[('DC3', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_svi')
    mult[('DC3', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_create_address')
    mult[('DC3', 'vlan')][0]['cmd']['ad'].append('ctemplates.cisco_add_vlan_to_trunk')
    for mult_el in mult_[('DC', 'no_vlan')]:
        if not (mult_el['eq_addr'] == '192.168.31.137'):
            mult[('DC3', 'vlan')].append(mult_el)

    return (mult)

def mult_dict_address_set():

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    mult.append({})
    mult[0]['eq_addr'] = '192.168.31.134'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['rm'].append('jtemplates.srx_delete_address_set')
    mult[0]['cmd']['ad'].append('jtemplates.srx_create_address_set')

    mult.append({})
    mult[1]['eq_addr'] = '192.168.31.133'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_address_set')
    mult[1]['cmd']['ad'].append('ctemplates.cisco_create_address_set')

    mult.append({})
    mult[2]['eq_addr'] = '192.168.31.138'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ctemplates.asa_delete_address_set')
    mult[2]['cmd']['ad'].append('ctemplates.asa_create_address_set')

    mult.append({})
    mult[3]['eq_addr'] = '192.168.31.136'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ctemplates.asa_delete_address_set')
    mult[3]['cmd']['ad'].append('ctemplates.asa_create_address_set')

    return (mult)

def mult_dict_application(): 

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = '192.168.31.134'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'].append('jtemplates.srx_delete_application')
    mult[0]['cmd']['ad'].append('jtemplates.srx_create_application')
    
    mult.append({}) 
    mult[1]['eq_addr'] = '192.168.31.133'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_application')
    mult[1]['cmd']['ad'].append('ctemplates.cisco_create_application')

    mult.append({})
    mult[2]['eq_addr'] = '192.168.31.138'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ctemplates.asa_delete_application')
    mult[2]['cmd']['ad'].append('ctemplates.asa_create_application')

    mult.append({})
    mult[3]['eq_addr'] = '192.168.31.139'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ctemplates.cisco_delete_application')
    mult[3]['cmd']['ad'].append('ctemplates.cisco_create_application')

    mult.append({})
    mult[4]['eq_addr'] = '192.168.31.136'
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ctemplates.cisco_delete_application')
    mult[4]['cmd']['ad'].append('ctemplates.cisco_create_application')

    return (mult)

def mult_dict_application_set():

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = '192.168.31.134'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'].append('jtemplates.srx_delete_application_set')
    mult[0]['cmd']['ad'].append('jtemplates.srx_create_application_set')

    mult.append({})
    mult[1]['eq_addr'] = '192.168.31.133'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_application_set')
    mult[1]['cmd']['ad'].append('ctemplates.cisco_create_application_set')

    mult.append({})
    mult[2]['eq_addr'] = '192.168.31.138'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ctemplates.asa_delete_application_set')
    mult[2]['cmd']['ad'].append('ctemplates.asa_create_application_set')

    mult.append({})
    mult[3]['eq_addr'] = '192.168.31.139'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ctemplates.cisco_delete_application_set')
    mult[3]['cmd']['ad'].append('ctemplates.cisco_create_application_set')

    mult.append({})
    mult[4]['eq_addr'] = '192.168.31.136'
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ctemplates.cisco_delete_application_set')
    mult[4]['cmd']['ad'].append('ctemplates.cisco_create_application_set')

    return (mult)

def mult_dict_policy():

##########  Description  #######
    '''
 same_dc - src and dst datacenters are the same
 diff_dc - src and dst datacenters are differenet
 same_vrf - src and dst vrf are the same
 diff_vrf - src and dstsrc and dst datacenters are the same
    '''
#############  BODY ############

    mult = {}
    mult[('same_dc', 'diff_vrf','DC1')]=[]
    mult[('same_dc', 'diff_vrf','DC1')].append({})
    mult[('same_dc', 'diff_vrf','DC1')][0]['eq_addr'] = '192.168.31.134'
    mult[('same_dc', 'diff_vrf','DC1')][0]['cmd'] = {}
    mult[('same_dc', 'diff_vrf','DC1')][0]['cmd']['ad'] = []
    mult[('same_dc', 'diff_vrf','DC1')][0]['cmd']['rm'] = []
    mult[('same_dc', 'diff_vrf','DC1')][0]['cmd']['rm'].append('jtemplates.srx_delete_policy')
    mult[('same_dc', 'diff_vrf','DC1')][0]['cmd']['ad'].append('jtemplates.srx_create_policy')
    mult[('same_dc', 'diff_vrf','DC1')].append({})
    mult[('same_dc', 'diff_vrf','DC1')][1]['eq_addr'] = '192.168.31.133'
    mult[('same_dc', 'diff_vrf','DC1')][1]['cmd'] = {}
    mult[('same_dc', 'diff_vrf','DC1')][1]['cmd']['ad'] = []
    mult[('same_dc', 'diff_vrf','DC1')][1]['cmd']['rm'] = []
    mult[('same_dc', 'diff_vrf','DC1')][1]['cmd']['rm'].append('ctemplates.cisco_delete_access')
    mult[('same_dc', 'diff_vrf','DC1')][1]['cmd']['ad'].append('ctemplates.cisco_create_access')

    mult[('same_dc', 'same_vrf','DC1')]=[]
    mult[('same_dc', 'same_vrf','DC1')].append({})
    mult[('same_dc', 'same_vrf','DC1')][0]['eq_addr'] = '192.168.31.133'
    mult[('same_dc', 'same_vrf','DC1')][0]['cmd'] = {}
    mult[('same_dc', 'same_vrf','DC1')][0]['cmd']['ad'] = []
    mult[('same_dc', 'same_vrf','DC1')][0]['cmd']['rm'] = []
    mult[('same_dc', 'same_vrf','DC1')][0]['cmd']['rm'].append('ctemplates.cisco_delete_access')
    mult[('same_dc', 'same_vrf','DC1')][0]['cmd']['ad'].append('ctemplates.cisco_create_access')

    mult[('diff_dc', 'diff_vrf','DC1')]=[]
    mult[('diff_dc', 'diff_vrf','DC1')].append({})
    mult[('diff_dc', 'diff_vrf','DC1')][0]['eq_addr'] = '192.168.31.134'
    mult[('diff_dc', 'diff_vrf','DC1')][0]['cmd'] = {}
    mult[('diff_dc', 'diff_vrf','DC1')][0]['cmd']['ad'] = []
    mult[('diff_dc', 'diff_vrf','DC1')][0]['cmd']['rm'] = []
    mult[('diff_dc', 'diff_vrf','DC1')][0]['cmd']['rm'].append('jtemplates.srx_delete_policy')
    mult[('diff_dc', 'diff_vrf','DC1')][0]['cmd']['ad'].append('jtemplates.srx_create_policy')
    mult[('diff_dc', 'diff_vrf','DC1')].append({})
    mult[('diff_dc', 'diff_vrf','DC1')][1]['eq_addr'] = '192.168.31.133'
    mult[('diff_dc', 'diff_vrf','DC1')][1]['cmd'] = {}
    mult[('diff_dc', 'diff_vrf','DC1')][1]['cmd']['ad'] = []
    mult[('diff_dc', 'diff_vrf','DC1')][1]['cmd']['rm'] = []
    mult[('diff_dc', 'diff_vrf','DC1')][1]['cmd']['rm'].append('ctemplates.cisco_delete_access')
    mult[('diff_dc', 'diff_vrf','DC1')][1]['cmd']['ad'].append('ctemplates.cisco_create_access')

    mult[('same_dc', 'diff_vrf','DC2')]=[]
    mult[('same_dc', 'diff_vrf','DC2')].append({})
    mult[('same_dc', 'diff_vrf','DC2')][0]['eq_addr'] = '192.168.31.138'
    mult[('same_dc', 'diff_vrf','DC2')][0]['cmd'] = {}
    mult[('same_dc', 'diff_vrf','DC2')][0]['cmd']['ad'] = []
    mult[('same_dc', 'diff_vrf','DC2')][0]['cmd']['rm'] = []
    mult[('same_dc', 'diff_vrf','DC2')][0]['cmd']['rm'].append('ctemplates.asa_delete_access')
    mult[('same_dc', 'diff_vrf','DC2')][0]['cmd']['ad'].append('ctemplates.asa_create_access')

    mult[('diff_dc', 'diff_vrf','DC2')]=[]
    mult[('diff_dc', 'diff_vrf','DC2')].append({})
    mult[('diff_dc', 'diff_vrf','DC2')][0]['eq_addr'] = '192.168.31.138'
    mult[('diff_dc', 'diff_vrf','DC2')][0]['cmd'] = {}
    mult[('diff_dc', 'diff_vrf','DC2')][0]['cmd']['ad'] = []
    mult[('diff_dc', 'diff_vrf','DC2')][0]['cmd']['rm'] = []
    mult[('diff_dc', 'diff_vrf','DC2')][0]['cmd']['rm'].append('ctemplates.asa_delete_access')
    mult[('diff_dc', 'diff_vrf','DC2')][0]['cmd']['ad'].append('ctemplates.asa_create_access')

    mult[('diff_dc', 'diff_vrf','DC3')]=[]
    mult[('diff_dc', 'diff_vrf','DC3')].append({})
    mult[('diff_dc', 'diff_vrf','DC3')][0]['eq_addr'] = '192.168.31.136'
    mult[('diff_dc', 'diff_vrf','DC3')][0]['cmd'] = {}
    mult[('diff_dc', 'diff_vrf','DC3')][0]['cmd']['ad'] = []
    mult[('diff_dc', 'diff_vrf','DC3')][0]['cmd']['rm'] = []
    mult[('diff_dc', 'diff_vrf','DC3')][0]['cmd']['rm'].append('ctemplates.zbf_delete_policy')
    mult[('diff_dc', 'diff_vrf','DC3')][0]['cmd']['ad'].append('ctemplates.zbf_create_policy')
     
    return mult

