from tabulate import tabulate
import sys
ip_address = '192.168.1.1'
octets = ip_address.split('.')
ip_addr_bin =[]
if len(octets) == 4:
    for n in octets:
        bin_ip = bin(int(n))
        bin_ip = bin_ip[2:]

        while True:
            if len(bin_ip) >= 8:
                break
            bin_ip = '0' + bin_ip
        ip_addr_bin.append(bin_ip)
    ip_addr_bin = ".".join(ip_addr_bin)




else:
    print 'Incorrect IP address'







