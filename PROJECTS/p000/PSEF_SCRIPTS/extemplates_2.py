# This template is for cli configuration of the equipment without "candidate config" feature

import re
# import cidr_to_netmask

'''The list of templates for pan
'''
######## vlan ###########


######## svi ###########


######## addresses  ###########

def create_address (eq_parameter, name, ipv4_prefix, parameters):
#    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
#    config_txt = '''set %s address %s ip-netmask %s/%s''' % (eq_parameter, name, network, netmask)
    config_txt = '''create address with eq_parameter: %s name: %s ipv4_prefix: %s parameters: %s''' % (eq_parameter, name, ipv4_prefix, str(parameters))
    return config_txt

def delete_address (eq_parameter, name, ipv4_prefix, parameters):
#    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''delete address with eq_parameter: %s name: %s ipv4_prefix: %s parameters: %s''' % (eq_parameter, name, ipv4_prefix, str(parameters))
    return config_txt

######## address-set  ##########

def create_address_set (eq_parameter, name,addresses, parameters):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = '%s' % address_element
        else:
            config_addresses = config_addresses + ' ' + '%s' % address_element

    config_addresses = '[ ' + config_addresses + ' ]'

    config_txt = '''create address-set with eq_parameter: %s name: %s addresses-list: %s parameters: %s''' % (eq_parameter, name, config_addresses, parameters)
    return config_txt

def delete_address_set (eq_parameter, name, addresses, parameters):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = '%s' % address_element
        else:
            config_addresses = config_addresses + ' ' + '%s' % address_element

    config_addresses = '[ ' + config_addresses + ' ]'

    config_txt = '''delete address-set with eq_parameter: %s name: %s addresses-list: %s parameters: %s''' % (eq_parameter, name, config_addresses, parameters)
    return config_txt


######### service (services) ###########

def create_service (eq_parameter, name, prot, ports, parameters):
    if (prot == '6'):
        prot_ = 'tcp'
    elif (prot == '17'):
        prot_ = 'udp'
    elif (prot == '1'):
        prot_ = 'icmp'
    else:
        prot_ = prot
    if 'lower-port' in ports:
        if (ports['lower-port'] < ports['upper-port']):
            ports_range = '%s-%s' % (ports['lower-port'], ports['upper-port'])
        else:
            ports_range = '%s' % ports['lower-port']
    else:
        ports_range = ''
    config_txt = '''create service with eq_parameter: %s name: %s protocol %s port %s parameters: %s''' % (eq_parameter, name, prot_, ports_range, parameters)

    return config_txt

def delete_service (eq_parameter, name, prot, ports, parameters):
    config_txt = '''delete service with eq_parameter: %s name: %s parameters: %s''' % (eq_parameter, name, parameters)
    return config_txt


######### service-set (services)  ###########

def create_service_set (eq_parameter, name, service, parameters):

    config_services = ''

    for service_element in service:
        if re.match(config_services, ''):
            config_services = '%s' % service_element
        else:
            config_services =  config_services + ' ' + '%s' % service_element

    config_services = '[ ' + config_services + ' ]'


    config_txt='''create service-set with eq_parameter: %s name: %s members: %s parameters: %s''' % (eq_parameter, name, config_services, parameters)

    return config_txt

def delete_service_set (eq_parameter, name, service, parameters):
    config_services = ''

    for service_element in service:
        if re.match(config_services, ''):
            config_services = '%s' % service_element
        else:
            config_services =  config_services + ' ' + '%s' % service_element

    config_services = '[ ' + config_services + ' ]'


    config_txt='''delete service-set with eq_parameter: %s name: %s parameters: %s''' % (eq_parameter, name, parameters)

    return config_txt

######### application-set (applications)  ###########

def create_application_set (eq_parameter, name, application, parameters):

    config_applications = ''

    for application_element in application:
        if re.match(config_applications, ''):
            config_applications = '%s' % application_element
        else:
            config_applications =  config_applications + ' ' + '%s' % application_element

    config_applications = '[ ' + config_applications + ' ]'


    config_txt='''create application-set with eq_parameter: %s name: %s members: %s parameters: %s''' % (eq_parameter, name, config_applications, parameters)

    return config_txt

