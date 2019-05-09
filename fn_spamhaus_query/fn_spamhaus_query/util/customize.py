# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_spamhaus_query"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_spamhaus_query package"""
    reload_params = {"package": u"fn_spamhaus_query",
                    "incident_fields": [], 
                    "action_fields": [u"spamhaus_domain_name_resource", u"spamhaus_ip_resource"], 
                    "function_params": [u"spamhaus_query_string", u"spamhause_search_resource"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_spamhaus_query"], 
                    "functions": [u"fn_spamhaus_query_submit_artifact"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_spamhaus_submit_domain_name", u"example_spamhaus_submit_ip_address"], 
                    "actions": [u"Example: SpamHaus: Submit Domain Name", u"Example: SpamHaus: Submit IP Address"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Action fields:
    #     spamhaus_domain_name_resource
    #     spamhaus_ip_resource
    #   Function inputs:
    #     spamhaus_query_string
    #     spamhause_search_resource
    #   Message Destinations:
    #     fn_spamhaus_query
    #   Functions:
    #     fn_spamhaus_query_submit_artifact
    #   Workflows:
    #     example_spamhaus_submit_domain_name
    #     example_spamhaus_submit_ip_address
    #   Rules:
    #     Example: SpamHaus: Submit Domain Name
    #     Example: SpamHaus: Submit IP Address


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMSwgImJ1aWxkX251bWJl
ciI6IDc2LCAidmVyc2lvbiI6ICIzMS4xLjc2In0sICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAy
LCAiaWQiOiAxMTEsICJleHBvcnRfZGF0ZSI6IDE1NTczOTk0NzQ4MTIsICJmaWVsZHMiOiBbeyJp
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
IHsiaWQiOiAyOTksICJuYW1lIjogInNwYW1oYXVzX2lwX3Jlc291cmNlIiwgInRleHQiOiAiU3Bh
bUhhdXMgSVAgUmVzb3VyY2UiLCAicHJlZml4IjogInByb3BlcnRpZXMiLCAidHlwZV9pZCI6IDYs
ICJ0b29sdGlwIjogInJlc291cmNlLW5hbWUgaXMgYSByZXF1aXJlZCBlbnVtZXJhdGVkIGZpZWxk
IHRoYXQgcmVwcmVzZW50cyB3aGljaCBibG9ja2xpc3Qgc2hvdWxkIGJlIHF1ZXJpZWQiLCAicGxh
Y2Vob2xkZXIiOiAiIiwgImlucHV0X3R5cGUiOiAic2VsZWN0IiwgInJlcXVpcmVkIjogImFsd2F5
cyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0
X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJu
YWwiOiBmYWxzZSwgInV1aWQiOiAiMGI0Y2Q4ZjMtOTdkYy00ZWNkLTk1MjktOTI2M2FiNmQwZTZm
IiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW3si
dmFsdWUiOiAyMTAsICJsYWJlbCI6ICJTQkwiLCAiZW5hYmxlZCI6IHRydWUsICJwcm9wZXJ0aWVz
IjogbnVsbCwgInV1aWQiOiAiNzMxMzliN2EtYTllMS00ZjM5LThhZTgtNDE4ZTk2MzU4ZjM4Iiwg
ImhpZGRlbiI6IGZhbHNlLCAiZGVmYXVsdCI6IHRydWV9LCB7InZhbHVlIjogMjExLCAibGFiZWwi
OiAiWEJMIiwgImVuYWJsZWQiOiB0cnVlLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlkIjogImE3
ODhkODgyLWE5ZDgtNDZiMS1hN2YwLTFkYmZiYzVlMjcyYyIsICJoaWRkZW4iOiBmYWxzZSwgImRl
ZmF1bHQiOiBmYWxzZX0sIHsidmFsdWUiOiAyMTIsICJsYWJlbCI6ICJQQkwiLCAiZW5hYmxlZCI6
IHRydWUsICJwcm9wZXJ0aWVzIjogbnVsbCwgInV1aWQiOiAiZGU0NDFkMWEtYzQ4NC00YWJjLTg2
NGMtOGNlNDc5NmU3MjExIiwgImhpZGRlbiI6IGZhbHNlLCAiZGVmYXVsdCI6IGZhbHNlfSwgeyJ2
YWx1ZSI6IDIxMywgImxhYmVsIjogIlNCTC1YQkwiLCAiZW5hYmxlZCI6IHRydWUsICJwcm9wZXJ0
aWVzIjogbnVsbCwgInV1aWQiOiAiNjU1ZDIzYjAtZDcwMC00MjQ1LWIzZDUtYjZjMzJjYmY1ODRj
IiwgImhpZGRlbiI6IGZhbHNlLCAiZGVmYXVsdCI6IGZhbHNlfSwgeyJ2YWx1ZSI6IDIxNCwgImxh
YmVsIjogIlpFTiIsICJlbmFibGVkIjogdHJ1ZSwgInByb3BlcnRpZXMiOiBudWxsLCAidXVpZCI6
ICI4NTFhODQxMS0zOWMwLTQxOWQtODQ1MC1jOGM2MTdiOWVhNmIiLCAiaGlkZGVuIjogZmFsc2Us
ICJkZWZhdWx0IjogZmFsc2V9LCB7InZhbHVlIjogMjE1LCAibGFiZWwiOiAiTVNSIiwgImVuYWJs
ZWQiOiB0cnVlLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlkIjogIjJjYzJmZmI4LTY4NWMtNDI0
MC1hMzM4LTdkNTViYWZiZmE5OSIsICJoaWRkZW4iOiBmYWxzZSwgImRlZmF1bHQiOiBmYWxzZX0s
IHsidmFsdWUiOiAyMTYsICJsYWJlbCI6ICJBVVRIQkwiLCAiZW5hYmxlZCI6IHRydWUsICJwcm9w
ZXJ0aWVzIjogbnVsbCwgInV1aWQiOiAiODM4ZjM0NjEtZDYxYS00ZDk2LThiZTItYTA2N2JlYTIz
YjU5IiwgImhpZGRlbiI6IGZhbHNlLCAiZGVmYXVsdCI6IGZhbHNlfV0sICJyZWFkX29ubHkiOiBm
YWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5
IjogImFjdGlvbmludm9jYXRpb24vc3BhbWhhdXNfaXBfcmVzb3VyY2UiLCAidGVtcGxhdGVzIjog
W10sICJkZXByZWNhdGVkIjogZmFsc2V9LCB7ImlkIjogMzAwLCAibmFtZSI6ICJzcGFtaGF1c19k
b21haW5fbmFtZV9yZXNvdXJjZSIsICJ0ZXh0IjogIlNwYW1IYXVzIERvbWFpbiBOYW1lIFJlc291
cmNlIiwgInByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgInR5cGVfaWQiOiA2LCAidG9vbHRpcCI6ICJy
ZXNvdXJjZS1uYW1lIGlzIGEgcmVxdWlyZWQgZW51bWVyYXRlZCBmaWVsZCB0aGF0IHJlcHJlc2Vu
dHMgd2hpY2ggYmxvY2tsaXN0IHNob3VsZCBiZSBxdWVyaWVkIiwgInBsYWNlaG9sZGVyIjogIiIs
ICJpbnB1dF90eXBlIjogInNlbGVjdCIsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAiaGlkZV9ub3Rp
ZmljYXRpb24iOiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2Vy
dmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1
dWlkIjogIjJjZmVhMjhiLThmOGYtNGY3ZC1hN2QyLTE0ZmQ1YjgyMGFkZiIsICJvcGVyYXRpb25z
IjogW10sICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVlcyI6IFt7InZhbHVlIjogMjE3LCAi
bGFiZWwiOiAiWlJEIiwgImVuYWJsZWQiOiB0cnVlLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlk
IjogIjE4MmY3NGQ2LWFhNzUtNGJjMS05NDgxLWI2NjcwMTZlZDc2ZCIsICJoaWRkZW4iOiBmYWxz
ZSwgImRlZmF1bHQiOiB0cnVlfSwgeyJ2YWx1ZSI6IDIxOCwgImxhYmVsIjogIkRCTCIsICJlbmFi
bGVkIjogdHJ1ZSwgInByb3BlcnRpZXMiOiBudWxsLCAidXVpZCI6ICI0OGEwNDdlNS1kYjNmLTRh
MGUtOWU1My00ZWJhMGMwZTBlZDgiLCAiaGlkZGVuIjogZmFsc2UsICJkZWZhdWx0IjogZmFsc2V9
XSwgInJlYWRfb25seSI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJyaWNoX3RleHQiOiBm
YWxzZSwgImV4cG9ydF9rZXkiOiAiYWN0aW9uaW52b2NhdGlvbi9zcGFtaGF1c19kb21haW5fbmFt
ZV9yZXNvdXJjZSIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQi
OiAzMDIsICJuYW1lIjogInNwYW1oYXVzZV9zZWFyY2hfcmVzb3VyY2UiLCAidGV4dCI6ICJzcGFt
aGF1c2Vfc2VhcmNoX3Jlc291cmNlIiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMTEsICJ0
b29sdGlwIjogInJlc291cmNlLW5hbWUgaXMgYSByZXF1aXJlZCBlbnVtZXJhdGVkIGZpZWxkIHRo
YXQgcmVwcmVzZW50cyB3aGljaCBibG9ja2xpc3Qgc2hvdWxkIGJlIHF1ZXJpZWQuIiwgInBsYWNl
aG9sZGVyIjogIlNCTCxYQkwsUEJMLFNCTC1YQkwsWkVOLE1TUixBVVRIQkwsWlJEIChkb21haW5z
IG9ubHkpLERCTCAoZG9tYWlucyBvbmx5KS4iLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInJlcXVp
cmVkIjogImFsd2F5cyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFs
c2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZh
bHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiNjgxZTRkMzYtZjlkMy00NmIzLThlNWUt
MjZmOTk3MDgxYzA5IiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAi
dmFsdWVzIjogW10sICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmlj
aF90ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vc3BhbWhhdXNlX3NlYXJj
aF9yZXNvdXJjZSIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQi
OiAzMDEsICJuYW1lIjogInNwYW1oYXVzX3F1ZXJ5X3N0cmluZyIsICJ0ZXh0IjogInNwYW1oYXVz
X3F1ZXJ5X3N0cmluZyIsICJwcmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDExLCAidG9vbHRpcCI6
ICJJUCBBZHJlc3Mgb3IgRG9tYWluIE5hbWUgdG8gYmUgY2hlY2tlZCBhZ2FpbnN0IFNwYW1oYXVz
IGRhdGFiYXNlLiIsICJwbGFjZWhvbGRlciI6ICJJUCBBZGRyZXNzL0RvbWFpbiBOYW1lIiwgImlu
cHV0X3R5cGUiOiAidGV4dCIsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAiaGlkZV9ub3RpZmljYXRp
b24iOiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjog
ZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjog
IjEyYTExYjY0LTE2YjMtNDUwOS05MzMyLTU5OTA5NmI5OWQ5OSIsICJvcGVyYXRpb25zIjogW10s
ICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogZmFsc2Us
ICJjaGFuZ2VhYmxlIjogdHJ1ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJf
X2Z1bmN0aW9uL3NwYW1oYXVzX3F1ZXJ5X3N0cmluZyIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJl
Y2F0ZWQiOiBmYWxzZX1dLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE1NTcz
OTk1MjI1ODcsICJjcmVhdGVfZGF0ZSI6IDE1NTczOTk1MjI1ODcsICJ1dWlkIjogImJmZWVjMmQ0
LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0
aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBh
Y2thZ2VzIChpbnRlcm5hbCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRl
cm5hbCkiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBu
dWxsLCAiaGlkZGVuIjogZmFsc2UsICJpZCI6IDB9XSwgInBoYXNlcyI6IFtdLCAiYXV0b21hdGlj
X3Rhc2tzIjogW10sICJvdmVycmlkZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3si
bmFtZSI6ICJmbl9zcGFtaGF1c19xdWVyeSIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJmbl9zcGFt
aGF1c19xdWVyeSIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgImV4cGVjdF9hY2siOiB0cnVlLCAi
dXNlcnMiOiBbIm5rYW5kaGExQGluLmlibS5jb20iXSwgInV1aWQiOiAiNmIzMDEyZDItMzdlMS00
ZGUwLWI1OTAtNzRiOWRiZTFkNGViIiwgImV4cG9ydF9rZXkiOiAiZm5fc3BhbWhhdXNfcXVlcnki
fV0sICJhY3Rpb25zIjogW3siaWQiOiAxMDgsICJuYW1lIjogIkV4YW1wbGU6IFNwYW1IYXVzOiBT
dWJtaXQgRG9tYWluIE5hbWUiLCAidHlwZSI6IDEsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIs
ICJjb25kaXRpb25zIjogW3sibWV0aG9kIjogImVxdWFscyIsICJmaWVsZF9uYW1lIjogImFydGlm
YWN0LnR5cGUiLCAidmFsdWUiOiAiRE5TIE5hbWUiLCAidHlwZSI6IG51bGwsICJldmFsdWF0aW9u
X2lkIjogbnVsbH1dLCAiYXV0b21hdGlvbnMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjog
W10sICJ3b3JrZmxvd3MiOiBbImV4YW1wbGVfc3BhbWhhdXNfc3VibWl0X2RvbWFpbl9uYW1lIl0s
ICJ2aWV3X2l0ZW1zIjogW3sic3RlcF9sYWJlbCI6IG51bGwsICJzaG93X2lmIjogbnVsbCwgImVs
ZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAi
Y29udGVudCI6ICIyY2ZlYTI4Yi04ZjhmLTRmN2QtYTdkMi0xNGZkNWI4MjBhZGYiLCAic2hvd19s
aW5rX2hlYWRlciI6IGZhbHNlfV0sICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAi
NDNkOWQwY2UtZDQxMS00OTYzLTlmZDgtYjIyNTg5NzY1MDcyIiwgImV4cG9ydF9rZXkiOiAiRXhh
bXBsZTogU3BhbUhhdXM6IFN1Ym1pdCBEb21haW4gTmFtZSIsICJsb2dpY190eXBlIjogImFsbCJ9
LCB7ImlkIjogMTA3LCAibmFtZSI6ICJFeGFtcGxlOiBTcGFtSGF1czogU3VibWl0IElQIEFkZHJl
c3MiLCAidHlwZSI6IDEsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJjb25kaXRpb25zIjog
W3sibWV0aG9kIjogImVxdWFscyIsICJmaWVsZF9uYW1lIjogImFydGlmYWN0LnR5cGUiLCAidmFs
dWUiOiAiSVAgQWRkcmVzcyIsICJ0eXBlIjogbnVsbCwgImV2YWx1YXRpb25faWQiOiBudWxsfV0s
ICJhdXRvbWF0aW9ucyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIndvcmtmbG93
cyI6IFsiZXhhbXBsZV9zcGFtaGF1c19zdWJtaXRfaXBfYWRkcmVzcyJdLCAidmlld19pdGVtcyI6
IFt7InN0ZXBfbGFiZWwiOiBudWxsLCAic2hvd19pZiI6IG51bGwsICJlbGVtZW50IjogImZpZWxk
X3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgImNvbnRlbnQiOiAiMGI0
Y2Q4ZjMtOTdkYy00ZWNkLTk1MjktOTI2M2FiNmQwZTZmIiwgInNob3dfbGlua19oZWFkZXIiOiBm
YWxzZX1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogImE4M2Q0YTljLTMyMDct
NGVhMi04MjNjLWExODJiZjZjODE2NSIsICJleHBvcnRfa2V5IjogIkV4YW1wbGU6IFNwYW1IYXVz
OiBTdWJtaXQgSVAgQWRkcmVzcyIsICJsb2dpY190eXBlIjogImFsbCJ9XSwgImxheW91dHMiOiBb
XSwgIm5vdGlmaWNhdGlvbnMiOiBudWxsLCAidGltZWZyYW1lcyI6IG51bGwsICJsb2NhbGUiOiBu
dWxsLCAiaW5kdXN0cmllcyI6IG51bGwsICJyZWd1bGF0b3JzIjogbnVsbCwgImdlb3MiOiBudWxs
LCAidGFza19vcmRlciI6IFtdLCAiYWN0aW9uX29yZGVyIjogW10sICJ0eXBlcyI6IFtdLCAic2Ny
aXB0cyI6IFtdLCAiaW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgIndvcmtmbG93cyI6IFt7
IndvcmtmbG93X2lkIjogOTIsICJuYW1lIjogIkV4YW1wbGU6IFNwYW1IYXVzOiBTdWJtaXQgSVAg
QWRkcmVzcyIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3NwYW1oYXVzX3N1Ym1pdF9p
cF9hZGRyZXNzIiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgImRlc2NyaXB0aW9uIjogIkNo
ZWNrIElQIEFkZHJlc3MgYWdhaW5zdCBTcGFtaGF1cyBEYXRhYmFzZSB0byBzZWUgd2hldGhlciBJ
UCBBZGRyZXNzIGlzIGluIGJsb2NrIGxpc3QgcmVjb3JkcyBvciBub3QuaWYgZ2l2ZW4gYXJ0aWZh
Y3QgYXBwZWFycyBpbiBvbmUgb2YgdGhlIGJsb2NrIGxpc3QgcmVjb3JkLCB0aGVuIGFydGlmYWN0
cyBkZXNjcmlwdGlvbiBmaWxlZCB3aWxsIGJlIHVwZGF0ZWQgd2l0aCBhZGRpdGlvbmFsIGluZm9y
bWF0aW9uLiIsICJjcmVhdG9yX2lkIjogIm5rYW5kaGExQGluLmlibS5jb20iLCAibGFzdF9tb2Rp
ZmllZF9ieSI6ICJua2FuZGhhMUBpbi5pYm0uY29tIiwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1
NTczMzQwNTYxOTgsICJleHBvcnRfa2V5IjogImV4YW1wbGVfc3BhbWhhdXNfc3VibWl0X2lwX2Fk
ZHJlc3MiLCAidXVpZCI6ICI0NDU0OWViYS1hODQ1LTRjOGUtYTU2Ny1kNzBjZGQ3NDBmMmUiLCAi
Y29udGVudCI6IHsid29ya2Zsb3dfaWQiOiAiZXhhbXBsZV9zcGFtaGF1c19zdWJtaXRfaXBfYWRk
cmVzcyIsICJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+
PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUy
NC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAx
MDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAw
NTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUy
NC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIg
eG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9
XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVz
cGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiZXhhbXBs
ZV9zcGFtaGF1c19zdWJtaXRfaXBfYWRkcmVzc1wiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1l
PVwiRXhhbXBsZTogU3BhbUhhdXM6IFN1Ym1pdCBJUCBBZGRyZXNzXCI+PGRvY3VtZW50YXRpb24+
Q2hlY2sgSVAgQWRkcmVzcyBhZ2FpbnN0IFNwYW1oYXVzIERhdGFiYXNlIHRvIHNlZSB3aGV0aGVy
IElQIEFkZHJlc3MgaXMgaW4gYmxvY2sgbGlzdCByZWNvcmRzIG9yIG5vdC5pZiBnaXZlbiBhcnRp
ZmFjdCBhcHBlYXJzIGluIG9uZSBvZiB0aGUgYmxvY2sgbGlzdCByZWNvcmQsIHRoZW4gYXJ0aWZh
Y3RzIGRlc2NyaXB0aW9uIGZpbGVkIHdpbGwgYmUgdXBkYXRlZCB3aXRoIGFkZGl0aW9uYWwgaW5m
b3JtYXRpb24uPC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVh
c3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wbmdpODk4PC9vdXRnb2luZz48L3N0YXJ0RXZl
bnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMTFvMnBnclwiIG5hbWU9XCJTcGFtaGF1
cyBRdWVyeSBTdWJtaXQgQXJ0aWZhY3RcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4
dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cImFjYjJhMDdjLTgxNWMt
NDU0MC04MDZhLWUxMTAwMmI4YTJjNlwiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5n
X3NjcmlwdFwiOlwicmVzdWx0c19kYXRhID0gcmVzdWx0cy5nZXQoJ2NvbnRlbnQnKVxcbnRtcF90
ZXh0ID0gXFxcIlxcXCJcXG50bXBfZGVzYyA9IGFydGlmYWN0LmRlc2NyaXB0aW9uXFxuaWYgcmVz
dWx0c19kYXRhLmdldCgnaXNfaW5fYmxvY2tsaXN0Jyk6XFxuICAgICB0bXBfdGV4dCA9IFxcXCIm
bHQ7YnImZ3Q7Jmx0O2JyJmd0OyZsdDtiJmd0O1RoaXMgYXJ0aWZhY3QgY2hlY2tlZCBhZ2FpbnN0
IFNwYW1oYXVzIGFuZCBpdCBpcyBpbiBibG9jayBsaXN0LiZsdDsvYiZndDtcXFwiXFxuICAgICBy
ZXNwX2xpc3QgPSByZXN1bHRzX2RhdGEuZ2V0KCdyZXNwJylcXG4gICAgIGZvciBjb2RlIGluIHJl
c3BfbGlzdDpcXG4gICAgICAgICAgY29kZSA9IHN0cihjb2RlKVxcbiAgICAgICAgICB0bXBfdGV4
dCArPSBcXFwiJmx0O2JyJmd0OyZsdDtiJmd0O2NvZGUgOiZsdDsvYiZndDsge30mbHQ7L2JyJmd0
O1xcXCIuZm9ybWF0KGNvZGUpXFxuICAgICAgICAgIHRtcF90ZXh0ICs9IFxcXCImbHQ7YnImZ3Q7
Jmx0O2ImZ3Q7ZGF0YXNldCA6Jmx0Oy9iJmd0OyB7fSZsdDsvYnImZ3Q7XFxcIi5mb3JtYXQocmVz
dWx0c19kYXRhLmdldChjb2RlKS5nZXQoJ2RhdGFzZXQnKSlcXG4gICAgICAgICAgdG1wX3RleHQg
Kz0gXFxcIiZsdDticiZndDsmbHQ7YiZndDtleHBsYW5hdGlvbiA6Jmx0Oy9iJmd0OyB7fSZsdDsv
YnImZ3Q7XFxcIi5mb3JtYXQocmVzdWx0c19kYXRhLmdldChjb2RlKS5nZXQoJ2V4cGxhbmF0aW9u
JykpXFxuICAgICAgICAgIHRtcF90ZXh0ICs9IFxcXCImbHQ7YnImZ3Q7Jmx0O2ImZ3Q7VVJMIDom
bHQ7L2ImZ3Q7ICZsdDsvYnImZ3Q7e30mbHQ7L2JyJmd0O1xcXCIuZm9ybWF0KHJlc3VsdHNfZGF0
YS5nZXQoY29kZSkuZ2V0KCdVUkwnKSlcXG5lbHNlOlxcbiAgICAgdG1wX3RleHQgPSBcXFwiJmx0
O2JyJmd0OyZsdDticiZndDsmbHQ7YiZndDtUaGlzIGFydGlmYWN0IGNoZWNrZWQgYWdhaW5zdCBT
cGFtaGF1cyBhbmQgaXQgaXMgbm90IGluIGJsb2NrIGxpc3QuJmx0Oy9iJmd0OyZsdDsvYnImZ3Q7
Jmx0Oy9iciZndDtcXFwiXFxuaWYgdG1wX2Rlc2M6XFxuICAgICB0bXBfZGVzYyA9IHRtcF9kZXNj
LmdldCgnY29udGVudCcpXFxuZWxzZTpcXG4gICAgIHRtcF9kZXNjID0gXFxcIlxcXCIgXFxuY29t
cGxldGVfdG1wX3RleHQgPSB0bXBfZGVzYyt0bXBfdGV4dFxcbnJpY2hfdGV4dCA9IGhlbHBlci5j
cmVhdGVSaWNoVGV4dChjb21wbGV0ZV90bXBfdGV4dClcXG5hcnRpZmFjdC5kZXNjcmlwdGlvbiA9
IHJpY2hfdGV4dFwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJpbnB1dHMuc3BhbWhhdXNf
cXVlcnlfc3RyaW5nID0gYXJ0aWZhY3QudmFsdWVcXG5pbnB1dHMuc3BhbWhhdXNlX3NlYXJjaF9y
ZXNvdXJjZSA9IHJ1bGUucHJvcGVydGllcy5zcGFtaGF1c19pcF9yZXNvdXJjZVwifTwvcmVzaWxp
ZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18w
bmdpODk4PC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzB4eDE5b3k8L291dGdvaW5n
Pjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wbmdpODk4XCIg
c291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tf
MTFvMnBnclwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8xZGMxdXhwXCI+PGluY29taW5nPlNl
cXVlbmNlRmxvd18weHgxOW95PC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9
XCJTZXF1ZW5jZUZsb3dfMHh4MTlveVwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzExbzJwZ3Jc
IiB0YXJnZXRSZWY9XCJFbmRFdmVudF8xZGMxdXhwXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRl
eHRBbm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3Rl
eHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4
XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90
YXRpb25fMWt4eGl5dFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xdmpm
eHF1XCI+PHRleHQ+QSB3b3JrZmxvdyB0byBjaGVjayBJUCBBZGRyZXNzIGFnYWluc3QgU3BhbWhh
dXMgZGF0YWJhc2UgdG8gc2VlIHdoZXRoZXIgZG9tYWluIGlzIGluIFNwYW1oYXVzIGJsb2NrIGxp
c3Qgb3Igbm90LjwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29j
aWF0aW9uXzB0NjZ6cmNcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xMW8ycGdyXCIgdGFyZ2V0
UmVmPVwiVGV4dEFubm90YXRpb25fMXZqZnhxdVwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlh
Z3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1c
InVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxl
bWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+
PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4
OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1c
IjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQ
TU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFr
eHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQ
TU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0
OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5
XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9
XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1O
RWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzExbzJwZ3Jc
IiBpZD1cIlNlcnZpY2VUYXNrXzExbzJwZ3JfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgw
XCIgd2lkdGg9XCIxMDBcIiB4PVwiMzU1XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+
PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wbmdpODk4XCIgaWQ9
XCJTZXF1ZW5jZUZsb3dfMG5naTg5OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNp
OnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIyNzZc
IiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1c
IjI3NlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2lu
dCB4PVwiMzU1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpC
UE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCIyOTFc
IiB5PVwiMTk5LjVcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1u
ZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMWRjMXV4cFwiIGlkPVwiRW5kRXZl
bnRfMWRjMXV4cF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIg
eD1cIjY1OFwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWln
aHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI2NzZcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5M
YWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNl
cXVlbmNlRmxvd18weHgxOW95XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMHh4MTlveV9kaVwiPjxvbWdk
aTp3YXlwb2ludCB4PVwiNDU1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+
PG9tZ2RpOndheXBvaW50IHg9XCI2NThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIw
NlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9
XCIwXCIgeD1cIjU1Ni41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6
QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8x
dmpmeHF1XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xdmpmeHF1X2RpXCI+PG9tZ2RjOkJvdW5kcyBo
ZWlnaHQ9XCI1M1wiIHdpZHRoPVwiNDAwXCIgeD1cIjQ1M1wiIHk9XCI2OVwiLz48L2JwbW5kaTpC
UE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzB0NjZ6
cmNcIiBpZD1cIkFzc29jaWF0aW9uXzB0NjZ6cmNfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQ1
NVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTg0XCIvPjxvbWdkaTp3YXlwb2ludCB4
PVwiNTk0XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxMjJcIi8+PC9icG1uZGk6QlBN
TkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlv
bnM+IiwgInZlcnNpb24iOiA3fSwgImFjdGlvbnMiOiBbXX0sIHsid29ya2Zsb3dfaWQiOiA5Mywg
Im5hbWUiOiAiRXhhbXBsZTogU3BhbUhhdXM6IFN1Ym1pdCBEb21haW4gTmFtZSIsICJwcm9ncmFt
bWF0aWNfbmFtZSI6ICJleGFtcGxlX3NwYW1oYXVzX3N1Ym1pdF9kb21haW5fbmFtZSIsICJvYmpl
Y3RfdHlwZSI6ICJhcnRpZmFjdCIsICJkZXNjcmlwdGlvbiI6ICJDaGVjayBEb21haW4gTmFtZSBh
Z2FpbnN0IFNwYW1oYXVzIERhdGFiYXNlIHRvIHNlZSB3aGV0aGVyIERvbWFpbiBOYW1lIGlzIGlu
IGJsb2NrIGxpc3QgcmVjb3JkcyBvciBub3QuaWYgZ2l2ZW4gYXJ0aWZhY3QgYXBwZWFycyBpbiBv
bmUgb2YgdGhlIGJsb2NrIGxpc3QgcmVjb3JkLCB0aGVuIGFydGlmYWN0cyBkZXNjcmlwdGlvbiBm
aWxlZCB3aWxsIGJlIHVwZGF0ZWQgd2l0aCBhZGRpdGlvbmFsIGluZm9ybWF0aW9uLiIsICJjcmVh
dG9yX2lkIjogIm5rYW5kaGExQGluLmlibS5jb20iLCAibGFzdF9tb2RpZmllZF9ieSI6ICJua2Fu
ZGhhMUBpbi5pYm0uY29tIiwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NTczMzQwMzAxNzYsICJl
eHBvcnRfa2V5IjogImV4YW1wbGVfc3BhbWhhdXNfc3VibWl0X2RvbWFpbl9uYW1lIiwgInV1aWQi
OiAiZThlNmE0ZTktYWFmZS00ZmY0LWIzNWYtNTAyOGI2NjI2YjM1IiwgImNvbnRlbnQiOiB7Indv
cmtmbG93X2lkIjogImV4YW1wbGVfc3BhbWhhdXNfc3VibWl0X2RvbWFpbl9uYW1lIiwgInhtbCI6
ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMg
eG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1s
bnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHht
bG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxu
czpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6
cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJo
dHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cu
dzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDov
L3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFtcGxlX3NwYW1oYXVzX3N1
Ym1pdF9kb21haW5fbmFtZVwiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBsZTog
U3BhbUhhdXM6IFN1Ym1pdCBEb21haW4gTmFtZVwiPjxkb2N1bWVudGF0aW9uPkNoZWNrIERvbWFp
biBOYW1lIGFnYWluc3QgU3BhbWhhdXMgRGF0YWJhc2UgdG8gc2VlIHdoZXRoZXIgRG9tYWluIE5h
bWUgaXMgaW4gYmxvY2sgbGlzdCByZWNvcmRzIG9yIG5vdC5pZiBnaXZlbiBhcnRpZmFjdCBhcHBl
YXJzIGluIG9uZSBvZiB0aGUgYmxvY2sgbGlzdCByZWNvcmQsIHRoZW4gYXJ0aWZhY3RzIGRlc2Ny
aXB0aW9uIGZpbGVkIHdpbGwgYmUgdXBkYXRlZCB3aXRoIGFkZGl0aW9uYWwgaW5mb3JtYXRpb24u
PC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91
dGdvaW5nPlNlcXVlbmNlRmxvd18xeDhwZW0zPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZp
Y2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMWtoZnVkcVwiIG5hbWU9XCJTcGFtaGF1cyBRdWVyeSBT
dWJtaXQgQXJ0aWZhY3RcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVs
ZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cImFjYjJhMDdjLTgxNWMtNDU0MC04MDZh
LWUxMTAwMmI4YTJjNlwiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwi
OlwicmVzdWx0c19kYXRhID0gcmVzdWx0cy5nZXQoJ2NvbnRlbnQnKVxcbnRtcF90ZXh0ID0gXFxc
IlxcXCJcXG50bXBfZGVzYyA9IGFydGlmYWN0LmRlc2NyaXB0aW9uXFxuaWYgcmVzdWx0c19kYXRh
LmdldCgnaXNfaW5fYmxvY2tsaXN0Jyk6XFxuICAgICB0bXBfdGV4dCA9IFxcXCImbHQ7YnImZ3Q7
Jmx0O2JyJmd0OyZsdDtiJmd0O1RoaXMgYXJ0aWZhY3QgY2hlY2tlZCBhZ2FpbnN0IFNwYW1oYXVz
IGFuZCBpdCBpcyBpbiBibG9jayBsaXN0LiZsdDsvYiZndDtcXFwiXFxuICAgICByZXNwX2xpc3Qg
PSByZXN1bHRzX2RhdGEuZ2V0KCdyZXNwJylcXG4gICAgIGZvciBjb2RlIGluIHJlc3BfbGlzdDpc
XG4gICAgICAgICAgY29kZSA9IHN0cihjb2RlKVxcbiAgICAgICAgICB0bXBfdGV4dCArPSBcXFwi
Jmx0O2JyJmd0OyZsdDtiJmd0O2NvZGUgOiZsdDsvYiZndDsge30mbHQ7L2JyJmd0O1xcXCIuZm9y
bWF0KGNvZGUpXFxuICAgICAgICAgIHRtcF90ZXh0ICs9IFxcXCImbHQ7YnImZ3Q7Jmx0O2ImZ3Q7
ZGF0YXNldCA6Jmx0Oy9iJmd0OyB7fSZsdDsvYnImZ3Q7XFxcIi5mb3JtYXQocmVzdWx0c19kYXRh
LmdldChjb2RlKS5nZXQoJ2RhdGFzZXQnKSlcXG4gICAgICAgICAgdG1wX3RleHQgKz0gXFxcIiZs
dDticiZndDsmbHQ7YiZndDtleHBsYW5hdGlvbiA6Jmx0Oy9iJmd0OyB7fSZsdDsvYnImZ3Q7XFxc
Ii5mb3JtYXQocmVzdWx0c19kYXRhLmdldChjb2RlKS5nZXQoJ2V4cGxhbmF0aW9uJykpXFxuICAg
ICAgICAgIHRtcF90ZXh0ICs9IFxcXCImbHQ7YnImZ3Q7Jmx0O2ImZ3Q7VVJMIDombHQ7L2ImZ3Q7
ICZsdDsvYnImZ3Q7e30mbHQ7L2JyJmd0O1xcXCIuZm9ybWF0KHJlc3VsdHNfZGF0YS5nZXQoY29k
ZSkuZ2V0KCdVUkwnKSlcXG5lbHNlOlxcbiAgICAgdG1wX3RleHQgPSBcXFwiJmx0O2JyJmd0OyZs
dDticiZndDsmbHQ7YiZndDtUaGlzIGFydGlmYWN0IGNoZWNrZWQgYWdhaW5zdCBTcGFtaGF1cyBh
bmQgaXQgaXMgbm90IGluIGJsb2NrIGxpc3QuJmx0Oy9iJmd0OyZsdDsvYnImZ3Q7Jmx0Oy9iciZn
dDtcXFwiXFxuaWYgdG1wX2Rlc2M6XFxuICAgICB0bXBfZGVzYyA9IHRtcF9kZXNjLmdldCgnY29u
dGVudCcpXFxuZWxzZTpcXG4gICAgIHRtcF9kZXNjID0gXFxcIlxcXCIgXFxuY29tcGxldGVfdG1w
X3RleHQgPSB0bXBfZGVzYyt0bXBfdGV4dFxcbnJpY2hfdGV4dCA9IGhlbHBlci5jcmVhdGVSaWNo
VGV4dChjb21wbGV0ZV90bXBfdGV4dClcXG5hcnRpZmFjdC5kZXNjcmlwdGlvbiA9IHJpY2hfdGV4
dFwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJpbnB1dHMuc3BhbWhhdXNfcXVlcnlfc3Ry
aW5nID0gYXJ0aWZhY3QudmFsdWVcXG5pbnB1dHMuc3BhbWhhdXNlX3NlYXJjaF9yZXNvdXJjZSA9
IHJ1bGUucHJvcGVydGllcy5zcGFtaGF1c19kb21haW5fbmFtZV9yZXNvdXJjZVwifTwvcmVzaWxp
ZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18x
eDhwZW0zPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzEzbDc1ZjU8L291dGdvaW5n
Pjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xeDhwZW0zXCIg
c291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tf
MWtoZnVkcVwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8xNGpkZjM2XCI+PGluY29taW5nPlNl
cXVlbmNlRmxvd18xM2w3NWY1PC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9
XCJTZXF1ZW5jZUZsb3dfMTNsNzVmNVwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzFraGZ1ZHFc
IiB0YXJnZXRSZWY9XCJFbmRFdmVudF8xNGpkZjM2XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRl
eHRBbm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3Rl
eHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4
XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90
YXRpb25fMWt4eGl5dFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xYzNi
M3BvXCI+PHRleHQ+PCFbQ0RBVEFbQSB3b3JrZmxvdyB0byBjaGVjayBEb21haW4gbmFtZXMgYWdh
aW5zdCBTcGFtaGF1cyBkYXRhYmFzZSB0byBzZWUgd2hldGhlciBkb21haW4gaXMgaW4gU3BhbWhh
dXMgYmxvY2sgbGlzdCBvciBub3QuXG5dXT48L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2Np
YXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8wZHJhcnltXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tf
MWtoZnVkcVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFjM2IzcG9cIi8+PC9wcm9jZXNz
PjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxh
bmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpC
UE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZl
bnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIg
eD1cIjE2MlwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWln
aHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5M
YWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJU
ZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+
PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1
NFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFz
c29jaWF0aW9uXzFzZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6
d2F5cG9pbnQgeD1cIjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxv
bWdkaTp3YXlwb2ludCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRc
Ii8+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2
aWNlVGFza18xa2hmdWRxXCIgaWQ9XCJTZXJ2aWNlVGFza18xa2hmdWRxX2RpXCI+PG9tZ2RjOkJv
dW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwiMTAwXCIgeD1cIjQyNVwiIHk9XCIxNjZcIi8+PC9i
cG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZs
b3dfMXg4cGVtM1wiIGlkPVwiU2VxdWVuY2VGbG93XzF4OHBlbTNfZGlcIj48b21nZGk6d2F5cG9p
bnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3
YXlwb2ludCB4PVwiNDI1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJw
bW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9
XCIzMTEuNVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdl
PjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMTRqZGYzNlwiIGlkPVwi
RW5kRXZlbnRfMTRqZGYzNl9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1c
IjM2XCIgeD1cIjc2OVwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5k
cyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI3ODdcIiB5PVwiMjI3XCIvPjwvYnBtbmRp
OkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVu
dD1cIlNlcXVlbmNlRmxvd18xM2w3NWY1XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMTNsNzVmNV9kaVwi
PjxvbWdkaTp3YXlwb2ludCB4PVwiNTI1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIy
MDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI3NjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIg
eT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIg
d2lkdGg9XCIwXCIgeD1cIjY0N1wiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBt
bmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRp
b25fMWMzYjNwb1wiIGlkPVwiVGV4dEFubm90YXRpb25fMWMzYjNwb19kaVwiPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiNTNcIiB3aWR0aD1cIjQ2NlwiIHg9XCI0OTZcIiB5PVwiNjJcIi8+PC9icG1u
ZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8w
ZHJhcnltXCIgaWQ9XCJBc3NvY2lhdGlvbl8wZHJhcnltX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9
XCI1MjVcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjE4M1wiLz48b21nZGk6d2F5cG9p
bnQgeD1cIjY3M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTE1XCIvPjwvYnBtbmRp
OkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1ORGlhZ3JhbT48L2RlZmlu
aXRpb25zPiIsICJ2ZXJzaW9uIjogMzB9LCAiYWN0aW9ucyI6IFtdfV0sICJyb2xlcyI6IFtdLCAi
d29ya3NwYWNlcyI6IFtdLCAiZnVuY3Rpb25zIjogW3siaWQiOiA1MSwgIm5hbWUiOiAiZm5fc3Bh
bWhhdXNfcXVlcnlfc3VibWl0X2FydGlmYWN0IiwgImRpc3BsYXlfbmFtZSI6ICJTcGFtaGF1cyBR
dWVyeSBTdWJtaXQgQXJ0aWZhY3QiLCAiZGVzY3JpcHRpb24iOiB7ImZvcm1hdCI6ICJ0ZXh0Iiwg
ImNvbnRlbnQiOiAiRnVuY3Rpb24gdG8gY2hlY2sgSVAgQWRkcmVzcyAmIERvbWFpbiBOYW1lcyBh
Z2FpbnN0IFNwYW1oYXVzIERhdGFiYXNlIHRvIHNlZSB3aGV0aGVyIElQIEFkZHJlc3Mgb3IgRG9t
YWluIE5hbWVzIGFwcGVhcnMgaW4gU3BhbWhhdXMgYmxvY2sgbGlzdCByZWNvcmRzIG9yIG5vdC4i
fSwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJmbl9zcGFtaGF1c19xdWVyeSIsICJleHBvcnRfa2V5
IjogImZuX3NwYW1oYXVzX3F1ZXJ5X3N1Ym1pdF9hcnRpZmFjdCIsICJ1dWlkIjogImFjYjJhMDdj
LTgxNWMtNDU0MC04MDZhLWUxMTAwMmI4YTJjNiIsICJ2ZXJzaW9uIjogMywgImNyZWF0b3IiOiB7
ImlkIjogNiwgInR5cGUiOiAidXNlciIsICJuYW1lIjogIm5rYW5kaGExQGluLmlibS5jb20iLCAi
ZGlzcGxheV9uYW1lIjogIk5pdGluIEthbmRoYXJlICJ9LCAibGFzdF9tb2RpZmllZF9ieSI6IHsi
aWQiOiA2LCAidHlwZSI6ICJ1c2VyIiwgIm5hbWUiOiAibmthbmRoYTFAaW4uaWJtLmNvbSIsICJk
aXNwbGF5X25hbWUiOiAiTml0aW4gS2FuZGhhcmUgIn0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAx
NTU2NjE5NDE1MTUzLCAidmlld19pdGVtcyI6IFt7InN0ZXBfbGFiZWwiOiBudWxsLCAic2hvd19p
ZiI6IG51bGwsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0
aW9uIiwgImNvbnRlbnQiOiAiMTJhMTFiNjQtMTZiMy00NTA5LTkzMzItNTk5MDk2Yjk5ZDk5Iiwg
InNob3dfbGlua19oZWFkZXIiOiBmYWxzZX0sIHsic3RlcF9sYWJlbCI6IG51bGwsICJzaG93X2lm
IjogbnVsbCwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rp
b24iLCAiY29udGVudCI6ICI2ODFlNGQzNi1mOWQzLTQ2YjMtOGU1ZS0yNmY5OTcwODFjMDkiLCAi
c2hvd19saW5rX2hlYWRlciI6IGZhbHNlfV0sICJ3b3JrZmxvd3MiOiBbeyJ3b3JrZmxvd19pZCI6
IDkzLCAibmFtZSI6ICJFeGFtcGxlOiBTcGFtSGF1czogU3VibWl0IERvbWFpbiBOYW1lIiwgInBy
b2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfc3BhbWhhdXNfc3VibWl0X2RvbWFpbl9uYW1lIiwg
Im9iamVjdF90eXBlIjogImFydGlmYWN0IiwgImRlc2NyaXB0aW9uIjogbnVsbCwgInV1aWQiOiBu
dWxsLCAiYWN0aW9ucyI6IFtdfSwgeyJ3b3JrZmxvd19pZCI6IDkyLCAibmFtZSI6ICJFeGFtcGxl
OiBTcGFtSGF1czogU3VibWl0IElQIEFkZHJlc3MiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhh
bXBsZV9zcGFtaGF1c19zdWJtaXRfaXBfYWRkcmVzcyIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFj
dCIsICJkZXNjcmlwdGlvbiI6IG51bGwsICJ1dWlkIjogbnVsbCwgImFjdGlvbnMiOiBbXX1dfV19
"""
    )