# def checkered1(n, x):
#     for i in range (0, n):
#         for y in range(0, i+1):
#             print("* ")
#             print(" ")

# checkered1(5,5)

steps = 4
lines = 1
l = 1
if l in range(lines):
    for r in range(steps):
        print('* ' + (' ' * l) + '* ' + '* ' + '* ')
        print(' *' + ('*' * l) + ' *' + ' *' + ' *') 
    