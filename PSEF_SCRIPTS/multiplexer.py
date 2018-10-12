'''
This is a core part of Demultiplexer Layer of our Psefabric Dataflow Model.
The point is to create a list of commands for each MO in our infrastructure in accordance to the global logic described in psef_logic.

We need to create these lists for the next cases: address creation/removal, address-set creation/removal, service creation/removal,
service-set creation/removal, policy creation/removal. So we have:

cmd_list_address (action_, address_)
cmd_list_address_set (action_, address_set_)
cmd_list_service (action_, service_)
cmd_list_service_set (action_, service_set_)
cmd_list_policy (action_, pol_)

As a reult we have a dict {cmd_for_host}

'''

import re
import sys
import cfg
import copy
import psef_logic
import host_to_type
from psef_index import policy_index
import psef_debug

def initiate_cmd_for_host():

##########  Description  #######
    '''
    Create empty dict cmd_for_host[host_el_] for each MO in our infrastrucrure.
    '''
#############  BODY ############
    host_to_type_ = host_to_type.host_to_type()
    for host_el_ in host_to_type_:
            cmd_for_host[host_el_] = {}
            cmd_for_host[host_el_]['rm'] = {}
            cmd_for_host[host_el_]['ad'] = {}
            cmd_for_host[host_el_]['rm']['policy'] = []
            cmd_for_host[host_el_]['rm']['address-set'] = []
            cmd_for_host[host_el_]['rm']['address'] = []
            cmd_for_host[host_el_]['rm']['service-set'] = []
            cmd_for_host[host_el_]['rm']['service'] = []
            cmd_for_host[host_el_]['rm']['application-set'] = []
            cmd_for_host[host_el_]['rm']['application'] = []
            cmd_for_host[host_el_]['ad']['policy'] = []
            cmd_for_host[host_el_]['ad']['address-set'] = []
            cmd_for_host[host_el_]['ad']['address'] = []
            cmd_for_host[host_el_]['ad']['service-set'] = []
            cmd_for_host[host_el_]['ad']['service'] = []
            cmd_for_host[host_el_]['ad']['application-set'] = []
            cmd_for_host[host_el_]['ad']['application'] = []
    return cmd_for_host

def cmd_list_address (action_, address_):

##########  Description  #######
    '''
    '''
#############  BODY ############
 
    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")
    mult_dict_add = copy.deepcopy(psef_logic.mult_dict_address(address_['configure']))
 
    for cmd_element in mult_dict_add:
        address_attributes = {'eq':cmd_element['eq_addr'], 'eq_parameter':cmd_element['eq_parameter'], 'name':address_['address-name'], 'address-alias-1':address_['address-alias-1'], 'ipv4-prefix':address_['ipv4-prefix'], 'structure':address_['structure']}
        address_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['address'].append(address_attributes)
    return cmd_for_host


