#!/usr/bin/python3

import sys
from scapy.all import *

packet = Ether(src=RandMAC("*:*:*:*:*:*") ,
               dst=RandMAC ("*:*:*:*:*:*")) / \
        IP(src=RandIP ("*.*.*.*") ,
           dst=RandIP ("*.*.*.*")) / \
        ICMP()