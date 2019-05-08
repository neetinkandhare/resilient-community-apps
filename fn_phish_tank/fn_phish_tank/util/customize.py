# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_phish_tank"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_phish_tank package"""
    reload_params = {"package": u"fn_phish_tank",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"phish_tank_check_url"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_phish_tank"], 
                    "functions": [u"fn_phish_tank_submit_url"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_phishtank_submit_url"], 
                    "actions": [u"Example: PhishTank: Submit URL"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     phish_tank_check_url
    #   Message Destinations:
    #     fn_phish_tank
    #   Functions:
    #     fn_phish_tank_submit_url
    #   Workflows:
    #     example_phishtank_submit_url
    #   Rules:
    #     Example: PhishTank: Submit URL


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMSwgImJ1aWxkX251bWJl
ciI6IDc2LCAidmVyc2lvbiI6ICIzMS4xLjc2In0sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAy
LCAiaWQiOiAxMDgsICJleHBvcnRfZGF0ZSI6IDE1NTczMjM5NTQ3NTcsICJmaWVsZHMiOiBbeyJp
ZCI6IDUxLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAidGV4dCI6ICJTaW11bGF0aW9uIiwgInBy
ZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMCwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUgaW5jaWRl
bnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4gIFRoaXMgZmllbGQgaXMg
cmVhZC1vbmx5LiIsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAiaGlkZV9ub3RpZmljYXRpb24i
OiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFs
c2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjogImMz
ZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNjYSIsICJvcGVyYXRpb25zIjogW10sICJv
cGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogdHJ1ZSwgImNo
YW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lk
ZW50L2luY190cmFpbmluZyIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0s
IHsiaWQiOiAyODksICJuYW1lIjogInBoaXNoX3RhbmtfY2hlY2tfdXJsIiwgInRleHQiOiAicGhp
c2hfdGFua19jaGVja191cmwiLCAicHJlZml4IjogbnVsbCwgInR5cGVfaWQiOiAxMSwgInRvb2x0
aXAiOiAiVVJMIHRvIGJlIGNoZWNrZWQgZm9yIHBoaXNoaW5nIHN0YXR1cy4iLCAicGxhY2Vob2xk
ZXIiOiAiIiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNl
LCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJs
YW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiZTNjOWU0NDYt
OTM1Yy00ZDdkLTliYzAtOTlhZGQ2OTMyMDk5IiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlv
bl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFi
bGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24v
cGhpc2hfdGFua19jaGVja191cmwiLCAidGVtcGxhdGVzIjogW10sICJkZXByZWNhdGVkIjogZmFs
c2V9XSwgImluY2lkZW50X3R5cGVzIjogW3sidXBkYXRlX2RhdGUiOiAxNTU3MzI0MTY4NDM4LCAi
Y3JlYXRlX2RhdGUiOiAxNTU3MzI0MTY4NDM4LCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgt
YWQzOS00YTAwMDQwNDRhYTAiLCAiZGVzY3JpcHRpb24iOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdl
cyAoaW50ZXJuYWwpIiwgImV4cG9ydF9rZXkiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50
ZXJuYWwpIiwgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImVu
YWJsZWQiOiBmYWxzZSwgInN5c3RlbSI6IGZhbHNlLCAicGFyZW50X2lkIjogbnVsbCwgImhpZGRl
biI6IGZhbHNlLCAiaWQiOiAwfV0sICJwaGFzZXMiOiBbXSwgImF1dG9tYXRpY190YXNrcyI6IFtd
LCAib3ZlcnJpZGVzIjogW10sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7Im5hbWUiOiAiZm5f
cGhpc2hfdGFuayIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJmbl9waGlzaF90YW5rIiwgImRlc3Rp
bmF0aW9uX3R5cGUiOiAwLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2VycyI6IFsibmthbmRoYTFA
aW4uaWJtLmNvbSJdLCAidXVpZCI6ICJkOWNiNTk2Mi1lNTQyLTQ3MjMtOGJmMi04ZmQ3NTE5ZmUz
OTgiLCAiZXhwb3J0X2tleSI6ICJmbl9waGlzaF90YW5rIn1dLCAiYWN0aW9ucyI6IFt7ImlkIjog
MTExLCAibmFtZSI6ICJFeGFtcGxlOiBQaGlzaFRhbms6IFN1Ym1pdCBVUkwiLCAidHlwZSI6IDEs
ICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJjb25kaXRpb25zIjogW3sibWV0aG9kIjogImVx
dWFscyIsICJmaWVsZF9uYW1lIjogImFydGlmYWN0LnR5cGUiLCAidmFsdWUiOiAiVVJMIiwgInR5
cGUiOiBudWxsLCAiZXZhbHVhdGlvbl9pZCI6IG51bGx9XSwgImF1dG9tYXRpb25zIjogW10sICJt
ZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAid29ya2Zsb3dzIjogWyJleGFtcGxlX3BoaXNodGFu
a19zdWJtaXRfdXJsIl0sICJ2aWV3X2l0ZW1zIjogW10sICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQw
MCwgInV1aWQiOiAiZTg0NWU1MTUtMDNmZC00NmRjLTgxNTAtNjg1MWQxOWY0NjhhIiwgImV4cG9y
dF9rZXkiOiAiRXhhbXBsZTogUGhpc2hUYW5rOiBTdWJtaXQgVVJMIiwgImxvZ2ljX3R5cGUiOiAi
YWxsIn1dLCAibGF5b3V0cyI6IFtdLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJ0aW1lZnJhbWVz
IjogbnVsbCwgImxvY2FsZSI6IG51bGwsICJpbmR1c3RyaWVzIjogbnVsbCwgInJlZ3VsYXRvcnMi
OiBudWxsLCAiZ2VvcyI6IG51bGwsICJ0YXNrX29yZGVyIjogW10sICJhY3Rpb25fb3JkZXIiOiBb
XSwgInR5cGVzIjogW10sICJzY3JpcHRzIjogW10sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6
IFtdLCAid29ya2Zsb3dzIjogW3sid29ya2Zsb3dfaWQiOiA5NSwgIm5hbWUiOiAiRXhhbXBsZTog
UGhpc2hUYW5rOiBTdWJtaXQgVVJMIiwgInByb2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfcGhp
c2h0YW5rX3N1Ym1pdF91cmwiLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAiZGVzY3JpcHRp
b24iOiAiQ2hlY2sgVVJMJ3MgYWdhaW5zdCBQaGlzaFRhbmtzKGh0dHBzOi8vd3d3LnBoaXNodGFu
ay5jb20vKSBEYXRhIGJhc2UgdG8gc2VlIFVSTCBpcyBmbGFnZ2VkIGFzIHBoaXNoaW5nIG9yIG5v
dCBwaGlzaGluZy4gYW5kIHRoZW4gdXBkYXRlIHRoZSBwaGlzaGluZyBzdGF0dXMgb24gYXJ0aWZh
Y3QgZGVzY3JpcHRpb24gZmllbGQuIiwgImNyZWF0b3JfaWQiOiAibmthbmRoYTFAaW4uaWJtLmNv
bSIsICJsYXN0X21vZGlmaWVkX2J5IjogIm5rYW5kaGExQGluLmlibS5jb20iLCAibGFzdF9tb2Rp
ZmllZF90aW1lIjogMTU1NzMyMzg4ODI5NiwgImV4cG9ydF9rZXkiOiAiZXhhbXBsZV9waGlzaHRh
bmtfc3VibWl0X3VybCIsICJ1dWlkIjogIjMxMGVkMmZiLWRkYzEtNDk3OS1iNjJlLTRjNjQzNWZj
OWJjNSIsICJjb250ZW50IjogeyJ3b3JrZmxvd19pZCI6ICJleGFtcGxlX3BoaXNodGFua19zdWJt
aXRfdXJsIiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwi
Pz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAw
NTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8y
MDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAx
MDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAw
NTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5c
IiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhz
aT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFt
ZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFt
cGxlX3BoaXNodGFua19zdWJtaXRfdXJsXCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJF
eGFtcGxlOiBQaGlzaFRhbms6IFN1Ym1pdCBVUkxcIj48ZG9jdW1lbnRhdGlvbj48IVtDREFUQVtD
aGVjayBVUkwncyBhZ2FpbnN0IFBoaXNoVGFua3MoaHR0cHM6Ly93d3cucGhpc2h0YW5rLmNvbS8p
IERhdGEgYmFzZSB0byBzZWUgVVJMIGlzIGZsYWdnZWQgYXMgcGhpc2hpbmcgb3Igbm90IHBoaXNo
aW5nLiBhbmQgdGhlbiB1cGRhdGUgdGhlIHBoaXNoaW5nIHN0YXR1cyBvbiBhcnRpZmFjdCBkZXNj
cmlwdGlvbiBmaWVsZC5dXT48L2RvY3VtZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2
ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzFtaW43bzM8L291dGdvaW5nPjwv
c3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFza18xNXRlNHdqXCIgbmFtZT1c
IlBoaXNoIFRhbmsgU3VibWl0IFVSTFwiIHJlc2lsaWVudDp0eXBlPVwiZnVuY3Rpb25cIj48ZXh0
ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlkPVwiNWI5ZTY3MTctOGM5ZC00
ZmQzLWJlZjMtNDZmYWUwODlmMWIxXCI+e1wiaW5wdXRzXCI6e30sXCJwb3N0X3Byb2Nlc3Npbmdf
c2NyaXB0XCI6XCIjIFBhcnNpbmcgdGhlIHJlc3VsdCByZXR1cm5lZCBmcm9tIGZ1bmN0aW9uIGZu
X3BoaXNoX3RhbmtcXG5jb250ZW50X2RpY3Rpb25hcnkgPSByZXN1bHRzLmdldCgnY29udGVudCcp
XFxucmVzdWx0X2RpY3Rpb25hcnkgPSBjb250ZW50X2RpY3Rpb25hcnkuZ2V0KCdyZXN1bHRzJylc
XG5VUkwgPSByZXN1bHRfZGljdGlvbmFyeS5nZXQoJ3VybCcpXFxucmljaF90ZXh0X3RtcCA9IFxc
XCImbHQ7YnImZ3Q7Jmx0O2ImZ3Q7VVJMOiB7fSZsdDsvYiZndDsmbHQ7L2JyJmd0O1xcXCIuZm9y
bWF0KFVSTClcXG5pZiByZXN1bHRfZGljdGlvbmFyeS5nZXQoJ2luX2RhdGFiYXNlJyk6XFxuICAg
ICBpZiByZXN1bHRfZGljdGlvbmFyeS5nZXQoJ3ZlcmlmaWVkJyk6XFxuICAgICAgICAgIGlmIHJl
c3VsdF9kaWN0aW9uYXJ5LmdldCgndmFsaWQnKTpcXG4gICAgICAgICAgICAgICByaWNoX3RleHRf
dG1wICs9IFxcXCImbHQ7cCBzdHlsZT0nY29sb3I6cmVkOycmZ3Q7Jmx0O2ImZ3Q7VGhpcyBVUkwg
aGFzIGJlZW4gY2hlY2tlZCBhZ2FpbnN0IFBoaXNoVGFuayBhbmQgaXQgaXMgVkFMSUQgUEhJU0gm
bHQ7L2ImZ3Q7XFxcIlxcbiAgICAgICAgICAgICAgIHBoaXNoX2lkID0gcmVzdWx0X2RpY3Rpb25h
cnkuZ2V0KCdwaGlzaF9pZCcpXFxuICAgICAgICAgICAgICAgZGV0YWlsc19wYWdlID0gcmVzdWx0
X2RpY3Rpb25hcnkuZ2V0KCdwaGlzaF9kZXRhaWxfcGFnZScpXFxuICAgICAgICAgICAgICAgdmVy
aWZpZWRfYXQgPSByZXN1bHRfZGljdGlvbmFyeS5nZXQoJ3ZlcmlmaWVkX2F0JylcXG4gICAgICAg
ICAgICAgICByaWNoX3RleHRfdG1wICs9IFxcXCImbHQ7YnImZ3Q7UGhpc2ggSUQ6IHswfSZsdDsv
YnImZ3Q7Jmx0O2JyJmd0O1BoaXNoIERldGFpbCBQYWdlOiAmbHQ7YSBocmVmPSd7MX0nJmd0O3sx
fSZsdDsvYSZndDsmbHQ7L2JyJmd0OyZsdDticiZndDsgVmVyaWZpZWQgYXQ6IHsyfSZsdDtici8m
Z3Q7Jmx0Oy9wJmd0O1xcXCIuZm9ybWF0KHBoaXNoX2lkLCBkZXRhaWxzX3BhZ2UsIHN0cih2ZXJp
ZmllZF9hdCkpXFxuICAgICAgICAgIGVsc2U6XFxuICAgICAgICAgICAgICAgcmljaF90ZXh0X3Rt
cCArPSBcXFwiJmx0O3Agc3R5bGU9J2NvbG9yOmdyZWVuOycmZ3Q7Jmx0O2ImZ3Q7VGhpcyBVUkwg
aGFzIGJlZW4gY2hlY2tlZCBhZ2FpbnN0IFBoaXNoVGFuayBhbmQgaXQgaXMgTk9UIFBISVNIJmx0
Oy9iJmd0OyZsdDsvcCZndDtcXFwiXFxuICAgICBlbHNlOlxcbiAgICAgICAgICByaWNoX3RleHRf
dG1wICs9IFxcXCImbHQ7cCBzdHlsZT0nY29sb3I6Z3JlZW47JyZndDsmbHQ7YiZndDtUaGlzIFVS
TCBoYXMgYmVlbiBjaGVja2VkIGFnYWluc3QgUGhpc2hUYW5rIGFuZCBpdCBpcyBub3QgdmVyaWZp
ZWQmbHQ7L2ImZ3Q7Jmx0Oy9wJmd0O1xcXCJcXG5lbHNlOlxcbiAgICAgcmljaF90ZXh0X3RtcCAr
PSBcXFwiJmx0O3Agc3R5bGU9J2NvbG9yOmdyZWVuOycmZ3Q7Jmx0O2ImZ3Q7VGhpcyBVUkwgaGFz
IGJlZW4gY2hlY2tlZCBhZ2FpbnN0IFBoaXNoVGFuayBhbmQgaXQgaXMgbm90IGZvdW5kIGluIHBo
aXNoVGFuayBEYXRhYmFzZS4mbHQ7L2ImZ3Q7Jmx0Oy9wJmd0O1xcXCJcXG4jIEFwcGVuZGluZyB0
byBleHN0aW5nIGFydGlmYWN0IGRlc2NyaXB0aW9uIGZpZWxkLlxcbnRtcF9kZXNjID0gYXJ0aWZh
Y3QuZGVzY3JpcHRpb25cXG5pZiB0bXBfZGVzYzpcXG4gICAgIHRtcF9kZXNjID0gdG1wX2Rlc2Mu
Z2V0KCdjb250ZW50JylcXG5lbHNlOlxcbiAgICAgdG1wX2Rlc2MgPSBcXFwiXFxcIlxcbmNvbXBs
ZXRlX3RtcF90ZXh0ID0gdG1wX2Rlc2MgKyByaWNoX3RleHRfdG1wXFxucmljaF90ZXh0ID0gaGVs
cGVyLmNyZWF0ZVJpY2hUZXh0KGNvbXBsZXRlX3RtcF90ZXh0KVxcbmxhdGVzdF9yaWNoX3RleHQg
PSBoZWxwZXIuY3JlYXRlUmljaFRleHQocmljaF90ZXh0X3RtcClcXG5pbmNpZGVudC5hZGROb3Rl
KGxhdGVzdF9yaWNoX3RleHQpXFxuYXJ0aWZhY3QuZGVzY3JpcHRpb24gPSByaWNoX3RleHRcXG5c
XG5cXG5cXG5cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiaW5wdXRzLnBoaXNoX3Rhbmtf
Y2hlY2tfdXJsID0gYXJ0aWZhY3QudmFsdWVcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVu
c2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMW1pbjdvMzwvaW5jb21pbmc+PG91
dGdvaW5nPlNlcXVlbmNlRmxvd18wd3R6OThpPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1
ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMW1pbjdvM1wiIHNvdXJjZVJlZj1cIlN0YXJ0RXZl
bnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzE1dGU0d2pcIi8+PGVuZEV2ZW50
IGlkPVwiRW5kRXZlbnRfMDZ4ajVkbFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMHd0ejk4aTwv
aW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzB3dHo5
OGlcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xNXRlNHdqXCIgdGFyZ2V0UmVmPVwiRW5kRXZl
bnRfMDZ4ajVkbFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0
XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+
PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0
RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRl
eHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMG93bzJhdFwiPjx0ZXh0PjwhW0NEQVRB
W0NoZWNrIFVSTCdzIFBoaXNoaW5nIHN0YXR1cyBmcm9tIFBoaXNoVGFuayhodHRwczovL3d3dy5w
aGlzaHRhbmsuY29tLykgZGF0YSBiYXNlLCBhbmQgdXBkYXRlIHRoZSBwaGlzaGluZyBzdGF0dXMg
b24gYXJ0aWZhY3QgZGVzY3JpcHRpb24gZmllbGQuXV0+PC90ZXh0PjwvdGV4dEFubm90YXRpb24+
PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMTUyaHVkaFwiIHNvdXJjZVJlZj1cIlNlcnZp
Y2VUYXNrXzE1dGU0d2pcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8wb3dvMmF0XCIvPjwv
cHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6
QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxi
cG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJT
dGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9
XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5k
aTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVt
ZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5
dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwi
IHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1l
bnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+
PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIy
MFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5
PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50
PVwiU2VydmljZVRhc2tfMTV0ZTR3alwiIGlkPVwiU2VydmljZVRhc2tfMTV0ZTR3al9kaVwiPjxv
bWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzMTlcIiB5PVwiMTY2
XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2Vx
dWVuY2VGbG93XzFtaW43bzNcIiBpZD1cIlNlcXVlbmNlRmxvd18xbWluN28zX2RpXCI+PG9tZ2Rp
OndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48
b21nZGk6d2F5cG9pbnQgeD1cIjMxOVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2
XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1c
IjBcIiB4PVwiMjU4LjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpC
UE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzA2eGo1ZGxc
IiBpZD1cIkVuZEV2ZW50XzA2eGo1ZGxfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIg
d2lkdGg9XCIzNlwiIHg9XCI1OTguNzYzMjY1MzA2MTIyNFwiIHk9XCIxODhcIi8+PGJwbW5kaTpC
UE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI2MTYu
NzYzMjY1MzA2MTIyNFwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQ
TU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzB3dHo5
OGlcIiBpZD1cIlNlcXVlbmNlRmxvd18wd3R6OThpX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0
MTlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQg
eD1cIjU5OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBN
TkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTA5XCIg
eT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpC
UE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wb3dvMmF0XCIgaWQ9XCJUZXh0
QW5ub3RhdGlvbl8wb3dvMmF0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI2MlwiIHdpZHRo
PVwiNDMxXCIgeD1cIjQ2MFwiIHk9XCI1OVwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpC
UE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzE1Mmh1ZGhcIiBpZD1cIkFzc29jaWF0
aW9uXzE1Mmh1ZGhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQxOVwiIHhzaTp0eXBlPVwib21n
ZGM6UG9pbnRcIiB5PVwiMTg3XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTk2XCIgeHNpOnR5cGU9
XCJvbWdkYzpQb2ludFwiIHk9XCIxMjFcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBN
TlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgInZlcnNpb24iOiAx
Nn0sICJhY3Rpb25zIjogW119XSwgInJvbGVzIjogW10sICJ3b3Jrc3BhY2VzIjogW10sICJmdW5j
dGlvbnMiOiBbeyJpZCI6IDUyLCAibmFtZSI6ICJmbl9waGlzaF90YW5rX3N1Ym1pdF91cmwiLCAi
ZGlzcGxheV9uYW1lIjogIlBoaXNoIFRhbmsgU3VibWl0IFVSTCIsICJkZXNjcmlwdGlvbiI6IHsi
Zm9ybWF0IjogInRleHQiLCAiY29udGVudCI6ICJGdW5jdGlvbiB0byBjaGVjayBVUkxzIGFnYWlu
c3QgUGhpc2hUYW5rcyhodHRwczovL3d3dy5waGlzaHRhbmsuY29tLykgRGF0YWJhc2UgdG8gc2Vl
IFVSTCBpcyBmbGFnZ2VkIGFzIHBoaXNoaW5nIG9yIG5vdCBwaGlzaGluZy4ifSwgImRlc3RpbmF0
aW9uX2hhbmRsZSI6ICJmbl9waGlzaF90YW5rIiwgImV4cG9ydF9rZXkiOiAiZm5fcGhpc2hfdGFu
a19zdWJtaXRfdXJsIiwgInV1aWQiOiAiNWI5ZTY3MTctOGM5ZC00ZmQzLWJlZjMtNDZmYWUwODlm
MWIxIiwgInZlcnNpb24iOiAxLCAiY3JlYXRvciI6IHsiaWQiOiA2LCAidHlwZSI6ICJ1c2VyIiwg
Im5hbWUiOiAibmthbmRoYTFAaW4uaWJtLmNvbSIsICJkaXNwbGF5X25hbWUiOiAiTml0aW4gS2Fu
ZGhhcmUgIn0sICJsYXN0X21vZGlmaWVkX2J5IjogeyJpZCI6IDYsICJ0eXBlIjogInVzZXIiLCAi
bmFtZSI6ICJua2FuZGhhMUBpbi5pYm0uY29tIiwgImRpc3BsYXlfbmFtZSI6ICJOaXRpbiBLYW5k
aGFyZSAifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NTczMjAzMzc4NjMsICJ2aWV3X2l0ZW1z
IjogW3sic3RlcF9sYWJlbCI6IG51bGwsICJzaG93X2lmIjogbnVsbCwgImVsZW1lbnQiOiAiZmll
bGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAiY29udGVudCI6ICJlM2M5ZTQ0
Ni05MzVjLTRkN2QtOWJjMC05OWFkZDY5MzIwOTkiLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNl
fV0sICJ3b3JrZmxvd3MiOiBbeyJ3b3JrZmxvd19pZCI6IDk1LCAibmFtZSI6ICJFeGFtcGxlOiBQ
aGlzaFRhbms6IFN1Ym1pdCBVUkwiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9waGlz
aHRhbmtfc3VibWl0X3VybCIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJkZXNjcmlwdGlv
biI6IG51bGwsICJ1dWlkIjogbnVsbCwgImFjdGlvbnMiOiBbXX1dfV19
"""
    )