'''
The psefabric.py is the dataflow manager
- runs scripts in the correct order 
- responsible for data exchanging between them.
'''

import xmltodict
from deepdiff import DeepDiff
import re
from ncclient import manager
import os
import versionfile as vrs

import cda
import psef_index
import multiplexer
import cfg
import mult_cfg
import json
import psef_debug
import copy



PSEFABRIC =os.environ['PSEFABRIC'] + "/PSEFABRIC"

def version_file(flg_ok_):
    if (re.search (flg_ok_, "OK")):
        if os.path.isfile("%s/PSEF_CONF/pse-config.xml" % PSEFABRIC):
            if (vrs.VersionFile("%s/PSEF_CONF/pse-config.xml" % PSEFABRIC)):
                with open('%s/PSEF_CONF/pse-config.xml' % PSEFABRIC, 'w') as f3:
                    f3.write(c)
                    f3.flush()
                print ("OK")
            else:
                print ("Versioning file failed")
        else:
            if (os.system("cp $PSEFABRIC/PSEFABRIC/PSEF_CONF/pse-config-initial.xml $PSEFABRIC/PSEFABRIC/PSEF_CONF/pse-config.xml.000 2>/dev/null")):
                print ("cp pse-config-initial.xml pse-config.xml failed")
            else:
                with open('%s/PSEF_CONF/pse-config.xml' % PSEFABRIC, 'w') as f4:
                    f4.write(c)
                    f4.flush()
                print("OK")


########  Main body ########

# logins
username='admin'
password='admin'
host='127.0.0.1'
port = 2022
diff_dict_full =''
diff_dict = ''

    #########################################################################
    #                                                                       #
    #                                   1.                                  #
    #               configuration management engine layer                   #
    #                                                                       #
    #    - reads configuration from psefabric (xml format)                  #
    #    - saves configuration files in $PSEABRIC/PSEF_CONF/                #
    #    - transfer old and new configuration in dictionary                 #
    #      this dictionaries are used on configuration analyser layer       #
    #                                                                       #
    #                                                                       #
    #                                                                       #
    #########################################################################


# take new and old xml config files and transfirm them to the dictionaries

