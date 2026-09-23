port = 443

if port == 22:
    print("Commonly used for SSH.")
elif port == 80:
    print("Commonly used for HTTP.")
elif port == 443:
    print("Commonly used for HTTPS.")
else:
    print("Another port number.")