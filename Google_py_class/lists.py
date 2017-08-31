'''
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print sum

if 1 in squares:
    print '1 is in squares...skipping'



for num in squares:
    sum += num
print sum  ## 30
'''

squares = [1, 5, 4, 9, 16]
squares.sort()
print squares
print squares.index(4)