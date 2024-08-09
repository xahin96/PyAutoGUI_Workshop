from scapy.layers.inet import IP, ICMP, sr1
from scapy.packet import ls

from scapy.all import *

iph = IP(src="10.0.2.4", dst="10.10.10.10")

# Show the fields of the IP header
ls(IP())
