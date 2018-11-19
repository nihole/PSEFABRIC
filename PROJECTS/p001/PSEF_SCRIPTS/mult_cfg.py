    ######################################
    #                                    #
    #                  5.                #
    #     configuration encapsulator     #
    #                layer               #
    #                                    #
    ######################################


'''
Three purposes of this layer:
    - some additional configuration manipulation, for example:
      (additional modules may be used for this purposes)
        - removing of duplicated lines
        - restoring of correct order of commnads if necessary
    - encapsulation or adaptation of the configuration files to protocols or tools are used at Layer 6 (telnet/ssh, neconf, ansible etc.)
    - saving of configuration files (folder $PSEFABRIC/PSEF_CONF/EQ_CONF/)

'''

import versionfile as vrs
import os
import host_to_type
import re
import copy
import ex_cfg_correction

PSEFABRIC = os.environ['PSEFABRIC']

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
        if (re.search('juniper', host_[eq_addr])):
#            config = ex_cfg_correction.ex_cli_correction(cfg_[eq_addr])
            config = cfg_[eq_addr]
            version_file(eq_addr, config,'xml')
        elif (re.search('cisco', host_[eq_addr])):
#            config = ex_cfg_correction.ex_cli_correction(cfg_[eq_addr])
            config = cfg_[eq_addr]
            version_file(eq_addr, config,'txt')

#        elif 
#        elif
#        ... 
#        else
           
        del host_[eq_addr]
    return "OK"
