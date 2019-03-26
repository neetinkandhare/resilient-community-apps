# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_grpc_interface"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_grpc_interface package"""
    reload_params = {"package": u"fn_grpc_interface",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"grpc_channel", u"grpc_function", u"grpc_function_data"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_grpc"], 
                    "functions": [u"function_grpc"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_grpc_communication_interface"], 
                    "actions": [u"Example: GRPC Communication Interface"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     grpc_channel
    #     grpc_function
    #     grpc_function_data
    #   Message Destinations:
    #     fn_grpc
    #   Functions:
    #     function_grpc
    #   Workflows:
    #     example_grpc_communication_interface
    #   Rules:
    #     Example: GRPC Communication Interface


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogImI3NjVlMzEyLTU1NGYt
NDNlOC05ZDZiLTM3ZTQ4ZDA0NDc2NSIsICJkZXNjcmlwdGlvbiI6ICJDb21tdW5pY2F0ZSB3aXRo
IEdSUEMgU2VydmVycyIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJleHBvcnRfa2V5Ijog
ImV4YW1wbGVfZ3JwY19jb21tdW5pY2F0aW9uX2ludGVyZmFjZSIsICJ3b3JrZmxvd19pZCI6IDQ0
LCAibGFzdF9tb2RpZmllZF9ieSI6ICJua2FuZGhhMUBpbi5pYm0uY29tIiwgImNvbnRlbnQiOiB7
InhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5p
dGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVM
XCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9E
SVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENc
IiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIg
eG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4
c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6
Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwi
aHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFtcGxlX2dycGNf
Y29tbXVuaWNhdGlvbl9pbnRlcmZhY2VcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4
YW1wbGU6IEdSUEMgQ29tbXVuaWNhdGlvbiBJbnRlcmZhY2VcIj48ZG9jdW1lbnRhdGlvbj5Db21t
dW5pY2F0ZSB3aXRoIEdSUEMgU2VydmVyczwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1c
IlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMTRrc2tmbTwvb3V0
Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzFuZmNmdGZc
IiBuYW1lPVwiR1JQQ1wiIHJlc2lsaWVudDp0eXBlPVwiZnVuY3Rpb25cIj48ZXh0ZW5zaW9uRWxl
bWVudHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlkPVwiMGY5Njk2MDgtZjIyZi00YTZiLWE3NDMt
YWYwMWEyMWQ2OTNjXCI+e1wiaW5wdXRzXCI6e1wiMzNiZjdjNDEtMWY0NS00ZDJjLWI5MTUtOTEx
NDUzZGIxZDVlXCI6e1wiaW5wdXRfdHlwZVwiOlwic3RhdGljXCIsXCJzdGF0aWNfaW5wdXRcIjp7
XCJtdWx0aXNlbGVjdF92YWx1ZVwiOltdLFwidGV4dF92YWx1ZVwiOlwibG9jYWxob3N0OjUwMDUy
XCJ9fSxcImQwOTg3OGRjLWQxMWYtNGUyZS1iMTEyLWQ1M2U1ODgyZTI1ZlwiOntcImlucHV0X3R5
cGVcIjpcInN0YXRpY1wiLFwic3RhdGljX2lucHV0XCI6e1wibXVsdGlzZWxlY3RfdmFsdWVcIjpb
XSxcInRleHRfdmFsdWVcIjpcImhlbGxvd29yZF9zc2w6U2F5SGVsbG9UaHJlZShIZWxsb1JlcXVl
c3QpXCJ9fX0sXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJkYXRhX3JlY2VpdmVkID0gcmVz
dWx0c1snY29udGVudCddXFxuc2VydmVyX2FkZHJlc3MgPSByZXN1bHRzWydjaGFubmVsJ11cXG5y
aWNoX3RleHQgPSBoZWxwZXIuY3JlYXRlUmljaFRleHQoXFxcIiZsdDtwJmd0OyZsdDtiJmd0O2No
YW5uZWwgOiAmbHQ7L2ImZ3Q7e30mbHQ7L3AmZ3Q7Jmx0O3AmZ3Q7Jmx0O2ImZ3Q7e30mbHQ7L2Im
Z3Q7Jmx0Oy9wJmd0O1xcXCIuZm9ybWF0KHNlcnZlcl9hZGRyZXNzLGRhdGFfcmVjZWl2ZWQpKVxc
bmluY2lkZW50LmFkZE5vdGUocmljaF90ZXh0KVwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6
XCJkZWYgZGljdF90b19qc29uX3N0cihkKTpcXG4gIFxcXCJcXFwiXFxcIkZ1bmN0aW9uIHRoYXQg
Y29udmVydHMgYSBkaWN0aW9uYXJ5IGludG8gYSBKU09OIHN0cmluZy5cXG4gICAgIFN1cHBvcnRz
IHR5cGVzOiBiYXNlc3RyaW5nLCB1bmljb2RlLCBib29sLCBpbnQgYW5kIG5lc3RlZCBkaWN0cy5c
XG4gICAgIERvZXMgbm90IHN1cHBvcnQgbGlzdHMuXFxuICAgICBJZiB0aGUgdmFsdWUgaXMgTm9u
ZSwgaXQgc2V0cyBpdCB0byBGYWxzZS5cXFwiXFxcIlxcXCJcXG5cXG4gIGpzb25fZW50cnkgPSB1
J1xcXCJ7MH1cXFwiOnsxfSdcXG4gIGpzb25fZW50cnlfc3RyID0gdSdcXFwiezB9XFxcIjpcXFwi
ezF9XFxcIidcXG4gIGVudHJpZXMgPSBbXVxcblxcbiAgZm9yIGVudHJ5IGluIGQ6XFxuICAgIGtl
eSA9IGVudHJ5XFxuICAgIHZhbHVlID0gZFtlbnRyeV1cXG5cXG4gICAgaWYgdmFsdWUgaXMgTm9u
ZTpcXG4gICAgICB2YWx1ZSA9IEZhbHNlXFxuXFxuICAgIGlmIGlzaW5zdGFuY2UodmFsdWUsIGxp
c3QpOlxcbiAgICAgIGhlbHBlci5mYWlsKCdkaWN0X3RvX2pzb25fc3RyIGRvZXMgbm90IHN1cHBv
cnQgUHl0aG9uIExpc3RzJylcXG5cXG4gICAgaWYgaXNpbnN0YW5jZSh2YWx1ZSwgYmFzZXN0cmlu
Zyk6XFxuICAgICAgdmFsdWUgPSB2YWx1ZS5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwi
JylcXG4gICAgICBlbnRyaWVzLmFwcGVuZChqc29uX2VudHJ5X3N0ci5mb3JtYXQodW5pY29kZShr
ZXkpLCB1bmljb2RlKHZhbHVlKSkpXFxuXFxuICAgIGVsaWYgaXNpbnN0YW5jZSh2YWx1ZSwgdW5p
Y29kZSk6XFxuICAgICAgZW50cmllcy5hcHBlbmQoanNvbl9lbnRyeS5mb3JtYXQodW5pY29kZShr
ZXkpLCB1bmljb2RlKHZhbHVlKSkpXFxuICAgIFxcbiAgICBlbGlmIGlzaW5zdGFuY2UodmFsdWUs
IGJvb2wpOlxcbiAgICAgIHZhbHVlID0gJ3RydWUnIGlmIHZhbHVlID09IFRydWUgZWxzZSAnZmFs
c2UnXFxuICAgICAgZW50cmllcy5hcHBlbmQoanNvbl9lbnRyeS5mb3JtYXQoa2V5LCB2YWx1ZSkp
XFxuXFxuICAgIGVsaWYgaXNpbnN0YW5jZSh2YWx1ZSwgaW50KTpcXG4gICAgICBlbnRyaWVzLmFw
cGVuZChqc29uX2VudHJ5LmZvcm1hdCh1bmljb2RlKGtleSksIHZhbHVlKSlcXG5cXG4gICAgZWxp
ZiBpc2luc3RhbmNlKHZhbHVlLCBkaWN0KTpcXG4gICAgICBlbnRyaWVzLmFwcGVuZChqc29uX2Vu
dHJ5LmZvcm1hdChrZXksIGRpY3RfdG9fanNvbl9zdHIodmFsdWUpKSlcXG5cXG4gICAgZWxzZTpc
XG4gICAgICBoZWxwZXIuZmFpbCgnZGljdF90b19qc29uX3N0ciBkb2VzIG5vdCBzdXBwb3J0IHRo
aXMgdHlwZTogezB9Jy5mb3JtYXQodHlwZSh2YWx1ZSkpKVxcblxcbiAgcmV0dXJuIHUnezB9IHsx
fSB7Mn0nLmZvcm1hdCh1J3snLCAnLCcuam9pbihlbnRyaWVzKSwgdSd9JylcXG5pbnB1dHMuZ3Jw
Y19mdW5jdGlvbl9kYXRhID0gZGljdF90b19qc29uX3N0cih7XFxcIm5hbWVcXFwiOiBcXFwiaGVs
bG8gRnJvbSBOaXRpblxcXCJ9KVxcblxcblwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5z
aW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18xNGtza2ZtPC9pbmNvbWluZz48b3V0
Z29pbmc+U2VxdWVuY2VGbG93XzB0dXY2dHo8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVl
bmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xNGtza2ZtXCIgc291cmNlUmVmPVwiU3RhcnRFdmVu
dF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMW5mY2Z0ZlwiLz48ZW5kRXZlbnQg
aWQ9XCJFbmRFdmVudF8xdWtodnhwXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18wdHV2NnR6PC9p
bmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMHR1djZ0
elwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzFuZmNmdGZcIiB0YXJnZXRSZWY9XCJFbmRFdmVu
dF8xdWtodnhwXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRc
Ij48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48
YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3RhcnRF
dmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48dGV4
dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8wNm1tZWU2XCI+PHRleHQ+PCFbQ0RBVEFb
XG5UaGlzIEZ1bmN0aW9uIHByb3ZpZGVzIGEgZ2VuZXJhbCBwdXJwb3NlIHdyYXBwZXIgZm9yIHVz
ZSBhbnkgZ1JQQyAoZ29vZ2xlIFJlbW90ZSBQcm9jcmVkdXJlIENhbGwpIENsaWVudCBBcHBsaWNh
dGlvbi5cbl1dPjwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29j
aWF0aW9uXzA1eGNkNmFcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xbmZjZnRmXCIgdGFyZ2V0
UmVmPVwiVGV4dEFubm90YXRpb25fMDZtbWVlNlwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlh
Z3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1c
InVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxl
bWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+
PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTMxXCIgeT1cIjE4
OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1c
IjkwXCIgeD1cIjEyNlwiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQ
TU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFr
eHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQ
TU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0
OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTQ1
XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjNcIi8+PG9tZ2RpOndheXBvaW50IHg9
XCIxNDZcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1O
RWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzFuZmNmdGZc
IiBpZD1cIlNlcnZpY2VUYXNrXzFuZmNmdGZfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgw
XCIgd2lkdGg9XCIxMDBcIiB4PVwiMzM4LjMxODg2OTgyODQ1NjFcIiB5PVwiMTY2XCIvPjwvYnBt
bmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93
XzE0a3NrZm1cIiBpZD1cIlNlcXVlbmNlRmxvd18xNGtza2ZtX2RpXCI+PG9tZ2RpOndheXBvaW50
IHg9XCIxNjdcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5
cG9pbnQgeD1cIjMzOFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1u
ZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTJcIiB3aWR0aD1cIjkwXCIgeD1c
IjIwNy41XCIgeT1cIjE4NVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+
PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8xdWtodnhwXCIgaWQ9XCJF
bmRFdmVudF8xdWtodnhwX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwi
MzZcIiB4PVwiNTc1LjMxODg2OTgyODQ1NjFcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVs
PjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTJcIiB3aWR0aD1cIjBcIiB4PVwiNTkzLjMxODg2OTgy
ODQ1NjFcIiB5PVwiMjI4XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+
PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wdHV2NnR6XCIgaWQ9
XCJTZXF1ZW5jZUZsb3dfMHR1djZ0el9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNDM4XCIgeHNp
OnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI1NzVc
IiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48
b21nZGM6Qm91bmRzIGhlaWdodD1cIjEyXCIgd2lkdGg9XCIwXCIgeD1cIjUwNi41XCIgeT1cIjE4
NVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hh
cGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wNm1tZWU2XCIgaWQ9XCJUZXh0QW5ub3Rh
dGlvbl8wNm1tZWU2X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI5NVwiIHdpZHRoPVwiNTc0
XCIgeD1cIjUwMVwiIHk9XCI0M1wiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRn
ZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzA1eGNkNmFcIiBpZD1cIkFzc29jaWF0aW9uXzA1
eGNkNmFfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQzOFwiIHhzaTp0eXBlPVwib21nZGM6UG9p
bnRcIiB5PVwiMTkyXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNjI3XCIgeHNpOnR5cGU9XCJvbWdk
YzpQb2ludFwiIHk9XCIxMzhcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5l
PjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgIndvcmtmbG93X2lkIjogImV4
YW1wbGVfZ3JwY19jb21tdW5pY2F0aW9uX2ludGVyZmFjZSIsICJ2ZXJzaW9uIjogNTB9LCAibGFz
dF9tb2RpZmllZF90aW1lIjogMTU1MzYxOTQ2MDM2OSwgImNyZWF0b3JfaWQiOiAibmthbmRoYTFA
aW4uaWJtLmNvbSIsICJhY3Rpb25zIjogW10sICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxl
X2dycGNfY29tbXVuaWNhdGlvbl9pbnRlcmZhY2UiLCAibmFtZSI6ICJFeGFtcGxlOiBHUlBDIENv
bW11bmljYXRpb24gSW50ZXJmYWNlIn1dLCAiYWN0aW9ucyI6IFt7ImxvZ2ljX3R5cGUiOiAiYWxs
IiwgIm5hbWUiOiAiRXhhbXBsZTogR1JQQyBDb21tdW5pY2F0aW9uIEludGVyZmFjZSIsICJ2aWV3
X2l0ZW1zIjogW10sICJ0eXBlIjogMSwgIndvcmtmbG93cyI6IFsiZXhhbXBsZV9ncnBjX2NvbW11
bmljYXRpb25faW50ZXJmYWNlIl0sICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJ0aW1lb3V0
X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAiZmI1OTM3MmQtMTcwMC00ZDNiLWIwMTktMGM2NTRm
MGYxN2RiIiwgImF1dG9tYXRpb25zIjogW10sICJleHBvcnRfa2V5IjogIkV4YW1wbGU6IEdSUEMg
Q29tbXVuaWNhdGlvbiBJbnRlcmZhY2UiLCAiY29uZGl0aW9ucyI6IFtdLCAiaWQiOiA1OSwgIm1l
c3NhZ2VfZGVzdGluYXRpb25zIjogW119XSwgImxheW91dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRf
dmVyc2lvbiI6IDIsICJpZCI6IDg3LCAiaW5kdXN0cmllcyI6IG51bGwsICJwaGFzZXMiOiBbXSwg
ImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGwsICJsb2NhbGUiOiBudWxsLCAic2VydmVy
X3ZlcnNpb24iOiB7Im1ham9yIjogMzEsICJ2ZXJzaW9uIjogIjMxLjEuNzYiLCAiYnVpbGRfbnVt
YmVyIjogNzYsICJtaW5vciI6IDF9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3b3Jrc3BhY2VzIjog
W10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImZ1bmN0aW9ucyI6IFt7ImRpc3BsYXlfbmFtZSI6
ICJHUlBDIiwgImRlc2NyaXB0aW9uIjogeyJjb250ZW50IjogIkEgZnVuY3Rpb24gdG8gY29tbXVu
aWNhdGUgd2l0aCBHUlBDIFNlcnZlcnMgYmFzZWQgb24gdGhlIENvbW11bmljYXRpb24gTWV0aG9k
cyBTcGVjaWZpZWQuIiwgImZvcm1hdCI6ICJ0ZXh0In0sICJjcmVhdG9yIjogeyJkaXNwbGF5X25h
bWUiOiAiTml0aW4gS2FuZGhhcmUgIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDYsICJuYW1lIjog
Im5rYW5kaGExQGluLmlibS5jb20ifSwgInZpZXdfaXRlbXMiOiBbeyJzaG93X2lmIjogbnVsbCwg
ImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJl
bGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICIzM2JmN2M0MS0xZjQ1LTRkMmMtYjkx
NS05MTE0NTNkYjFkNWUiLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAi
ZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVs
ZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250ZW50IjogImQwOTg3OGRjLWQxMWYtNGUyZS1iMTEy
LWQ1M2U1ODgyZTI1ZiIsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJm
aWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxl
bWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiOWRkZGRmNjItNjBmNy00NTBhLWE5YWMt
MmZkYjg1ZTNjNGEzIiwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJleHBvcnRfa2V5IjogImZ1bmN0
aW9uX2dycGMiLCAidXVpZCI6ICIwZjk2OTYwOC1mMjJmLTRhNmItYTc0My1hZjAxYTIxZDY5M2Mi
LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIk5pdGluIEthbmRoYXJlICIs
ICJ0eXBlIjogInVzZXIiLCAiaWQiOiA2LCAibmFtZSI6ICJua2FuZGhhMUBpbi5pYm0uY29tIn0s
ICJ2ZXJzaW9uIjogNSwgIndvcmtmbG93cyI6IFt7ImRlc2NyaXB0aW9uIjogbnVsbCwgIm9iamVj
dF90eXBlIjogImFydGlmYWN0IiwgImFjdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBsZTogR1JQ
QyBDb21tdW5pY2F0aW9uIEludGVyZmFjZSIsICJ3b3JrZmxvd19pZCI6IDQ0LCAicHJvZ3JhbW1h
dGljX25hbWUiOiAiZXhhbXBsZV9ncnBjX2NvbW11bmljYXRpb25faW50ZXJmYWNlIiwgInV1aWQi
OiBudWxsfV0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTUzMjUwOTEzNzcwLCAiZGVzdGluYXRp
b25faGFuZGxlIjogImZuX2dycGMiLCAiaWQiOiAzOCwgIm5hbWUiOiAiZnVuY3Rpb25fZ3JwYyJ9
XSwgIm5vdGlmaWNhdGlvbnMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJpbmNpZGVudF90
eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTU1MzYyMDI5MzczNywgImRlc2NyaXB0aW9uIjogIkN1
c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6
YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjogIkN1c3RvbWl6YXRp
b24gUGFja2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1NTM2MjAyOTM3MzcsICJ1
dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJlbmFibGVkIjog
ZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxz
ZX1dLCAic2NyaXB0cyI6IFtdLCAidHlwZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjog
W3sidXVpZCI6ICJiMDg3ZjMzYS0yMWM3LTRhOWMtYjYwNS0wMmM3MTk5NzYzOTIiLCAiZXhwb3J0
X2tleSI6ICJmbl9ncnBjIiwgIm5hbWUiOiAiZm5fZ3JwYyIsICJkZXN0aW5hdGlvbl90eXBlIjog
MCwgInByb2dyYW1tYXRpY19uYW1lIjogImZuX2dycGMiLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1
c2VycyI6IFsibmthbmRoYTFAaW4uaWJtLmNvbSJdfV0sICJpbmNpZGVudF9hcnRpZmFjdF90eXBl
cyI6IFtdLCAicm9sZXMiOiBbXSwgImZpZWxkcyI6IFt7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVf
aWQiOiAwLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAiYmxh
bmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJp
ZCI6IDUxLCAicmVhZF9vbmx5IjogdHJ1ZSwgInV1aWQiOiAiYzNmMGUzZWQtMjFlMS00ZDUzLWFm
ZmItZmU1Y2EzMzA4Y2NhIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJib29sZWFu
IiwgInRvb2x0aXAiOiAiV2hldGhlciB0aGUgaW5jaWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEg
cmVndWxhciBpbmNpZGVudC4gIFRoaXMgZmllbGQgaXMgcmVhZC1vbmx5LiIsICJpbnRlcm5hbCI6
IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXki
OiAiaW5jaWRlbnQvaW5jX3RyYWluaW5nIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJu
YW1lIjogImluY190cmFpbmluZyIsICJkZXByZWNhdGVkIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nl
bl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0
eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAiZ3JwY19jaGFubmVs
IiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0
cnVlLCAiaWQiOiAxNDEsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiMzNiZjdjNDEtMWY0
NS00ZDJjLWI5MTUtOTExNDUzZGIxZDVlIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6
ICJ0ZXh0IiwgInRvb2x0aXAiOiAidGhpcyBmaWVsZCBjb250YWluIHRoZSBjaGFubmVsIGluZm8g
b2YgdGhlIEdSUEMgU2VydmVyIFJ1bm5pbmcgZXg6aG9zdElQOlBvcnQiLCAiaW50ZXJuYWwiOiBm
YWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5Ijog
Il9fZnVuY3Rpb24vZ3JwY19jaGFubmVsIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJw
bGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJncnBjX2NoYW5uZWwiLCAiZGVwcmVjYXRlZCI6IGZh
bHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJyZXF1aXJlZCI6ICJhbHdh
eXMiLCAidmFsdWVzIjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9w
ZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJncnBjX2Z1bmN0aW9uX2RhdGEiLCAiYmxhbmtf
b3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6
IDE0OCwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICI5ZGRkZGY2Mi02MGY3LTQ1MGEtYTlh
Yy0yZmRiODVlM2M0YTMiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogInRleHQiLCAi
dG9vbHRpcCI6ICJBZGRpdGlvbmFsIGRhdGEgRmllbGRzIHRvIHNlbmQgZGF0YSBmcm9tIGNsaWVu
dCB0byBzZXJ2ZXIuIGRhdGEgZm9ybWF0IHdpbGwgYmUgaW4ganNvbiBhbmQga2V5IHNob3VsZCBt
YXRjaCB0aGUgcmVxdWVzdCBmdW5jdGlvbiBwYXJhbWV0ZXIuIiwgImludGVybmFsIjogZmFsc2Us
ICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1
bmN0aW9uL2dycGNfZnVuY3Rpb25fZGF0YSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAi
cGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiZ3JwY19mdW5jdGlvbl9kYXRhIiwgImRlcHJlY2F0
ZWQiOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjog
W119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJtcyI6
IHt9LCAidGV4dCI6ICJncnBjX2Z1bmN0aW9uIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJl
Zml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxNDcsICJyZWFkX29ubHkiOiBm
YWxzZSwgInV1aWQiOiAiZDA5ODc4ZGMtZDExZi00ZTJlLWIxMTItZDUzZTU4ODJlMjVmIiwgImNo
b3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiVGhpcyBmaWVs
ZHMgY29udGFpbnMgZGF0YSBmcm9tIC5wcm90byBmaWxlIGkuZSBwYWNrYWdlX25hbWUgOiBycGMg
ZnVuY3Rpb24gbmFtZShncnBjIHJlcXVlc3QgZnVuY3Rpb24pIGV4OiBoZWxsb3dvcmQgOiBTYXlI
ZWxsbyhIZWxsb1JlcXVlc3QpIiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxz
ZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2dycGNfZnVuY3Rp
b24iLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1l
IjogImdycGNfZnVuY3Rpb24iLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5f
Ynlfc2VydmVyIjogZmFsc2UsICJyZXF1aXJlZCI6ICJhbHdheXMiLCAidmFsdWVzIjogW119XSwg
Im92ZXJyaWRlcyI6IFtdLCAiZXhwb3J0X2RhdGUiOiAxNTUzNjE5NTkwOTQ0fQ==
"""
    )