import re
import vocabulary


def aci_attach_epg (contract_name, epg_name, path, relation):
    t = re.search('(uni/.*)/.*$', path)
    a = re.search('uni/.*/(.*)$', path)
    tenant_path = t.group(1)
    app = a.group(1)
    epg_path = path + '/' + epg_name 


    if (relation == 'cons'):
        contract_path = epg_path + '/' + 'rscons-%s' % contract_name
    if (relation == 'prov'):
        contract_path = epg_path + '/' + 'rsprov-%s' % contract_name

    config_json = '{"fvTenant":{"attributes":{"dn":%s,"status":"modified"},"children":[{"fvAp":{"attributes":{"dn":%s,"name":%s, "status":"modified"},"children":[{"fvAEPg":{"attributes":{"dn":%s,"status":"modified"},"children":[{"fvRsCons":{"attributes":{"dn":%s,"status":"created,modified"},"children":[]}}]}}]}}]}}' % (tenant_path,path,app,epg_path,contract_path)
    
    return (config_json)

def aci_detach_epg (contract_name, epg_name, path, relation):

    t = re.search('(uni/.*)/.*$', path)
    a = re.search('uni/.*/(.*)$', path)
    tenant_path = t.group(1)
    app = a.group(1)
    epg_path = path + '/' + epg_name
    if (relation == 'cons'):
        contract_path = epg_path + '/' + 'rscons-%s' % contract_name
    if (relation == 'prov'):
        contract_path = epg_path + '/' + 'rsprov-%s' % contract_name

    config_json = '{"fvTenant":{"attributes":{"dn":%s,"status":"modified"},"children":[{"fvAp":{"attributes":{"dn":%s,"name":%s, "status":"deleted"},"children":[{"fvAEPg":{"attributes":{"dn":%s,"status":"modified"},"children":[{"fvRsCons":{"attributes":{"dn":%s,"status":"created,modified"},"children":[]}}]}}]}}]}}' % (tenant_path,path,app,epg_path,contract_path)


    return (config_json)

def aci_create_policy (eq_parameter, psefname, epg_dict_cons, epg_dict_prov, application_sets, subject_dict, src_str, dst_str, parameters, action):

# eq_parameter and application_sets are  not used in this case

    # if 'epg' parameter is false then exit
    if (parameters[vocabulary.par_rvoc['epg-plc']] == 'false'):
        return None

    name = parameters[vocabulary.par_rvoc['aci-contract-name']]


    # Subject creation:
    config_sbj = ''
    # Filters creation
    for subject_el in subject_dict:
        config_fltr_ = ''
        for filter_el in subject_el['services']:
            config_fltr_el = '{"vzRsSubjFiltAtt":{"attributes":{"action":"permit","priorityOverride":"default","tnVzFilterName":"%s"}}}' % filter_el['parameters'][vocabulary.par_rvoc['aci-filter-name']] 
            if (config_fltr_ == ''):
                config_fltr_ = config_fltr_el
            else:
                config_fltr_ = config_fltr_ + ',' + config_fltr_el
        config_fltr = '[' + config_fltr_ + ']'
        if (config_sbj == ''):
            config_sbj_part = '{"vzSubj":{"attributes":{"name":"%s","revFltPorts":"yes"},"children":' % subject_el['parameters'][vocabulary.par_rvoc['aci-subject-name'] ]
            config_sbj = config_sbj_part + config_fltr
        else:
            config_sbj_part = '{"vzSubj":{"attributes":{"name":"%s","revFltPorts":"yes"},"children":' % subject_el['parameters'][vocabulary.par_rvoc['aci-subject-name'] ]
            config_sbj = config_sbj + ',' + config_sbj_part + config_fltr
        config_sbj = '[' + config_sbj + '}}]'

