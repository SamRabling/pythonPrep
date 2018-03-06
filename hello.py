print "hello tejas"
#commenting out on python :D
def say_hello(name):
    if name:
     print 'hello,' + name + 'from inside the function'
    else:
     print 'no name'
print 'outside of function'
name = 'Sam'
print 'My name is', name
print 'my name is' + name
first_name = 'sam'
last_name = 'coder'
print 'my name is {} {}' .format(first_name, last_name)
x = "Hello World"
print x.upper()

for count in range(0,5):
    print 'looping - ', count

my_list = [4, 'dog', 99, ['things', 'inside'], 'hello world!']
for element in my_list:
    print element

for count in range (0,5):
    print "looping - ", count

count = 0
while count <5: 
    print 'looping -', count
    count += 1