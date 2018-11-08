

'''
        Sequence is important. This sequence we will have in our configuration files.
       
        rm policy
        rm address-create
        rm address
        rm service-create
        rm service
        rm application
        rm application-create
        rm policy
        add service
        add service-create
        add application
        add application-create
        add address
        add address-create
        add policy
'''

import re

def ex_cli_correction(cfg_txt):

    # remove dublicated lines:
    
    cmd_list = sorted(set(cfg_txt.splitlines()))

# restore correct order:

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
        if (re.search('^delete policy', line)):
            cmd_seq['rm_policy'].append(line)
        elif (re.search('^create policy', line)):
            cmd_seq['add_policy'].append(line)

        elif (re.search('^delete service-set', line)):
            cmd_seq['rm_service_set'].append(line)
        elif (re.search('^create service-set', line)):
            cmd_seq['add_service_set'].append(line)
        
        elif (re.search('^delete application-set', line)):
            cmd_seq['rm_application_set'].append(line)
        elif (re.search('^create application-set', line)):
            cmd_seq['add_application_set'].append(line)
        
        elif (re.search('^delete address-set', line)):
            cmd_seq['rm_address_set'].append(line)
        elif (re.search('^create address-set', line)):
            cmd_seq['add_address_set'].append(line)
        
        elif (re.search('^delete service', line)):
            cmd_seq['rm_service'].append(line)
        elif (re.search('^create service', line)):
            cmd_seq['add_service'].append(line)

        elif (re.search('^delete application', line)):
            cmd_seq['rm_application'].append(line)
        elif (re.search('^create address', line)):
            cmd_seq['add_application'].append(line)

        elif (re.search('^delete address', line)):
            cmd_seq['rm_address'].append(line)
        elif (re.search('^create address', line)):
            cmd_seq['add_address'].append(line)

    cmd_list_new = []

    cmd_list_new = cmd_seq['rm_policy'] + cmd_seq['rm_address_set'] + cmd_seq['rm_service_set'] + cmd_seq['rm_application_set'] \
    + cmd_seq['rm_address'] + cmd_seq['rm_service'] + cmd_seq['rm_application'] \
    + cmd_seq['add_application'] + cmd_seq['add_service'] + cmd_seq['add_address'] \
    + cmd_seq['add_application_set'] + cmd_seq['add_service_set'] + cmd_seq['add_address_set'] + cmd_seq['add_policy']
        

    return '\n'.join(cmd_list_new)

