import re

'''
The list of templates for juniper srx
'''

###################   policy   ###########################

def srx_create_policy (name, source_address_set_list, destination_address_set_list, service_list, action ):
    config_match_source = ''
    config_match_destination = ''
    config_match_service = ''
    

    for source_address_set_element in source_address_set_list:
        if re.match(config_match_source, ''):
            config_match_source = '<source-address>%s</source-address>' % source_address_set_element['address-set-name'] 
        else:
            config_match_source = config_match_source + '\n<source-address>%s</source-address>' % source_address_set_element['address-set-name']
           
    for destination_address_set_element in destination_address_set_list:
        if re.match(config_match_destination, ''):
            config_match_destination = '<destination-address>%s</destination-address>' % destination_address_set_element['address-set-name'] 
        else:
            config_match_destination = config_match_destination + '\n<destination-address>%s</destination-address>' % destination_address_set_element['address-set-name']
                            
    for service_element in service_list['service-set']:
        if re.match(config_match_service, ''):
            config_match_service = '<service>%s</service>' % service_element
        else:
            config_match_service = config_match_service + '\n<service>%s</service>' % service_element

    config_match = config_match_source + '\n' + config_match_destination + '\n' + config_match_service   
    
    config_xml = '''
<security>
<policies> 
<global>            
<policy>        
<name>%s</name>
<match> 
%s
</match>    
<then>      
<permit>
</permit>
</then>
</policy>
</global>
</policies>
</security> ''' % (name, config_match) 
    return config_xml


def srx_delete_policy(name, source_address_set_list, destination_address_set_list, service_list, action ):
    config_xml ='''
<security>
<policies> 
<global>            
<policy operation='delete'>        
<name>%s</name>
</policy>
</global>
</policies> 
</security>''' % name
    return config_xml


###############  address  ###############################

def srx_create_address (name, ipv4_prefix, vlan, vrf):
    config_xml = '''
<security>
<address-book>
<name>global</name>
<address>
<name>%s</name>
<ip-prefix>%s</ip-prefix>
</address>
</address-book>
</security>''' % (name, ipv4_prefix)
    return config_xml

def srx_delete_address (name, ipv4_prefix, vlan, vrf):
    config_xml = '''
<security>
<address-book>
<name>global</name>
<address operation='delete'>
<name>%s</name>
</address>
</address-book>
</security>''' % name
    return config_xml


################  address-set  ##########################

def srx_create_address_set (name,addresses):

    config_addresses = ''

    for address_element in addresses:
        if re.match(config_addresses, ''):
            config_addresses = '<address>\n<name>%s</name>\n</address>' % address_element
        else:
            config_addresses = config_addresses + '\n' + '<address>\n<name>%s</name>\n</address>' % address_element


    config_xml='''
<security>
<address-book>
<name>global</name>
<address-set>       
<name>%s</name>
%s
</address-set>
</address-book>
</security>''' % (name, config_addresses)
    return config_xml


def srx_delete_address_set (name, addresses):
    config_xml = '''
<security>
<address-book>
<name>global</name>
<address-set operation='delete'>
<name>%s</name>
</address-set>
</address-book>
</security>''' % name
    return config_xml

############  service #############################

def srx_create_service (name, prot, ports):
    if 'lower-port' in ports:
        ports_range = '<destination-port>%s-%s</destination-port>' % (ports['lower-port'], ports['upper-port'])
    else:
        ports_range = ''
    config_xml = '''
<services>
<service>
<name>%s</name>
<protocol>%s</protocol>
%s
</service>
</services>''' % (name, prot, ports_range)
    return config_xml

def srx_delete_service (name, prot, ports):
    config_xml = '''
<services>
<service operation='delete'>
<name>%s</name>
</service>
</services>''' % name
    return config_xml



##############  service-set ########################

def srx_create_service_set (name, service):

    config_services = ''

    for service_element in service:
        if re.match(config_services, ''):
            config_services = '<service>\n<name>%s</name>\n</service>' % service_element
        else:
            config_services = config_services + '\n' + '<service>\n<name>%s</name>\n</service>' % service_element


    config_xml='''
<services>
<service-set>       
<name>%s</name>
%s
</service-set>
</services>''' % (name, config_services)
    return config_xml


def srx_delete_service_set (name, service):
    config_xml = '''
<services>
<service-set operation='delete'>
<name>%s</name>
</service-set>
</services>''' % name
    return config_xml
