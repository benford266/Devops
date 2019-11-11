from scapy.all import *

iftocap = 'en0'


def capturecdp(interface):
    list_contrib('cdp')
    cdppacket = sniff(iface=interface, count=1, filter="ether dst 01:00:0c:cc:cc:cc")
    device = cdppacket[0]['CDPMsgDeviceID'].val.decode()
    port = cdppacket[0]['CDPMsgPortID']
    list = [device, port]
    return list


capturecdp(iftocap)
