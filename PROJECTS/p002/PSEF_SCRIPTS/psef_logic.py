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
mult_dict_sapplication()
mult_dict_application_set()
mult_dict_policy()
'''

import re
import copy
import host_to_type
import vocabulary

def mult_dict_address(str_list, parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    if (parameters[vocabulary.par_rvoc['configure-addr']] == 'true'):
    # May be some logic based on par1, par2, ... value
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        mult[0][vocabulary.eq_rvoc['device-group']] = 'shared'
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
    if (parameters[vocabulary.par_rvoc['configure-addrset']] == 'true'):
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        mult[0][vocabulary.eq_rvoc['device-group']] = 'shared'
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
    if (parameters[vocabulary.par_rvoc['configure-svc']] == 'true'):
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        mult[0][vocabulary.eq_rvoc['device-group']] = 'shared'
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
    if (parameters[vocabulary.par_rvoc['configure-svcset']] == 'true'):
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        mult[0][vocabulary.eq_rvoc['device-group']] = 'shared'
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
    if (parameters[vocabulary.par_rvoc['configure-app']] == 'true'):   
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        mult[0][vocabulary.eq_rvoc['device-group']] = 'shared'
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
    if (parameters[vocabulary.par_rvoc['configure-appset']] == 'true'):   
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        mult[0][vocabulary.eq_rvoc['device-group']] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    return (mult)


def mult_dict_policy(src_str, dst_str, service_sets_dict, parameters):

##########  Description  #######
########## End of description #####


    # Some logical variables may be defined
    # For example:

    src_dc = src_str[0]
    dst_dc = dst_str[0]
    src_area = src_str[1]
    dst_area = dst_str[1]
    src_zone = src_str[2]
    dst_zone = dst_str[2]
    src_sub_zone = src_str[3]
    dst_sub_zone = dst_str[3]

    if (re.match(src_dc, dst_dc)):
        same_dc_flag = True
    else:
        same_dc_flag = False

    if (re.match(src_area, dst_area)):
        same_area_flag = True
    else:
        same_area_flag = False

    if (re.match(src_zone, dst_zone)):
        same_zone_flag = True
    else:
        same_zone_flag = False

    if (re.match(src_sub_zone, dst_sub_zone)):
        same_sub_zone_flag = True
    else:
        same_sub_zone_flag = False

    if (same_dc_flag and same_zone_flag and same_area_flag and not same_sub_zone_flag):
    # Only contracts on ACI side
        mult = []
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = host_to_type.map_apic_host_[src_dc]
        mult[0][vocabulary.eq_rvoc['tenant']] = host_to_type.map_aci_tenant[src_dc][src_area]
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('acitemplates.aci_delete_policy')
        mult[0]['cmd']['ad'].append('acitemplates.aci_create_policy')

    if (same_dc_flag and same_area_flag and not same_zone_flag):
    # Policy on PA side between different zones inside the same VSYS
        mult = []
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        mult[0][vocabulary.eq_rvoc['device-group']] = host_to_type.map_pa_device-group[src_dc][src_area]
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')

    if (same_dc_flag and not same_area_flag):
    # Policy on PA side between different VSYSes (or FWs)
        mult = []
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        # For source VSYS
        mult[0][vocabulary.eq_rvoc['device-group']] = host_to_type.map_pa_device-group[src_dc][src_area]
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_transit')
        mult.append({})
        mult[1][vocabulary.eq_rvoc['host']] = 'panorama'
        # For destination VSYS
        mult[1][vocabulary.eq_rvoc['device-group']] = host_to_type.map_pa_device-group[dst_dc][dst_area]
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_transit')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy_src_transit')

    if (not same_dc_flag):
    # Policy on PA side between different VSYSes (or FWs)
        mult = []
        mult.append({})
        mult[0][vocabulary.eq_rvoc['host']] = 'panorama'
        # For source DC/VSYS
        mult[0][vocabulary.eq_rvoc['device-group']] = host_to_type.map_pa_device-group[src_dc][src_area]
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_transit')
        mult.append({})
        mult[1][vocabulary.eq_rvoc['host']] = 'panorama'
        # For destination DC/VSYS
        mult[1][vocabulary.eq_rvoc['device-group']] = host_to_type.map_pa_device-group[dst_dc][dst_area]
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_transit')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy_src_transit')

    return (mult)

