'''
dict_correct() 
takes configuration dictionary and corrects some elements in it

ddiff_dict()
takes the difference between new and old psefabric configurations (type dict) and transforms it to the dict convenient for further operations
'''

import re
import copy
from deepdiff import DeepDiff

def dict_correct(psef_conf_):

##########  Description  #######
    '''
    In case when we expect a list of child elements in xml file (new or old psefabric configuration) but we have only one element, xmltodict interprets this element as a single 
    variable (not a list). 
    So we want to change the type of this variable to list type. 
    '''
#############  BODY ############
 
    if 'addresses' in psef_conf_['data']:   
        if not isinstance (psef_conf_['data']['addresses'],list):
            address_element_ = psef_conf_['data']['addresses']
            psef_conf_['data']['addresses'] = []
            psef_conf_['data']['addresses'].append(address_element)
    if 'address-sets' in psef_conf_['data']:
        if not isinstance (psef_conf_['data']['address-sets'],list):
            address_set_element = psef_conf_['data']['address-sets']
            psef_conf_['data']['address-sets'] = []
            psef_conf_['data']['address-sets'].append(address_set_element)
        for n, address_set_el in enumerate(psef_conf_['data']['address-sets']):
            if not isinstance (address_set_el['addresses'],list):
                address_el_list = address_set_el['addresses']
                psef_conf_['data']['address-sets'][n]['addresses'] = []
                psef_conf_['data']['address-sets'][n]['addresses'].append(address_el_list)
    if 'services' in psef_conf_['data']:
        if not isinstance (psef_conf_['data']['services'],list):
            service_element = psef_conf_['data']['services']
            psef_conf_['data']['services'] = []
            psef_conf_['data']['services'].append(service_element)
    if 'service-sets' in psef_conf_['data']:
        if not isinstance (psef_conf_['data']['service-sets'],list):
            service_set_element = psef_conf_['data']['service-sets']
            psef_conf_['data']['service-sets'] = []
            psef_conf_['data']['service-sets'].append(service_set_element)
        for i, services_set_el in enumerate(psef_conf_['data']['service-sets']):
            if not isinstance (services_set_el['services'],list):
                service_el_list = services_set_el['services']
                psef_conf_['data']['service-sets'][i]['services'] = []
                psef_conf_['data']['service-sets'][i]['services'].append(service_el_list)
    if 'applications' in psef_conf_['data']:
        if not isinstance (psef_conf_['data']['applications'],list):
            application_element = psef_conf_['data']['applications']
            psef_conf_['data']['applications'] = []
            psef_conf_['data']['applications'].append(application_element)
    if 'application-sets' in psef_conf_['data']:
        if not isinstance (psef_conf_['data']['application-sets'],list):
            application_set_element = psef_conf_['data']['application-sets']
            psef_conf_['data']['application-sets'] = []
            psef_conf_['data']['application-sets'].append(application_set_element)
        for i, applications_set_el in enumerate(psef_conf_['data']['application-sets']):
            if not isinstance (applications_set_el['applications'],list):
                application_el_list = applications_set_el['applications']
                psef_conf_['data']['application-sets'][i]['applications'] = []
                psef_conf_['data']['application-sets'][i]['applications'].append(application_el_list)

    if ('policies' in psef_conf_['data']):
        if not isinstance (psef_conf_['data']['policies'],list):
            policy_element = psef_conf_['data']['policies']
            psef_conf_['data']['policies'] = []
            psef_conf_['data']['policies'].append(policy_element)
        for policy_element_ in psef_conf_['data']['policies']:
            if 'source-address-sets' in policy_element_['match']:
                if not isinstance (policy_element_['match']['source-address-sets'],list):
                    source_addresses_set_element_ = policy_element_['match']['source-address-sets']
		    policy_element_['match']['source-address-sets']=[]
                    policy_element_['match']['source-address-sets'].append(source_addresses_set_element_)
            if 'destination-address-sets' in policy_element_['match']:
                if not isinstance (policy_element_['match']['destination-address-sets'],list):
                    destination_addresses_set_element_ = policy_element_['match']['destination-address-sets']
                    policy_element_['match']['destination-address-sets']=[]
                    policy_element_['match']['destination-address-sets'].append(destination_addresses_set_element_)
            if 'service-sets' in policy_element_['match']:
                if not isinstance (policy_element_['match']['service-sets'],list):
                    service_set_element_ = policy_element_['match']['service-sets']
                    policy_element_['match']['service-sets'] = []
                    policy_element_['match']['service-sets'].append(service_set_element_)
            if 'application-sets' in policy_element_['match']:
                if not isinstance (policy_element_['match']['application-sets'],list):
                    application_set_element_ = policy_element_['match']['application-sets']
                    policy_element_['match']['application-sets'] = []
                    policy_element_['match']['application-sets'].append(application_set_element_)
       
    return psef_conf_

