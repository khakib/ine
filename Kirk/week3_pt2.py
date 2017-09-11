from tabulate import tabulate

entry1 = "*  1.0.192.0/18   157.130.10.233     0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233     0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233     0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233     0 701 6762 6762 6762 6762 38040 9737 i"

for entry in [entry1, entry2, entry3, entry4]:
    entry_split = entry.split()
    prefix_split = entry_split[1]
    asn = entry_split[4:-1]
    print tabulate([[prefix_split,asn]], headers=['Prefix','ASN'])


