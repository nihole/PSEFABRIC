    ######################################
    #                                    #
    #                  4.                #
    #        configurator layer          #
    #                                    #
    ######################################



'''
For different MOs (Management Objects) different configuration formats may be used. 
For example:

- api: json/xml/netconf/..
- cli: text
- without candidate config (for example cisco-like interface)
- with candidate config (for example juniper or palo-alto interface)
- ...

To provide correct configuration for different cases 2 dictionaries are taken from demultiplexer layer (3):

- cmd_for_host_diff
- cmd_for_host_full

If we have candidate configuration feature (changes are implemented only after committing the configuration) then cmd_for_host_full is enough. For each changed object we may remove it and implement a new configuration for this object.

But if we don't have candidate configuration feature then we have to remove only objects we are going to remove (not to change). For this purpose cmd_for_host_diff is used for removing and cmd_for_host_full for creation.

'''

import re
import mult_cfg
import ptemplates
import ptemplates
import host_to_type

cfg = {}
def create_configs (cmd_for_host_diff, cmd_for_host_full):

##########  Description  #######
    '''
    Extracts data from dict cmd_for_host and transforms it into configuration lines using templates.
    '''
#############  BODY ############ 
    
    host = host_to_type.host_to_type()

    for eq_name in cmd_for_host_full:
        cfg[eq_name] = ''

        '''
        Sequence is important. But it also can be changed if necessary on "configuration excapsulator laer". This sequence we will have in our configuration files.
       
        rm policy
        rm address-set
        rm address
        rm service-set
        rm service
        rm application
        rm application-set
        add service
        add service-set
        add application
        add application-set
        add address
        add address-set
        add policy
        '''

