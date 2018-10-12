'''
'''
import mult_cfg
import ptemplates

cfg = {}
def create_configs (cmd_for_host):

##########  Description  #######
    '''
    Extracts data from dict cmd_for_host and transforms it into configuration lines using templates.
    '''
#############  BODY ############ 

    for eq_name in cmd_for_host:
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
        if len(cmd_for_host[eq_name]['rm']['policy']):
            policy_list = remove_doubled_names(cmd_for_host[eq_name]['rm']['policy'])
            for el in policy_list:
                for command_element in el['command-list']:
                    cfg_new = eval(command_element + "(el['eq_parameter'], el['policy-alias-1'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add service

        if len(cmd_for_host[eq_name]['ad']['service']):
            for el in cmd_for_host[eq_name]['ad']['service']:
                for command_element in el['command-list']:
                    if 'ports' in el:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['service-alias-1'],el['prot'],el['ports']['destination-port-range'])")
                    else:
                        cfg_new = eval(command_element + "(el['eq_parameter'], el['service-alias-1'],el['prot'],{})")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add service-set

        if len(cmd_for_host[eq_name]['ad']['service-set']):
            for el in cmd_for_host[eq_name]['ad']['service-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['eq_parameter'], el['service-set-alias-1'],el['service'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add application-set


        if len(cmd_for_host[eq_name]['ad']['application-set']):
            for el in cmd_for_host[eq_name]['ad']['application-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['application'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''


# add address

        if len(cmd_for_host[eq_name]['ad']['address']):
            for el in cmd_for_host[eq_name]['ad']['address']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['eq_parameter'], el['address-alias-1'],el['ipv4-prefix'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add address-set

        if len(cmd_for_host[eq_name]['ad']['address-set']):
            for el in cmd_for_host[eq_name]['ad']['address-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['eq_parameter'], el['address-set-alias-1'],el['address'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''



# rm address-set

        if len(cmd_for_host[eq_name]['rm']['address-set']):
            for el in cmd_for_host[eq_name]['rm']['address-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['eq_parameter'], el['address-set-alias-1'],el['address'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# rm address

        if len(cmd_for_host[eq_name]['rm']['address']):
            for el in cmd_for_host[eq_name]['rm']['address']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['eq_parameter'], el['address-alias-1'],el['ipv4-prefix'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# rm service-set

        if len(cmd_for_host[eq_name]['rm']['service-set']):
            for el in cmd_for_host[eq_name]['rm']['service-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['eq_parameter'], el['service-set-alias-1'],el['service'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# rm service

        if len(cmd_for_host[eq_name]['rm']['service']):
            for el in cmd_for_host[eq_name]['rm']['service']:
                for command_element in el['command-list']:
                    if 'ports' in el:
                        cfg_new = eval (command_element + "(el['eq_parameter'], el['service-alias-1'],el['prot'],el['ports']['destination-port-range'])")
                    else:
                        cfg_new = eval(command_element + "(el['eq_parameter'], el['service-alias-1'],el['prot'],{})")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''


# rm application-set

        if len(cmd_for_host[eq_name]['rm']['application-set']):
            for el in cmd_for_host[eq_name]['rm']['application-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['eq_parameter'], el['name'],el['application'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''


# add policy


        if len(cmd_for_host[eq_name]['ad']['policy']):
            policy_list = cmd_for_host[eq_name]['ad']['policy']
            for el in policy_list:
                for command_element in el['command-list']:
                    cfg_new = eval(command_element + "(el['eq_parameter'], el['policy-alias-1'],el['source-addresses'],el['destination-addresses'],el['applications'],el['services'],el['src_dc'], el['src_area'], el['src_zone'], el['dst_dc'], el['dst_area'], el['dst_zone'], 'permit')")
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
