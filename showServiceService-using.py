from pprint import pprint
from ttp import ttp
import json
import time

with open("showServiceService-using.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="Show_Service_Service-using">         
{{ServiceId}}           {{Service_TYPE}}      {{Admin_State}} {{Oper_State}} {{Customer_id}}          {{Service_Name}}
</group>
"""
  
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)

'''
[
    {
        "Show_Service_Service-using": [
            {
                "Admin_State": "Down",
                "Customer_id": "1",
                "Oper_State": "Down",
                "ServiceId": "10",
                "Service_Name": "10",
                "Service_TYPE": "VPRN"
            },
            {
                "Admin_State": "Down",
                "Customer_id": "1",
                "Oper_State": "Down",
                "ServiceId": "56",
                "Service_Name": "56",
                "Service_TYPE": "Mirror"
            },
            {
                "Admin_State": "Up",
                "Customer_id": "1",
                "Oper_State": "Up",
                "ServiceId": "500",
                "Service_Name": "500",
                "Service_TYPE": "VPRN"
            },
            {
                "Admin_State": "Up",
                "Customer_id": "1",
                "Oper_State": "Down",
                "ServiceId": "2147483648",
                "Service_Name": "_tmnx_InternalIesService",
                "Service_TYPE": "IES"
            },
            {
                "Admin_State": "Up",
                "Customer_id": "1",
                "Oper_State": "Down",
                "ServiceId": "2147483649",
                "Service_Name": "_tmnx_InternalVplsService",
                "Service_TYPE": "intVpls"
            }
        ]
    }
]
'''
