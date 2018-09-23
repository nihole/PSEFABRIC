'''
This is essential element of the demultiplexer layes of Psefabric Dataflow Model and one of the key elements of the psefabric concept.
The python dictionaries created here are used in multiplexer.py.
The matter is that depending on the values of the structural elements (for networks in this realization) we have to program a specific set of commands for different MOs.
And we need some algorithm for that. So these dictionaries describe this logic.
We need to program logic for the adding/removal of addresses, address_sets, applications, application_sets, policies. So we have:
def mult_dict_address()
def mult_dict_address_set()
def mult_dict_application()
def mult_dict_application_set()
def mult_dict_policy()
'''

import re
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
    mult[('DC', 'no_vlan')][0]['eq_addr'] = 'OSS_AA'
    mult[('DC', 'no_vlan')][0]['cmd'] = {}
    mult[('DC', 'no_vlan')][0]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][0]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][0]['cmd']['ad'].append('ptemplates.pan_create_address')
    mult[('DC', 'no_vlan')][0]['cmd']['rm'].append('ptemplates.pan_delete_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][1]['eq_addr'] = 'OSS_INTERNET'
    mult[('DC', 'no_vlan')][1]['cmd'] = {}
    mult[('DC', 'no_vlan')][1]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][1]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][1]['cmd']['rm'].append('ptemplates.pan_delete_address')
    mult[('DC', 'no_vlan')][1]['cmd']['ad'].append('ptemplates.pan_create_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][2]['eq_addr'] = 'INTERNAL_AA'
    mult[('DC', 'no_vlan')][2]['cmd'] = {}
    mult[('DC', 'no_vlan')][2]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][2]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][2]['cmd']['rm'].append('ptemplates.pan_delete_address')
    mult[('DC', 'no_vlan')][2]['cmd']['ad'].append('ptemplates.pan_create_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][3]['eq_addr'] = 'EXTERNAL_AA'
    mult[('DC', 'no_vlan')][3]['cmd'] = {}
    mult[('DC', 'no_vlan')][3]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][3]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][3]['cmd']['rm'].append('ptemplates.pan_delete_address')
    mult[('DC', 'no_vlan')][3]['cmd']['ad'].append('ptemplates.pan_create_address')

    mult[('DC', 'no_vlan')].append({})
    mult[('DC', 'no_vlan')][4]['eq_addr'] = 'CORPO_INTERNET'
    mult[('DC', 'no_vlan')][4]['cmd'] = {}
    mult[('DC', 'no_vlan')][4]['cmd']['ad'] = []
    mult[('DC', 'no_vlan')][4]['cmd']['rm'] = []
    mult[('DC', 'no_vlan')][4]['cmd']['rm'].append('ptemplates.pan_delete_address')
    mult[('DC', 'no_vlan')][4]['cmd']['ad'].append('ptemplates.pan_create_address')

    return (mult)

def mult_dict_address_set():

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    mult.append({})
    mult[0]['eq_addr'] = 'OSS_AA'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[0]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    mult.append({})
    mult[1]['eq_addr'] = 'OSS_INTERNET'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[1]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    mult.append({})
    mult[2]['eq_addr'] = 'INTERNAL_AA'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[2]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    mult.append({})
    mult[3]['eq_addr'] = 'EXTERNAL_AA'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[3]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    mult.append({})
    mult[4]['eq_addr'] = 'CORPO_INTERNET'
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ptemplates.pan_delete_address_set')
    mult[4]['cmd']['ad'].append('ptemplates.pan_create_address_set')

    return (mult)

def mult_dict_application(): 

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = 'OSS_AA'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[0]['cmd']['ad'].append('ptemplates.pan_create_application')
    
    mult.append({}) 
    mult[1]['eq_addr'] = 'OSS_INTERNET'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[1]['cmd']['ad'].append('ptemplates.pan_create_application')

    mult.append({})
    mult[2]['eq_addr'] = 'INTERNAL_AA'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[2]['cmd']['ad'].append('ptemplates.pan_create_application')

    mult.append({})
    mult[3]['eq_addr'] = 'EXTERNAL_AA'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[3]['cmd']['ad'].append('ptemplates.pan_create_application')

    mult.append({})
    mult[4]['eq_addr'] = 'CORPO_INTERNET'
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ptemplates.pan_delete_application')
    mult[4]['cmd']['ad'].append('ptemplates.pan_create_application')

    return (mult)

def mult_dict_application_set():

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult=[]
    mult.append({})
    mult[0]['eq_addr'] = 'OSS_AA'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[0]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    mult.append({})
    mult[1]['eq_addr'] = 'OSS_INTERNET'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[1]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    mult.append({})
    mult[2]['eq_addr'] = 'INTERNAL_AA'
    mult[2]['cmd'] = {}
    mult[2]['cmd']['ad'] = []
    mult[2]['cmd']['rm'] = []
    mult[2]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[2]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    mult.append({})
    mult[3]['eq_addr'] = 'EXTERNAL_AA'
    mult[3]['cmd'] = {}
    mult[3]['cmd']['ad'] = []
    mult[3]['cmd']['rm'] = []
    mult[3]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[3]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    mult.append({})
    mult[4]['eq_addr'] = 'CORPO_INTERNET'
    mult[4]['cmd'] = {}
    mult[4]['cmd']['ad'] = []
    mult[4]['cmd']['rm'] = []
    mult[4]['cmd']['rm'].append('ptemplates.pan_delete_application_set')
    mult[4]['cmd']['ad'].append('ptemplates.pan_create_application_set')

    return (mult)

def mult_dict_policy(src_dc, src_vrf, src_area, src_zone, dst_dc, dst_vrf, dst_area, dst_zone):

##########  Description  #######

    if (re.match(src_dc, dst_dc)):
        same_dc_flag = True
    else:
        same_dc_flag = False

    if (re.match(src_vrf, dst_vrf)):
        same_vrf_flag = True
    else:
        same_vrf_flag = False

    if (re.match(src_area, dst_area)):
        same_area_flag = True
    else:
        same_area_flag = False

    if (re.match(src_zone, dst_zone)):
        same_zone_flag = True
    else:
        same_zone_flag = False

    if ((not same_vrf_flag) and same_area_flag and (re.match(dst_area, 'OSS_AA'))):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'OSS_AA'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_oss_transit')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_oss_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_oss_transit')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_src_oss_transit')

    if ((not same_vrf_flag) and same_area_flag and (re.match(dst_area, 'INTERNAL_AA'))):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'INTERNAL_AA'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_inter_area')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_inter_area')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_inter_area')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_src_inter_area')

    if ((not same_vrf_flag) and (re.match(src_area, 'OSS_AA')) and (re.match(dst_area, 'INTERNAL_AA'))):
        mult = []
        mult.append({})
        mult[0]['eq_addr'] = 'OSS_AA'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[0]['cmd']['rm'].append('ptemplates.pan_delete_policy_allapp_dst_inter_area')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[0]['cmd']['ad'].append('ptemplates.pan_create_policy_allapp_dst_inter_area')
        mult.append({})
        mult[1]['eq_addr'] = 'INTERNAL_AA'
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy')
        mult[1]['cmd']['rm'].append('ptemplates.pan_delete_policy_src_inter_area')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy')
        mult[1]['cmd']['ad'].append('ptemplates.pan_create_policy_src_inter_area')

    return mult
