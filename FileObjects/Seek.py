import time
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



with open('Test.txt', 'r') as selected_user_file:
    selected_user_file.seek(0)  #Begin from the begining - thats what seek(0) means
    username = selected_user_file.readlines()[0].split(',')[0]
    selected_user_file.seek(0)
    password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
print('Welcome', username, 'Today is', time.strftime("%d/%m/%Y"))
print('Your password is', password)
selected_user_file.close()


'''
