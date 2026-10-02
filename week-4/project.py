def check_port(port):
    if port == 80:
        return "HTTP port"
    elif port == 443:
        return "HTTPS port"
    elif port == 22:
        return "SSH port"
    else:
        return "Unknown port"

print(check_port(80))
print(check_port(443))
print(check_port(22))
print(check_port(9999))