def delete_application_set (eq_parameter, name, application, parameters):
    config_applications = ''

    for application_element in application:
        if re.match(config_applications, ''):
            config_applications = '%s' % application_element
        else:
            config_applications =  config_applications + ' ' + '%s' % application_element

    config_applications = '[ ' + config_applications + ' ]'


    config_txt='''delete application-set with eq_parameter: %s name %s parameters: %s''' % (eq_parameter, name, parameters)

    return config_txt


######### access ###########


def create_policy (eq_parameter, name, source_address_set_list, destination_address_set_list, application_set_list, service_set_list, src_str, dst_str, parameters, action ):
    config_access = ''
    config_match_source= ''
    config_match_destination = ''
    config_match_service = ''
    config_match_application = ''

    for source_address_set_element in source_address_set_list:
        if re.match(config_match_source, ''):
            config_match_source = '%s' % source_address_set_element["address-set-name"]
        else:
#            print source_address_set_element
            config_match_source = config_match_source + ' %s' % source_address_set_element["address-set-name"]

    config_match_source = '[ ' + config_match_source + ' ]'

    for destination_address_set_element in destination_address_set_list:
        if re.match(config_match_destination, ''):
            config_match_destination = '%s' % destination_address_set_element["address-set-name"]
        else:
            config_match_destination = config_match_destination + ' %s' % destination_address_set_element["address-set-name"]

    config_match_destination = '[ ' + config_match_destination + ' ]'

    for service_set_element in service_set_list:
        if re.match(config_match_service, ''):
            config_match_service = ' %s' % service_set_element
        else:
            config_match_service = config_match_service + ' %s' % service_set_element

    config_match_service = '[ ' + config_match_service + ' ]'

    for application_set_element in application_set_list:
        if re.match(config_match_application, ''):
            config_match_application = ' %s' % application_set_element
        else:
            config_match_application = config_match_application  + ' %s' % application_set_element

    config_match_application = '[ ' + config_match_application  + ' ]'

    config_txt_par = ''
    config_txt_addresses = ''
    config_txt_services = ''
    config_txt_applications = ''
    config_txt_action = ''

    config_txt_par = '''
create policy with eq_parameter: %s name: %s parameters: %s'''  % (eq_parameter, name, parameters)

    config_txt_addresses = '''
create policy with eq_parameter: %s name: %s src: %s dst: %s''' % (eq_parameter, name, config_match_source, config_match_destination )

    config_txt_services = '''
create policy with eq_parameter: %s name: %s service: %s''' % (eq_parameter, name, config_match_service) 

    config_txt_applications = '''
create policy with eq_parameter: %s name: %s application: %s''' % (eq_parameter, name, config_match_application)

    config_txt_action = '''
create policy with eq_parameter: %s name: %s action allow''' % (eq_parameter, name)

    config_txt = config_txt_par + config_txt_addresses + config_txt_applications + config_txt_services + config_txt_action

    return config_txt

def delete_policy (name, eq_parameter, parameters, source_address_set_list, destination_address_set_list, service_set_dicts,  status):
    config_txt = ''
    if (status == 'delete'):
        config_txt = '''
delete policy with eq_parameter: %s name: %s parameters: %s ''' % (eq_parameter, name, parameters)
    else:
        for source_address_set_element in source_address_set_list:
            config_txt_add = '''
delete policy with eq_parameter: %s name: %s parameters: %s src_address_set %s''' % (eq_parameter, name, parameters, source_address_set_element['address-set-name'])
            config_txt = config_txt + config_txt_add
        for destination_address_set_element in destination_address_set_list:
            config_txt_add = '''
delete policy with eq_parameter: %s name: %s parameters: %s dst_address_set %s''' % (eq_parameter, name, parameters, destination_address_set_element['address-set-name'])
            config_txt = config_txt+ config_txt_add

    return config_txt
