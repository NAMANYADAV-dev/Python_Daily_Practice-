# ports = [22,80,443,53]
# print(ports[0])
# print(ports[len(ports)-1])
# print(len(ports))

# ports.append(8080)
# print(ports)

# ports.remove(80)
# print(ports)

# print(443 in ports)

# dangerous_ports = [21 ,23 , 445 , 3389]

# ports = int(input("Enter your favourite ports: "))

# for port in dangerous_ports:
#     if ports == port:
#         print("Potentially Dangerous")
#         break
#     elif ports == port:
#         print("It is not Dangerous")
#         break
#     else:
#         print("Not in dangerous port list ")
        


ports = [443 , 22 , 8080 , 80 , 53]

ports.sort()

print(ports)