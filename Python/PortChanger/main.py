import sys
from scapy.all import *
from tkinter import *

desklist = []

#gets list of available interfaces
interfacelist = get_if_list()

#puts desks entered into list
def desktolist(desksq):
    desklist = []
    for line in desksq.splitlines():    
        desklist.append(line)
    return desklist

#used to capture 1 cdp packet and return device and port
def capturecdp(interface):
    list_contrib('cdp')
    cdppacket = sniff(iface=interface, count=1, filter="ether dst 01:00:0c:cc:cc:cc")
    device = cdppacket[0]['CDPMsgDeviceID'].val.decode()
    port = cdppacket[0]['CDPMsgPortID']
    list = [device, port]
    return list


# actions

#Capture button
def capture():
    deskbox.insert(INSERT,'Capture Started')

#Stop Capture button
def capturestop():
    global deskbox
    dbvalue = deskbox.get('1.0', "end-1c")
    desklistnew = desktolist(dbvalue)
    outputbox.insert(INSERT,desklistnew)

#Exit buttom
def exit():
    sys.exit()







# Gui design
window = Tk()
window.title("Port Changer")
window.geometry('500x500')
window.configure(background='grey')

#Define objects
lbl = Label(window,text='Please Enter Desks Below:')
iflbl = Label(window, text="Please select Interface:")
deskbox = Text(window,width=70, height=10)
capturebtn = Button(window, text='Capture Ports', command=capture)
stopcapturebtn = Button(window, text='Stop Capture', command=capturestop)
outputbox = Text(window, width=70, height=20)
exitbtn = Button(window, text='Exit Application', command=exit)
ifselect = OptionMenu(window, '', *interfacelist)


#Style GUI
lbl.grid(column=0, row=0, columnspan=2)
deskbox.grid(column=0, row=1, columnspan=2)
iflbl.grid(column=0, row=2)
ifselect.grid(column=1, row=2)
ifselect.config(width=30)
capturebtn.grid(column=0, row=3)
stopcapturebtn.grid(column=1, row=3)
outputbox.grid(column=0, row=4, columnspan=2)
exitbtn.grid(column=0, row=5, columnspan=2)


#Run GUI
window.mainloop()
