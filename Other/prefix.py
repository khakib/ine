import math
Cluster = {'BETA', 'BJS', 'BOM', 'CMH', 'CORP', 'DUB', 'FRA',
           'GRU', 'IAD', 'ICN', 'LCK', 'LHR', 'NRT', 'PDT', 'PDX',
           'SFO', 'SIN', 'SYD', 'YUL', 'ZHY'}

c = str(raw_input("Please enter a cluster: ")).upper()

v4 = int(raw_input("Please enter V4 Received prefix : "))
v6 = int(raw_input("Please enter V6 Received prefix : "))
v6_pref = math.ceil((v6 * .20) + v6)
v4_pref = math.ceil((v4 * .20) + v4)
V6_ACCEPTED_MIN=1
V4_ACCEPTED_MAX=v4_pref
V6_ACCEPTED_MAX=v6_pref

print ('V4_RECEIVED_MAX={}').format(int(v4_pref))
print ('V6_RECEIVED_MAX={}').format(int(v6_pref))
if (c in Cluster) == True:
    print 'DEVICE_IN_CLUSTER=true REGION={}'.format(c).lower()
else:
    print 'DEVICE_IN_CLUSTER=false REGION=false'
