import re
import cidr_to_netmask

'''
The list of templates for pan
'''

######## vlan ###########


######## svi ###########


######## address  ###########

def pan_create_address (eq, name, ipv4_prefix, vlan, vrf):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''
set shared address %s ip-netwask %s/%s
''' % (name, network, netmask)
    return config_txt

def pan_delete_address (eq, name, ipv4_prefix, vlan, vrf):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''
delete shared address %s    
''' % name
    return config_txt

######## address-set  ##########

def pan_create_address_set (eq, name,addresses):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = '%s' % address_element
        else:
            config_addresses = config_addresses + ' ' + '%s' % address_element

    config_addresses = '[ ' + config_addresses + ' ]'

    config_txt = '''
set shared address-group %s static %s
''' % (name, config_addresses)
    return config_txt

def pan_delete_address_set (eq, name,addresses):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = '%s' % address_element
        else:
            config_addresses = config_addresses + ' ' + '%s' % address_element

    config_addresses = '[ ' + config_addresses + ' ]'

    config_txt = '''
delete shared address-group %s
''' % name
    return config_txt


######### application (services) ###########

def pan_create_application (eq, name, prot, ports):
    if (prot == '6'):
        prot_ = 'tcp'
    elif (prot == '17'):
        prot_ = 'udp'
    elif (prot == '1'):
        prot_ = 'icmp'
    else:
        prot_ = prot
    if 'lower-port' in ports:
        ports_range = '%s-%s' % (ports['lower-port'], ports['upper-port'])
    else:
        ports_range = ''
    config_txt = '''
set shared services %s protocol %s port %s
''' % ( name, prot_, ports_range)

    return config_txt

def pan_delete_application (eq, name, prot, ports):
    config_txt = '''
delete shared services %s''' % name
    return config_txt


######### application-set (services)  ###########

def pan_create_application_set (eq, name, application):

    config_applications = ''

    for application_element in application:
        if re.match(config_applications, ''):
            config_applications = '%s' % application_element
        else:
            config_applications =  config_applications + ' ' + '%s' % application_element

    config_applications = '[ ' + config_applications + ' ]'


    config_txt='''
set shared service-group %s member %s
''' % (name, config_applications)

    return config_txt

def pan_delete_application_set (eq, name, application):

    config_txt = '''
delete shared service-group %s
''' % name
    return config_txt

######### access ###########


def pan_create_policy_allapp_dst_oss_transit (eq, name, source_address_set_list, destination_address_set_list, application_set_list, src_dc, src_area, src_zone, src_sub_zone, dst_dc, dst_area, dst_zone, dst_sub_zone, action ):

    name = name + '_to_transit'
    config_txt = ''
    app_any = ['any']
    config_txt = pan_create_policy (eq, name, source_address_set_list, destination_address_set_list, app_any, src_dc, src_area, src_zone, src_sub_zone, dst_dc, dst_area, 'oss-transit', dst_sub_zone, action )
    
    return config_txt

def pan_create_policy_src_oss_transit (eq, name, source_address_set_list, destination_address_set_list, application_set_list, src_dc, src_area, src_zone, src_sub_zone, dst_dc, dst_area, dst_zone, dst_sub_zone, action ):

    name = name + '_from_transit'
    config_txt = ''
    config_txt = pan_create_policy (eq, name, source_address_set_list, destination_address_set_list, application_set_list, src_dc, src_area, 'oss-transit', src_sub_zone, dst_dc, dst_area, dst_zone, dst_sub_zone, action )

    return config_txt

def pan_create_policy_allapp_dst_inter_area (eq, name, source_address_set_list, destination_address_set_list, application_set_list, src_dc, src_area, src_zone, src_sub_zone, dst_dc, dst_area, dst_zone, dst_sub_zone, action ):

    name = name + '_to_transit'
    config_txt = ''
    app_any = ['any']
    config_txt = pan_create_policy (eq, name, source_address_set_list, destination_address_set_list, app_any, src_dc, src_area, src_zone, src_sub_zone, dst_dc, dst_area, 'inter-area-transit', dst_sub_zone, action )

    return config_txt

