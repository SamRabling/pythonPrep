#1 
def greetings():
    greetings = "Hello "
    name = "dojo"
    print name + greetings

greetings()

#2
def iterate():
    arr=['Wish', 'Mop', 'Bleet', 'March', 'Jerk']
    for x in arr:
        print x
iterate()

#3
def multiplication(num):
    lst = []
    for i in range (25):
        num  *= 2
        lst.append(num)
    print lst
multiplication(1)
    

def input(string):
    newstr = ""
    for i in range(len(string)):
        newstr += string[-(i + 1)]



    print newstr

input("racecars")

def xyz():
    x = 10
    print x
    x *= 7
    print x
    y = 30
    print y
    z = y + x
    print z
    z *= 3
    print z
    z -= y
    print z
    z /= 27
    print z
    x = z + y
    print x
    y = 3
    print y
    x += y
    print(x)
    if x % 10 == 0:
        return "True"
    else:
        return "False"

print xyz()