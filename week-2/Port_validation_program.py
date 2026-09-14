port = int(input("Enter a port number : "))
valid_port = port >= 1 and port <= 65535 
print(f"valid port: {valid_port}")
