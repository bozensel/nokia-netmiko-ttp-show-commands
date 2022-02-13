from pprint import pprint
from ttp import ttp
import json
import time

with open("showCardDetail.txt") as f:
   data_to_parse = f.read()

ttp_template = """
<group name="Card_Detail">
===============================================================================
Card {{Card_id|DIGIT}}
===============================================================================
Slot      Provisioned Type                         Admin Operational   Comments
              Equipped Type (if different)         State State         
-------------------------------------------------------------------------------
{{Slot_id|DIGIT}}         {{Card_Type}}                             {{Admin_State}}    {{Operational_State}}            
IOM Card Specific Data
    Clock source                  : none
    Named Pool Mode               : Disabled
    Fail On Error                 : {{Fail_on_Error}}
    Reset On Recoverable Error    : Disabled
    Available MDA slots           : 2
    Installed MDAs                : 2

FP 1 Specific Data
    WRED Admin State              : Out Of Service
    WRED buffer-allocation max    : 2500
    WRED buffer-allocation min    : 2500
    WRED reserved-cbs max         : 2500
    WRED reserved-cbs min         : 2500
    WRED Slope Policy             : default
    hi-bw-mc-srcEgress Alarm      : disabled
    hi-bw-mc-srcEgress Group      : 0
    mc-path-mgmt Admin State      : Out Of Service
    Ingress Bandwidth Policy      : default
    Stable Pool Sizing            : False
    Ingress Buffer Allocation     : 50.00
    Ingress Buffer Pool Size      : 1904640 KB
    Egress Buffer Pool Size       : 1904640 KB
    Initial Extract Priority Mode : uniform
    HS Pool Policy                : None
    HS Fixed High Threshold Delta : default
    Generation                    : {{Generation}}

Hardware Data
    Platform type                 : 7750
    Part number                   : {{Part_Number}}
    CLEI code                     : IPUCA741AA
    Serial number                 : {{Serial_Number}}
    Manufacture date              : 03242015
    Manufacturing deviations      : (Not Specified)
    Manufacturing assembly number : 82-0464-08
    Administrative state          : up
    Operational state             : up
    Temperature                   : 54C
    Temperature threshold         : 75C
    Software boot (rom) version   : {{Soft_rom_version}} on Mon Nov 12 07:00:31 PST
                                    2018 by builder
    Software version              : TiMOS-I-16.0.R9 iom/hops64 Nokia 7750 SR
                                    Copyright (c) 2000-2019 Nokia.
                                    All rights reserved. All use subject to
                                    applicable license agreements.
                                    Built on Wed Aug 21 12:25:15 PDT 2019 by
                                    builder in /builds/c/160B/R9/panos/main
    Time of last boot             : {{Last_reboot_date}} {{Last_reboot_time}}
    Current alarm state           : alarm cleared
    Base MAC address              : e4:81:84:80:a2:3b
    Firmware revision status      : acceptable
    Last bootup reason            : {{Last_bootup_reason}}
    Memory capacity               : 4,096 MB
</group>
"""

parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
# print(results)

#converting str to json. 
result = json.loads(results)

print(result)

# for i in result[0]['Card_Detail']:
#     print(i['Card_id'])


