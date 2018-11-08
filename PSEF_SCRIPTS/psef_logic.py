'''
This is essential element of the demultiplexer layes of Psefabric Dataflow Model and one of the key elements of the psefabric concept.
The python dictionaries created here are used in multiplexer.py.
The matter is that depending on the values of the structural elements (for networks in this realization) we have to program a specific set of commands for different MOs.
And we need some algorithm for that. So these dictionaries describe this logic.
We need to program logic for the adding/removal of addresses, address_sets, services, service_sets, policies. So we have:
mult_dict_address()
mult_dict_address_set()
mult_dict_service()
mult_dict_service_set()
mult_dict_policy()
'''

import re
import copy


# Change the list of parameters if needed
def mult_dict_address(str1, str2, par1, par2):

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
    mult[0]['cmd']['ad'].append('extemplates.create_address')
    mult[0]['cmd']['rm'].append('extemplates.delete_address')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates.create_address')
    mult[1]['cmd']['rm'].append('extemplates.delete_address')

    return (mult)

# Change the list of parameters if needed
def mult_dict_address_set(par1, par2):

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
    mult[0]['cmd']['ad'].append('extemplates.create_address_set')
    mult[0]['cmd']['rm'].append('extemplates.delete_address_set')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates.create_address_set')
    mult[1]['cmd']['rm'].append('extemplates.delete_address_set')

    return (mult)

# Change the list of parameters if needed
def mult_dict_service(par1, par2):

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
    mult[0]['cmd']['ad'].append('extemplates.create_service')
    mult[0]['cmd']['rm'].append('extemplates.delete_service')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates.create_service')
    mult[1]['cmd']['rm'].append('extemplates.delete_service')

    return (mult)

# Change the list of parameters if needed
def mult_dict_service_set(par1, par2):

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
    mult[0]['cmd']['ad'].append('extemplates.create_service_set')
    mult[0]['cmd']['rm'].append('extemplates.delete_service_set')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates.create_service_set')
    mult[1]['cmd']['rm'].append('extemplates.delete_service_set')

    return (mult)

# Change the list of parameters if needed
def mult_dict_application(par1, par2):

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
def mult_dict_application_set(par1, par2):

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
    mult[0]['cmd']['ad'].append('extemplates.create_application_set')
    mult[0]['cmd']['rm'].append('extemplates.delete_application_set')
    mult.append({})
    mult[1]['eq_addr'] = 'example_device2'
    mult[1]['eq_parameter'] = 'some_parameter'
    mult[1]['cmd'] = {}
    mult[1]['cmd']['ad'] = []
    mult[1]['cmd']['rm'] = []
    mult[1]['cmd']['ad'].append('extemplates.create_application_set')
    mult[1]['cmd']['rm'].append('extemplates.delete_application_set')

    return (mult)


def mult_dict_policy(src_str_1, src_str_2, src_str_3, src_str_4, dst_str_1, dst_str_2, dst_str_3, dst_str_4, service_sets_dict):

##########  Description  #######
########## End of description #####

    mult = []

    # Some logical variables may be defined
    # For example:

    if (re.match(src_str_1, dst_str_2)):
        same_str_1_flag = True
    else:
        same_str_1_flag = False

    if (re.match(src_str_2, dst_str_2)):
        same_str_2_flag = True
    else:
        same_str_2_flag = False

    if (re.match(src_str_3, dst_str_3)):
        same_str_3_flag = True
    else:
        same_str_3_flag = False

    if (re.match(src_str_4, dst_str_4)):
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
        mult[0]['cmd']['ad'].append('extemplates.create_policy')
        mult[0]['cmd']['rm'].append('extemplates.delete_policy')
        mult.append({})
        mult[1]['eq_addr'] = 'example_device2'
        mult[1]['eq_parameter'] = 'some_parameter'
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['ad'].append('extemplates.create_policy')
        mult[1]['cmd']['rm'].append('extemplates.delete_policy')

    else:
        mult = []
        # May be some logic based on par1, par2, ... value
        mult.append({})
        mult[0]['eq_addr'] = 'example_device1'
        mult[0]['eq_parameter'] = 'some_parameter'
        mult[0]['cmd'] = {}
        mult[0]['cmd']['ad'] = []
        mult[0]['cmd']['rm'] = []
        mult[0]['cmd']['ad'].append('extemplates.create_policy')
        mult[0]['cmd']['rm'].append('extemplates.delete_policy')
        mult.append({})
        mult[1]['eq_addr'] = 'example_device2'
        mult[1]['eq_parameter'] = 'some_parameter'
        mult[1]['cmd'] = {}
        mult[1]['cmd']['ad'] = []
        mult[1]['cmd']['rm'] = []
        mult[1]['cmd']['ad'].append('extemplates.create_policy')
        mult[1]['cmd']['rm'].append('extemplates.delete_policy')

    return (mult)

