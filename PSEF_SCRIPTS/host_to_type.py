'''
Administrator has to describe the equipment of psefabric.
In this realisation of psefabric the words 'cisco'  and 'juniper' are essential.
The mul_cfg.py script uses them in the deciding how to process the data.
'''

def host_to_type():
    host = {}
    host['OSS_AA'] = 'pa_panorama'
    host['OSS_INTERNET'] = 'pa_panorama'
    host['INTERNAL_AA'] = 'pa_panorama'
    host['EXTERNAL_AA'] = 'pa_panorama'
    host['CORPO_INTERNET'] = 'pa_panorama'
    return host
