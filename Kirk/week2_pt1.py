from tabulate import tabulate
ip_addr = raw_input('Please enter IP address: ')
octet = ip_addr.split('.')

if len(octet) == 3:
    octet.append('0')
elif len(octet) == 4:
    octet[3] = '0'
ip_number = '.'.join(octet)
a = bin(int(octet[0]))
b = bin(int(octet[1]))
c = bin(int(octet[2]))
d = hex(int(octet[0]))


print tabulate([[ip_number,a,b,c,d]],headers=['Network','First Octet','Second Octect','Third Octet','First Octet hex'])


