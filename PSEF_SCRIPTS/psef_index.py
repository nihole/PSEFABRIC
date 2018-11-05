'''

address_index()
indexes address-sets and returns the dictionary address_set_to_struct

policy_index()
indexes policies and returns the dictionary policy_

  Indexation: term "indexation" in our context means the process of dict creation with "resolving element" as keys and
                - list of addresses (with this resolving element)  as a value in case of address-set indexation
                - list of source/destination address-sets (which have the addresses with this resolving element)  as a value in case of address-set indexation

     Resolve element: "resolving element" is a combination of structure parameters necessary for making a decision about policies configuration.
     Definition of "resolving element" depends on network design.
     For example, it might be a combination of vrf, data-center and equipment or some combination of some logical parameters like areas, sub-areas, zones.

          Structure: we use "structure" to determine the list of commands for each MO we have to perform in accordance with psefabric configuration change.

'''

import psef_debug
import copy

def policy_index (policy_, add_):

##########  Description  #######
    '''
    Resolve element in this design is a combination of zone, area, sub-zone  

    '''
#############  BODY ############

    
    struct_to_policy = {}
    struct_to_source = {}
    struct_to_destination = {}
    source_address_set_list = []
    destination_address_set_list = []

# Create a list of all dictionaries of source address-sets for policy_
    source_address_set_list = policy_['match']['source-address-sets']

# Create a list of all dictionaries of destination address-sets for policy_
    destination_address_set_list = policy_['match']['destination-address-sets']

    for source_address_set_dict in source_address_set_list:
        for source_address_set_ in source_address_set_dict:
            if (add_=='ad'):
                for resolving_element_ in address_set_index_new[source_address_set_]['structure-to-addresses']:
                    if resolving_element_ not in struct_to_source:
                        struct_to_source[resolving_element_] = []
                        struct_to_source_el_ = {}
                        struct_to_source_el_ = copy.deepcopy(address_set_index_new[source_address_set_])
                        struct_to_source_el_['structure-to-addresses'] = address_set_index_new[source_address_set_]['structure-to-addresses'][resolving_element_]
                        struct_to_source[resolving_element_].append(struct_to_source_el_)
                        del struct_to_source_el_ 
                    else:
                        struct_to_source_el_ = {}
                        struct_to_source_el_['structure-to-addresses'] = address_set_index_new[source_address_set_]['structure-to-addresses'][resolving_element_]
                        struct_to_source[resolving_element_].append(struct_to_source_el_)
            elif (add_ == 'rm'):
                for resolving_element_ in address_set_index_old[source_address_set_]['structure-to-addresses']:
                    if resolving_element_ not in struct_to_source:
                        struct_to_source[resolving_element_] = []
                        struct_to_source_el_ = {}
                        struct_to_source_el_ = copy.deepcopy(address_set_index_new[source_address_set_])
                        struct_to_source_el_['structure-to-addresses'] = address_set_index_old[source_address_set_]['structure-to-addresses'][resolving_element_]
                        struct_to_source[resolving_element_].append(struct_to_source_el_)
                        del struct_to_source_el_
                    else:
                        struct_to_source_el_ = {}
                        struct_to_source_el_['structure-to-addresses'] = address_set_index_old[source_address_set_]['structure-to-addresses'][resolving_element_]
                        struct_to_source[resolving_element_].append(struct_to_source_el_)
            else:
                print "Incorect value of add_ in  policy_index"
    for destination_address_set_dict in destination_address_set_list:
        for destination_address_set_ in destination_address_set_dict:
            if (add_=='ad'):
                for resolving_element_ in address_set_index_new[destination_address_set_]['structure-to-addresses']:
                    if resolving_element_ not in struct_to_destination:
                        struct_to_destination[resolving_element_] = []
                        struct_to_destination_el_ = {}
                        struct_to_destination_el_ = copy.deepcopy(address_set_index_new[destination_address_set_])
                        struct_to_destination_el_['structure-to-addresses'] = address_set_index_new[destination_address_set_]['structure-to-addresses'][resolving_element_]
                        struct_to_destination[resolving_element_].append(struct_to_destination_el_)
                        del struct_to_destination_el_
                    else:
                        struct_to_destination_el_ = {}
                        struct_to_destination_el_['structure-to-addresses'] = address_set_index_old[destination_address_set_]['structure-to-addresses'][resolving_element_]
                        struct_to_destination[resolving_element_].append(struct_to_destination_el_)
            elif (add_ == 'rm'):
                for resolving_element_ in address_set_index_old[destination_address_set_]['structure-to-addresses']:
                    if resolving_element_ not in struct_to_destination:
                        struct_to_destination[resolving_element_] = []
                        struct_to_destination_el_ = {}
                        struct_to_destination_el_ = copy.deepcopy(address_set_index_new[destination_address_set_])
                        struct_to_destination_el_['structure-to-addresses'] = address_set_index_old[destination_address_set_]['structure-to-addresses'][resolving_element_]
                        struct_to_destination[resolving_element_].append(struct_to_destination_el_)
                        del struct_to_destination_el_
                    else:
                        struct_to_destination_el_ = {}
                        struct_to_destination_el_['structure-to-addresses'] = address_set_index_old[destination_address_set_]['structure-to-addresses'][resolving_element_]
                        struct_to_destination[resolving_element_].append(struct_to_destination_el_)
            else:
                print "Incorect value of add_ in  policy_index"

    policy_index = copy.deepcopy(policy_)
    del policy_index['match']['source-address-sets']
    del policy_index['match']['destination-address-sets']
    policy_index['match']['source-address-sets'] = {}
    policy_index['match']['source-address-sets'] = struct_to_source
    policy_index['match']['destination-address-sets'] = {}
    policy_index['match']['destination-address-sets'] = struct_to_destination

    psef_debug.WriteDebug('psef_index', policy_index)

    return (policy_index)

def address_index (psef_conf):

##########  Description  #######
    '''
    Resolve element in this design is a combination of zone, area, sub-zone
    '''

#############  BODY ############a

    psef_conf_ = copy.deepcopy(psef_conf)
    
    address_index_ = {}
    address_set_index_ = {}

    if 'addresses' in psef_conf_['data']:
        for address_element_ in psef_conf_['data']['addresses']:
            address_index_[address_element_['address-name']] = address_element_

    if 'address-sets' in psef_conf_['data']:
        for address_set_element in psef_conf_['data']['address-sets']:
            address_set_index_[address_set_element['address-set-name']] = {}
            address_set_index_[address_set_element['address-set-name']] = copy.deepcopy(address_set_element)
            del address_set_index_[address_set_element['address-set-name']]['addresses']
            address_set_index_[address_set_element['address-set-name']]['structure-to-addresses'] = {}
            structure_to_addresses_el_= address_set_index_[address_set_element['address-set-name']]['structure-to-addresses']
            for addr_element in address_set_element['addresses']:
                resolving_element = (address_index_[addr_element]['structure']['zone'], address_index_[addr_element]['structure']['area'], address_index_[addr_element]['structure']['sub-zone'])
                if not resolving_element in structure_to_addresses_el_:
                    structure_to_addresses_el_[resolving_element] = []
                    structure_to_addresses_el_[resolving_element].append(address_index_[addr_element])
                else:
                    structure_to_addresses_el_[resolving_element].append(address_index_[addr_element])
    return address_set_index_