def cmd_list_address_set (action_, address_set_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    mult_dict_add_set = psef_logic.mult_dict_address_set(address_set_['configure'])

    for cmd_element in mult_dict_add_set:
        address_set_attributes = {'eq':cmd_element['eq_addr'], 'eq_parameter':cmd_element['eq_parameter'], 'name':address_set_['address-set-name'], 'address-set-alias-1':address_set_['address-set-alias-1'], 'address-set-alias-2':address_set_['address-set-alias-2'], 'address':address_set_['addresses']}
        address_set_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['address-set'].append(address_set_attributes)
    return cmd_for_host


def cmd_list_service (action_, service_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    mult_dict_app = psef_logic.mult_dict_service(service_['configure'])

    for cmd_element in mult_dict_app:
        service_attributes = {'eq':cmd_element['eq_addr'], 'eq_parameter':cmd_element['eq_parameter'], 'name':service_['service-name'], 'service-alias-1':service_['service-alias-1'], 'prot':service_['prot']}
        if 'ports' in service_:
            service_attributes['ports'] = service_['ports']
        service_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['service'].append(service_attributes)
    return cmd_for_host

def cmd_list_service_set (action_, service_set_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    mult_dict_add_set = psef_logic.mult_dict_service_set(service_set_['configure'])

    for cmd_element in mult_dict_add_set:
        service_set_attributes = {'eq':cmd_element['eq_addr'], 'eq_parameter':cmd_element['eq_parameter'], 'name':service_set_['service-set-name'], 'service-set-alias-1':service_set_['service-set-alias-1'], 'service-set-alias-2':service_set_['service-set-alias-2'], 'service':service_set_['services']}
        service_set_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['service-set'].append(service_set_attributes)
    return cmd_for_host


def cmd_list_applciation (action_, applciation_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    mult_dict_app = psef_logic.mult_dict_applciation(application_['configure'])

    for cmd_element in mult_dict_app:
        applciation_attributes = {'eq':cmd_element['eq_addr'], 'eq_parameter':cmd_element['eq_parameter'], 'name':applciation_['applciation-name'], 'prot':applciation_['prot']}
        if 'ports' in applciation_:
            applciation_attributes['ports'] = applciation_['ports']
        applciation_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['applciation'].append(applciation_attributes)
    return cmd_for_host


def cmd_list_application_set (action_, application_set_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    mult_dict_add_set = psef_logic.mult_dict_application_set(application_set_['configure'])

    for cmd_element in mult_dict_add_set:
        application_set_attributes = {'eq':cmd_element['eq_addr'], 'eq_parameter':cmd_element['eq_parameter'], 'name':application_set_['application-set-name'], 'application':application_set_['applications']}
        application_set_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['application-set'].append(application_set_attributes)
    return cmd_for_host



def cmd_list_policy (action_, pol_):

##########  Description  #######
    '''
    '''
#############  BODY ############
    
    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")
#    mult_dict_pol = psef_logic.mult_dict_policy()
    src_address_set_list = []
    name_ = pol_['policy-name']
    policy_alias_1 = pol_['policy-alias-1']
    policy_alias_2 = pol_['policy-alias-2']
#    service_set_list = pol_['match']['service-sets'] 
    application_set_list = pol_['match']['application-sets']
    act = 'permit'
    service_set_list = []
    for service_set_el in pol_['match']['service-sets']:
        service_set_list.append(service_set_el['service-set-alias-1'])

####### all sorce or destination addresses/address-sets should be from the same dc,vrf,area,zone  ########
    for src_resolve_element in pol_['match']['source-addresses']:
        src_address_set_list = pol_['match']['source-addresses'][src_resolve_element]
        dst_address_set_list = []
        for dst_resolve_element in pol_['match']['destination-addresses']: 
            dst_address_set_list = pol_['match']['destination-addresses'][dst_resolve_element]
            src_zone_ = src_resolve_element[0]
            src_area_ = src_resolve_element[1]
            src_dc_ = src_address_set_list[0]['structure-to-addresses'][0]['structure']['dc']
            dst_zone_ = dst_resolve_element[0]
            dst_area_ = dst_resolve_element[1]
            dst_dc_ = dst_address_set_list[0]['structure-to-addresses'][0]['structure']['dc']
            
            message = '''
            VVVVVVVVVVVVVVVVV
            src_dc: %s
            src_area: %s
            src_zone: %s
            dsr_dc: %s
            dst_area: %s
            dst_zone: %s
            AAAAAAAAAAAAAAAAAA
            '''  % (src_dc_, src_area_, src_zone_, dst_dc_, dst_area_, dst_zone_) 

#            print message

            policy_attributes = {}
            mult_dict_pol = psef_logic.mult_dict_policy(src_dc_, src_area_, src_zone_, dst_dc_, dst_area_, dst_zone_, pol_['match']['service-sets'])
            for cmd_element in mult_dict_pol:
                policy_attributes = {'eq':cmd_element['eq_addr'], 'eq_parameter':cmd_element['eq_parameter'], 'name':name_, "policy-alias-1":policy_alias_1, "policy-alias-2":policy_alias_2, 'source-addresses':src_address_set_list, 'destination-addresses':dst_address_set_list, 'applications':application_set_list, 'services':service_set_list, 'src_dc':src_dc_, 'src_area':src_area_, 'src_zone':src_zone_, 'dst_dc':src_dc_, 'dst_area':src_area_, 'dst_zone':dst_zone_, 'action':act }
                policy_attributes['command-list'] = cmd_element['cmd'][action_]
                cmd_for_host[cmd_element['eq_addr']][action_]['policy'].append(policy_attributes)


    return cmd_for_host

def multiplex(diff_list):

##########  Description  #######
    '''
    '''
#############  BODY ############

    policy_index_ = {'ad':[], 'rm':[]} 

    for policy_rm_element in diff_list['policies_rm']:
        pol_index_rm = policy_index(policy_rm_element, 'rm')
        policy_index_['rm'].append(pol_index_rm)
        cmd_list_policy ('rm', pol_index_rm )
    for policy_ad_element in diff_list['policies_ad']:
        pol_index_ad = policy_index(policy_ad_element, 'ad')
        policy_index_['ad'].append(pol_index_ad)
        cmd_list_policy ('ad', pol_index_ad)
    for address_set_rm_element in diff_list['address_sets_rm']:
        cmd_list_address_set ('rm', address_set_rm_element)
    for address_rm_element in diff_list['addresses_rm']:
        cmd_list_address ('rm', address_rm_element)
    for address_ad_element in diff_list['addresses_ad']:
        cmd_list_address ('ad', address_ad_element)
    for address_set_ad_element in diff_list['address_sets_ad']:
        cmd_list_address_set ('ad', address_set_ad_element)

    for service_set_rm_element in diff_list['service_sets_rm']:
        cmd_list_service_set ('rm', service_set_rm_element)
    for service_rm_element in diff_list['services_rm']:
        cmd_list_service ('rm', service_rm_element)
    for service_ad_element in diff_list['services_ad']:
        cmd_list_service ('ad', service_ad_element)
    for service_set_ad_element in diff_list['service_sets_ad']:
        cmd_list_service_set ('ad', service_set_ad_element)
    
    for application_set_rm_element in diff_list['application_sets_rm']:
        cmd_list_application_set ('rm', application_set_rm_element)
    for application_rm_element in diff_list['applications_rm']:
        None
#        cmd_list_application ('rm', application_rm_element)
    for application_ad_element in diff_list['applications_ad']:
        None
#        cmd_list_application ('ad', application_ad_element)
    for application_set_ad_element in diff_list['application_sets_ad']:
        cmd_list_application_set ('ad', application_set_ad_element)
    
    if psef_debug.deb:   # if debuging is on then:
            psef_debug.WriteDebug('policy_index', policy_index_)

    return cmd_for_host

cmd_for_host = {}
cmd_for_host = initiate_cmd_for_host()  

