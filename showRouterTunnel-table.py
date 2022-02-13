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

'''
[
    {
        "Show_Router_Ospf_Neighbor": [
            {
                "Area_ID": "0.0.0.0",
                "Interface-Name": "toSR7-3",
                "Neighbor_State": "Full",
                "Pri": "1",
                "RetxQ": "0",
                "Rtr_Id": "10.10.10.3",
                "TTL": "33"
            },
            {
                "Area_ID": "1.1.1.1",
                "Interface-Name": "toSR7-4",
                "Neighbor_State": "Full",
                "Pri": "10",
                "RetxQ": "0",
                "Rtr_Id": "10.10.12.3",
                "TTL": "34"
            }
        ]
    }
]
'''
