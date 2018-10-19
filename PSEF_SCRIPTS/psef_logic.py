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

def mult_dict_address(ifcfg):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    if (ifcfg == 'true'):
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_address')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_address')

    return (mult)

def mult_dict_address_set(ifcfg):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    if (ifcfg == 'true'):
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    return (mult)

def mult_dict_service(ifcfg): 

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    if (ifcfg == 'true'):
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_service')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_service')
    
    return (mult)

def mult_dict_service_set(ifcfg):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    if (ifcfg == 'true'):
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_service_set')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_service_set')

    return (mult)

def mult_dict_application(ifcfg):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    if (ifcfg == 'true'):   
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []

    return (mult)

def mult_dict_application_set(ifcfg):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    if (ifcfg == 'true'):   
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'shared'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    return (mult)


def mult_dict_policy(src_dc, src_area, src_zone, dst_dc, dst_area, dst_zone, service_sets_dict):

##########  Description  #######
########## End of description #####

    map_aci_ = host_to_type.area_to_eq_aci()

    mult = []

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

    if (same_zone_flag and same_area_flag):
        
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

    if ((not same_zone_flag) and same_area_flag and (re.match(dst_area, 'oss_aa'))):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'OSS_AA'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_oss_transit')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_oss_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_oss_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_src_oss_transit')

    if ((not same_zone_flag) and same_area_flag and (re.match(dst_area, 'internal_aa'))):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'INTERNAL_AA'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_inter_area')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_inter_area')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_inter_area')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_src_inter_area')

    if ((not same_zone_flag) and (re.match(src_area, 'oss_aa')) and (re.match(dst_area, 'int_aa'))):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'OSS_AA'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_inter_area')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_inter_area')
        mult.append({})
        mult[1]['eq_addr'] = 'panorama'
        mult[1]['eq_parameter'] = 'INTERNAL_AA'
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_inter_area')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy_src_inter_area')


    if ((not same_zone_flag) and (re.match(src_area, 'int_aa')) and (re.match(dst_area, 'oss_aa'))):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'panorama'
        mult[0]['eq_parameter'] = 'INTERNAL_AA'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_inter_area')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_inter_area')
        mult.append({})
        mult[1]['eq_addr'] = 'panorama'
        mult[1]['eq_parameter'] = 'OSS_AA'
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_inter_area')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy_src_inter_area')

    return (mult)

