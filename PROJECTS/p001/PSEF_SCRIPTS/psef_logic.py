'''
This is essential element of the demultiplexer layes of Psefabric Dataflow Model and one of the key elements of the psefabric concept.
The python dictionaries created here are used in multiplexer.py.
The matter is that depending on the values of the structural elements (for adrresses in this realization) we have to program a specific set of commands for different MOs.
And we need some algorithm for that. So these dictionaries describe this logic.
We need to program logic for the adding/removal of addresses, address_sets, services, service_sets, policies. So we have:

mult_dict_address()
mult_dict_address_set()
mult_dict_service()
mult_dict_service_set()
mult_dict_sservice()
mult_dict_service_set()
mult_dict_policy()
'''

import re
import copy
import vocabulary


# Change the list of parameters if needed
def mult_dict_address(str_dict, parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    # May be some logic based on par1, par2, ... value
    mult.append({})
    mult[0]['eq_addr'] = 'dc1_fw1'
    mult[0]['eq_parameter'] = ''
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'].append('jtemplates.srx_create_address')
    mult[0]['cmd']['rm'].append('jtemplates.srx_delete_address')

    mult.append({})
    mult[1]['eq_addr'] = 'dc1_sw1'
    mult[1]['eq_parameter'] = ''
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('ctemplates.cisco_create_address')
    mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_address')

    if ((str_dict[vocabulary.str_rvoc['device']] == 'dc1_sw1') and (parameters[vocabulary.par_rvoc["aggregation-addr"]] == 'false')):
        mult[1]['cmd']['rm'].append('ctemplates.cisco_remove_vlan_to_trunk')
        mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_svi')
        mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_vlan')
        mult[1]['cmd']['ad'].append('ctemplates.cisco_create_vlan')
        mult[1]['cmd']['ad'].append('ctemplates.cisco_create_svi')
        mult[1]['cmd']['ad'].append('ctemplates.cisco_add_vlan_to_trunk')

    mult.append({})
    mult[2]['eq_addr'] = 'dc2_fw1'
    mult[2]['eq_parameter'] = ''
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['ad'].append('ctemplates.asa_create_address')
    mult[2]['cmd']['rm'].append('ctemplates.asa_delete_address')
    mult.append({})
    mult[3]['eq_addr'] = 'dc3_r1'
    mult[3]['eq_parameter'] = ''
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['ad'].append('ctemplates.cisco_create_address')
    mult[3]['cmd']['rm'].append('ctemplates.cisco_delete_address')
    mult.append({})
    mult[4]['eq_addr'] = 'dc2_sw1'
    mult[4]['eq_parameter'] = ''
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    if ((str_dict[vocabulary.str_rvoc['device']] == 'dc2_sw1') and (parameters[vocabulary.par_rvoc["aggregation-addr"]] == 'false')):
        mult[4]['cmd']['rm'].append('ctemplates.cisco_remove_vlan_to_trunk')
        mult[4]['cmd']['rm'].append('ctemplates.cisco_delete_svi')
        mult[4]['cmd']['rm'].append('ctemplates.cisco_delete_vlan')
        mult[4]['cmd']['ad'].append('ctemplates.cisco_create_vlan')
        mult[4]['cmd']['ad'].append('ctemplates.cisco_create_svi')
        mult[4]['cmd']['ad'].append('ctemplates.cisco_add_vlan_to_trunk')
    mult.append({})
    mult[5]['eq_addr'] = 'dc3_sw1'
    mult[5]['eq_parameter'] = ''
    mult[5]['cmd'] = {}
    mult[5]['cmd']['ad'] = []
    mult[5]['cmd']['rm'] = []
    if ((str_dict[vocabulary.str_rvoc['device']] == 'dc3_sw1') and (parameters[vocabulary.par_rvoc["aggregation-addr"]] == 'false')):
        mult[5]['cmd']['rm'].append('ctemplates.cisco_remove_vlan_to_trunk')
        mult[5]['cmd']['rm'].append('ctemplates.cisco_delete_svi')
        mult[5]['cmd']['rm'].append('ctemplates.cisco_delete_vlan')
        mult[5]['cmd']['ad'].append('ctemplates.cisco_create_vlan')
        mult[5]['cmd']['ad'].append('ctemplates.cisco_create_svi')
        mult[5]['cmd']['ad'].append('ctemplates.cisco_add_vlan_to_trunk')
    

    return (mult)

# Change the list of parameters if needed
def mult_dict_address_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    mult.append({})
    mult[0]['eq_addr'] = 'dc1_fw1'
    mult[0]['eq_parameter'] = ''
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['rm'].append('jtemplates.srx_delete_address_set')
    mult[0]['cmd']['ad'].append('jtemplates.srx_create_address_set')

    mult.append({})
    mult[1]['eq_addr'] = 'dc1_sw1'
    mult[1]['eq_parameter'] = ''
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_address_set')
    mult[1]['cmd']['ad'].append('ctemplates.cisco_create_address_set')

    mult.append({})
    mult[2]['eq_addr'] = 'dc2_fw1'
    mult[2]['eq_parameter'] = ''
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ctemplates.asa_delete_address_set')
    mult[2]['cmd']['ad'].append('ctemplates.asa_create_address_set')

    mult.append({})
    mult[3]['eq_addr'] = 'dc3_r1'
    mult[3]['eq_parameter'] = ''
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ctemplates.asa_delete_address_set')
    mult[3]['cmd']['ad'].append('ctemplates.asa_create_address_set')

    return (mult)


def mult_dict_application(parameters): 

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = 'dc1_fw1'
    mult[0]['eq_parameter'] = ''
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    
    mult.append({}) 
    mult[1]['eq_addr'] = 'dc1_sw1'
    mult[1]['eq_parameter'] = ''
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []

    mult.append({})
    mult[2]['eq_addr'] = 'dc2_fw1'
    mult[2]['eq_parameter'] = ''
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []

    mult.append({})
    mult[3]['eq_addr'] = 'dc2_sw1'
    mult[3]['eq_parameter'] = ''
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []

    mult.append({})
    mult[4]['eq_addr'] = 'dc3_r1'
    mult[4]['eq_parameter'] = ''
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []

    return (mult)

def mult_dict_application_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = 'dc1_fw1'
    mult[0]['eq_parameter'] = ''
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []

    mult.append({})
    mult[1]['eq_addr'] = 'dc1_sw1'
    mult[1]['eq_parameter'] = ''
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []

    mult.append({})
    mult[2]['eq_addr'] = 'dc2_fw1'
    mult[2]['eq_parameter'] = ''
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []

    mult.append({})
    mult[3]['eq_addr'] = 'dc2_sw1'
    mult[3]['eq_parameter'] = ''
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []

    mult.append({})
    mult[4]['eq_addr'] = 'dc3_r1'
    mult[4]['eq_parameter'] = ''
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []

    return (mult)





def mult_dict_service(parameters): 

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = 'dc1_fw1'
    mult[0]['eq_parameter'] = ''
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'].append('jtemplates.srx_delete_application')
    mult[0]['cmd']['ad'].append('jtemplates.srx_create_application')
    
    mult.append({}) 
    mult[1]['eq_addr'] = 'dc1_sw1'
    mult[1]['eq_parameter'] = ''
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_service')
    mult[1]['cmd']['ad'].append('ctemplates.cisco_create_service')

    mult.append({})
    mult[2]['eq_addr'] = 'dc2_fw1'
    mult[2]['eq_parameter'] = ''
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ctemplates.asa_delete_service')
    mult[2]['cmd']['ad'].append('ctemplates.asa_create_service')

    mult.append({})
    mult[3]['eq_addr'] = 'dc2_sw1'
    mult[3]['eq_parameter'] = ''
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []

    mult.append({})
    mult[4]['eq_addr'] = 'dc3_r1'
    mult[4]['eq_parameter'] = ''
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ctemplates.cisco_delete_service')
    mult[4]['cmd']['ad'].append('ctemplates.cisco_create_service')

    return (mult)

def mult_dict_service_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = 'dc1_fw1'
    mult[0]['eq_parameter'] = ''
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'].append('jtemplates.srx_delete_application_set')
    mult[0]['cmd']['ad'].append('jtemplates.srx_create_application_set')

    mult.append({})
    mult[1]['eq_addr'] = 'dc1_sw1'
    mult[1]['eq_parameter'] = ''
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ctemplates.cisco_delete_service_set')
    mult[1]['cmd']['ad'].append('ctemplates.cisco_create_service_set')

    mult.append({})
    mult[2]['eq_addr'] = 'dc2_fw1'
    mult[2]['eq_parameter'] = ''
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ctemplates.asa_delete_service_set')
    mult[2]['cmd']['ad'].append('ctemplates.asa_create_service_set')

    mult.append({})
    mult[3]['eq_addr'] = 'dc2_sw1'
    mult[3]['eq_parameter'] = ''
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []

    mult.append({})
    mult[4]['eq_addr'] = 'dc3_r1'
    mult[4]['eq_parameter'] = ''
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ctemplates.cisco_delete_service_set')
    mult[4]['cmd']['ad'].append('ctemplates.cisco_create_service_set')

    return (mult)


def mult_dict_policy(src_str, dst_str, service_sets_dict, parameters):

##########  Description  #######
########## End of description #####


    src_dc = src_str[0]
    dst_dc = dst_str[0]
    src_vrf = src_str[1]
    dst_vrf = dst_str[1]
    src_zone = src_str[2]
    dst_zone = dst_str[2]

    if (re.match(src_dc, dst_dc)):
        same_dc_flag = True
    else:
        same_dc_flag = False

    if (re.match(src_vrf, dst_vrf)):
        same_vrf_flag = True
    else:
        same_vrf_flag = False

    if (re.match(src_zone, dst_zone)):
        same_zone_flag = True
    else:
        same_zone_flag = False

    mult = []

# Then depending on these values we may program psefabric actions.
    # For example:

    if (dst_dc == 'DC1'):
        mult.append({})
        mult[0]['eq_addr'] = 'dc1_sw1'
        mult[0]['eq_parameter'] = ''
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'].append('ctemplates.cisco_create_access')
        mult[0]['cmd']['rm'].append('ctemplates.cisco_delete_access')
        if (not (same_dc_flag and same_vrf_flag)):
            # May be some logic based on par1, par2, ... value
            mult.append({})
            mult[1]['eq_addr'] = 'dc1_fw1'
            mult[1]['eq_parameter'] = ''
            mult[1]['cmd'] = {}
            mult[1]['cmd']['ad'] = []
            mult[1]['cmd']['rm'] = []
            mult[1]['cmd']['ad'].append('jtemplates.srx_create_policy')
            mult[1]['cmd']['rm'].append('jtemplates.srx_delete_policy')
    elif (dst_dc == 'DC2'):
        if (not (same_dc_flag and same_vrf_flag)):
            # May be some logic based on par1, par2, ... value
            mult.append({})
            mult[0]['eq_addr'] = 'dc2_fw1'
            mult[0]['eq_parameter'] = ''
            mult[0]['cmd'] = {}
            mult[0]['cmd']['ad'] = []
            mult[0]['cmd']['rm'] = []
            mult[0]['cmd']['ad'].append('ctemplates.asa_create_access')
            mult[0]['cmd']['rm'].append('ctemplates.asa_delete_access')
    elif (dst_dc == 'DC3'):
        if (not same_dc_flag and not same_vrf_flag):
            # May be some logic based on par1, par2, ... value
            mult.append({})
            mult[0]['eq_addr'] = 'dc3_r1'
            mult[0]['eq_parameter'] = ''
            mult[0]['cmd'] = {}
            mult[0]['cmd']['ad'] = []
            mult[0]['cmd']['rm'] = []
            mult[0]['cmd']['ad'].append('ctemplates.zbf_create_policy')
            mult[0]['cmd']['rm'].append('ctemplates.zbf_delete_policy')

    return (mult)

