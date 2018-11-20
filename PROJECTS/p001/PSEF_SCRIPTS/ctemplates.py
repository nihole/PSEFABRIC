import re
import cidr_to_netmask

'''
The list of templates for cisco
'''

######## vlan ###########

def cisco_create_vlan (name, ipv4_prefix, vlan, vrf, interface):
    config_txt = '''
vlan %s
name %s''' % (vlan, name)
    return config_txt

def cisco_delete_vlan (name, ipv4_prefix, vlan, vrf, interface):
    config_txt = '''
no vlan %s''' % vlan
    return config_txt

######## svi ###########

def cisco_create_svi (name, ipv4_prefix, vlan, vrf, interface):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    vrf_forw = ''
    if not vrf == 'none':
        vrf_forw = 'ip vrf forwarding %s\n' % vrf
    config_txt = '''
interface vlan%s
description %s
%sip address %s %s
no shut''' % (vlan, name, vrf_forw, gate, netmask) 
    return config_txt

def cisco_delete_svi (name, ipv4_prefix, vlan, vrf, interface):
    config_txt = '''
no interface vlan%s''' % vlan
    return config_txt

######## address  ###########

def cisco_create_address (name, ipv4_prefix, vlan, vrf, interface):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''
object-group network %s
%s %s''' % (name, network, netmask)
    return config_txt

def cisco_delete_address (name, ipv4_prefix, vlan, vrf, interface):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''
no object-group network %s''' % (name)

    return config_txt
def asa_create_address (name, ipv4_prefix, vlan, vrf, interface):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''
object-group network %s
network-object %s %s''' % (name, network, netmask)
    return config_txt

def asa_delete_address (name, ipv4_prefix, vlan, vrf, interface):
    network, netmask, gate = cidr_to_netmask.cidr_to_netmask(ipv4_prefix)
    config_txt = '''
no object-group network %s
object-group network %s
no network-object %s %s
no object-group network %s''' % (name, name, network, netmask, name)
    return config_txt


######## vlan_to_trunk ##########

def cisco_add_vlan_to_trunk (name, ipv4_prefix, vlan, vrf, interface):
    config_txt = ''
    if not (vlan == 'none' or interface == 'none'):
        config_txt = '''
interface %s
switchport trunk allowed vlan add %s''' % (interface, vlan)
    return config_txt


def cisco_remove_vlan_to_trunk (name, ipv4_prefix, vlan, vrf, interface):
    config_txt = ''
    if not (vlan == 'none' or interface == 'none'):
        config_txt = '''
interface %s
switchport trunk allowed vlan remove %s''' % (interface, vlan)
    return config_txt

######## address-set  ##########

def cisco_create_address_set (name,addresses):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = 'group-object %s' % address_element
        else:
            config_addresses = config_addresses + '\n' + 'group-object %s' % address_element
    config_txt = '''
object-group network %s
%s''' % (name, config_addresses)
    return config_txt

def cisco_delete_address_set (name,addresses):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = 'no group-object %s' % address_element
        else:
            config_addresses = config_addresses + '\n' + 'no group-object %s' % address_element
    config_txt = '''
no object-group network %s
object-group network %s
%s
no object-group network %s''' % (name, name, config_addresses,name)

    return config_txt



def asa_create_address_set (name,addresses):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = 'group-object %s' % address_element
        else:
            config_addresses = config_addresses + '\n' + 'group-object %s' % address_element
    config_txt = '''
object-group network %s
%s''' % (name, config_addresses)
    return config_txt

def asa_delete_address_set (name,addresses):
    config_addresses = ''
    for address_element in addresses:
        if ( config_addresses == ''):
            config_addresses = 'no group-object %s' % address_element
        else:
            config_addresses = config_addresses + '\n' + 'no group-object %s' % address_element

    config_txt = '''
object-group network %s
%s
no object-group network %s
no object-group network %s''' % (name, config_addresses, name, name)
    return config_txt
######### service ###########

def cisco_create_service (name, prot, ports):
    if (prot == '6'):
        prot_ = 'tcp'
    elif (prot == '17'):
        prot_ = 'udp'
    elif (prot == '1'):
        prot_ = 'icmp'
    else:
        prot_ = prot
    if 'lower-port' in ports:
        ports_range = 'range %s %s' % (ports['lower-port'], ports['upper-port'])
    else:
        ports_range = ''
    config_txt = '''
object-group service %s
%s %s''' % ( name, prot_, ports_range)

    return config_txt

def cisco_delete_service (name, prot, ports):
    config_txt = '''
no object-group service %s''' % name
    return config_txt


def asa_create_service (name, prot, ports):
    if (prot == '6'):
        prot_ = 'tcp'
    elif (prot == '17'):
        prot_ = 'udp'
    elif (prot == '1'):
        prot_ = 'icmp'
    else:
        prot_ = prot
    if 'lower-port' in ports:
        ports_range = 'destination range %s %s' % (ports['lower-port'], ports['upper-port'])
    else:
        ports_range = ''
    config_txt = '''
