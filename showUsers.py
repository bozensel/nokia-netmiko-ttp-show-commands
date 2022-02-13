from pprint import pprint
from ttp import ttp
import json
import time

with open("showUsers.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="showUsers" method="table">
{{User|re(".?")|re(".*")}}                             {{Type}}      {{Login_Date}} {{Login_Time}}           {{Idle_day}} {{Idle_time}} --
  {{Session_ID}}   {{From}}
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
        "showUsers": [
            {
                "From": "--",
                "Session_ID": "6"
            },
            {
                "Idle_day": "0d",
                "Idle_time": "00:00:00",
                "Login_Date": "08FEB2022",
                "Login_Time": "10:53:29",
                "Type": "SSHv2",
                "User": "admin                           "
            },
            {
                "From": "135.244.199.185",
                "Session_ID": "132"
            },
            {
                "Idle_day": "0d",
                "Idle_time": "00:03:35",
                "Login_Date": "09FEB2022",
                "Login_Time": "11:32:50",
                "Type": "SSHv2",
                "User": "admin                           "
            },
            {
                "From": "10.144.208.82",
                "Session_ID": "143"
            }
        ]
    }
]
'''
