from pprint import pprint
from ttp import ttp
import json
import time

with open("showRouterTunnel-table.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="Show_Router_Tunnel-table">         
{{Prefix|PREFIX}}   {{Protocol}}       {{Encap_Type}}  {{Tunnel_id}}       {{Preference}}        {{Next_hop|IP}}   {{Metric}}
</group>
"""
  
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)
