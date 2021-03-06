'''
This is essential element of the demultiplexer layes of Psefabric Dataflow Model and one of the key elements of the psefabric concept.
The python dictionaries created here are used in multiplexer.py.
The matter is that depending on the values of the structural elements (for adrresses in this realization) we have to program a specific set of commands for different MOs.
And we need some algorithm for that. So these dictionaries describe this logic.
We need to program logic for the adding/removal of addresses, address_sets, services, service_sets, policies. So we have:

mult_dict_address()
mult_dict_address_set()
mult_dict_service()
mult_dict_service_set()
mult_dict_sapplication()
mult_dict_application_set()
mult_dict_policy()
'''

import re
import copy


# Change the list of parameters if needed
def mult_dict_address(str_list, parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    # May be some logic based on par1, par2, ... value
    mult.append({})
    mult[0]['eq_addr'] = 'example_device1'
    mult[0]['eq_parameter'] = 'some_parameter'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'].append('extemplates_1.create_address')
    mult[0]['cmd']['rm'].append('extemplates_1.delete_address')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates_2.create_address')
    mult[1]['cmd']['rm'].append('extemplates_2.delete_address')

    return (mult)

# Change the list of parameters if needed
def mult_dict_address_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    # May be some logic based on par1, par2, ... value
    mult.append({})
    mult[0]['eq_addr'] = 'example_device1'
    mult[0]['eq_parameter'] = 'some_parameter'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'].append('extemplates_1.create_address_set')
    mult[0]['cmd']['rm'].append('extemplates_1.delete_address_set')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates_2.create_address_set')
    mult[1]['cmd']['rm'].append('extemplates_2.delete_address_set')

    return (mult)

# Change the list of parameters if needed
def mult_dict_service(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    # May be some logic based on par1, par2, ... value
    mult.append({})
    mult[0]['eq_addr'] = 'example_device1'
    mult[0]['eq_parameter'] = 'some_parameter'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'].append('extemplates_1.create_service')
    mult[0]['cmd']['rm'].append('extemplates_1.delete_service')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates_2.create_service')
    mult[1]['cmd']['rm'].append('extemplates_2.delete_service')

    return (mult)

# Add the list of parameters if needed
def mult_dict_service_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    # May be some logic based on par1, par2, ... value
    mult.append({})
    mult[0]['eq_addr'] = 'example_device1'
    mult[0]['eq_parameter'] = 'some_parameter'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'].append('extemplates_1.create_service_set')
    mult[0]['cmd']['rm'].append('extemplates_1.delete_service_set')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates_2.create_service_set')
    mult[1]['cmd']['rm'].append('extemplates_2.delete_service_set')

    return (mult)

# Add the list of parameters if needed
def mult_dict_application(parameters):

    mult = []
    # May be some logic based on par1, par2, ... value
    mult.append({})
    mult[0]['eq_addr'] = 'example_device1'
    mult[0]['eq_parameter'] = 'some_parameter'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []

    return (mult)


# Change the list of parameters if needed
def mult_dict_application_set(parameters):

##########  Description  #######
    '''
    '''
#############  BODY ############

    mult = []
    # May be some logic based on par1, par2, ... value
    mult.append({})
    mult[0]['eq_addr'] = 'example_device1'
    mult[0]['eq_parameter'] = 'some_parameter'
    mult[0]['cmd'] = {}
    mult[0]['cmd']['ad'] = []
    mult[0]['cmd']['rm'] = []
    mult[0]['cmd']['ad'].append('extemplates_1.create_application_set')
    mult[0]['cmd']['rm'].append('extemplates_1.delete_application_set')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates_2.create_application_set')
    mult[1]['cmd']['rm'].append('extemplates_2.delete_application_set')

    return (mult)


def mult_dict_policy(src_str, dst_str, service_sets_dict, parameters):

##########  Description  #######
########## End of description #####

    mult = []

    # Some logical variables may be defined
    # For example:

    if (re.match(src_str[0], dst_str[0])):
        same_str_1_flag = True
    else:
        same_str_1_flag = False

    if (re.match(src_str[1], dst_str[1])):
        same_str_2_flag = True
    else:
        same_str_2_flag = False

    if (re.match(src_str[2], dst_str[2])):
        same_str_3_flag = True
    else:
        same_str_3_flag = False

    if (re.match(src_str[3], dst_str[3])):
        same_str_4_flag = True
    else:
        same_str_4_flag = False

# Then depending on these values we may program psefabric actions.
    # For example:

    if (same_str_1_flag and same_str_2_flag and not same_str_3_flag):
        mult = []
        # May be some logic based on par1, par2, ... value
        mult.append({})
        mult[0]['eq_addr'] = 'example_device1'
        mult[0]['eq_parameter'] = 'some_parameter'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'].append('extemplates_1.create_policy')
        mult[0]['cmd']['rm'].append('extemplates_1.delete_policy')
        mult.append({})
        mult[1]['eq_addr'] = 'example_device2'
        mult[1]['eq_parameter'] = 'some_parameter'
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['ad'].append('extemplates_2.create_policy')
        mult[1]['cmd']['rm'].append('extemplates_2.delete_policy')

    else:
        mult = []
        # May be some logic based on par1, par2, ... value
        mult.append({})
        mult[0]['eq_addr'] = 'example_device1'
        mult[0]['eq_parameter'] = 'some_parameter'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'].append('extemplates_1.create_policy')
        mult[0]['cmd']['rm'].append('extemplates_1.delete_policy')
        mult.append({})
        mult[1]['eq_addr'] = 'example_device2'
        mult[1]['eq_parameter'] = 'some_parameter'
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['ad'].append('extemplates_2.create_policy')
        mult[1]['cmd']['rm'].append('extemplates_2.delete_policy')

    return (mult)

