cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

ios_version = cisco_ios.split(',')[2]
version = ios_version.split()[1]
print('ios version is "{}"'.format(version))