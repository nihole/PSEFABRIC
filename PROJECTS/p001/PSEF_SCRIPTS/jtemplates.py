import re

'''
The list of templates for juniper srx
'''

###################   policy   ###########################

def srx_create_policy (name, source_address_set_list, destination_address_set_list, application_list, action ):
#    eq_paramete, parameters are not used
    config_match_source = ''
    config_match_destination = ''
    config_match_application = ''

    

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
                            
    for application_element in application_list:
        if re.match(config_match_application, ''):
            config_match_application = '<application>%s</application>' % application_element
        else:
            config_match_application = config_match_application + '\n<application>%s</application>' % application_element

    config_match = config_match_source + '\n' + config_match_destination + '\n' + config_match_application   
    
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


def srx_delete_policy(name):
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

def srx_create_address (name, ipv4_prefix, vlan, vrf, interface):
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

def srx_delete_address (name, ipv4_prefix, vlan, vrf, interface):
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

############  application #############################

def srx_create_application (name, prot, ports):
    if 'lower-port' in ports:
        ports_range = '<destination-port>%s-%s</destination-port>' % (ports['lower-port'], ports['upper-port'])
    else:
        ports_range = ''
    config_xml = '''
<applications>
<application>
<name>%s</name>
<protocol>%s</protocol>
%s
</application>
</applications>''' % (name, prot, ports_range)
    return config_xml

def srx_delete_application (name, prot, ports):
    config_xml = '''
<applications>
<application operation='delete'>
<name>%s</name>
</application>
</applications>''' % name
    return config_xml



##############  application-set ########################

def srx_create_application_set (name, application):

    config_applications = ''

    for application_element in application:
        if re.match(config_applications, ''):
            config_applications = '<application>\n<name>%s</name>\n</application>' % application_element
        else:
            config_applications = config_applications + '\n' + '<application>\n<name>%s</name>\n</application>' % application_element


    config_xml='''
<applications>
<application-set>       
<name>%s</name>
%s
</application-set>
</applications>''' % (name, config_applications)
    return config_xml


def srx_delete_application_set (name, application):
    config_xml = '''
<applications>
<application-set operation='delete'>
<name>%s</name>
</application-set>
</applications>''' % name
    return config_xml