def ddiff_dict(ddiff_):

##########  Description  #######
    '''
 takes the difference between new and old psefabric configurations (type dict) and transforms it to the dict convenient for further operations
   '''
#############  BODY ############

    diff_dict_ = {}
    regex_addr = "\['data'\]\['addresses'\]"
    regex_svc = "\['data'\]\['services'\]"
    regex_app = "\['data'\]\['applications'\]"
    regex_addr_set = "\['data'\]\['address-sets'\]"
    regex_svc_set = "\['data'\]\['service-sets'\]"
    regex_app_set = "\['data'\]\['application-sets'\]"
    regex_policies = "\['data'\]\['policies'\]"
#    regex_policies_policy = "\['data'\]\['policies'\]\['policy'\]"
    addresses_rm = []
    address_sets_rm = []
    addresses_ad = []
    address_sets_ad = []
    services_rm = []
    service_sets_rm = []
    services_ad = []
    service_sets_ad = []

    applications_rm = []
    application_sets_rm = []
    applications_ad = []
    application_sets_ad = []

    policies_rm = []
    policies_ad = []

    for key in ddiff_:
        if (re.search(r'item_removed', key)):
            for key_rm in ddiff_[key]:
                if (re.search(regex_addr, key_rm)):
                    if not isinstance (ddiff_[key][key_rm],list):
                        addresses_rm.append(ddiff_[key][key_rm])
                    else:
                        addresses_rm = ddiff_[key][key_rm]
                if (re.search(regex_addr_set, key_rm)):
                    if not isinstance (ddiff_[key][key_rm],list):
                        address_sets_rm.append(ddiff_[key][key_rm])
                    else:
                        address_sets_rm = ddiff_[key][key_rm]

                if (re.search(regex_svc, key_rm)):
                    if not isinstance (ddiff_[key][key_rm],list):
                        services_rm.append(ddiff_[key][key_rm])
                    else:
                        services_rm = ddiff_[key][key_rm]
                if (re.search(regex_svc_set, key_rm)):
                    if not isinstance (ddiff_[key][key_rm],list):
                        service_sets_rm.append(ddiff_[key][key_rm])
                    else:
                        service_sets_rm = ddiff_[key][key_rm]

                if (re.search(regex_app, key_rm)):
                    if not isinstance (ddiff_[key][key_rm],list):
                        applications_rm.append(ddiff_[key][key_rm])
                    else:
                        applications_rm = ddiff_[key][key_rm]
                if (re.search(regex_app_set, key_rm)):
                    if not isinstance (ddiff_[key][key_rm],list):
                        application_sets_rm.append(ddiff_[key][key_rm])
                    else:
                        application_sets_rm = ddiff_[key][key_rm]
                
                
                if (re.search(regex_policies, key_rm)):
                    if not isinstance (ddiff_[key][key_rm],list):
                        policies_rm.append(ddiff_[key][key_rm])
                    else:
                        policies_rm = ddiff_[key][key_rm]
        if (re.search(r'item_added', key)):
            for key_ad in ddiff_[key]:
                if (re.search(regex_addr, key_ad)):
                    if not isinstance (ddiff_[key][key_ad],list):
                        addresses_ad.append(ddiff_[key][key_ad])
                    else: 
                        addresses_ad = ddiff_[key][key_ad]
                if (re.search(regex_addr_set, key_ad)):
                    if not isinstance (ddiff_[key][key_ad],list):
                        address_sets_ad.append(ddiff_[key][key_ad])
                    else:
                        address_sets_ad = ddiff_[key][key_ad]

                if (re.search(regex_svc, key_ad)):
                    if not isinstance (ddiff_[key][key_ad],list):
                        services_ad.append(ddiff_[key][key_ad])
                    else:
                        services_ad = ddiff_[key][key_ad]
                if (re.search(regex_svc_set, key_ad)):
                    if not isinstance (ddiff_[key][key_ad],list):
                        service_sets_ad.append(ddiff_[key][key_ad])
                    else:
                        service_sets_ad = ddiff_[key][key_ad]

                if (re.search(regex_app, key_ad)):
                    if not isinstance (ddiff_[key][key_ad],list):
                        applications_ad.append(ddiff_[key][key_ad])
                    else:
                        applications_ad = ddiff_[key][key_ad]
                if (re.search(regex_app_set, key_ad)):
                    if not isinstance (ddiff_[key][key_ad],list):
                        application_sets_ad.append(ddiff_[key][key_ad])
                    else:
                        application_sets_ad = ddiff_[key][key_ad]

                if (re.search(regex_policies, key_ad)):
                    if not isinstance (ddiff_[key][key_ad],list):
                        policies_ad.append(ddiff_[key][key_ad])
                    else:
                        policies_ad = ddiff_[key][key_ad]
    diff_dict_['addresses_ad'] = addresses_ad
    diff_dict_['address_sets_ad'] = address_sets_ad
    diff_dict_['services_ad'] = services_ad
    diff_dict_['service_sets_ad'] = service_sets_ad
    diff_dict_['applications_ad'] = applications_ad
    diff_dict_['application_sets_ad'] = application_sets_ad
    diff_dict_['policies_ad'] = policies_ad
    diff_dict_['addresses_rm'] = addresses_rm
    diff_dict_['address_sets_rm'] = address_sets_rm
    diff_dict_['services_rm'] = services_rm
    diff_dict_['service_sets_rm'] = service_sets_rm
    diff_dict_['applications_rm'] = applications_rm
    diff_dict_['application_sets_rm'] = application_sets_rm
    diff_dict_['policies_rm'] = policies_rm

