from scapy.all import *
from threading import Thread
from time import sleep

class Sniffer(Thread):
    def __init__(self, interface='en0'):
        super().__init__()
        self.interface = interface

    def run(self):
        sniff(iface=self.interface, filter='ip',prn=self.print_packet)

    def print_packet(self, packet):
        ip_layer = packet.getlayer(IP)
        print("{src} --> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))

sniffer = Sniffer()

print("[*] Start Sniffing...")
sniffer.start()

try:
    while True:
        sleep(100)
except KeyboardInterrupt:
    print("[*] Stop Sniffing")
    sniffer.join()