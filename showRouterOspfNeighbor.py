from pprint import pprint
from ttp import ttp
import json
import time

with open("showRouterOspfNeighbor.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="Show_Router_Ospf_Neighbor">         
{{Interface-Name}}                          {{Rtr_Id}}      {{Neighbor_State}}       {{Pri|DIGIT}}    {{RetxQ}}       {{TTL|DIGIT}}
   {{Area_ID}}
</group>
"""
  
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)
