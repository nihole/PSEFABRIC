'''
This module is used by mult_cfg.py for creation of configuration files for pa-like cli.

If we have to lines
  - set SOMETHING [ set 1 of variables ] and
  - delete  SOMETHING [ set 2 of variables ]
Then we compare set 1 and set 2 and stay only one line
  - set/delete SOMETHING [ set 3 of variables ]

For example if we have:
  delete shared address-group test12-set static [ test2 ]
  set shared address-group test12-set static [ test1 test2 ]

Then we have to receive 
  set shared address-group test12-set static [ test1 ]

But if we have:
  set shared address-group test12-set static [ test2 ]
  delete shared address-group test12-set static [ test1 test2 ]

Then the result will be 
  delete shared address-group test12-set static [ test1 ]

'''

import re

def pa_config_correction(cfg_txt):

##########  Description  #######
    '''
    '''
#############  BODY ############

    cmd_list = cfg_txt.splitlines()
    delete_ = {}
    set_ = {}
    new_set_ = {}
    new_delete_ = {}
    for el in cmd_list:
        match_el = re.match( r'^set (.*) \[\s+(.*)\s+\]$', el)
        key_el = ''
        parameters_str = ''
        if match_el:
            key_el = match_el.group(1)
            parameters_str = match_el.group(2)
            parameters_list = parameters_str.split(" ")
            set_[key_el] = parameters_list
        match_el = re.match( r'^delete (.*) \[\s+(.*)\s+\]$', el)
        key_el = ''
        parameters_str = ''
        if match_el:
            key_el = match_el.group(1)
            parameters_str = match_el.group(2)
            parameters_list = parameters_str.split(" ")
            delete_[key_el] = parameters_list
                
    for key_el_set in set_:
        if key_el_set in delete_:
            m = set(set_[key_el_set]) & set(delete_[key_el_set])
            new_set_[key_el_set] = set(set_[key_el_set]) - set(m)
            if not new_set_[key_el_set]:
                del new_set_[key_el_set]
            new_delete_[key_el_set] = set(delete_[key_el_set]) - set(m)
            if not new_delete_[key_el_set]:
                del new_delete_[key_el_set]
        
            

    print "DDDDDDDDDDDDDDDDD VVVVVVVVVVVVVVVVVVVV"
    print set_
    print delete_
    print new_set_
    print new_delete_
    print "DDDDDDDDDDDDDDDD ^^^^^^^^^^^^^^^^^^^^^"
