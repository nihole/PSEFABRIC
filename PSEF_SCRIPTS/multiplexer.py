
    ######################################
    #                                    #
    #                 3.                 #
    #         demultiplexing layer       #
    #                                    #
    ######################################


'''
This is a core part of Demultiplexer Layer of our Psefabric Dataflow Model.
The goal is to create a list of configuration commands for each MO.

We need to create these lists for the next cases: address creation/removal, address-set creation/removal, service creation/removal,
service-set creation/removal, application creation/removal, application-set creation/removal, policy creation/removal. So we have:

cmd_list_address (action_, address_)
cmd_list_address_set (action_, address_set_)
cmd_list_service (action_, service_)
cmd_list_service_set (action_, service_set_)
cmd_list_application (action_, application_)
cmd_list_application_set (action_, application_set_)
cmd_list_policy (action_, pol_)

Two dictionaries are initiated from psefabric.py module:
    cmd_for_host
    policy_index_
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
    This function:
    - extracts all necessary parameters (only 'configure' in our case)
    - transmit them to psef_logic and get a dict with MOs as keys and a lists of configuration commands as values
    - add information related to addresses configuration to a new dict (cmd_for_host)
    '''

#############  BODY ############
 
    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    # Change the list of parameters and structure elements if needed 
    mult_dict_add = copy.deepcopy(psef_logic.mult_dict_address(address_['structure']))
 
    for cmd_element in mult_dict_add:
        address_attributes = {}
        address_attributes['eq'] = cmd_element['eq_addr']
        address_attributes['eq_parameter'] = cmd_element['eq_parameter']
        address_attributes['name'] = address_['address-name']
        address_attributes['ipv4-prefix'] = address_['ipv4-prefix']
        address_attributes['structure'] = address_['structure']
        address_attributes['parameters'] = address_['parameters']

        address_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['address'].append(address_attributes)


def cmd_list_address_set (action_, address_set_):

##########  Description  #######
    '''
    This function:
    - extracts all necessary parameters (only 'configure' in our case)
    - transmit them to psef_logic and get a dict with MOs as keys and a lists of configuration commands as values
    - add information related to address-sets configuration to a new dict (cmd_for_host)
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    # Change the list of parameters if needed 
    # If structure elemets are needed address_set index_new/old should be used
    mult_dict_add_set = psef_logic.mult_dict_address_set()
    address_list = []
    j = 0
    for address_dict_el in address_set_['addresses']:
        # Change it if you want to use different name (not a psefabric's name)
        address_list.append(address_set_['addresses'][j]["address-name"])
        j = j + 1
    for cmd_element in mult_dict_add_set:
        address_set_attributes = {}
        address_set_attributes['eq'] = cmd_element['eq_addr']
        address_set_attributes['eq_parameter'] = cmd_element['eq_parameter']
        address_set_attributes['name'] = address_set_['address-set-name']
        address_set_attributes['address-list'] = address_list
        address_set_attributes['parameters'] = address_set_['parameters']

        address_set_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['address-set'].append(address_set_attributes)


def cmd_list_service (action_, service_):

##########  Description  #######
    '''
    This function:
    - extracts all necessary parameters (only 'configure' in our case)
    - transmit them to psef_logic and get a dict with MOs as keys and a lists of configuration commands as values
    - add information related to services configuration to a new dict (cmd_for_host)
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    # Add the list of parameters if needed 
    mult_dict_app = psef_logic.mult_dict_service()

    for cmd_element in mult_dict_app:
        service_attributes = {}
        service_attributes['eq'] = cmd_element['eq_addr']
        service_attributes['eq_parameter'] = cmd_element['eq_parameter']
        service_attributes['name'] = service_['service-name']
        service_attributes['prot'] = service_['prot']
        service_attributes['parameters'] = service_['parameters']

        if 'ports' in service_:
            service_attributes['ports'] = service_['ports']
        service_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['service'].append(service_attributes)

def cmd_list_service_set (action_, service_set_):

