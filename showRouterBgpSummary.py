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

# print(result[0]["BGP_Summary"])
