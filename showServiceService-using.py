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
