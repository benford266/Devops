from scapy.all import *
from threading import Thread
from time import sleep

class Sniffer(Thread):
    def __init__(self, interface='Local Area Connection'):
        super().__init__()
        self.interface = interface

    def run(self):
        load_contrib('lldp')
        sniff(iface=self.interface,count=1,  filter='lldp',prn=self.print_packet)

    def print_packet(self, packet):
        load_contrib('lldp')
        ip_layer = packet[]
        print(ip_layer)

sniffer = Sniffer()

print("[*] Start Sniffing...")
sniffer.start()

try:
    while True:
        sleep(100)
except KeyboardInterrupt:
    print("[*] Stop Sniffing")
    sniffer.join()