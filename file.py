from pysnmp.hlapi import *

def get_if_octets(ip, community, if_index):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets', if_index)),
               ObjectType(ObjectIdentity('IF-MIB', 'ifOutOctets', if_index)))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        in_octets = int(varBinds[0].prettyPrint().split("=")[1])
        out_octets = int(varBinds[1].prettyPrint().split("=")[1])
        return in_octets, out_octets

ip = "192.168.1.1"
community = "public"
if_index = "1"
in_octets, out_octets = get_if_octets(ip, community, if_index)
print("In Octets: ", in_octets)
print("Out Octets: ", out_octets)
