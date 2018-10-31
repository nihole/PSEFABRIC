

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

import re

def pa_cli_correction(cfg_txt):

    cmd_list = sorted(set(cfg_txt.splitlines()))
    cmd_seq = {}
    cmd_seq['rm_policy'] = []
    cmd_seq['rm_address_set'] = []
    cmd_seq['rm_address'] = []
    cmd_seq['rm_service_set'] = []
    cmd_seq['rm_service'] = []
    cmd_seq['rm_application_set'] = []
    cmd_seq['rm_application'] = []
    cmd_seq['add_service'] = []
    cmd_seq['add_service_set'] = []
    cmd_seq['add_application'] = []
    cmd_seq['add_application_set'] = []
    cmd_seq['add_address'] = []
    cmd_seq['add_address_set'] = []
    cmd_seq['add_policy'] = []

    for line in cmd_list:
        if (re.search('^delete.*security rules', line)):
            cmd_seq['rm_policy'].append(line)
        elif (re.search('^set.*security rules', line)):
            cmd_seq['add_policy'].append(line)

        elif (re.search('^delete.*service-group', line)):
            cmd_seq['rm_service_set'].append(line)
        elif (re.search('^set.*service-group', line)):
            cmd_seq['add_service_set'].append(line)
        
        elif (re.search('^delete.*application-group', line)):
            cmd_seq['rm_application_set'].append(line)
        elif (re.search('^set.*application-group', line)):
            cmd_seq['add_application_set'].append(line)
        
        elif (re.search('^delete.*address-group', line)):
            cmd_seq['rm_address_set'].append(line)
        elif (re.search('^set.*address-group', line)):
            cmd_seq['add_address_set'].append(line)
        
        elif (re.search('^delete.*service', line)):
            cmd_seq['rm_service'].append(line)
        elif (re.search('^set.*service', line)):
            cmd_seq['add_service'].append(line)

        elif (re.search('^delete.*application', line)):
            cmd_seq['rm_application'].append(line)
        elif (re.search('^set.*address', line)):
            cmd_seq['add_application'].append(line)

        elif (re.search('^delete.*address', line)):
            cmd_seq['rm_address'].append(line)
        elif (re.search('^set.*address', line)):
            cmd_seq['add_address'].append(line)

    cmd_list_new = []

    cmd_list_new = cmd_seq['rm_policy'] + cmd_seq['rm_address_set'] + cmd_seq['rm_service_set'] + cmd_seq['rm_application_set'] \
    + cmd_seq['rm_address'] + cmd_seq['rm_service'] + cmd_seq['rm_application'] \
    + cmd_seq['add_application'] + cmd_seq['add_service'] + cmd_seq['add_address'] \
    + cmd_seq['add_application_set'] + cmd_seq['add_service_set'] + cmd_seq['add_address_set'] + cmd_seq['add_policy']
        

    return '\n'.join(cmd_list_new)