##########  Description  #######
    '''
    This function:
    - extracts all necessary parameters (only 'configure' in our case)
    - transmit them to psef_logic and get a dict with MOs as keys and a lists of configuration commands as values
    - add information related to service-sets configuration to a new dict (cmd_for_host)
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")


    # Add the list of parameters if needed 
    mult_dict_add_set = psef_logic.mult_dict_service_set()
    service_list = []
    j = 0
    for service_dict_el in service_set_['services']:
        # Change it if you want to use different name (not a psefabric's name)
        service_list.append(service_dict_el["service-name"])
        j = j + 1
    for cmd_element in mult_dict_add_set:
        service_set_attributes = {}
        service_set_attributes['eq'] = cmd_element['eq_addr']
        service_set_attributes['eq_parameter'] = cmd_element['eq_parameter']
        service_set_attributes['name'] = service_set_['service-set-name']
        service_set_attributes['service-list'] = service_list
        service_set_attributes['parameters'] = service_set_['parameters']

        service_set_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['service-set'].append(service_set_attributes)


def cmd_list_applciation (action_, applciation_):

##########  Description  #######
    '''
    This function:
    - extracts all necessary parameters (only 'configure' in our case)
    - transmit them to psef_logic and get a dict with MOs as keys and a lists of configuration commands as values
    - add information related to application configuration to a new dict (cmd_for_host)
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    # Change the list of parameters if needed 
    mult_dict_app = psef_logic.mult_dict_applciation(application_['app_par_1'], application_['app_par_2'])

    for cmd_element in mult_dict_app:
        applciation_attributes = {}
        application_attributes['eq'] = cmd_element['eq_addr']
        application_attributes['eq_parameter'] = cmd_element['eq_parameter']
        application_attributes['name'] = application_['application-name']
        application_attributes['parameters'] = application_['parameters']

        applciation_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['applciation'].append(applciation_attributes)


def cmd_list_application_set (action_, application_set_):

##########  Description  #######
    '''
    This function:
    - extracts all necessary parameters (only 'configure' in our case)
    - transmit them to psef_logic and get a dict with MOs as keys and a lists of configuration commands as values
    - add information related to application-sets configuration to a new dict (cmd_for_host)
    '''
#############  BODY ############

    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

    # Change the list of parameters if needed 
    mult_dict_add_set = psef_logic.mult_dict_application_set()
 
    application_list = []

    for application_dict_el in application_set_['applications']:
        # Change it if you want to use different name (not a psefabric's name)
        application_list.append(application_dict_el["application-name"])
    for cmd_element in mult_dict_add_set:
        application_set_attributes = {}
        application_set_attributes['eq'] = cmd_element['eq_addr']
        application_set_attributes['eq_parameter'] = cmd_element['eq_parameter']
        application_set_attributes['name'] = application_set_['application-set-name']
        application_set_attributes['application-list'] = application_list
        application_set_attributes['parameters'] = application_set_['parameters']

        application_set_attributes['command-list'] = cmd_element['cmd'][action_]
        cmd_for_host[cmd_element['eq_addr']][action_]['application-set'].append(application_set_attributes)



def cmd_list_policy (action_, pol_):

##########  Description  #######
    '''
    This function:
    - extracts all necessary parameters
    - transmit them to psef_logic and get a dict with MOs as keys and a lists of configuration commands as values
    - add information related to policy configuration to a new dict (cmd_for_host)
    '''
#############  BODY ############

    
    if not (re.match(action_, 'rm') or re.match(action_, 'ad')):
        sys.exit("Incorrect action!!")

