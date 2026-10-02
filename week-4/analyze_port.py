def analyze_port(port):
    if port == 22:
        return "SSH - Remote Administration"
    elif port == 88:
        return "HTTP - Web Traffic"
    elif port == 443:
        return "HTTPS - Secure Web Traffic"
    elif port == 53:
        return "DNS - Domain Name Resolution"
    else:
        return "Unknown Service"


ports = [22 , 53 , 80 , 443 , 9999]

for port in ports:
    print(port, "->", analyze_port(port))

