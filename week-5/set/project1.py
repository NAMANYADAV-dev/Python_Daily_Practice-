# firewall_logs = [
#     "10.0.0.8",
#     "172.16.0.8",
#     "198.18.0.10",
#     "192.168.0.20"
# ]


# server_logs = [
#     "10.0.0.5",
#     "172.16.0.30",
#     "198.18.0.20",
#     "192.168.0.60"
# ]


# firewall_ips = set(firewall_logs)
# server_ips = set(server_logs)


# common_ips = firewall_ips & server_ips

# all_ips = firewall_ips | server_ips

# firewall_only  = firewall_ips - server_ips

# print("Firewall unique IPs:", firewall_ips)
# print("Server unique IPs:", server_ips)
# print("Common IPs:", common_ips)
# print("All unique IPs:", all_ips)
# print("Firewall-only IPs:", firewall_only)
# print("Total unique IPs:", len(all_ips))