# rm policy
# In our example panorama_1 equipment have a configuration interface with possibility of candidate config. 
# It meens that to change configuration of the object we may remove old and create a new object
# cmd_for_host_full dict is used for this purpose

        if (re.search('panorama', host[eq_name])):
            if (cmd_for_host_full[eq_name]['rm']['policy']):
                policy_list = cmd_for_host_full[eq_name]['rm']['policy']
                for el in policy_list:
                    for command_element in el['command-list']:
                        cfg_new = eval(command_element + "(el['eq_parameter'], el['name'], el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# In our example panorama_2 equipment don't have candidate config feature. 
# It meens that to change configuration of the object if we need to delete something we have to delete exactly what we need to delete (no more)
# cmd_for_host_diff dict is used for this purpose

        if (re.search('aci', host[eq_name])):
            if (cmd_for_host_diff[eq_name]['rm']['policy']):
                policy_list_rm = cmd_for_host_diff[eq_name]['rm']['policy']
                for el_rm in policy_list_rm:
                    if (cmd_for_host_full[eq_name]['ad']['policy']):
                        policy_ad_list = cmd_for_host_full[eq_name]['ad']['policy']
                        for el_ad in policy_ad_list:
                            if el_rm['name'] in el_ad.itervalues():
                                status = 'change'
                            else:
                                status = 'delete'
                    else:
                        status = 'delete'
                    for command_element in el_rm['command-list']:
                        cfg_new = eval(command_element + "(el_rm['name'], el_rm['eq_parameter'], el_rm['parameters'], el_rm['source-address-sets'], el_rm['destination-address-sets'], el_rm['service-set-dicts'], status)")
                        if cfg_new:
                            cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# rm address-set
        if (re.search('panorama', host[eq_name])):
            if (cmd_for_host_diff[eq_name]['rm']['address-set']):
                for el in cmd_for_host_full[eq_name]['rm']['address-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['address-list'], el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# rm address
        if (re.search('panorama', host[eq_name])):
            if (cmd_for_host_diff[eq_name]['rm']['address']):
                for el in cmd_for_host_diff[eq_name]['rm']['address']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['ipv4-prefix'], el['parameters'])")
                        if cfg_new:
                            cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
    
# rm service-set
        if (re.search('panorama', host[eq_name])):
            if (cmd_for_host_diff[eq_name]['rm']['service-set']):
                for el in cmd_for_host_full[eq_name]['rm']['service-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['service-list'],el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
# rm service
        if (re.search('panorama', host[eq_name])):
            if (cmd_for_host_diff[eq_name]['rm']['service']):
                for el in cmd_for_host_diff[eq_name]['rm']['service']:
                    for command_element in el['command-list']:
                        if 'ports' in el:
                            cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['prot'],el['ports']['destination-port-range'], el['parameters'])")
                        else:
                            cfg_new = eval(command_element + "(el['eq_parameter'], el['name'],el['prot'],{},el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''


# rm application-set
        if (re.search('panorama', host[eq_name])):
            if (cmd_for_host_diff[eq_name]['rm']['application-set']):
                for el in cmd_for_host_full[eq_name]['rm']['application-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['application-list'],el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

## rm application
#        if (eq_name == 'panorama'):
#            if (cmd_for_host_diff[eq_name]['rm']['application']):
#                for el in cmd_for_host_full[eq_name]['rm']['application']:
#                    for command_element in el['command-list']:
#                        if 'ports' in el:
#                            cfg_new = eval (command_element + "(el['eq_parameter'], el['app_par_3'],el['prot'],el['ports']['destination-port-range'])")
#                        else:
#                            cfg_new = eval(command_element + "(el['eq_parameter'], el['app_par_3'],el['prot'],{})")
#                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
#                        cfg_new = ''

# add service
        if (re.search('panorama', host[eq_name])):
            if len(cmd_for_host_full[eq_name]['ad']['service']):
                for el in cmd_for_host_full[eq_name]['ad']['service']:
                    for command_element in el['command-list']:
                        if 'ports' in el:
                            cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['prot'],el['ports']['destination-port-range'],el['parameters'])")
                        else:
                            cfg_new = eval(command_element + "(el['eq_parameter'], el['name'],el['prot'],{},el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# add service-set
        if (re.search('panorama', host[eq_name])):
            if len(cmd_for_host_full[eq_name]['ad']['service-set']):
                for el in cmd_for_host_full[eq_name]['ad']['service-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['service-list'], el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# add application-set
        if (re.search('panorama', host[eq_name])):
            if len(cmd_for_host_full[eq_name]['ad']['application-set']):
                for el in cmd_for_host_full[eq_name]['ad']['application-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['application-list'], el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''


# add address
        if (re.search('panorama', host[eq_name])):
            if len(cmd_for_host_full[eq_name]['ad']['address']):
                for el in cmd_for_host_full[eq_name]['ad']['address']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['ipv4-prefix'], el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# add address-set
        if (re.search('panorama', host[eq_name])):
            if len(cmd_for_host_full[eq_name]['ad']['address-set']):
                for el in cmd_for_host_full[eq_name]['ad']['address-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['address-list'], el['parameters'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# add policy

        if (re.search('panorama', host[eq_name]) or re.search('aci', host[eq_name])):
            if len(cmd_for_host_full[eq_name]['ad']['policy']):
                policy_list = cmd_for_host_full[eq_name]['ad']['policy']
                for el in policy_list:
                    for command_element in el['command-list']:
                        cfg_new = eval(command_element + "(el['eq_parameter'], el['name'],el['source-address-sets'],el['destination-address-sets'],el['application-sets'],el['service-sets'],el['src_str'],el['dst_str'],el['parameters'],'permit')")
                        if cfg_new:
                            cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
    return cfg

def remove_doubled_names(mylist):

##########  Description  #######
    '''
    For removing doubled policy configurations
    '''
#############  BODY ############
    newlist = []
    namelist = []
    for i in mylist:
        if i['name'] not in namelist:
            newlist.append(i)
            namelist.append(i['name'])
    return newlist
