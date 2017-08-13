'''
x = int(raw_input("Please enter an integer: "))
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'


friends = ('Joey','Chandler','Ross','Monica','Rachel')
for f in friends:
    if friends == 'Joey' and f == 'Chandler':
        break
    elif f == 'Chandler':
        print '{} is the best!!'.format(f)
    else:
        print '{} made my life better!!'.format(f)

for i in range(4):
    print ('Hello World')

x = int(1)
while x < 5:
    x += 1
    print ('Try again!')
for i in range(4): print ('Hello World')

'''



