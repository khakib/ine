i = int(input('Please enter an integer: '))
to_eighth = []
while i < 1000:
    to_eighth.append(i)
    if i == 100:
        break
    i += 1

print (to_eighth)