with manager.connect(host = '127.0.0.1', port = 2022, username = 'admin', password = 'admin', hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    psef_conf_new_ = xmltodict.parse(c)

if os.path.isfile('%s/PSEF_CONF/pse-config.xml' % PSEFABRIC):
    with open('%s/PSEF_CONF/pse-config.xml' % PSEFABRIC) as fd2:
        psef_conf_old_  = xmltodict.parse(fd2.read())
    fd2.close() 
elif os.path.isfile('%s/PSEF_CONF/pse-config-initial.xml' % PSEFABRIC):
    with open('%s/PSEF_CONF/pse-config-initial.xml' % PSEFABRIC) as fd1:
        psef_conf_old_  = xmltodict.parse(fd1.read())
    fd1.close()
else:
#    if (os.system("python create_pse_config_initial.py 2>/dev/null")):
    if (os.system("python $PSEFABRIC/PSEFABRIC/PSEF_SCRIPTS/create_pse_config_initial.py")):
        print "Failed to create pse-config-initial.xml"
    else:
        print "pse-config-initial.xml has been created"
        with open('%s/PSEF_CONF/pse-config-initial.xml' % PSEFABRIC) as fd1:
            psef_conf_old_  = xmltodict.parse(fd1.read())
        fd1.close()

    #############################################################################
    #                                                                           #
    #                                 2.                                        #
    #                   configuration analyser layer                            #
    #                                                                           #
    #    - psefabric configuration dictionary correction:                       #
    #        - dict_correct()                                                   #
    #        - default_change()                                                 #
    #    - creating "full" psefabric configuration dictionary                   #
    #        - psef_full()                                                      #
    #            - address_full()                                               #
    #            - service_full()                                               #
    #            - application_full()                                           #
    #    - creating a dict with a difference between full new and old           #
    #      psefabric configuration dictionaries                                 #
    #        - ddiff_dict()                                                     #
    #    - policy indexation                                                    #
    #        psef_index.policy_index()                                          #
    #                                                                           #
    #                                                                           #
    #############################################################################


# correct dictionaries psef_conf_new/psef_conf_old (see the description of the dict_correct)
# chabge default values of some parameters if necessary

cda.psef_conf_new =  cda.dict_correct(psef_conf_new_)
cda.psef_conf_old =  cda.dict_correct(psef_conf_old_)

#cda.psef_conf_new =  cda.default_change(cda.dict_correct(psef_conf_new_))
#cda.psef_conf_old =  cda.default_change(cda.dict_correct(psef_conf_old_))

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('psef_conf_new', cda.psef_conf_new)
    psef_debug.WriteDebug('psef_conf_old', cda.psef_conf_old)

cda.psef_conf_new =  cda.default_change(cda.psef_conf_new)
cda.psef_conf_old =  cda.default_change(cda.psef_conf_old)

# create separate dictionaries for addresses and 
# create separate full (with addresses information) dictionaries for address-sets

(cda.address_full_new, cda.address_set_full_new)  = cda.address_full (cda.psef_conf_new)
(cda.address_full_old, cda.address_set_full_old)  = cda.address_full (cda.psef_conf_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('address_full_new', cda.address_full_new)
    psef_debug.WriteDebug('address_full_old', cda.address_full_old)
    psef_debug.WriteDebug('address_set_full_new', cda.address_set_full_new)
    psef_debug.WriteDebug('address_set_full_old', cda.address_set_full_old)

# create separate dictionaries for services and 
# create separate full (with services information) dictionaries for service-sets

(cda.service_full_new, cda.service_set_full_new)  = cda.service_full (cda.psef_conf_new)
(cda.service_full_old, cda.service_set_full_old)  = cda.service_full (cda.psef_conf_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('service_full_new', cda.service_full_new)
    psef_debug.WriteDebug('service_full_old', cda.service_full_old)
    psef_debug.WriteDebug('service_set_full_new', cda.service_set_full_new)
    psef_debug.WriteDebug('service_set_full_old', cda.service_set_full_old)

# create separate dictionaries for applications and 
# create separate full (with services information) dictionaries for application-sets

(cda.application_full_new, cda.application_set_full_new)  = cda.application_full (cda.psef_conf_new)
(cda.application_full_old, cda.application_set_full_old)  = cda.application_full (cda.psef_conf_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('application_full_new', cda.application_full_new)
    psef_debug.WriteDebug('application_full_old', cda.application_full_old)
    psef_debug.WriteDebug('application_set_full_new', cda.application_set_full_new)
    psef_debug.WriteDebug('application_set_full_old', cda.application_set_full_old)

# create full psefabric configuration dictionaries:
# with full address-sets
# with full service-sets
# with full application-sets
# with full policies (with addresses, address-sets, services, service-sets, applications, application-sets information)


cda.psef_conf_full_new = cda.psef_full(cda.psef_conf_new, cda.address_set_full_new, cda.service_set_full_new, cda.application_set_full_new, cda.address_full_new, cda.service_full_new, cda.application_full_new)
cda.psef_conf_full_old = cda.psef_full(cda.psef_conf_old, cda.address_set_full_old, cda.service_set_full_old, cda.application_set_full_old, cda.address_full_old, cda.service_full_old, cda.application_full_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('psef_conf_policy_full_new', cda.psef_conf_full_new)
    psef_debug.WriteDebug('psef_conf_policy_full_old', cda.psef_conf_full_old)

# take difference between new and old full configuration dictionaries

diff_dict_full = cda.ddiff_dict(DeepDiff(cda.psef_conf_full_old, cda.psef_conf_full_new, verbose_level=2, ignore_order=True, report_repetition=False))

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('diff_dict_full', diff_dict_full)

psef_index.address_set_index_new  = psef_index.address_index (cda.psef_conf_new)
psef_index.address_set_index_old  = psef_index.address_index (cda.psef_conf_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('address_set_index_new', psef_index.address_set_index_new)
    psef_debug.WriteDebug('address_set_index_old', psef_index.address_set_index_old)


    ##################################################################################
    #                                                                                #
    #                                       3.                                       #
    #                              demultiplexer layer                               #
    #                                                                                #
    #    This is a core part of Demultiplexer Layer of our Psefabric Dataflow Model. #
    #    The goal is to create a list of configuration commands for each MO.         #
    #                                                                                #
    #    We need to create these lists for the next cases: address creation/removal, #
    #    address-set creation/removal, service creation/removal,                     #
    #    service-set creation/removal, application creation/removal, application-set #
    #    creation/removal, policy creation/removal.                                  #
    #                                                                                #
    #                                                                                #
    ##################################################################################

# cmd_for_host and policy_index initiation:

multiplexer.cmd_for_host = {}
multiplexer.policy_index_ = {}
multiplexer.initiate_cmd_for_host()
multiplexer.policy_index_ = {'ad':[], 'rm':[]}

# cmd_for_host creation. Using psef_logic this function creats a list of cinfiguration commands for each Management Object (MO). This information is added to diff_dict_full. 
multiplexer.demultiplex(diff_dict_full)

cmd_for_host_full = copy.deepcopy(multiplexer.cmd_for_host)
policy_index_full = copy.deepcopy(multiplexer.policy_index_)


if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cmd_for_host_full', cmd_for_host_full)
    psef_debug.WriteDebug('policy_index', policy_index_full)

cmd_for_host_mult = multiplexer.multiplex(cmd_for_host_full)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cmd_for_host_mult', cmd_for_host_mult)

cmd_for_host_diff = multiplexer.policy_opt(cmd_for_host_mult)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cmd_for_host_diff', cmd_for_host_diff)


    ####################################################################################
    #                                                                                  #
    #                                           4.                                     #
    #                                   configurator layer                             #
    #                                                                                  #
    #    For different MOs (Management Objects) different configuration                #
    #    formats may be used.                                                          #
    #    For example:                                                                  #
    #                                                                                  #
    #    - api: json/xml/netconf/..                                                    #
    #    - cli: text                                                                   #
    #    - without candidate config (for example cisco-like interface)                 #
    #    - with candidate config (for example juniper or palo-alto interface)          #
    #    - ...                                                                         #
    #                                                                                  #
    #    To provide correct configuration for different cases 2 dictionaries           #
    #    are taken from demultiplexer layer (3):                                       #
    #                                                                                  #
    #    - cmd_for_host_diff                                                           #
    #    - cmd_for_host_full                                                           #
    #                                                                                  #
    ####################################################################################

# Create configyration
cfg.cfg = cfg.create_configs(cmd_for_host_diff, cmd_for_host_mult)
if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cfg', cfg.cfg)

    #####################################################################################
    #                                                                                   #
    #                                           5.                                      #
    #                           configuration encapsulator layer                        #
    #                                                                                   #
    #    Three purposes of this layer:                                                  #
    #        - some additional configuration manipulation, for example:                 #
    #        (additional modules may be used for this purposes)                         #
    #            - removing of duplicated lines                                         #
    #            - restoring of correct order of commnads if necessary                  #
    #        - encapsulation or adaptation of the configuration files to protocols      #
    #          or tools are used at Layer 6 (telnet/ssh, neconf, ansible etc.)          #
    #        - saving of configuration files (folder $PSEFABRIC/PSEF_CONF/EQ_CONF/)     #
    #                                                                                   #
    #                                                                                   #
    #                                                                                   #
    #                                                                                   #
    #####################################################################################

# Write configuration to files
flg_ok = mult_cfg.mult_cfg(cfg.cfg)

# Write configuration of psefabric
version_file(flg_ok)

