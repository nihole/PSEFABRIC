from ncclient import manager
import tempfile
import os


filename = "pse-config"

with manager.connect(host='127.0.0.1', port=2022, username='admin', password='admin', hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(c)
        temp.flush()
os.system("more " + temp.name)
