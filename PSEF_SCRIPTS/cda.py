'''
def dict_correct() 
takes configuration dictionary and corrects some elements in it

def ddiff_dict()
takes the difference between new and old psefabric configurations (type dict) and transforms it to the dict convenient for further operations
'''

import re

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
            psef_conf_['data']['addresses'].append(address_element_)
    if 'address-sets' in psef_conf_['data']:
        if not isinstance (psef_conf_['data']['address-sets'],list):
            address_set_element_ = psef_conf_['data']['address-sets']
            psef_conf_['data']['address-sets'] = []
            psef_conf_['data']['address-sets'].append(address_set_element_)
        for n, address_set_el_ in enumerate(psef_conf_['data']['address-sets']):
            if not isinstance (address_set_el_['addresses'],list):
                address_el_list = address_set_el_['addresses']
                psef_conf_['data']['address-sets'][n]['addresses'] = []
                psef_conf_['data']['address-sets'][n]['addresses'].append(address_el_list)
    if 'applications' in psef_conf_['data']:
        if not isinstance (psef_conf_['data']['applications'],list):
            application_element_ = psef_conf_['data']['applications']
            psef_conf_['data']['applications'] = []
            psef_conf_['data']['applications'].append(application_element_)
    if 'application-sets' in psef_conf_['data']:
        if not isinstance (psef_conf_['data']['application-sets'],list):
            application_set_element_ = psef_conf_['data']['application-sets']
            psef_conf_['data']['application-sets'] = []
            psef_conf_['data']['application-sets'].append(application_set_element_)
        for i, applications_set_el_ in enumerate(psef_conf_['data']['application-sets']):
            if not isinstance (applications_set_el_['applications'],list):
                application_el_list = applications_set_el_['applications']
                psef_conf_['data']['application-sets'][i]['applications'] = []
                psef_conf_['data']['application-sets'][i]['applications'].append(application_el_list)
    if ('policies' in psef_conf_['data']):
        if not isinstance (psef_conf_['data']['policies'],list):
            application_element_ = psef_conf_['data']['policies']
            psef_conf_['data']['policies'] = []
            psef_conf_['data']['policies'].append(application_element_)
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
    regex_app = "\['data'\]\['applications'\]"
    regex_addr_set = "\['data'\]\['address-sets'\]"
    regex_app_set = "\['data'\]\['application-sets'\]"
    regex_policies = "\['data'\]\['policies'\]"
#    regex_policies_policy = "\['data'\]\['policies'\]\['policy'\]"
    addresses_rm = []
    address_sets_rm = []
    addresses_ad = []
    address_sets_ad = []
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
    diff_dict_['applications_ad'] = applications_ad
    diff_dict_['application_sets_ad'] = application_sets_ad
    diff_dict_['policies_ad'] = policies_ad
    diff_dict_['addresses_rm'] = addresses_rm
    diff_dict_['address_sets_rm'] = address_sets_rm
    diff_dict_['applications_rm'] = applications_rm
    diff_dict_['application_sets_rm'] = application_sets_rm
    diff_dict_['policies_rm'] = policies_rm

    diff_dictt_ = diff_opt (diff_dict_)

    return (diff_dictt_)

def diff_opt (dict_diff):

    '''
    If we change addresses in address-set, then it looks like we remove this address-set and after that add new one with the final set of addresses.
    It results in some problems. This function is used to solve it. We compare the lists in both cases (old adderss-set and new one) and stay only one operation (add or rm)

    The same situation is for application/application-set
    '''
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


