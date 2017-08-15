import math
<<<<<<< HEAD
Cluster = {'BETA', 'BJS', 'BOM', 'CMH', 'CORP', 'DUB', 'FRA',
           'GRU', 'IAD', 'ICN', 'LCK', 'LHR', 'NRT', 'PDT', 'PDX',
           'SFO', 'SIN', 'SYD', 'YUL', 'ZHY'}
=======
v4 = int(input("Please enter V4 Accepted Max : "))
v6 = int(input("Please enter V6 Accepted Max : "))
v4_pref = math.ceil((v4 * .20) + v4)
v6_pref = math.ceil((v6 * .20) + v6)
print ('Total v4 prefixes is {} :').format(v4_pref)
print ('Total v6 prefixes is {} :').format(v6_pref)
>>>>>>> 5a7a17cbe7a813ddb0842408523ff05d9664dc7a

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
