from netmiko import Netmiko
from getpass import getpass

net_connect = Netmiko(
    "localhost",
    username="cisco",
    password=getpass(),
    device_type="cisco_ios",
)

print(net_connect.find_prompt())
net_connect.disconnect()