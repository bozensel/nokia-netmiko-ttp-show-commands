# Düzeltilmesi gereken kısımlar var, # ile gösterilen kullanıcılar ve ilk satır tam gözükmüyor. 

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


