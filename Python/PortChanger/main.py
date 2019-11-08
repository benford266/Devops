import sys
from scapy.all import *
from tkinter import *
desklist = []
interfacelist = get_if_list()
def desktolist(desksq):
    desklist = []
    for line in desksq.splitlines():    
        desklist.append(line)
    return desklist

def capturecdp():
    ip = '0.0.0.0'


# actions
def capture():
    deskbox.insert(INSERT,'Capture Started')


def capturestop():
    global deskbox
    dbvalue = deskbox.get('1.0', END)
    desklist = desktolist(dbvalue)
    outputbox.insert(INSERT,desklist)
    deskbox.insert(INSERT,'Capture Stopped')


def exit():
    sys.exit()


# Gui design
window = Tk()
window.title("Port Changer")
window.geometry('500x500')
window.configure(background='grey')

#Define objects
lbl = Label(window,text='Please Enter Desks Below:')
deskbox = Text(window,width=70, height=10)
capturebtn = Button(window, text='Capture Ports', command=capture)
stopcapturebtn = Button(window, text='Stop Capture', command=capturestop)
outputbox = Text(window, width=70, height=20)
exitbtn = Button(window, text='Exit Application', command=exit)
ifselect = OptionMenu(window, ' ', *interfacelist)

#Style GUI
lbl.grid(column=0, row=0, columnspan=2)
deskbox.grid(column=0, row=1, columnspan=2)
ifselect.grid(column=0, row=2, columnspan=2)
capturebtn.grid(column=0, row=3)
stopcapturebtn.grid(column=1, row=3)
outputbox.grid(column=0, row=4, columnspan=2)
exitbtn.grid(column=0, row=5, columnspan=2)

window.mainloop()
