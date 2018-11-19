
import re

def cisco_cli_correction(cfg_txt):

    config_ = 'conf t' + '\n' + cfg_txt + '\n' + 'exit' + '\n'
#    config_ = str_annihilation.str_annihilation('conf t' + '\n' + cfg_txt + '\n' + 'exit' + '\n')

    return (config_)
