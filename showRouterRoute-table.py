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
