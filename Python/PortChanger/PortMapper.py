import sys
from scapy.all import *
from tkinter import *


#Functions
interfacelist = get_if_list()

# Capture CDP Packet
def capturecdp(interface):
    load_contrib('cdp')
    cdppacket = sniff(iface=interface, count=1, filter="ether dst 01:00:0c:cc:cc:cc")
    device = cdppacket[0]['CDPMsgDeviceID'].val.decode()
    port = cdppacket[0]['CDPMsgPortID'].iface.decode()
    list = [device, port]
    return list

# Start Capture
def capture():
    capturepress = True
    while capturepress:
        port = capturecdp('Local Area Connection')
        time.sleep(1)
        global output
        output.insert(INSERT,port)

#Exit buttom
def exit():
    sys.exit()

# Gui design
window = Tk()
window.title("Port Mapper")
window.geometry('500x500')
window.configure(background='grey')

# Define Objects
lbl = Label(window,text='Port Mapper')
iflbl = Label(window, text="Please select Interface:")
capturebtn = Button(window, text='Start Capture', command=capture)
ifselect = OptionMenu(window, '', *interfacelist)
output = Text(window,width=62, height=25)
exitbtn = Button(window, text='Exit Application', command=exit)


# Grid
lbl.grid(column=0, row=0, columnspan=3)
iflbl.grid(column=0, row=2)
ifselect.grid(column=1, row=2)
capturebtn.grid(column=2, row=2)
output.grid(column=0, row=4, columnspan=3)
exitbtn.grid(column=0, row=5, columnspan=3)

#Start
window.mainloop()
