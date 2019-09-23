## mac address search


print("****** Bens Port Changer ******")
 
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
  maclist = maclist + [macadd.lower()]
 
## Clean up list of mac addresses
 
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
  if ("Po" or "Gi" or "Fa") in l:
    interface = l[-8:]
    interface = interface.replace (" ","")
    interfacelist = interfacelist + [str(interface)]
 

## Get VLAN information from user
print("\n\n Please enter Vlan information \n\n") 
dvlan = input("Please enter data vlan: ")
vvlan = input("Please enter voice vlan: ")

## Prints the switch config outto switch
print("\n\nBelow is the config changes to paste into the switch\n\n")
for port in interfacelist:
  print("int {} \n switchport access vlan {} \n switchport voice vlan {}".format(port,dvlan,vvlan))
 