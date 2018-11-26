import re

def collection_header():
    co_header =  '''
{
	"info": {
		"name": "test",
		"_postman_id": "e61529df-a10b-69e0-7e49-56647667624a",
		"description": "",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
        	{
			"name": "login",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\\"aaaUser\\" : { \\"attributes\\": {\\"name\\":\\"admin\\",\\"pwd\\":\\"C1sco12345\\" } } } "
				},
				"url": {
					"raw": "https://198.18.133.200/api/aaaLogin.json",
					"protocol": "https",
					"host": [
						"198",
						"18",
						"133",
						"200"
					],
					"path": [
						"api",
						"aaaLogin.json"
					]
				},
				"description": "login"
			},
			"response": []
		},

    '''
    return co_header

def rest_header(n):
    reg_name = "req_" + str(n)
    re_header =  '''
		{
			"name": "%s",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "
    ''' % reg_name

    return re_header

def rest_tail():
    re_tail  =  '''"
				},
				"url": {
					"raw": "https://198.18.133.200/api/mo/uni.json",
					"protocol": "https",
					"host": [
						"198",
						"18",
						"133",
						"200"
					],
					"path": [
						"api",
						"mo",
						"uni.json"
					]
				},
				"description": ""
			},
			"response": []
		}
    '''
    return re_tail


def aci_json_correction(cfg_json):

    cfg_json_ = collection_header()
    n = 0
    cmd_list = cfg_json.splitlines()
    for line in cmd_list:
        if not line:
            continue
        new_line = line.replace('\"', '\\"')
        if n == 0:
            cfg_json_ = cfg_json_.rstrip()  + rest_header(n).rstrip() + new_line.rstrip() + rest_tail()
        else:
            cfg_json_ = cfg_json_.rstrip().rstrip()  + "," + rest_header(n).rstrip() + new_line.rstrip() + rest_tail()
            
        n = n + 1

    cfg_json_ = cfg_json_ + '\t ]' +'\n}'


    return cfg_json_
