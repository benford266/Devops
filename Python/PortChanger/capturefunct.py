from scapy.all import *

iftocap = 'Local Area Connection'


def capturecdp(interface):
    load_contrib('cdp')
    cdppacket = sniff(iface=interface, count=1, filter="ip")
    device = cdppacket[0]['CDPMsgDeviceID'].val.decode()
    port = cdppacket[0]['CDPMsgPortID'].iface.decode()
    list = [device, port]
    return list


capturecdp(iftocap)
