from pprint import pprint
from ttp import ttp
import json
import time

with open("showRouterMplsLspPathDetail.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="MPLS_Lsp_Path_Detail">         
LSP Name         : {{LSP_Name}}
Path LSP ID      : {{Path_LSP_id}}                
From             : {{From}}         To                   : {{To}}
Admin State      : {{Admin_State}}                   Oper State           : {{Oper_State}}
Path Name        : {{Path_Name}} Path Type            : {{Path_Type}}
Path Admin       : {{Path_Admin_State}}                   Path Oper            : {{Path_Oper_State}}
Out Interface    : {{Out_Interface}}            Out Label            : {{Out_Label}}
Path Up Time     : {{Path_Uptime_Date}} {{Path_Uptime_Time}}         Path Down Time       : 0d 00:00:00
Retry Limit      : 0                    Retry Timer          : {{Retry_Time}} sec
Neg MTU          : {{Neg_Mtu}}                 Oper MTU             : {{Oper_Mtu}}
Hop Limit        : {{Hop_Limit}}                  Oper HopLimit        : {{Oper_Hop_Limit}}
Hold Priority    : {{Hold_Priority}}                    Oper Hold Priority   : 0
</group>
"""
  
parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)
