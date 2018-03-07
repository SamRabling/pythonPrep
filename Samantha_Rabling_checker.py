# def checkered1(n, x):
#     for i in range (0, n):
#         for y in range(0, i+1):
#             print("* ")
#             print(" ")

# checkered1(5,5)

def checkers (l):
    for i in range (1,l):
        if i % 2 == 0:
            print (' *  *  *  *  *')
        if i % 2 != 0:
            print ('*  *  *  *  *  ')
checkers(5)
    