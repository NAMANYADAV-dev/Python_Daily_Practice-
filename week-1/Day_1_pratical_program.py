# Collect user input for the security assessment details
analyst_name = input ("Enter analyst name : ")
target_ip = input ("Enter authorized target IP: ") 
target_port = int(input("Enter target port : "))
permisssion_id = input("Enter permission ID: ")
target_hostname = input("Enter target hostname : ")
protocol_name = input ("Enter Protocols name: ")
maximum_attempts = input("Enter maximum_attempts: ")

# Display the security assessment information in a readable format
print("\n... Security Assessment Information...")

print(f"Analyst name: {analyst_name}")
print(f"Target IP : {target_ip}")
print(f"Target port : {target_port}")
print(f"Permission ID: {permisssion_id}")
print(f"Target hostname : {target_hostname}")
print(f"Target hostname : {protocol_name}")
print(f"Target hostname : {maximum_attempts}")

# Show the data type of each stored value
print("\n... Data Types ...")

print(type (analyst_name))
print(type (target_ip))
print(type (target_port))
print(type (permisssion_id))
print(type (target_hostname))
print(type (protocol_name))
print(type (maximum_attempts))
