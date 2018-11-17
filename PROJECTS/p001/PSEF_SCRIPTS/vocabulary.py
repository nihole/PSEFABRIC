# Is used in cda.default_change()
# For different projects parameter's and structre names may be different.
# To avoid a changing of this names in the code these dictionaties are used
# Keys are always the same and values are parameters and values names used in YANG code for the CONFD intergace configuration for the specific project


par_voc = {}
par_voc['addr_par_1'] = 'configure-addr'
par_voc['addr_par_2'] = 'addr_par_2'
par_voc['addr_par_3'] = 'pa-address-obj-name'
par_voc['addr_par_4'] = 'addr_par_4'
par_voc['addr_par_5'] = 'addr_par_5'
par_voc['addr_par_6'] = 'addr_par_6'

par_voc['addrset_par_1'] = 'configure-addrset'
par_voc['addrset_par_2'] = 'epg-addrset'
par_voc['addrset_par_3'] = 'pa-address-grp-name'
par_voc['addrset_par_4'] = 'aci-epg-name'
par_voc['addrset_par_5'] = 'path'
par_voc['addrset_par_6'] = 'addrset_par_6'

par_voc['svc_par_1'] = 'configure-svc'
par_voc['svc_par_2'] = 'svc_par_2'
par_voc['svc_par_3'] = 'pa-service-name'
par_voc['svc_par_4'] = 'aci-filter-name'
par_voc['svc_par_5'] = 'svc_par_5'
par_voc['svc_par_6'] = 'svc_par_6'

par_voc['svcset_par_1'] = 'configure-svcset'
par_voc['svcset_par_2'] = 'svcset_pae_2'
par_voc['svcset_par_3'] = 'pa-service-grp-name'
par_voc['svcset_par_4'] = 'aci-subject-name'
par_voc['svcset_par_5'] = 'svcset_par_5'
par_voc['svcset_par_6'] = 'svcset_par_6'

par_voc['app_par_1'] = 'configure-app'
par_voc['app_par_2'] = 'app_par_2'
par_voc['app_par_3'] = 'pa-application-name'
par_voc['app_par_4'] = 'app_par_4'
par_voc['app_par_5'] = 'app_par_5'
par_voc['app_par_6'] = 'app_par_6'

par_voc['appset_par_1'] = 'configure-appset'
par_voc['appset_par_2'] = 'appset_par_2'
par_voc['appset_par_3'] = 'pa-application-grp-name'
par_voc['appset_par_4'] = 'appset_par_4'
par_voc['appset_par_5'] = 'appset_par_5'
par_voc['appset_par_6'] = 'appset_par_6'

par_voc['plc_par_1'] = 'configure-plc'
par_voc['plc_par_2'] = 'epg-plc'
par_voc['plc_par_3'] = 'pa-policy-name'
par_voc['plc_par_4'] = 'aci-contract-name'
par_voc['plc_par_5'] = 'plc_par_5'
par_voc['plc_par_6'] = 'plc_par_6'

str_voc = {}
str_voc['str_1'] = 'dc'
str_voc['str_2'] = 'area'
str_voc['str_3'] = 'zone'
str_voc['str_4'] = 'sub-zone'
str_voc['str_5'] = 'str_5'
str_voc['str_6'] = 'str_6'
str_voc['str_7'] = 'str_7'
str_voc['str_8'] = 'str_8'
str_voc['str_9'] = 'str_9'


par_rvoc = dict((v,k) for k,v in par_voc.iteritems())
str_rvoc = dict((v,k) for k,v in str_voc.iteritems())

eq_rvoc = {}
eq_rvoc['host'] = 'eq_addr'
eq_rvoc['tenant'] = 'eq_parameter'
eq_rvoc['device-group'] = 'eq_parameter'
