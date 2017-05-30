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
    if (('policies' in psef_conf_['data']) and ('policy' in psef_conf_['data']['policies'])):
        if not isinstance (psef_conf_['data']['policies']['policy'],list):
            application_element_ = psef_conf_['data']['policies']['policy']
            psef_conf_['data']['policies']['policy'] = []
            psef_conf_['data']['policies']['policy'].append(application_element_)
        for policy_element_ in psef_conf_['data']['policies']['policy']:
            if 'source-addresses' in policy_element_['match']:
                if not isinstance (policy_element_['match']['source-addresses']['address-set'],list):
                    source_addresses_set_element_ = policy_element_['match']['source-addresses']['address-set']
		    policy_element_['match']['source-addresses']['address-set']=[]
                    policy_element_['match']['source-addresses']['address-set'].append(source_addresses_set_element_)
            if 'destination-addresses' in policy_element_['match']:
                if not isinstance (policy_element_['match']['destination-addresses']['address-set'],list):
                    destination_addresses_set_element_ = policy_element_['match']['destination-addresses']['address-set']
                    policy_element_['match']['destination-addresses']['address-set']=[]
                    policy_element_['match']['destination-addresses']['address-set'].append(destination_addresses_set_element_)
            if 'applications' in policy_element_['match']:
                if not isinstance (policy_element_['match']['applications']['application-set'],list):
                    application_set_element_ = policy_element_['match']['applications']['application-set']
                    policy_element_['match']['applications']['application-set'] = []
                    policy_element_['match']['applications']['application-set'].append(application_set_element_)
       
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
    regex_policies_policy = "\['data'\]\['policies'\]\['policy'\]"
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
                if (re.search(regex_policies_policy, key_rm)):
                    policies_rm.append(ddiff_[key][key_rm])
                elif (re.search(regex_policies, key_rm)):
                    policies_rm = ddiff_[key][key_rm]['policy']
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
                if (re.search(regex_policies_policy, key_ad)):
                    policies_ad.append(ddiff_[key][key_ad])
                elif (re.search(regex_policies, key_ad)):            
                    policies_ad = ddiff_[key][key_ad]['policy']

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

    return (diff_dict_)

