
def pa_cli_correction(cfg_txt):

    
    cmd_list = cfg_txt.splitlines()

    cmd_list_new = []

    for elem in cmd_list:
        if elem not in cmd_list_new:
            cmd_list_new.append(elem)

    return '\n'.join(cmd_list_new)

