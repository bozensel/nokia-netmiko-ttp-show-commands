from pprint import pprint
from ttp import ttp
import json
import time

with open("showSystemInformation.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="Show_System_Information">         
System Name            : {{System_Name}}
System Type            : {{System_Type}} {{System_Type_2}}
System Version         : {{Version}}
System Up Time         : {{System_Uptime_Days}} days, {{System_Uptime_HR_MIN_SEC}} (hr:min:sec)
Last Saved Config      : {{Last_Saved_Config}}
Time Last Saved        : {{Last_Time_Saved_Date}} {{Last_Time_Saved_HR_MIN_SEC}}
Time Last Modified     : {{Last_Time_Modified_Date}} {{Last_Time_Modifed_HR_MIN_SEC}}
</group>
"""
  
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)