object-group service %s
service-object %s %s''' % (name, prot_, ports_range)

    return config_txt

def asa_delete_service (name, prot, ports):
    config_txt = '''
no object-group service %s''' % name
    return config_txt


######### service-set  ###########

def cisco_create_service_set (name, service):

    config_services = ''

    for service_element in service:
        if re.match(config_services, ''):
            config_services = 'group-object %s' % service_element
        else:
            config_services = config_services + '\n' + 'group-object %s' % service_element


    config_txt='''
object-group service %s
%s''' % (name, config_services)

    return config_txt

def cisco_delete_service_set (name, service):

    config_services = ''

    for service_element in service:
        if re.match(config_services, ''):
            config_services = 'no group-object %s' % service_element
        else:
            config_services = config_services + '\n' + 'no group-object %s' % service_element


    config_txt='''
no object-group service %s
object-group service %s
%s
no object-group service %s''' % (name, name, config_services, name)

    return config_txt



def asa_create_service_set (name, service):

    config_services = ''

    for service_element in service:
        if re.match(config_services, ''):
            config_services = 'group-object %s' % service_element
        else:
            config_services = config_services + '\n' + 'group-object %s' % service_element


    config_txt='''
object-group service %s
%s''' % (name, config_services)

    return config_txt

def asa_delete_service_set (name, service):

    config_services = ''

    for service_element in service:
        if re.match(config_services, ''):
            config_services = 'no group-object %s' % service_element
        else:
            config_services = config_services + '\n' + 'no group-object %s' % service_element


    config_txt='''
no object-group service %s
object-group service %s
%s
no object-group service %s''' % (name, name, config_services, name)

    return config_txt



######### access ###########

def cisco_create_access (name, source_address_set_list, destination_address_set_list, service_list, action ):
    config_access = ''

    for source_address_set_element in source_address_set_list:
        for destination_address_set_element in destination_address_set_list:
            for service_element in service_list:
                config_access = config_access +  'permit object-group %s object-group %s object-group %s\n' % (service_element, source_address_set_element['address-set-name'], destination_address_set_element['address-set-name'])


    config_txt = '''
ip access-list extended all_vlans_out
%s''' % config_access

    return config_txt

def cisco_delete_access (name, source_address_set_list, destination_address_set_list, service_list, action ):
    config_access = ''

    for source_address_set_element in source_address_set_list:
        for destination_address_set_element in destination_address_set_list:
            for service_element in service_list:
                config_access = config_access +  'no permit object-group %s object-group %s object-group %s\n' % (service_element, source_address_set_element['address-set-name'], destination_address_set_element['address-set-name'])

    config_txt = '''
ip access-list extended all_vlans_out
%s''' % config_access
    return config_txt  

def zbf_create_policy (name, source_address_set_list, destination_address_set_list, service_list, action ):
    config_access = ''

    for source_address_set_element in source_address_set_list:
        for destination_address_set_element in destination_address_set_list:
            for service_element in service_list:
                config_access = config_access +  'permit object-group %s object-group %s object-group %s\n' % (service_element, source_address_set_element['address-set-name'], destination_address_set_element['address-set-name'])


    config_txt = '''
ip access-list extended vpn-to-trust
%s''' % config_access

    return config_txt

def zbf_delete_policy (name, source_address_set_list, destination_address_set_list, service_list, action ):
    config_access = ''

    for source_address_set_element in source_address_set_list:
        for destination_address_set_element in destination_address_set_list:
            for service_element in service_list:
                config_access = config_access +  'no permit object-group %s object-group %s object-group %s\n' % (service_element, source_address_set_element['address-set-name'], destination_address_set_element['address-set-name'])

    config_txt = '''
ip access-list extended vpn-to-trust
%s''' % config_access

    return config_txt
  

def asa_create_access (name, source_address_set_list, destination_address_set_list, service_list, action ):
    config_access = ''

    for source_address_set_element in source_address_set_list:
        for destination_address_set_element in destination_address_set_list:
            for service_element in service_list:
                config_access = config_access +  'access-list all_zones_out extended permit object-group %s object-group %s object-group %s\n' % (service_element, source_address_set_element['address-set-name'], destination_address_set_element['address-set-name'])


    config_txt = '''
%s''' % config_access

    return config_txt

def asa_delete_access (name, source_address_set_list, destination_address_set_list, service_list, action ):
    config_access = ''

    for source_address_set_element in source_address_set_list:
        for destination_address_set_element in destination_address_set_list:
            for service_element in service_list:
                config_access = config_access +  'no access-list all_zones_out extended permit object-group %s object-group %s object-group %s\n' % (service_element, source_address_set_element['address-set-name'], destination_address_set_element['address-set-name'])

    config_txt = '''
ip access-list extended all_vlans_out
%s''' % config_access

    return config_txt
