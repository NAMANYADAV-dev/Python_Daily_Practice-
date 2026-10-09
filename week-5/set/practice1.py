# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}

# print(A.issubset(B))
# print(B.issubset(A))


# A = {10, 20, 30}
# B = {40, 50, 60}
# C = {30, 40, 50}

# print(A.isdisjoint(B))
# print(A.isdisjoint(C))


# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# result = {x * 2 for x in numbers if x % 2 == 0}

# print(result)

# A = frozenset([1, 2, 3])

# print(2 in A)
# print(A.union({4, 5}))


detected_ips = {
    "192.168.1.10",
    "10.0.0.5",
    "172.16.0.8"
}

blocked_ips = {
    "10.0.0.5",
    "192.168.1.50"
}

print(detected_ips & blocked_ips)
print(detected_ips - blocked_ips)
print(detected_ips | blocked_ips)