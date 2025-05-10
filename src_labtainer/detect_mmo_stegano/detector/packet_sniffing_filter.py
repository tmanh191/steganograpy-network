from scapy.all import sniff, IP, TCP, Raw


ip_nguon    = "?.?.?.?"
ip_dich   = "?.?.?.?"
port_dich  = ????

def goi_callback(pkt):
    if IP in pkt and TCP in pkt:
        if (pkt[IP].src == ip_nguon and
            pkt[IP].dst == ip_dich and
            pkt[TCP].dport == port_dich):

            if Raw in pkt:
                payload = pkt[Raw].load

                with open("result.txt", "a") as f:
                    f.write(repr(payload) + "\n")  


            print(f"[+] Gói TCP từ {pkt[IP].src} đến {pkt[IP].dst}:{pkt[TCP].dport}")
            pkt.show()

def main():
    bpf_filter = f"tcp and src host {ip_nguon} and dst host {ip_dich} and dst port {port_dich}"
    print(f"Đang bắt gói TCP từ {ip_nguon} đến {ip_dich}, port {port_dich}...")
    sniff(filter=bpf_filter, prn=goi_callback, store=0)

if __name__ == "__main__":
    main()
