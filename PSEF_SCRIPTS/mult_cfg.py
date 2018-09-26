'''
The aim of this layer is encapsulation or adaptation of data to protocols or tools are used at Layer 6 (telnet/ssh, neconf, ansible etc.).
Files are written to a folder $PSEFABRIC/PSEF_CONF/EQ_CONF/.
'''

import versionfile as vrs
import os
import host_to_type
import re
import pa_config_correction
import copy
PSEFABRIC = os.environ['PSEFABRIC'] + "/PSEFABRIC"

def version_file(eq_addr_, conf_, ext_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    path_ = '%s/PSEF_CONF/EQ_CONF/%s.%s'   % (PSEFABRIC, eq_addr_, ext_)
    if not  os.path.isfile(path_):
        open(path_, 'a')
    if (vrs.VersionFile(path_)):
        with open(path_, 'w') as f10:
            f10.write(conf_)
            f10.flush()
    else:
        print ("Versioning file failed")



def mult_cfg(cfg_):

##########  Description  #######
    '''
    '''
#############  BODY ############

    host_ = copy.deepcopy(host_to_type.host_to_type())
    for eq_addr in cfg_:
        if re.search('juniper', host_[eq_addr]):
            config_ = '<configuration>' + '\n' + cfg_[eq_addr]  + '\n' + '</configuration>'
            version_file(eq_addr, config_,'xml')
        elif re.search('panorama', host_[eq_addr]):
            config_ = cfg_[eq_addr]
#            config_ = 'configure' + '\n' + cfg_[eq_addr] + '\n' + 'exit' + '\n'
            # We need to make some reduction in the case of cli configuration. For more informatiom see str_annihilation.py
#            config = str_annihilation.str_annihilation(config_)
#            config = pa_config_correction.pa_config_correction(config_)
            config = config_
            version_file(eq_addr, config,'txt')
        del host_[eq_addr]
    for rest_hosts in  host_:
        if re.search('juniper', host_[rest_hosts]): 
            config = ''
            version_file(rest_hosts, config,'xml')
        elif re.search('panorama', host_[rest_hosts]):
            config = ''
            version_file(rest_hosts, config,'txt') 
    return "OK"