#    diff_dictt_ = diff_opt (diff_dict_)
    diff_dictt_ = diff_dict_
    
    return (diff_dictt_)

def diff_opt (dict_diff_):

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
    dict_diff = copy.deepcopy(dict_diff_)
    
    # addresses optimization

    addresses_list_rm = dict_diff["addresses_rm"]
    addresses_list_add = dict_diff["addresses_ad"]

    if (dict_diff["addresses_rm"] and dict_diff["addresses_ad"]):
        i = 0
        while i < len(addresses_list_rm):
            j = 0
            while j < len(addresses_list_add):
                if (addresses_list_rm[i]["address-name"] == addresses_list_add[j]["address-name"]):
                    del addresses_list_rm[i]
                    del addresses_list_ad[j]
                    i = i - 1
                    break
                j = j + 1
            i = i + 1

    # services optimization

    services_list_rm = dict_diff["services_rm"]
    services_list_add = dict_diff["services_ad"]

    if (dict_diff["services_rm"] and dict_diff["services_ad"]):
        i = 0
        while i < len(services_list_rm):
            j = 0
            while j < len(services_list_add):
                if (services_list_rm[i]["service-name"] == services_list_add[j]["service-name"]):
                    del services_list_rm[i]
                    del services_list_ad[j]
                    i = i - 1
                    break
                j = j + 1
            i = i + 1

    # address-set optimization
    
    addresses_sets_list_rm = dict_diff["address_sets_rm"]
    addresses_sets_list_add = dict_diff["address_sets_ad"]


    if (dict_diff["address_sets_rm"] and dict_diff["address_sets_ad"]):
        i = 0
        while i < len(addresses_sets_list_rm):
            j = 0
            while j < len(addresses_sets_list_add):
                if (addresses_sets_list_rm[i]["address-set-name"] == addresses_sets_list_add[j]["address-set-name"]):
                    address_rm_list = addresses_sets_list_rm[i]["addresses"]
                    address_add_list = addresses_sets_list_add[j]["addresses"]
                    m = set(address_rm_list) & set(address_add_list)
                    address_rm_list = list(set(address_rm_list) - m)
                    address_add_list = list(set(address_add_list) - m)
                    if not address_rm_list:
#                        del addresses_sets_list_rm[i]
#                        i = i - 1 
                        continue
                    else:
                        addresses_sets_list_rm[i]["addresses"] = address_rm_list
                    if not address_add_list:
#                        del addresses_sets_list_add[j]
#                        j = j - 1
                        continue
                    else:
                        addresses_sets_list_add[j]["addresses"] = address_add_list
                    break
                j = j + 1
            i = i + 1

    # service-set optimization

    service_sets_list_rm = dict_diff["service_sets_rm"]
    service_sets_list_add = dict_diff["service_sets_ad"]

    if (True and dict_diff["service_sets_rm"] and dict_diff["service_sets_ad"]):
        i = 0
        while i < len(service_sets_list_rm):
            j = 0
            while j < len(service_sets_list_add):
                m = ''
                if (service_sets_list_rm[i]["service-set-name"] == service_sets_list_add[j]["service-set-name"]):
                    service_rm_list = service_sets_list_rm[i]["services"]
                    service_add_list = service_sets_list_add[j]["services"]
                    m = set(service_rm_list) & set(service_add_list)
                    service_rm_list = list(set(service_rm_list) - m)
                    service_add_list = list(set(service_add_list) - m)
                    if not service_rm_list:
