from __future__ import print_function

num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# print str([1,2,3,4,5,6,7,8,9,10,11,12])[1:-1]
for i in range(1, len(num)):
    print (i, end=' ')
    for j in range(1, len(num)):
        print ((i * j), end=' ')
print ()