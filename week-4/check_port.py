def check_port(port):
    if port == 22:
        return "SSH"
    elif port == 80:
        return "HTTP"
    elif port == 443:
        return "HTTPS"
    else:
        return "Unknown"

def analyze_port(port):
    service = check_port(port)


    return f"Port {port}: {service}"


print(analyze_port(443))