### Extract parameters ############


    src_address_set_list = []
    name_ = pol_['policy-name']

    application_set_list = pol_['match']['application-sets']
    act = 'permit'
    service_set_list = []
    service_set_lst = []
    for service_set_el in pol_['match']['service-sets']:
        service_set_list.append(service_set_el)
        service_set_lst.append(service_set_el['service-set-name'])

    for src_resolve_element in pol_['match']['source-address-sets']:
        src_address_set_list = pol_['match']['source-address-sets'][src_resolve_element]
        dst_address_set_list = []
        for dst_resolve_element in pol_['match']['destination-address-sets']: 
            dst_address_set_list = pol_['match']['destination-address-sets'][dst_resolve_element]
            src_str_1 = src_resolve_element[0]
            src_str_2 = src_resolve_element[1]
            src_str_3 = src_resolve_element[2]
            src_str_4 = src_resolve_element[3]
            dst_str_1 = dst_resolve_element[0]
            dst_str_2 = dst_resolve_element[1]
            dst_str_3 = dst_resolve_element[2]
            dst_str_4 = dst_resolve_element[3]
            
            policy_attributes = {}

            ### get a dict with MOs as keys and a lists of configuration commands as values ####
            mult_dict_pol = psef_logic.mult_dict_policy(list(src_resolve_element), list(dst_resolve_element), pol_['match']['service-sets'])
            
            ### add information related to policy configuration to a new dict (cmd_for_host) ###
            for cmd_element in mult_dict_pol:
                policy_attributes = {}
                policy_attributes['eq'] = cmd_element['eq_addr']
                policy_attributes['eq_parameter'] = cmd_element['eq_parameter']
                policy_attributes['name'] = name_
                policy_attributes['source-address-sets'] = src_address_set_list
                policy_attributes['destination-address-sets'] = dst_address_set_list
                policy_attributes['application-sets'] = application_set_list
                policy_attributes['service-set-dicts'] = service_set_list
                policy_attributes['service-sets'] = service_set_lst
                policy_attributes['src_str'] = list(src_resolve_element)
                policy_attributes['dst_str'] = list(dst_resolve_element)
                policy_attributes['parameters'] = pol_['parameters']

                policy_attributes['command-list'] = cmd_element['cmd'][action_]
                cmd_for_host[cmd_element['eq_addr']][action_]['policy'].append(policy_attributes)


def multiplex(diff_list):

##########  Description  #######
    '''
    '''
#############  BODY ############


#    policy_index_ = {'ad':[], 'rm':[]} 

    for policy_rm_element in diff_list['policies_rm']:
        pol_index_rm = policy_index(policy_rm_element, 'rm')
        policy_index_['rm'].append(pol_index_rm)
        policy_attributes = cmd_list_policy ('rm', pol_index_rm )

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
            psef_debug.WriteDebug('policy_index_full', policy_index_)

    return cmd_for_host


