from scapy.all import sniff


def packet_callback(packet):
    print("Received Packet:")
    print(packet.show())


# Specify the network interface to listen on and the port
iface = "en0"  # Adjust this to your network interface
port = 12345  # Port to listen on

# Define a filter to capture only UDP packets destined for the specified port
filter_str = f"udp port {port}"

print(f"Listening for packets on interface {iface}...")
sniff(iface=iface, prn=packet_callback, filter=filter_str, store=0)
