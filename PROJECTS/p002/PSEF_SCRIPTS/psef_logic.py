'''
This is essential element of the demultiplexer layes of Psefabric Dataflow Model and one of the key elements of the psefabric concept.
The python dictionaries created here are used in multiplexer.py.
The matter is that depending on the values of the structural elements (for networks in this realization) we have to program a specific set of commands for different MOs.
And we need some algorithm for that. So these dictionaries describe this logic.
We need to program logic for the adding/removal of addresses, address_sets, services, service_sets, policies. So we have:
mult_dict_address()
mult_dict_address_set()
mult_dict_service()
mult_dict_service_set()
mult_dict_policy()
'''

import re
import copy
import host_to_type


def mult_dict_address(str_list, parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    if (parameters['addr_par_1'] == 'true'):
    # May be some logic based on par1, par2, ... value
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'some_parameter'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_address')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_address')

    return (mult)

def mult_dict_address_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    if (parameters['addrset_par_1'] == 'true'):
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    return (mult)

def mult_dict_service(parameters): 

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    if (parameters['svc_par_1'] == 'true'):
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_service')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_service')
    
    return (mult)

def mult_dict_service_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    if (parameters['svcset_par_1'] == 'true'):
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_service_set')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_service_set')

    return (mult)

def mult_dict_application(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    if (parameters['app_par_1'] == 'true'):   
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []

    return (mult)

def mult_dict_application_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    if (parameters['appset_par_1'] == 'true'):   
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    return (mult)


def mult_dict_policy(src_str, dst_str, service_sets_dict, parameters):

##########  Description  #######
########## End of description #####

    mult = []

    # Some logical variables may be defined
    # For example:

    if (re.match(src_str[0], dst_str[0])):
        same_dc_flag = True
    else:
        same_dc_flag = False

    if (re.match(src_str[1], dst_str[1])):
        same_area_flag = True
    else:
        same_area_flag = False

    if (re.match(src_str[2], dst_str[2])):
        same_zone_flag = True
    else:
        same_zone_flag = False

    if (re.match(src_str[3], dst_str[3])):
        same_sub_zone_flag = True
    else:
        same_sub_zone_flag = False

    if (same_zone_flag and same_area_flag and not same_sub_zone_flag):
        
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = map_aci_['dc1'][src_area]
        mult[0]['eq_parameter'] = ''
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('acitemplates.aci_delete_policy')
        mult[0]['cmd']['ad'].append('acitemplates.aci_create_policy')
        mult.append({})
        mult[1]['eq_addr'] = map_aci_['dc2'][src_area]
        mult[1]['eq_parameter'] = ''
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['rm'].append('acitemplates.aci_delete_policy')
        mult[1]['cmd']['ad'].append('acitemplates.aci_create_policy')

    if (not same_zone_flag and same_area_flag):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = map_pa_['dc1'][src_area]
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_transit')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_src_transit')

    if (not same_area_flag):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = map_pa_['dc1'][src_area]
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_transit')
        mult.append({})
        mult[1]['eq_addr'] = 'panorama'
        mult[1]['eq_parameter'] = map_pa_['dc1'][dst_area]
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_transit')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy_src_transit')

    return (mult)

