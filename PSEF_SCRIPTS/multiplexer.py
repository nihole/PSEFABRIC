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


def policy_opt(cmd_for_host_full_):

    '''
    if we have some object removed and created we exclude it from the list (as for removed as for added lists):
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
                        address_rm_list = addresses_sets_list_rm[i]["address"]
                        address_add_list = addresses_sets_list_add[j]["address"]
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
                        service_rm_list = service_sets_list_rm[i]["service"]
                        service_add_list = service_sets_list_add[j]["service"]
                        m = set(service_rm_list) & set(service_add_list)
                        service_rm_list = list(set(service_rm_list) - m)
                        service_add_list = list(set(service_add_list) - m)
                        if not service_rm_list:
                            del service_sets_list_rm[i]
                            i = i - 1
                            break
                        else:
                            service_sets_list_rm[i]["service"] = service_rm_list
                        if not service_add_list:
                            del service_sets_list_add[j]
                            break
                        else:
                            service_sets_list_add[i]["service"] = service_add_list
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

#                        print "RMRMRMRMRMR VVVV\n%s\nSRCSRCSRCSRCAAAAA" % src_addr_set_list_rm
#                        print "ADADADADAAD  VVVV\n%s\nSRCSRCSRCSRCAAAAA" % src_addr_set_list_ad

                        m_src = set(src_address_set_list_ad) & set(src_address_set_list_rm)
                        if m_src:
                            for m in list(m_src):
                                l = 0
                                while l < len(src_addr_set_list_rm):
#                                    print "l = %s, m = %s, name = %s" % (l, m, src_addr_set_list_rm[l]["address-set-name"])
                                    if (m == src_addr_set_list_rm[l]["address-set-name"]):
                                        src_addr_set_list_rm.remove(src_addr_set_list_rm[l])
                                        break
                                    l = l + 1
                            for m in list(m_src):
                                l = 0
                                while l < len(src_addr_set_list_ad):
#                                    print "l = %s, m = %s, name = %s" % (l, m, src_addr_set_list_ad[l]["address-set-name"])
                                    if (m == src_addr_set_list_ad[l]["address-set-name"]):
                                        src_addr_set_list_ad.remove(src_addr_set_list_ad[l])
                                        break
                                    l = l + 1

                        m_dst = set(dst_address_set_list_ad) & set(dst_address_set_list_rm)
                        if m_dst:
                            for m in list(m_dst):
                                l = 0
                                while l < len(dst_addr_set_list_rm):
#                                    print "l = %s, m = %s, name = %s" % (l, m, dst_addr_set_list_rm[l]["address-set-name"])
                                    if (m == dst_addr_set_list_rm[l]["address-set-name"]):
                                        dst_addr_set_list_rm.remove(dst_addr_set_list_rm[l])
                                        break
                                    l = l + 1
                            for m in list(m_dst):
                                l = 0
                                while l < len(dst_addr_set_list_ad):
#                                    print "l = %s, m = %s, name = %s" % (l, m, dst_addr_set_list_ad[l]["address-set-name"])
                                    if (m == dst_addr_set_list_ad[l]["address-set-name"]):
                                        dst_addr_set_list_ad.remove(dst_addr_set_list_ad[l])
                                        break
                                    l = l + 1

                        # service-set in policy iptimization

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

                        # application-set in policy iptimization

                        app_set_list_rm = policies_list_rm[i]['application-sets']
                        app_set_list_ad = policies_list_add[j]['application-sets']

                        m_app = list(set(app_set_list_ad) & set(app_set_list_rm))

                        if m_app:
                            for m in m_app:
                                app_set_list_rm.remove(m)
                                app_set_list_ad.remove(m)


                        flag_ad = (policies_list_add[j]['source-address-sets'] or policies_list_add[j]['destination-address-sets'] or policies_list_add[j]["service-set-dicts"] or policies_list_add[j]['application-sets'] )
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
    service_set_lst = []
    for service_set_el in pol_['match']['service-sets']:
        service_set_list.append(service_set_el)
        service_set_lst.append(service_set_el['service-set-alias-1'])
####### all sorce or destination addresses/address-sets should be from the same dc,vrf,area,zone  ########
    for src_resolve_element in pol_['match']['source-address-sets']:
        src_address_set_list = pol_['match']['source-address-sets'][src_resolve_element]
        dst_address_set_list = []
        for dst_resolve_element in pol_['match']['destination-address-sets']: 
            dst_address_set_list = pol_['match']['destination-address-sets'][dst_resolve_element]
            src_zone_ = src_resolve_element[0]
            src_area_ = src_resolve_element[1]
            src_dc_ = src_address_set_list[0]['structure-to-addresses'][0]['structure']['dc']
            dst_zone_ = dst_resolve_element[0]
            dst_area_ = dst_resolve_element[1]
            dst_dc_ = dst_address_set_list[0]['structure-to-addresses'][0]['structure']['dc']
            
            message = '''
            VVVVVVVVVVVVVVVVV
            src_resolve_element: %s
            dst_resolve_element: %s
            src_dc: %s
            src_area: %s
            src_zone: %s
            dsr_dc: %s
            dst_area: %s
            dst_zone: %s
            AAAAAAAAAAAAAAAAAA
            '''  % (src_resolve_element, dst_resolve_element, src_dc_, src_area_, src_zone_, dst_dc_, dst_area_, dst_zone_) 


            policy_attributes = {}
            mult_dict_pol = psef_logic.mult_dict_policy(src_dc_, src_area_, src_zone_, dst_dc_, dst_area_, dst_zone_, pol_['match']['service-sets'])
            for cmd_element in mult_dict_pol:
                policy_attributes = {'eq':cmd_element['eq_addr'], 'eq_parameter':cmd_element['eq_parameter'], 'name':name_, "policy-alias-1":policy_alias_1, "policy-alias-2":policy_alias_2, 'source-address-sets':src_address_set_list, 'destination-address-sets':dst_address_set_list, 'application-sets':application_set_list, 'service-set-dicts':service_set_list, 'service-sets':service_set_lst, 'src_dc':src_dc_, 'src_area':src_area_, 'src_zone':src_zone_, 'dst_dc':src_dc_, 'dst_area':src_area_, 'dst_zone':dst_zone_, 'action':act }
                policy_attributes['command-list'] = cmd_element['cmd'][action_]
                cmd_for_host[cmd_element['eq_addr']][action_]['policy'].append(policy_attributes)


#    return cmd_for_host

def multiplex(diff_list):

##########  Description  #######
    '''
    '''
#############  BODY ############


#    policy_index_ = {'ad':[], 'rm':[]} 

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
    
#    if psef_debug.deb:   # if debuging is on then:
#            psef_debug.WriteDebug('policy_index', policy_index_)

#    return cmd_for_host



#cmd_for_host = {}
#initiate_cmd_for_host()

