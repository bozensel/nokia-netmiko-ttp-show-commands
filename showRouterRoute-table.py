from pprint import pprint
from ttp import ttp
import json
import time

with open("showRouterRoute-table.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="RouteTable">
{{Dest_Prefix_Flags_}}                            {{Type}}    {{Proto}}        {{Age}}        {{Pref|DIGIT}}
       {{Next_Hop_Interface_Name}}                                    {{Metric|DIGIT}}
</group>
"""

# create parser object and parse data using template:
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)

#converting str to json. 
result = json.loads(results)

'''
RESULT:
[
    {
        "RouteTable": [
            {
                "Age": "15d22h01m",
                "Dest_Prefix_Flags_": "10.10.10.1/32",
                "Metric": "0",
                "Next_Hop_Interface_Name": "system",
                "Pref": "0",
                "Proto": "Local",
                "Type": "Local"
            },
            {
                "Age": "17h12m34s",
                "Dest_Prefix_Flags_": "10.10.10.3/32",
                "Metric": "50",
                "Next_Hop_Interface_Name": "192.168.10.2",
                "Pref": "10",
                "Proto": "OSPF",
                "Type": "Remote"
            },
            {
                "Age": "17h11m56s",
                "Dest_Prefix_Flags_": "10.10.10.121/32",
                "Metric": "100",
                "Next_Hop_Interface_Name": "192.168.10.2",
                "Pref": "10",
                "Proto": "OSPF",
                "Type": "Remote"
            },
            {
                "Age": "18h20m52s",
                "Dest_Prefix_Flags_": "192.168.10.0/27",
                "Metric": "0",
                "Next_Hop_Interface_Name": "toSR7-3",
                "Pref": "0",
                "Proto": "Local",
                "Type": "Local"
            },
            {
                "Age": "17h12m34s",
                "Dest_Prefix_Flags_": "192.168.20.0/27",
                "Metric": "100",
                "Next_Hop_Interface_Name": "192.168.10.2",
                "Pref": "10",
                "Proto": "OSPF",
                "Type": "Remote"
            }
        ]
    }
]
'''
