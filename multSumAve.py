# PART 1
for i in range(0,1001):  #this for loop prints numbers of 1 to 1000
    print i

#PART 2
mults = []
for i in range(4, 1000001): #setting the range of the i
    if i%5==0:              #setting a conditional (multiples of 5)
        print i  

a = [1,2,5,10,255,3]
total = sum(a)          #adding the numbers in the list
print total

avg = sum(a) / len(a)
print avg