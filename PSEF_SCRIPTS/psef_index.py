'''
def address_index()
indexes the configuration by address and address-set and returns the structures address_set_to_struct, address_to_struct

def policy_index()
indexes the configuration by policies and returns the structure policy_

More details see in the descriptions of the functions
'''

def policy_index (policy_, add_):

##########  Description  #######
    '''
    Transforms the dictionary of the policy to convinient format.
    '''
#############  BODY ############

# add_ = 'ad' - add
# add_ = 'rm' - delete
    struct_to_policy = {}
    struct_to_source = {}
    struct_to_destination = {}
    source_address_set_list = []
    destination_address_set_list = []

# Create a list of all dictionaries of source address-sets for policy_
    source_address_set_list = policy_['match']['source-addresses']['address-set']

# Create a list of all dictionaries of destination address-sets for policy_
    destination_address_set_list = policy_['match']['destination-addresses']['address-set']

    for source_address_set_ in source_address_set_list:
        if (add_=='ad'):
            for key_s_to_p in address_set_index_new[source_address_set_]['structure-to-addresses']:
                if key_s_to_p not in struct_to_source:
                    struct_to_source[key_s_to_p] = []
                    struct_to_source_el_ = {}
                    struct_to_source_el_['address-set-name'] = source_address_set_
                    struct_to_source_el_['structure-to-addresses'] = address_set_index_new[source_address_set_]['structure-to-addresses'][key_s_to_p]
                    struct_to_source[key_s_to_p].append(struct_to_source_el_)
                else:
                    struct_to_source_el_['address-set-name'] = source_address_set_
                    struct_to_source_el_['structure-to-addresses'] = address_set_index_new[source_address_set_]['structure-to-addresses'][key_s_to_p]
                    struct_to_source[key_s_to_p].append(struct_to_source_el_)
        elif (add_ == 'rm'):
            for key_s_to_p in address_set_index_old[source_address_set_]['structure-to-addresses']:
                if key_s_to_p not in struct_to_source:
                    struct_to_source[key_s_to_p] = []
                    struct_to_source_el_ = {}
                    struct_to_source_el_['address-set-name'] = source_address_set_
                    struct_to_source_el_['structure-to-addresses'] = address_set_index_old[source_address_set_]['structure-to-addresses'][key_s_to_p]
                    struct_to_source[key_s_to_p].append(struct_to_source_el_)
                else:
                    struct_to_source_el_['address-set-name'] = source_address_set_
                    struct_to_source_el_['structure-to-addresses'] = address_set_index_old[source_address_set_]['structure-to-addresses'][key_s_to_p]
                    struct_to_source[key_s_to_p].append(struct_to_source_el_)
        else:
            print "Incorect value of add_ in  policy_index"
    for destination_address_set_ in destination_address_set_list:
        if (add_=='ad'):
            for key_s_to_p in address_set_index_new[destination_address_set_]['structure-to-addresses']:
                if key_s_to_p not in struct_to_destination:
                    struct_to_destination[key_s_to_p] = []
                    struct_to_destination_el_ = {}
                    struct_to_destination_el_['address-set-name'] = destination_address_set_
                    struct_to_destination_el_['structure-to-addresses'] = address_set_index_new[destination_address_set_]['structure-to-addresses'][key_s_to_p]
                    struct_to_destination[key_s_to_p].append(struct_to_destination_el_)
                else:
                    struct_to_destination_el_['address-set-name'] = destination_address_set_
                    struct_to_destination_el_['structure-to-addresses'] = address_set_index_old[destination_address_set_]['structure-to-addresses'][key_s_to_p]
                    struct_to_destination[key_s_to_p].append(struct_to_destination_el_)
        elif (add_ == 'rm'):
            for key_s_to_p in address_set_index_old[destination_address_set_]['structure-to-addresses']:
                if key_s_to_p not in struct_to_destination:
                    struct_to_destination[key_s_to_p] = []
                    struct_to_destination_el_ = {}
                    struct_to_destination_el_['address-set-name'] = destination_address_set_
                    struct_to_destination_el_['structure-to-addresses'] = address_set_index_old[destination_address_set_]['structure-to-addresses'][key_s_to_p]
                    struct_to_destination[key_s_to_p].append(struct_to_destination_el_)
                else:
                    struct_to_destination_el_['address-set-name'] = destination_address_set_
                    struct_to_destination_el_['structure-to-addresses'] = address_set_index_old[destination_address_set_]['structure-to-addresses'][key_s_to_p]
                    struct_to_destination[key_s_to_p].append(struct_to_destination_el_)
        else:
            print "Incorect value of add_ in  policy_index"
    policy_index = policy_
    policy_index['match']['source-addresses'] = {}
    policy_index['match']['source-addresses'] = struct_to_source
    policy_index['match']['destination-addresses'] = {}
    policy_index['match']['destination-addresses'] = struct_to_destination

    return (policy_index)

def address_index (psef_conf_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    address_index_ = {}
    address_set_index_ = {}
    if 'addresses' in psef_conf_['data']:
        for address_element_ in psef_conf_['data']['addresses']:
            address_index_[address_element_['address-name']] = address_element_
    if 'address-sets' in psef_conf_['data']:
        for address_set_element in psef_conf_['data']['address-sets']:
            address_set_index_[address_set_element['address-set-name']] = {}
            address_set_index_[address_set_element['address-set-name']]['address-set-name'] = address_set_element['address-set-name']
            address_set_index_[address_set_element['address-set-name']]['structure-to-addresses'] = {}
            structure_to_addresses_el_= address_set_index_[address_set_element['address-set-name']]['structure-to-addresses']
            for addr_element in address_set_element['addresses']:
                struct_el_ = (address_index_[addr_element]['structure']['dc'], address_index_[addr_element]['structure']['vrf'])
                if not struct_el_ in structure_to_addresses_el_:
                    structure_to_addresses_el_[struct_el_] = []
                    structure_to_addresses_el_[struct_el_].append(address_index_[addr_element])
                else:
                    structure_to_addresses_el_[struct_el_].append(address_index_[addr_element])
    
    return (address_index_, address_set_index_)
