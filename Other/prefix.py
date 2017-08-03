import math
v4 = int(raw_input("Please enter V4 Accepted Max : "))
v6 = int(raw_input("Please enter V6 Accepted Max : "))
v4_pref = math.ceil((v4 * .20) + v4)
v6_pref = math.ceil((v6 * .20) + v6)
print ('Total v4 prefixes is {} :').format(v4_pref)
print ('Total v6 prefixes is {} :').format(v6_pref)



