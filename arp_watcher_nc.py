#!/usr/bin/python3

from scapy.all import sniff , ARP
from signal import signal , SIGINT
import sys

arp_watcher_db_file = "/var/ cache/arp -watcher.db"
ip_mac = {}

# Save ARP table on shutdown
def sig_int_handler( signum , frame):
    print("Got SIGINT. Saving ARP database...")
    try:
        f = open( arp_watcher_db_file , "w")

        for (ip , mac) in ip_mac.items ():
            f.write(ip + " " + mac + "\n")

        f.close()
        print("Done.")
    except IOError:
        print("Cannot write file " + arp_watcher_db_file)

    sys.exit(1)


def watch_arp(pkt):
    # got is -at pkt (ARP response)
    if pkt[ARP].op == 2:
        print(pkt[ARP].hwsrc + " " + pkt[ARP].psrc)

        # Device is new. Remember it.
        if ip_mac.get(pkt[ ARP].psrc) == None:
            print("Found new device " + \
                    pkt[ARP].hwsrc + " " + \
                    pkt[ARP].psrc)
            ip_mac[pkt[ARP].psrc] = pkt[ARP].hwsrc
