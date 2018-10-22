'''
'''

import re
import mult_cfg
import ptemplates
import acitemplates

cfg = {}
def create_configs (cmd_for_host, cmd_for_host_full):

##########  Description  #######
    '''
    Extracts data from dict cmd_for_host and transforms it into configuration lines using templates.
    '''
#############  BODY ############ 

    for eq_name in cmd_for_host_full:
        cfg[eq_name] = ''

        '''
        Sequence is important. This sequence we will have in our configuration files.
       
        rm policy
        add service
        add service-set
        add application
        add application-set
        add address
        add address-set
        rm address-set
        rm address
        rm service-set
        rm service
        rm application
        rm application-set
        add policy
        '''

# rm policy
        if (eq_name == 'panorama'):
            if (cmd_for_host_full[eq_name]['rm']['policy']):
                policy_list = cmd_for_host_full[eq_name]['rm']['policy']
                for el in policy_list:
                    for command_element in el['command-list']:
                        cfg_new = eval(command_element + "(el['eq_parameter'], el['policy-alias-1'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
        if (re.search('aci_', eq_name)):
            if (cmd_for_host[eq_name]['rm']['policy']):
                policy_list = cmd_for_host[eq_name]['rm']['policy']
                j = 0
                for el in policy_list:
                    if (cmd_for_host[eq_name]['ad']['policy']):
                        policy_ad_list = cmd_for_host[eq_name]['ad']['policy']
                        for el_ad in policy_ad_list:
                            if el['name'] in el_ad.itervalues():
                                status = 'change'
                            else:
                                status = 'delete'
                    else:
                        status = 'delete'
                    for command_element in el['command-list']:
                        cfg_new = eval(command_element + "(el['policy-alias-2'], el['source-address-sets'], el['destination-address-sets'], el['service-set-dicts'], 'permit', status)")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
                j = j + 1


# add service
        if (eq_name == 'panorama'):
            if len(cmd_for_host_full[eq_name]['ad']['service']):
                for el in cmd_for_host_full[eq_name]['ad']['service']:
                    for command_element in el['command-list']:
                        if 'ports' in el:
                            cfg_new = eval (command_element + "(el['eq_parameter'], el['service-alias-1'],el['prot'],el['ports']['destination-port-range'])")
                        else:
                            cfg_new = eval(command_element + "(el['eq_parameter'], el['service-alias-1'],el['prot'],{})")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# add service-set
        if (eq_name == 'panorama'):
            if len(cmd_for_host_full[eq_name]['ad']['service-set']):
                for el in cmd_for_host_full[eq_name]['ad']['service-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['service-set-alias-1'],el['service'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# add application-set
        if (eq_name == 'panorama'):
            if len(cmd_for_host_full[eq_name]['ad']['application-set']):
                for el in cmd_for_host_full[eq_name]['ad']['application-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['application'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''


# add address
        if (eq_name == 'panorama'):
            if len(cmd_for_host_full[eq_name]['ad']['address']):
                for el in cmd_for_host_full[eq_name]['ad']['address']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['address-alias-1'],el['ipv4-prefix'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# add address-set
        if (eq_name == 'panorama'):
            if len(cmd_for_host_full[eq_name]['ad']['address-set']):
                for el in cmd_for_host_full[eq_name]['ad']['address-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['address-set-alias-1'],el['address'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''


# rm address-set
        if (eq_name == 'panorama'):
            if (cmd_for_host[eq_name]['rm']['address-set']):
                for el in cmd_for_host[eq_name]['rm']['address-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['address-set-alias-1'],el['address'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''

# rm address
        if (eq_name == 'panorama'):
            if (cmd_for_host[eq_name]['rm']['address']):
                for el in cmd_for_host[eq_name]['rm']['address']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['address-alias-1'],el['ipv4-prefix'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
    
# rm service-set
        if (eq_name == 'panorama'):
            if (cmd_for_host[eq_name]['rm']['service-set']):
                for el in cmd_for_host[eq_name]['rm']['service-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['service-set-alias-1'],el['service'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
# rm service
        if (eq_name == 'panorama'):
            if (cmd_for_host[eq_name]['rm']['service']):
                for el in cmd_for_host[eq_name]['rm']['service']:
                    for command_element in el['command-list']:
                        if 'ports' in el:
                            cfg_new = eval (command_element + "(el['eq_parameter'], el['service-alias-1'],el['prot'],el['ports']['destination-port-range'])")
                        else:
                            cfg_new = eval(command_element + "(el['eq_parameter'], el['service-alias-1'],el['prot'],{})")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''


# rm application-set
        if (eq_name == 'panorama'):
            if (cmd_for_host[eq_name]['rm']['application-set']):
                for el in cmd_for_host[eq_name]['rm']['application-set']:
                    for command_element in el['command-list']:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['application'])")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''


# add policy

        if (eq_name == 'panorama'):
            if len(cmd_for_host_full[eq_name]['ad']['policy']):
                policy_list = cmd_for_host_full[eq_name]['ad']['policy']
                for el in policy_list:
                    for command_element in el['command-list']:
                        cfg_new = eval(command_element + "(el['eq_parameter'], el['policy-alias-1'],el['source-address-sets'],el['destination-address-sets'],el['application-sets'],el['service-sets'],el['src_dc'], el['src_area'], el['src_zone'], el['dst_dc'], el['dst_area'], el['dst_zone'], 'permit')")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
        if (re.search('aci_', eq_name)):
            if len(cmd_for_host_full[eq_name]['ad']['policy']):
                policy_list = cmd_for_host_full[eq_name]['ad']['policy']
                j = 0
                for el in policy_list:
                    for command_element in el['command-list']:
                        cfg_new = eval(command_element + "(el['policy-alias-2'], el['source-address-sets'],el['destination-address-sets'],el['service-set-dicts'], 'permit')")
                        cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                        cfg_new = ''
                    j = j + 1

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