#                        del service_sets_list_rm[i]
#                        i = i - 1
                        continue
                    else:
                        service_sets_list_rm[i]["services"] = service_rm_list
                    if not service_add_list:
#                        del service_sets_list_add[j]
#                        j = j - 1
                        continue
                    else:
                        service_sets_list_add[i]["services"] = service_add_list
                    break
                j = j + 1
            i = i + 1

    # application-set optimization

    application_sets_list_rm = dict_diff["application_sets_rm"]
    application_sets_list_add = dict_diff["application_sets_ad"]

    if (True and dict_diff["application_sets_rm"] and dict_diff["application_sets_ad"]):
        i = 0
        while i < len(application_sets_list_rm):
            j = 0
            while j < len(application_sets_list_add):
                m = ''
                if (application_sets_list_rm[i]["application-set-name"] == application_sets_list_add[j]["application-set-name"]):
                    application_rm_list = application_sets_list_rm[i]["applications"]
                    application_add_list = application_sets_list_add[j]["applications"]
                    m = set(application_rm_list) & set(application_add_list)
                    application_rm_list = list(set(application_rm_list) - m)
                    application_add_list = list(set(application_add_list) - m)
                    if not application_rm_list:
#                        del application_sets_list_rm[i]
#                        i = i - 1
                        continue
                    else:
                        application_sets_list_rm[i]["applications"] = application_rm_list
                    if not application_add_list:
#                        del application_sets_list_add[j]
#                        j = j - 1
                        continue
                    else:
                        application_sets_list_add[i]["applications"] = application_add_list
                    break
                j = j + 1
            i = i + 1

    # policy optimization

    policies_list_add = dict_diff["policies_ad"]
    policies_list_rm = dict_diff["policies_rm"]

    if (dict_diff["policies_rm"] and dict_diff["policies_ad"]):
        i = 0
        while i < len(policies_list_rm):
            j = 0
            while j < len(policies_list_add):
                if (policies_list_rm[i]["policy-name"] == policies_list_add[j]["policy-name"]):
                # address-sets in policy optimization 

                    src_address_set_list_rm = []
                    src_address_set_list_ad = []
                    dst_address_set_list_rm = []
                    dst_address_set_list_ad = []

                    src_addr_set_list_rm = policies_list_rm[i]['match']['source-address-sets']
                    src_addr_set_list_ad = policies_list_add[j]['match']['source-address-sets']
                    dst_addr_set_list_rm = policies_list_rm[i]['match']['destination-address-sets']
                    dst_addr_set_list_ad = policies_list_add[j]['match']['destination-address-sets']
                    
                    for src_addr_set_dict_rm in src_addr_set_list_rm:
                        for src_addr_set_rm in src_addr_set_dict_rm:
                            src_address_set_list_rm.append(src_addr_set_rm)

                    for src_addr_set_dict_ad in src_addr_set_list_ad:
                        for src_addr_set_ad in src_addr_set_dict_ad:
                            src_address_set_list_ad.append(src_addr_set_ad)

                    for dst_addr_set_dict_rm in dst_addr_set_list_rm:
                        for dst_addr_set_rm in dst_addr_set_dict_rm:
                            dst_address_set_list_rm.append(dst_addr_set_rm)

                    for dst_addr_set_dict_ad in dst_addr_set_list_ad:
                        for dst_addr_set_ad in dst_addr_set_dict_ad:
                            dst_address_set_list_ad.append(dst_addr_set_ad)
                    
                    m_src = set(src_address_set_list_ad) & set(src_address_set_list_rm)
                    if m_src:
                        l = 0
                        while l < len(src_addr_set_list_rm):
#                        for src_addr_set_dict_rm in src_addr_set_list_rm:
                            for src_addr_set_rm in src_addr_set_list_rm[l]:
                                for m in m_src:
                                    if (m == src_addr_set_rm):
                                        src_addr_set_list_rm.remove(src_addr_set_list_rm[l])
                                        l = l - 1
                                        break
                            l = l + 1
                        l = 0
                        while l < len(src_addr_set_list_ad):
#                        for src_addr_set_dict_ad in src_addr_set_list_ad:
                            for src_addr_set_ad in src_addr_set_list_ad[l]:
                                for m in m_src:
                                    if (m == src_addr_set_ad):
                                        src_addr_set_list_ad.remove(src_addr_set_list_ad[l])
                                        l = l - 1
                                        break
                            l = l + 1
                    m_dst = set(dst_address_set_list_ad) & set(dst_address_set_list_rm)
                    if m_dst:
                        l = 0
                        while l < len(dst_addr_set_list_rm):
