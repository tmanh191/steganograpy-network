from scapy.all import sniff

def packet_callback(packet):
    print("="*50)
    packet.show() 

print("Đang bắt toàn bộ gói tin...")
sniff(prn=packet_callback, store=False)
