'''
def dict_correct() 
takes configuration dictionary and corrects some elements in it

def ddiff_dict()
takes the difference between new and old psefabric configurations (type dict) and transforms it to the dict convenient for further operations
'''

import re
import copy

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

    diff_dictt_ = diff_opt (diff_dict_)

    return (diff_dictt_)

def diff_opt (dict_diff):

    '''
    If we change addresses in address-set, then it looks like we remove this address-set and after that add new one with the final set of addresses.
    It results in some problems. This function is used to solve it. We compare the lists in both cases (old adderss-set and new one) and stay only one operation (add or rm)

    The same situation is for service/service-set
    '''
    
    addresses_list_rm = dict_diff["addresses_rm"]
    addresses_list_add = dict_diff["addresses_ad"]

    if (dict_diff["addresses_rm"] and dict_diff["addresses_ad"]):
        i = 0
        while i < len(addresses_list_rm):
            j = 0
            while j < len(addresses_list_add):
                if (addresses_list_rm[i]["address-name"] == addresses_list_add[j]["address-name"]):
                    del addresses_list_rm[i]
                    i = i - 1
                    break
                j = j + 1
            i = i + 1

    services_list_rm = dict_diff["services_rm"]
    services_list_add = dict_diff["services_ad"]

    if (dict_diff["services_rm"] and dict_diff["services_ad"]):
        i = 0
        while i < len(services_list_rm):
            j = 0
            while j < len(services_list_add):
                if (services_list_rm[i]["service-name"] == services_list_add[j]["service-name"]):
                    del services_list_rm[i]
                    i = i - 1
                    break
                j = j + 1
            i = i + 1
    
    addresses_sets_list_rm = dict_diff["address_sets_rm"]
    addresses_sets_list_add = dict_diff["address_sets_ad"]
    if (True and dict_diff["address_sets_rm"] and dict_diff["address_sets_ad"]):
        i = 0
        while i < len(addresses_sets_list_rm):
            j = 0
            while j < len(addresses_sets_list_add):
                m = ''
                if (addresses_sets_list_rm[i]["address-set-name"] == addresses_sets_list_add[j]["address-set-name"]):
                    address_rm_list = addresses_sets_list_rm[i]["addresses"]
                    address_add_list = addresses_sets_list_add[j]["addresses"]
                    m = set(address_rm_list) & set(address_add_list)
                    address_rm_list = list(set(address_rm_list) - m)
                    address_add_list = list(set(address_add_list) - m)
                    if not address_rm_list:
                        del addresses_sets_list_rm[i]
                        i = i - 1 
                    else:
                        addresses_sets_list_rm[i]["addresses"] = address_rm_list
                    if not address_add_list:
                        del addresses_sets_list_add[j]
                        j = j - 1
                    else:
                        addresses_sets_list_add[j]["addresses"] = address_add_list
                    break
                j = j + 1
            i = i + 1

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
                        del service_sets_list_rm[i]
                        i = i - 1
                    else:
                        service_sets_list_rm[i]["services"] = service_rm_list
                    if not service_add_list:
                        del service_sets_list_add[j]
                        j = j - 1
                    else:
                        service_sets_list_add[i]["services"] = service_add_list
                    break
                j = j + 1
            i = i + 1

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
                        del application_sets_list_rm[i]
                        i = i - 1
                    else:
                        application_sets_list_rm[i]["applications"] = application_rm_list
                    if not application_add_list:
                        del application_sets_list_add[j]
                        j = j - 1
                    else:
                        application_sets_list_add[i]["applications"] = application_add_list
                    break
                j = j + 1
            i = i + 1

    return (dict_diff)

def dict_full_policy (psef_conf, address_set_index):

    psef_conf_ = copy.deepcopy(psef_conf)
    address_set_index_ = copy.deepcopy(address_set_index)

    if ('policies' in psef_conf_['data']):
        for policy_ in psef_conf_['data']['policies']:
            for source_address_set_ in policy_["match"]["source-address-sets"]:
                policy_["match"]["source-address-sets"].remove(source_address_set_)
                address_set_dict_ = {}
                address_set_index_dict = address_set_index_[source_address_set_]
                for struct_key, struct_value in address_set_index_dict['structure-to-addresses'].items():
                    if isinstance(struct_key, tuple):
                        new_str_key = "(%s,%s)" % struct_key
                        address_set_index_dict['structure-to-addresses'][new_str_key] = struct_value
                        del address_set_index_dict['structure-to-addresses'][struct_key]
                address_set_dict_ = { source_address_set_:address_set_index_dict }
                policy_["match"]["source-address-sets"].append(address_set_dict_)

            for destination_address_set_ in policy_["match"]["destination-address-sets"]:
                policy_["match"]["destination-address-sets"].remove(destination_address_set_)
                address_set_dict_ = {}
                address_set_index_dict = address_set_index_[destination_address_set_]
                for struct_key, struct_value in address_set_index_dict['structure-to-addresses'].items():
                    if isinstance(struct_key, tuple):
                        new_str_key = "(%s,%s)" % struct_key
                        address_set_index_dict['structure-to-addresses'][new_str_key] = struct_value
                        del address_set_index_dict['structure-to-addresses'][struct_key]
                address_set_dict_ = { destination_address_set_:address_set_index_dict }
                policy_["match"]["destination-address-sets"].append(address_set_dict_)


        return (psef_conf_)