def policy_opt(cmd_for_host_full_):

    '''
    Changing of an object is realiased as two operations: remove & creation in the cmd_for_host dict. It means that this changing object is persent in both lists (as creation as deleting).
    The purpose of this function is to exclude such objects from the both lists.
    New dictionary (cmd_for_host_diff) will be used together with the old one (cmd_for_host_full) in configuration decision process.
    We have to take into account the next objects:

    addresses
    address-sets
    services
    service-sets
    applications
    application-sets
    address-sets in policy
    service-sets in policy
    application-sets in policy
    '''

    cmd_for_host_ = {}
    cmd_for_host_ = copy.deepcopy(cmd_for_host_full_)

    for eq_el in cmd_for_host_:

    # addresses optimization

        addresses_list_rm = cmd_for_host_[eq_el]["rm"]["address"]
        addresses_list_add = cmd_for_host_[eq_el]["ad"]["address"]

        if (bool(addresses_list_rm) and bool(addresses_list_add)):
            i = 0
            while i < len(addresses_list_rm):
                j = 0
                while j < len(addresses_list_add):
                    if (addresses_list_rm[i]["name"] == addresses_list_add[j]["name"]):
                        del addresses_list_rm[i]
                        del addresses_list_add[j]
                        i = i - 1
                        break
                    j = j + 1
                i = i + 1

    # services optimization

        services_list_rm = cmd_for_host_[eq_el]["rm"]["service"]
        services_list_add = cmd_for_host_[eq_el]["ad"]["service"]

        if (bool(services_list_rm) and bool(services_list_rm)):
            i = 0
            while i < len(services_list_rm):
                j = 0
                while j < len(services_list_add):
                    if (services_list_rm[i]["name"] == services_list_add[j]["name"]):
                        del services_list_rm[i]
                        del services_list_add[j]
                        i = i - 1
                        break
                    j = j + 1
                i = i + 1

    # address-set optimization

        addresses_sets_list_rm = cmd_for_host_[eq_el]["rm"]["address-set"]
        addresses_sets_list_add = cmd_for_host_[eq_el]["ad"]["address-set"]


        if (bool(addresses_sets_list_rm) and bool(addresses_sets_list_add)):
            i = 0
            while i < len(addresses_sets_list_rm):
                j = 0
                while j < len(addresses_sets_list_add):
                    if (addresses_sets_list_rm[i]["name"] == addresses_sets_list_add[j]["name"]):
                        address_rm_list = addresses_sets_list_rm[i]["address-list"]
                        address_add_list = addresses_sets_list_add[j]["address-list"]
                        m = set(address_rm_list) & set(address_add_list)
                        address_rm_list = list(set(address_rm_list) - m)
                        address_add_list = list(set(address_add_list) - m)
                        if not address_rm_list:
                            del addresses_sets_list_rm[i]
                            i = i - 1
                            break
                        else:
                            addresses_sets_list_rm[i]["address"] = address_rm_list
                        if not address_add_list:
                            del addresses_sets_list_add[j]
                            break
                        else:
                            addresses_sets_list_add[j]["address"] = address_add_list
                        break
                    j = j + 1
                i = i + 1

    # service-set optimization

        service_sets_list_rm = cmd_for_host_[eq_el]["rm"]["service-set"]
        service_sets_list_add = cmd_for_host_[eq_el]["ad"]["service-set"]

        if (bool(service_sets_list_rm) and bool(service_sets_list_add)):
            i = 0
            while i < len(service_sets_list_rm):
                j = 0
                while j < len(service_sets_list_add):
                    if (service_sets_list_rm[i]["name"] == service_sets_list_add[j]["name"]):
                        service_rm_list = service_sets_list_rm[i]["service-list"]
                        service_add_list = service_sets_list_add[j]["service-list"]
                        m = set(service_rm_list) & set(service_add_list)
                        service_rm_list = list(set(service_rm_list) - m)
                        service_add_list = list(set(service_add_list) - m)
                        if not service_rm_list:
                            del service_sets_list_rm[i]
                            i = i - 1
                            break
                        else:
                            service_sets_list_rm[i]["service-list"] = service_rm_list
                        if not service_add_list:
                            del service_sets_list_add[j]
                            break
                        else:
                            service_sets_list_add[i]["service-list"] = service_add_list
                        break
                    j = j + 1
                i = i + 1

    # application-set optimization

        application_sets_list_rm = cmd_for_host_[eq_el]["rm"]["application-set"]
        application_sets_list_add = cmd_for_host_[eq_el]["ad"]["application-set"]

        if (bool(application_sets_list_rm) and bool(application_sets_list_add)):
            i = 0
            while i < len(application_sets_list_rm):
                j = 0
                while j < len(application_sets_list_add):
                    if (application_sets_list_rm[i]["name"] == application_sets_list_add[j]["name"]):
                        application_rm_list = application_sets_list_rm[i]["application"]
                        application_add_list = application_sets_list_add[j]["application"]
                        m = set(application_rm_list) & set(application_add_list)
                        application_rm_list = list(set(application_rm_list) - m)
                        application_add_list = list(set(application_add_list) - m)
                        if not application_rm_list:
                            del application_sets_list_rm[i]
                            i = i - 1
                            break
                        else:
                            application_sets_list_rm[i]["applications"] = application_rm_list
                        if not application_add_list:
                            del application_sets_list_add[j]
                            break
                        else:
                            application_sets_list_add[i]["applications"] = application_add_list
                        break
                    j = j + 1
                i = i + 1

    # policy optimization
        policies_list_add = cmd_for_host_[eq_el]["ad"]["policy"]
        policies_list_rm = cmd_for_host_[eq_el]["rm"]["policy"]

        if (policies_list_add and policies_list_rm):
            i = 0
            while i < len(policies_list_rm):
                j = 0
                while j < len(policies_list_add):
                    if (policies_list_rm[i]["name"] == policies_list_add[j]["name"]):
                    # address-sets in policy optimization

                        src_address_set_list_rm = []
                        src_address_set_list_ad = []
                        dst_address_set_list_rm = []
                        dst_address_set_list_ad = []

                        src_addr_set_list_rm = policies_list_rm[i]['source-address-sets']
                        src_addr_set_list_ad = policies_list_add[j]['source-address-sets']
                        dst_addr_set_list_rm = policies_list_rm[i]['destination-address-sets']
                        dst_addr_set_list_ad = policies_list_add[j]['destination-address-sets']

                        for src_addr_set_dict_rm in src_addr_set_list_rm:
                            src_address_set_list_rm.append(src_addr_set_dict_rm["address-set-name"])

                        for src_addr_set_dict_ad in src_addr_set_list_ad:
                            src_address_set_list_ad.append(src_addr_set_dict_ad["address-set-name"])

                        for dst_addr_set_dict_rm in dst_addr_set_list_rm:
                            dst_address_set_list_rm.append(dst_addr_set_dict_rm["address-set-name"])

                        for dst_addr_set_dict_ad in dst_addr_set_list_ad:
                            dst_address_set_list_ad.append(dst_addr_set_dict_ad["address-set-name"])


                        m_src = set(src_address_set_list_ad) & set(src_address_set_list_rm)
                        if m_src:
                            for m in list(m_src):
                                l = 0
                                while l < len(src_addr_set_list_rm):
                                    if (m == src_addr_set_list_rm[l]["address-set-name"]):
                                        src_addr_set_list_rm.remove(src_addr_set_list_rm[l])
                                        break
                                    l = l + 1
                            for m in list(m_src):
                                l = 0
                                while l < len(src_addr_set_list_ad):
                                    if (m == src_addr_set_list_ad[l]["address-set-name"]):
                                        src_addr_set_list_ad.remove(src_addr_set_list_ad[l])
                                        break
                                    l = l + 1

                        m_dst = set(dst_address_set_list_ad) & set(dst_address_set_list_rm)
                        if m_dst:
                            for m in list(m_dst):
                                l = 0
                                while l < len(dst_addr_set_list_rm):
                                    if (m == dst_addr_set_list_rm[l]["address-set-name"]):
                                        dst_addr_set_list_rm.remove(dst_addr_set_list_rm[l])
                                        break
                                    l = l + 1
                            for m in list(m_dst):
                                l = 0
                                while l < len(dst_addr_set_list_ad):
                                    if (m == dst_addr_set_list_ad[l]["address-set-name"]):
                                        dst_addr_set_list_ad.remove(dst_addr_set_list_ad[l])
                                        break
                                    l = l + 1

                        # service-set in policy optimization

                        service_set_list_rm = []
                        service_set_list_ad = []

                        svc_set_list_rm = policies_list_rm[i]["service-set-dicts"]
                        svc_set_list_ad = policies_list_add[j]["service-set-dicts"]

                        for svc_set_dict_rm in svc_set_list_rm:
                            service_set_list_rm.append(svc_set_dict_rm["service-set-name"])

                        for svc_set_dict_ad in svc_set_list_ad:
                            service_set_list_ad.append(svc_set_dict_ad["service-set-name"])

                        m_svc = list(set(service_set_list_ad) & set(service_set_list_rm))
                        if m_svc:
                            j = 0
                            while j < len(svc_set_list_rm):
                                service_set_dict_rm = svc_set_list_rm[j]
                                for m in m_svc:
                                    if (m == service_set_dict_rm["service-set-name"]):
                                        svc_set_list_rm.remove(service_set_dict_rm)
                                        j = j - 1
                                        break
                                j = j + 1
                            j = 0
                            while j < len(svc_set_list_ad):
                                service_set_dict_ad = svc_set_list_ad[j]
                                for m in m_svc:
                                    if (m == service_set_dict_ad["service-set-name"]):
                                        svc_set_list_ad.remove(service_set_dict_ad)
                                        j = j - 1
                                        break
                                j = j + 1

                        # application-set in policy optimization

                        app_set_list_rm = policies_list_rm[i]['application-sets']
                        app_set_list_ad = policies_list_add[j]['application-sets']

                        m_app = list(set(app_set_list_ad) & set(app_set_list_rm))

                        if m_app:
                            for m in m_app:
                                app_set_list_rm.remove(m)
                                app_set_list_ad.remove(m)


                        flag_ad = (policies_list_add[j]['source-address-sets'] or policies_list_add[j]['destination-address-sets'] or policies_list_add[j]["service-set-dicts"] or  policies_list_add[j]['application-sets'] )
                        if not flag_ad:
                            del policies_list_add[j]
                            j = j - 1
                    j = j + 1

                flag_rm = (policies_list_rm[i]['source-address-sets'] or policies_list_rm[i]['destination-address-sets'] or policies_list_rm[i]["service-set-dicts"] or policies_list_rm[i]['application-sets'] )
                if not flag_rm:
                    del policies_list_rm[i]
                    i = i - 1
                i = i + 1
    return (cmd_for_host_)




