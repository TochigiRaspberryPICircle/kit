import requests

hook_url = "https://maker.ifttt.com/trigger/hello/with/key/"
id_key = '<webhooksのkey>' # Look at Documentation
requests.post(hook_url + id_key, json={"value1":"prm1", "value2":"prm2", , "value3":"prm3"})