#                        for dst_addr_set_dict_rm in dst_addr_set_list_rm:
                            for dst_addr_set_rm in dst_addr_set_list_rm[l]:
                                for m in m_dst:
                                    if (m == dst_addr_set_rm):
                                        dst_addr_set_list_rm.remove(dst_addr_set_list_rm[l])
                                        l = l - 1
                                        break
                            l = l + 1
                        l = 0
                        while l < len(dst_addr_set_list_ad):
#                        for dst_addr_set_dict_ad in dst_addr_set_list_ad:
                            for dst_addr_set_ad in dst_addr_set_list_ad[l]:
                                for m in m_dst:
                                    if (m == dst_addr_set_ad):
                                        dst_addr_set_list_ad.remove(dst_addr_set_list_ad[l])
                                        l = l - 1
                                        break
                            l = l + 1

                    # service-set in policy iptimization

                    service_set_list_rm = []
                    service_set_list_ad = []

                    svc_set_list_rm = policies_list_rm[i]['match']['service-sets']
                    svc_set_list_ad = policies_list_add[j]['match']['service-sets']

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

                    app_set_list_rm = policies_list_rm[i]['match']['application-sets']
                    app_set_list_ad = policies_list_add[j]['match']['application-sets']

                    m_app = list(set(app_set_list_ad) & set(app_set_list_rm))
                    
                    if m_app:
                        for m in m_app:
                            app_set_list_rm.remove(m)
                            app_set_list_ad.remove(m)


                    flag_rm = (policies_list_rm[i]['match']['source-address-sets'] or policies_list_rm[i]['match']['destination-address-sets'] or policies_list_rm[i]['match']['service-sets'] or policies_list_rm[i]['match']['application-sets'] )
                    if not flag_rm:
                        del policies_list_rm[i]
                        i = i - 1
                    flag_ad = (policies_list_add[j]['match']['source-address-sets'] or policies_list_add[j]['match']['destination-address-sets'] or policies_list_add[j]['match']['service-sets'] or policies_list_add[j]['match']['application-sets'] )
                    if not flag_ad:
                        del policies_list_add[j]
                        j = j - 1

                j = j + 1
            i = i + 1
    return (dict_diff)

def dict_full_policy (psef_conf, address_set_index, service_set_index):

    psef_conf_ = copy.deepcopy(psef_conf)
    address_set_index_ = copy.deepcopy(address_set_index)
    service_set_index_ = copy.deepcopy(service_set_index)

    if ('policies' in psef_conf['data']):
        j = 0
        for policy_ in psef_conf['data']['policies']:
            i = 0
            for source_address_set_ in policy_["match"]["source-address-sets"]:
                address_set_dict_ = {}
                address_set_index_dict = address_set_index_[source_address_set_]
                for struct_key, struct_value in address_set_index_dict['structure-to-addresses'].items():
                    if isinstance(struct_key, tuple):
                        new_str_key = "(%s,%s)" % struct_key
                        address_set_index_dict['structure-to-addresses'][new_str_key] = struct_value
                        del address_set_index_dict['structure-to-addresses'][struct_key]
                address_set_dict_ = { source_address_set_:address_set_index_dict }
                psef_conf_['data']['policies'][j]["match"]["source-address-sets"][i] = address_set_dict_
                i = i + 1
            i = 0
            for destination_address_set_ in policy_["match"]["destination-address-sets"]:
                address_set_dict_ = {}
                address_set_index_dict = address_set_index_[destination_address_set_]
                for struct_key, struct_value in address_set_index_dict['structure-to-addresses'].items():
                    if isinstance(struct_key, tuple):
                        new_str_key = "(%s,%s)" % struct_key
                        address_set_index_dict['structure-to-addresses'][new_str_key] = struct_value
                        del address_set_index_dict['structure-to-addresses'][struct_key]
                address_set_dict_ = { destination_address_set_:address_set_index_dict }
                psef_conf_['data']['policies'][j]["match"]["destination-address-sets"][i] = address_set_dict_
                i = i + 1
            i = 0
            for service_set_ in policy_["match"]["service-sets"]:
                service_set_dict_ = {}
                service_set_index_dict = {}
                service_set_index_dict = service_set_index_[service_set_]
                psef_conf_['data']['policies'][j]["match"]["service-sets"][i] = service_set_index_dict
                i = i + 1
            j = j + 1

    return (psef_conf_)

