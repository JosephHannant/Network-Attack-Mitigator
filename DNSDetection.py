import scapy.all as scapy
from collections import deque
import time

queuePack = deque(maxlen=10)


"""The packetProcessor takes in packet from the scan function and ensures it is what it is looking for"""


def dnsPacketProcessor(packet):
    if packet.haslayer(scapy.UDP) and packet.haslayer(scapy.IP) and packet.haslayer(scapy.DNSRR) and packet.haslayer(scapy.DNS):
        """Used to ensure there is a packet to be handed in so the function doesn't run unnecessarily"""
        if len(queuePack) > 0:
            """Loop for every pack in the array"""
            for currentPack in queuePack:

                time.sleep(1)
                """Checks nothing is altered in the packet"""
                if currentPack[scapy.IP].payload != packet[scapy.IP].payload and currentPack[scapy.IP].dport == packet[scapy.IP].dport and currentPack[scapy.IP].dst == packet[scapy.IP].dst and currentPack[scapy.DNS].qd.qname == packet[scapy.DNS].qd.qname and currentPack[scapy.IP].sport == packet[scapy.IP].sport and currentPack[scapy.DNS].id == packet[scapy.DNS].id and currentPack[scapy.DNSRR].rdata != packet[scapy.DNSRR].rdata:
                    print "A DNS spoofing attack has been detected"
                    print "The Domain " + (currentPack[scapy.DNS].qd.qname) + " is currently being spoofed"
                    print "Please reset your connection and do not enter sensitive information on any sites"
                else:
                    print"No DNS attack detected"
                    print "The Domain "+(currentPack[scapy.DNS].qd.qname)+" is not currently being spoofed"
                    print "The IP " + (currentPack[scapy.DNSRR].rdata)+" is correct for "+(currentPack[scapy.DNS].qd.qname)
        queuePack.append(packet)


"""Scanner used to sniff for packets"""


def scannerDNS():
    scapy.sniff(filter="", store=0, prn=dnsPacketProcessor)


"""Function to be called on in the CommandLineMenu"""


def startDNS():
    print"Now monitoring for DNS attacks"
    scannerDNS()
    print"Monitoring for DNS attacks ended"
