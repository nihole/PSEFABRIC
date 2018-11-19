import re

def juniper_xml_correction(cfg_xml):

    config_ = '<configuration>' + '\n' + cfg_xml  + '\n' + '</configuration>'

    return config_
