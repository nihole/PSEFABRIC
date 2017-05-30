'''
'''
import mult_cfg
import ctemplates
import jtemplates

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
        rm address-set
        rm address
        rm application-set
        rm application
        add application
        add application-set
        add address
        add address-set
        add policy
        '''

# rm policy

        if len(cmd_for_host[eq_name]['rm']['policy']):
            policy_list = remove_doubled_names(cmd_for_host[eq_name]['rm']['policy'])
            for el in policy_list:
                for command_element in el['command-list']:
                    cfg_new = eval(command_element + "(el['name'],el['source-addresses'],el['destination-addresses'],el['applications'],'permit')")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# rm address-set

        if len(cmd_for_host[eq_name]['rm']['address-set']):
            for el in cmd_for_host[eq_name]['rm']['address-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['name'],el['address'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# rm address

        if len(cmd_for_host[eq_name]['rm']['address']):
            for el in cmd_for_host[eq_name]['rm']['address']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['name'],el['ipv4-prefix'],el['structure']['vlan'], el['structure']['vrf'], el['structure']['interface'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# rm application-set

        if len(cmd_for_host[eq_name]['rm']['application-set']):
            for el in cmd_for_host[eq_name]['rm']['application-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['name'],el['application'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# rm application

        if len(cmd_for_host[eq_name]['rm']['application']):
            for el in cmd_for_host[eq_name]['rm']['application']:
                for command_element in el['command-list']:
                    if 'ports' in el:
                        cfg_new = eval (command_element + "(el['name'],el['prot'],el['ports']['destination-port-range'])")
                    else:
                        cfg_new = eval(command_element + "(el['name'],el['prot'],{})")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add applcation

        if len(cmd_for_host[eq_name]['ad']['application']):
            for el in cmd_for_host[eq_name]['ad']['application']:
                for command_element in el['command-list']:
                    if 'ports' in el:
                        cfg_new = eval (command_element + "(el['name'],el['prot'],el['ports']['destination-port-range'])")
                    else:
                        cfg_new = eval(command_element + "(el['name'],el['prot'],{})")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add application-set

        if len(cmd_for_host[eq_name]['ad']['application-set']):
            for el in cmd_for_host[eq_name]['ad']['application-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['name'],el['application'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add address

        if len(cmd_for_host[eq_name]['ad']['address']):
            for el in cmd_for_host[eq_name]['ad']['address']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['name'],el['ipv4-prefix'],el['structure']['vlan'], el['structure']['vrf'], el['structure']['interface'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add address-set

        if len(cmd_for_host[eq_name]['ad']['address-set']):
            for el in cmd_for_host[eq_name]['ad']['address-set']:
                for command_element in el['command-list']:
                    cfg_new = eval (command_element + "(el['name'],el['address'])")
                    cfg[eq_name] = cfg[eq_name] + '\n' + cfg_new
                    cfg_new = ''

# add policy


        if len(cmd_for_host[eq_name]['ad']['policy']):
            policy_list = cmd_for_host[eq_name]['ad']['policy']
            for el in policy_list:
                for command_element in el['command-list']:
                    cfg_new = eval(command_element + "(el['name'],el['source-addresses'],el['destination-addresses'],el['applications'],'permit')")
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
