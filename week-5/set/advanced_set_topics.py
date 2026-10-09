# A = {1,2,3}
# B = {1,2,3,4,5}
# C ={1,2,10}

# print(A.issubset(B))
# print(C.issubset(B))


# A = {1 , 2 , 3}
# B = {1 , 2, 3, 4, 5}
# print(B.issubset(A))
# print(A.issubset(B))


# A = {1,2,3}
# B = {4,5,6}
# print(A.isdisjoint(B))


# A = {1,2,3}
# B = {4,5,6,3}
# print(A.isdisjoint(B))


# firewall_ips = {"192.168.1.10", "10.0.0.5"}
# server_ips = {"172.16.0.8", "192.168.1.20"}

# if firewall_ips.isdisjoint(server_ips):
#     print("No common IP addresses")
# else:
#     print("Common IP addresses found")


# A = {1 , 2, 3}
# B = {3 , 4 , 5}
# print(A.union(B))
# print(A.difference(B))
# print(A.intersection(B))
# print(A.symmetric_difference(B))


# numbers = {1 , 2, 3, 4, 5}
# squares = {x*x for x in numbers}
# print(squares)


# numbers = {1,2,3,4,5,6,7,8,9,10}
# even_numbers = {x for x in numbers if x % 2 == 0 }
# print(even_numbers)


# usernames = {"NAMAN","RAHUL","AMAN","NAMAN"}
# normalized = {name.lower() for name in usernames}
# print(normalized)

# A = frozenset([10 ,29 , 39])
# print(A)
# print(type(A))

# permissions = frozenset({"read","write"})
# role = {
#     permissions: "editor"
# }

# print(role[permissions])