'''
This module is used by mult_cfg.py for creation of configuration files for cisco-like cli.
We have 2 cases for using:
- If we have 2 equal strings except only "no" at the beginning, then we delete the line with "no".
- If we alse have 2 strins:
  'switchport trunk allowed vlan remove vlan_number',
  'switchport trunk allowed vlan add vlan_number'
  with equal vlan_number, then we delete the line with "remove"
'''

import re

def str_annihilation(cfg_txt):

##########  Description  #######
    '''
    '''
#############  BODY ############

    cmd_list = cfg_txt.splitlines()
    no_ = {}
    vlan_rm_ = {}
    for el in reversed(cmd_list):
        if (el[0:3] == 'no '):
            if not el[3:] in no_: 
                no_[el[3:]] = 1
            else:
                if (no_[el[3:]]==0):
                    cmd_list.remove(el)
                    no_.pop(el[3:])
        elif (re.match('switchport trunk allowed vlan remove ', el)):
            vlan = el.replace('switchport trunk allowed vlan remove ', '')
            # now el is equel vlan number
            if not vlan in vlan_rm_:
                vlan_rm_[vlan] = 1
            else:
                if (vlan_rm_[vlan] == 0):
                    cmd_list.remove(el)
                    vlan_rm_.pop(vlan)
        elif not (el[0:3] == 'no ' or re.match('switchport trunk allowed vlan add ', el)):
            if not el in no_:
                no_[el] = 0
            else:
                if (no_[el]==1):
                    cmd_list.remove('no ' + el)
                    no_.pop(el)
        elif (re.match('switchport trunk allowed vlan add ', el)):
            vlan = el.replace('switchport trunk allowed vlan add ', '')
            if not vlan in vlan_rm_:
                vlan_rm_[vlan] = 0
            else:
                if (vlan_rm_[vlan]==1):
                    cmd_list.remove('switchport trunk allowed vlan remove ' + vlan)
                    vlan_rm_.pop(el)
        else:
            print "Unknown case in str_annihilation.py"
    return '\n'.join(cmd_list)

