'''


f = open('/Users/khakib/PycharmProjects/INE/FileObjects/Test.txt', 'r+')
f.write('This is not a test\nThis is not a test\nThis is not a test')
f.close()
print f

with open('Test.txt') as f:
    data = f.read()

print 'Status of file %s' %(f)
print data


f = open('Test.txt', 'r+')
print 'Name of file: ', f.name
print 'Name of file: ', f.mode
f.seek(0)
line = f.readline()
print "Read Line: %s" % (line)

'''





