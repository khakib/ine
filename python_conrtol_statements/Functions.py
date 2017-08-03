hostnames = ('iad1-br-tra-r1', 'iad1-br-tra-r2',
             'ams1-br-tra-r3', 'ams3-br-tra-r4',
             'sfo5-br-entra-r1', 'sfo5-br-tra-r5')

def get_role_by_hostname(hostname):
    info = {}
    info['location'] = hostname.split('-')[0]
    info['role'] = hostname.split('-')[1]
    info['model'] = hostname.split('-')[2]
    return info

for h in hostnames:
    info = get_role_by_hostname(h)
    print 'hostname: %s' % h
    print 'location: %s' % info['location']
    print 'role: %s' % info['role']
    print 'model: %s' % info['model']