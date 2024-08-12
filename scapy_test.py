from scapy.layers.inet import IP, ICMP, sr1
from scapy.packet import ls

from scapy.all import *


# Define a callback function to handle sniffed packets
def packet_callback(packet):
    print("Sniffed Packet:")
    packet.show()

    # Example: Spoof a response packet (for demonstration purposes only)
    if packet.haslayer(IP) and packet.haslayer(ICMP):
        # Craft a spoofed ICMP Echo Reply packet
        ip = IP(src=packet[IP].dst, dst=packet[IP].src)
        icmp = ICMP(type=0, id=packet[ICMP].id, seq=packet[ICMP].seq)  # Echo Reply
        spoofed_packet = ip / icmp
        print("Sending Spoofed Packet:")
        send(spoofed_packet)


# Sniff packets on the network
def start_sniffing(interface):
    print(f"Starting to sniff on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, filter="icmp", store=0)


# Specify the network interface to sniff on (e.g., 'eth0', 'wlan0', etc.)
interface = 'en0'  # Change this to your network interface
start_sniffing(interface)
