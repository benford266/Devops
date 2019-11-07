#! python3 
# portchanger.py
#
# Script to do vlan changes on cisco switches.

import sys
import re



print("\n\n****** Port Changer ******\n\n")

#check for valid mac address 
def maccheck(macaddress):
  if re.match("[0-9a-f]{2}([-:.])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", macaddress.lower()):
    return 1
  else:
    return 0




## Get mac addresses from user
maclist = []
maccount = ''
while True:
  if maccount == '':
    print("Enter Mac Address(return empty line to stop): ")
    maccount = '1'  
  macadd = input()
  if macadd == '':
    break
  # Test for valid mac address and add to list if valid
  if maccheck(macadd) == 1:
    maclist.append(macadd.lower()) 
 
## Clean up list of mac addresses
# only replaces colons in string 
#cleanlist = [mac.replace(":","") for mac in maclist]
# RegEX to clean up special chars between bits.
cleanlist = [mac.replace(":","") for mac in maclist]
 
## Split to last 4 chars
splitlist = [split[-4:] for split in cleanlist]
 

#print("Below are the mac addresses")
#print(maclist)
 
#print("Below are the removed chars")
#print(cleanlist)
 
## Print out Cisco commands
print("Below are the commands to run in Cisco")
for split in splitlist:
  print("show mac add | inc {}".format(split))
 
## Get switch info from UserWarning
switchout = []
configcount = ''
while True:
    if configcount == '':
        print("\n\n\nEnter Switch output (return empty line to stop): ")
        configcount = '1'
    switchline = input()
    if switchline  == '':
        break
    switchout = switchout + [switchline]

## Gets interface information from the switch output
interfacelist = []
 
for l in switchout:
  if ("Gi" or "Fa") in l:
    interface = l[-8:]
    interface = interface.replace (" ","")
    interfacelist = interfacelist + [str(interface)]
 
## Check ports vs mac
if len(interfacelist) != len(splitlist):
  countcont = input("You entered {} Mac addesses but only found {} ports. Do you want to continue? (y/n)".format(len(splitlist), len(interfacelist)))
  if countcont == 'n':
    sys.exit()

## Get VLAN information from user
print("\n\n Please enter Vlan information \n\n") 
dvlan = input("Please enter data vlan: ")
vvlan = input("Please enter voice vlan: ")

## Prints the switch config outto switch
print("\n\nBelow is the config changes to paste into the switch\n\n")
for port in interfacelist:
  print("int {} \n switchport access vlan {} \n switchport voice vlan {}".format(port,dvlan,vvlan))
 