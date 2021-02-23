import scapy.all as scapy
from scapy.layers import http
from datetime import datetime
import time
"""This is the module which checks if an ARP attack is taking place."""
"""This function takes in an ip and returns a mac address."""


def macGet(ip):

    requestARP =scapy.ARP(pdst=ip)
    casted = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    castARP = casted/requestARP
    castList = scapy.srp(castARP, timeout=1, verbose=False)[0]

    return castList[0][1].hwsrc


"""This function uses scapy.sniff to get the packets which it then passes into the packet processor"""


def scanner(interface):
    scapy.sniff(iface=interface, store=False, prn=packetProcessor)


"""This function takes the packet received and checks the mac address of it and compares it to the mac address
generated when the packet is passed into the macGet function"""


def packetProcessor(packet):

    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op ==2:

        try:
            """Sleep is used to control the output load."""
            time.sleep(1)
            trueMac = macGet(packet[scapy.ARP].psrc)
            currentMac = packet[scapy.ARP].hwsrc

            currentTime = datetime.now()
            currentTimeStr = currentTime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            """If statement which tests the mac from the scanner function against the mac from the macGet function"""
            if trueMac != currentMac:
                time.sleep(1)
                print("An ARP attack is taking place at "+ currentTimeStr)
                print("True =")+trueMac
                print("Current =")+currentMac
            else:
                time.sleep(1)
                print("No ARP attack detected at " + currentTimeStr)
                print("True =")+trueMac
                print("Current =")+currentMac
        except IndexError:
            pass


"""Function used to be called by the CommandLineMenu to start the ARP attack detection"""
def startARP():
    print("Now monitoring for ARP attacks")
    scanner("eth0")
    print("Ending monitoring for ARP attacks")
