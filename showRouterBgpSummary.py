from pprint import pprint
from ttp import ttp
import json
import time

with open("showRouterBgpSummary.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="BGP_Summary">         
{{Neighbor|IP}}
               {{AS}}     {{PktRcvd}}    0 {{date}} 0/0/0 ({{Connection_Type}})
                         {{PktSent}}    0           1/1/1 ({{Connection_Type2}})
</group>
"""
  
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
# print(results)

#converting str to json. 
result = json.loads(results)

# print(result)

'''
RESULT:
[{'BGP_Summary': [{'AS': '65000', 'Connection_Type': 'IPv4', 'Connection_Type2': 'VpnIPv4', 'Neighbor': '10.10.10.121', 'PktRcvd': '5588', 'PktSent': '5590', 'date': '01d22h31m'}, {'AS': '65000', 'Connection_Type': 'IPv4', 'Neighbor': '10.10.10.125', 'PktRcvd': '1111', 'date': '01d11h11m'}]}]
'''
