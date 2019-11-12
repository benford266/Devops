import sys
from scapy.all import *
from tkinter import *

#Randoms
# Loads Tkinter
window = Tk()
# Gets interface list
interfacelist = get_if_list()
# Used to set interface
ifset = StringVar(window)
ifset.set("Local Area Connection")




#Functions



# Capture CDP Packet
def capturecdp(interface):
    cdppacket = sniff(iface=interface, count=1)
    return cdppacket

# Start Capture
def capture():
    port = capturecdp(ifset.get())
    time.sleep(1)
    global output
    output.insert(INSERT,port)
    output.insert(INSERT, '\n')


#Exit buttom
def exit():
    sys.exit()

# Gui design

window.title("Port Mapper")
window.geometry('500x500')
window.configure(background='grey')

# Define Objects
lbl = Label(window,text='Port Mapper')
iflbl = Label(window, text="Please select Interface:")
capturebtn = Button(window, text='Get Port', command=capture)
ifselect = OptionMenu(window, ifset, *interfacelist)
output = Text(window,width=70, height=25)
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