def pan_create_policy_src_inter_area (eq, name, source_address_set_list, destination_address_set_list, application_set_list, src_dc, src_area, src_zone, src_sub_zone, dst_dc, dst_area, dst_zone, dst_sub_zone, action ):

    name = name + '_from_transit'
    config_txt = ''
    config_txt = pan_create_policy (eq, name, source_address_set_list, destination_address_set_list, application_set_list, src_dc, src_area, 'inter-area-transit', src_sub_zone, dst_dc, dst_area, dst_zone, dst_sub_zone, action )

    return config_txt

def pan_delete_policy_allapp_dst_oss_transit (eq, name ):
    
    name = name + '_to_transit'
    config_txt = ''
#    app_any = ['any']
    config_txt = pan_delete_policy (eq, name)

    return config_txt

def pan_delete_policy_src_oss_transit (eq, name):

    name = name + '_from_transit'
    config_txt = ''
    config_txt = pan_delete_policy (eq, name)

    return config_txt

def pan_delete_policy_allapp_dst_inter_area (eq, name):

    name = name + '_to_transit'
    config_txt = ''
#    app_any = ['any']
    config_txt = pan_delete_policy (eq, name)

    return config_txt

def pan_delete_policy_src_inter_area (eq, name):

    name = name + '_from_transit'
    config_txt = ''
    config_txt = pan_delete_policy (eq, name)

    return config_txt

def pan_create_policy (eq, name, source_address_set_list, destination_address_set_list, application_set_list, src_dc, src_area, src_zone, src_sub_zone, dst_dc, dst_area, dst_zone, dst_sub_zone, action ):
    config_access = ''
    config_match_source= ''
    config_match_destination = ''
    config_match_application = ''

    for source_address_set_element in source_address_set_list:
        if re.match(config_match_source, ''):
            config_match_source = '%s' % source_address_set_element['address-set-name']
        else:
            config_match_source = config_match_source + ' %s' % source_address_set_element['address-set-name']

    config_match_source = '[ ' + config_match_source + ' ]'

    for destination_address_set_element in destination_address_set_list:
        if re.match(config_match_destination, ''):
            config_match_destination = '%s' % destination_address_set_element['address-set-name']
        else:
            config_match_destination = config_match_destination + ' %s' % destination_address_set_element['address-set-name']

    config_match_destination = '[ ' + config_match_destination + ' ]'

    for application_set_element in application_set_list:
        if re.match(config_match_application, ''):
            config_match_application = ' %s' % application_set_element
        else:
            config_match_application = config_match_application + ' %s' % application_set_element

    config_match_application = '[ ' + config_match_application + ' ]'

    config_txt_zone = ''
    config_txt_addresses = ''
    config_txt_applications = ''
    config_txt_action = ''

    config_txt_zone = '''
set device-group %s pre-rulebase security rules %s to %s
set device-group %s pre-rulebase security rules %s from %s''' % (eq, name, src_zone, eq, name, dst_zone)

    config_txt_addresses = '''
set device-group %s pre-rulebase security rules %s source %s
set device-group %s pre-rulebase security rules %s destination %s''' % (eq, name, config_match_source, eq, name, config_match_destination )

    config_txt_applications = '''
set device-group %s pre-rulebase security rules %s application %s
set device-group %s pre-rulebase security rules %s service %s''' % (eq, name, 'any', eq, name, config_match_application) 

    config_txt_action = '''
set device-group %s pre-rulebase security rules %s action allow''' % (eq, name)

    config_txt = config_txt_zone + config_txt_addresses + config_txt_applications + config_txt_action

    return config_txt

def pan_delete_policy (eq, name):

    config_txt = '''
delete device-group %s pre-rulebase security rules %s''' % (eq, name)

    return config_txt
