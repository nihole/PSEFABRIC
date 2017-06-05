'''
The psefabric.py is the dataflow manager. It runs scripts in the correct order and is responsible for exchanging data between them.
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

def version_file(flg_ok_):
    if (re.search (flg_ok_, "OK")):
        if os.path.isfile('../PSEF_CONF/pse-config.xml'):
            if (vrs.VersionFile('../PSEF_CONF/pse-config.xml')):
                with open('../PSEF_CONF/pse-config.xml', 'w') as f3:
                    f3.write(c)
                    f3.flush()
                print ("OK")
            else:
                print ("Versioning file failed")
        else:
            if (os.system("cp ../PSEF_CONF/pse-config-initial.xml ../PSEF_CONF/pse-config.xml.000 2>/dev/null")):
                print ("cp pse-config-initial.xml pse-config.xml failed")
            else:
                with open('../PSEF_CONF/pse-config.xml', 'w') as f4:
                    f4.write(c)
                    f4.flush()
                print("OK")


########  Main body ########

# logins
username='admin'
password='admin'
host='127.0.0.1'
port = 2022

# take new and old xml config files and transfirm them to the dictionaries

with manager.connect(host = '127.0.0.1', port = 2022, username = 'admin', password = 'admin', hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    psef_conf_new_ = xmltodict.parse(c)

if os.path.isfile('../PSEF_CONF/pse-config.xml'):
    with open('../PSEF_CONF/pse-config.xml') as fd2:
        psef_conf_old_  = xmltodict.parse(fd2.read())
    fd2.close() 
elif os.path.isfile('../PSEF_CONF/pse-config-initial.xml'):
    with open('../PSEF_CONF/pse-config-initial.xml') as fd1:
        psef_conf_old_  = xmltodict.parse(fd1.read())
    fd1.close()
else:
#    if (os.system("python create_pse_config_initial.py 2>/dev/null")):
    if (os.system("python create_pse_config_initial.py")):
        print "Failed to create pse-config-initial.xml"
    else:
        print "pse-config-initial.xml has been created"

# correct these dictionaries with the def cda.dict_correct (see the description of the dict_correct)

cda.psef_conf_new =  cda.dict_correct(psef_conf_new_)
cda.psef_conf_old =  cda.dict_correct(psef_conf_old_)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('psef_conf_new', cda.psef_conf_new)
    psef_debug.WriteDebug('psef_conf_old', cda.psef_conf_old)

# make indexation by addresses and address-sets with the def cda.address_index (see the description of the address_index)

(psef_index.address_index_new, psef_index.address_set_index_new)  = psef_index.address_index (cda.psef_conf_new)
(psef_index.address_index_old, psef_index.address_set_index_old)  = psef_index.address_index (cda.psef_conf_old)

if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('address_index_new', psef_index.address_index_new)
    psef_debug.WriteDebug('address_index_old', psef_index.address_index_old)
    psef_debug.WriteDebug('address_set_index_new', psef_index.address_set_index_new)
    psef_debug.WriteDebug('address_set_index_old', psef_index.address_set_index_old)

# make the difference between new and old configs

ddiff = DeepDiff(cda.psef_conf_old, cda.psef_conf_new, verbose_level=2, ignore_order=True, report_repetition=True)
if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('ddiff', ddiff)

# transform the structure of the ddiff dictionary to more convinient view
cda.diff_dict = cda.ddiff_dict(ddiff)
if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('diff_dict', cda.diff_dict)

# Extract set of commands for each MO
multiplexer.cmd_for_host = multiplexer.multiplex(cda.diff_dict)
if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cmd_for_host', multiplexer.cmd_for_host)

# Create configyration
cfg.cfg = cfg.create_configs(multiplexer.cmd_for_host)
if psef_debug.deb:   # if debuging is on then:
    psef_debug.WriteDebug('cfg', cfg.cfg)

# Write configuration to files
flg_ok = mult_cfg.mult_cfg(cfg.cfg)

# Write configuration of psefabric
version_file(flg_ok)