# Contracts creation:    
    config_cntr_part = '{"fvTenant":{"attributes":{"dn":"uni/tn-common","status":"modified"},"children":[{"vzBrCP":{"attributes":{"dn":"uni/tn-common/brc-%s","name":"%s","scope":"context"},"children":' % (subject_el['parameters'][vocabulary.par_rvoc['aci-subject-name'] ], subject_el['parameters'][vocabulary.par_rvoc['aci-subject-name'] ])
    config_cntr = config_cntr_part + config_sbj + '}}]}}'

# EPGs attachment
    config_epg = ''
    config_epg_cons = ''
    config_epg_prov = ''
    for epg_cons_el in epg_dict_cons:
        if (config_epg_cons == ''):
            config_epg_cons = aci_attach_epg(name, epg_cons_el['parameters'][vocabulary.par_rvoc['aci-epg-name']], epg_cons_el['parameters'][vocabulary.par_rvoc['path']], 'cons') 
        else:
            config_epg_cons = config_epg_cons + '\n' + aci_attach_epg(name, epg_cons_el['parameters'][vocabulary.par_rvoc['aci-epg-name']], epg_cons_el['parameters'][vocabulary.par_rvoc['path']], 'cons')
    for epg_prov_el in epg_dict_prov:
        if (config_epg_prov == ''):
            config_epg_prov = aci_attach_epg(name, epg_prov_el['parameters'][vocabulary.par_rvoc['aci-epg-name']], epg_prov_el['parameters'][vocabulary.par_rvoc['path']], 'prov')        
        else:
            config_epg_prov = config_epg_prov + '\n' + aci_attach_epg(name, epg_prov_el['parameters'][vocabulary.par_rvoc['aci-epg-name']], epg_prov_el['parameters'][vocabulary.par_rvoc['path']], 'prov')
    
    config_epg = config_epg_cons + '\n' + config_epg_prov
    
    config_json = config_cntr + '\n' + config_epg

    return (config_json)

def aci_delete_policy (psefname, tenant, parameters, epg_dict_cons, epg_dict_prov, subject_dict, status):

# eq_parameter is  not used in this case

    # if 'epg' parameter is false then exit
    if (parameters[vocabulary.par_rvoc['epg-plc']] == 'false'):
        return None

    name = parameters[vocabulary.par_rvoc['aci-contract-name']]

# EPGs attachment
    config_epg = ''
    config_epg_cons = ''
    config_epg_prov = ''
    for epg_cons_el in epg_dict_cons:
        if (config_epg_cons == ''):
            config_epg_cons = aci_detach_epg(name, epg_cons_el['parameters'][vocabulary.par_rvoc['aci-epg-name']], epg_cons_el['parameters'][vocabulary.par_rvoc['path']], 'cons')
        else:
            config_epg_cons = config_epg_cons + '\n' + aci_detach_epg(name, epg_cons_el['parameters'][vocabulary.par_rvoc['aci-epg-name']], epg_cons_el['parameters'][vocabulary.par_rvoc['path']], 'cons')
    for epg_prov_el in epg_dict_prov:
        if (config_epg_prov == ''):
            config_epg_prov = aci_detach_epg(name, epg_prov_el['parameters'][vocabulary.par_rvoc['aci-epg-name']], epg_prov_el['parameters'][vocabulary.par_rvoc['path']], 'prov')
        else:
            config_epg_prov = config_epg_prov + '\n' + aci_detach_epg(name, epg_prov_el['parameters'][vocabulary.par_rvoc['aci-epg-name']], epg_prov_el['parameters'][vocabulary.par_rvoc['path']], 'prov')

    config_epg = config_epg_cons + '\n' + config_epg_prov

    if (status == 'change'):
        config_cntr = aci_create_policy (name, {}, {}, subject_dict, action )
    elif (status == 'delete'):
        config_cntr = '{"fvTenant":{"attributes":{"dn":"uni/tn-common","status":"modified"},"children":[{"vzBrCP":{"attributes":{"dn":"uni/tn-common/brc-%s","status":"deleted"},"children":[]}}]}}' % name

    config_json = config_cntr + '\n' + config_epg

    
    
    return (config_json)
