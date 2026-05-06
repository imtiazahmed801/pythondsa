log_file = [
    "192.168.1.2 - GET /home",
    "192.168.1.1 - POST /login",
    "192.168.1.4 - GET /about",
    "192.168.1.3 - POST /login",
    "192.168.1.1 - GET /home",
    "192.168.1.2 - GET /home",
    "192.168.1.2 - GET /home",
    "192.168.1.4 - GET /about",
    "192.168.1.6 - GET /home",
    "192.168.1.7 - POST /login",
    "192.168.1.8 - GET /home",
    "192.168.1.9 - GET /home",
    "192.168.1.2 - POST /login",
    "192.168.1.3 - GET /home",
    "192.168.1.2 - GET /about"
]

endpoint_dict = {}
ipaddr_dict = {}

for line in log_file:
    parts = line.split()
    ip_addr = parts[0]
    endpoint = parts[3]
    
    endpoint_dict[endpoint] = endpoint_dict.get(endpoint, 0) + 1
    ipaddr_dict[ip_addr] = ipaddr_dict.get(ip_addr, 0) + 1

frequent_endpoint = max(endpoint_dict, key=endpoint_dict.get)
num_endpoint = max(endpoint_dict.values())

freq_ip = max(ipaddr_dict, key=ipaddr_dict.get)
num_ip = max(ipaddr_dict.values())

print("------------------------------------")
print("Endpoints Stats:")
print("------------------")
for endpoint, count in endpoint_dict.items():
    print(f"{endpoint} -> {count}")

print("------------------------------------")
print("IP Stats:")
print("-------------------")
for ip_addr, count in ipaddr_dict.items():
    print(f"{ip_addr} -> {count}")

print("------------------------------------")
print(f"{frequent_endpoint} was visited {num_endpoint} times.")
print(f"{freq_ip} made {num_ip} requests.")
