from scapy.layers.inet import IP, ICMP, UDP, sr1
from scapy.packet import ls

from scapy.all import *


# Define source and destination
src_ip = "10.0.0.1"  # Spoofed source IP
dst_ip = "10.0.0.2"  # Destination IP (should be your server's IP)
dst_port = 12345     # Port to send to

# Create the UDP packet
packet = IP(src=src_ip, dst=dst_ip)/UDP(sport=12345, dport=dst_port)/b"Hello, this is a spoofed packet!"

print(f"Sending spoofed packet from {src_ip} to {dst_ip}:{dst_port}")
send(packet)
