import sys
from scapy.all import *
from tkinter import *
from threading import Thread

#Randoms
# Loads Tkinter
# Gets interface list
interfacelist = get_if_list()
# Used to set interface


# Packet Capture Class

class Sniffer(Thread):
    def __init__(self, interface='en0'):
        super().__init__()
        self.interface = interface

    def run(self):
        load_contrib('cdp')
        sniff(iface=self.interface, count=1, filter='ip',prn=self.print_packet)


    def print_packet(self, packet):
        ip_layer = packet.getlayer(IP)
        return ("{src} --> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))



# GUI class

class GUI(Thread):
    def __init__(self, master):
        self.master = master
        # Gui design

        master.title("Port Mapper")
        master.geometry('500x500')
        master.configure(background='grey')

        # Define Objects
        self.lbl = Label(master, text='Port Mapper')
        self.iflbl = Label(master, text="Please select Interface:")
        self.capturebtn = Button(master, text='Get Port', command=self.dobits)
        self.ifselect = OptionMenu(master, ' ', *interfacelist)
        self.output = Text(master, width=70, height=25)
        self.exitbtn = Button(master, text='Exit Application', command=master.quit)

        # Grid
        self.lbl.grid(column=0, row=0, columnspan=3)
        self.iflbl.grid(column=0, row=2)
        self.ifselect.grid(column=1, row=2)
        self.capturebtn.grid(column=2, row=2)
        self.output.grid(column=0, row=4, columnspan=3)
        self.exitbtn.grid(column=0, row=5, columnspan=3)

    def test(self):
        start = GUI()
        start.start()

    def dobits(self):
        snifferr = Sniffer()
        output = snifferr.start()
        self.output.insert(INSERT, str(output))








#Start
root = Tk()
my_gui = GUI(root)
root.mainloop()
