# def odd_even():
#     numType = ''
#     oddeven = ''
#     for i in range(1, 2000):
#         if isinstance(i, int):
#             numType = 'number '
#             if i % 2 == 0:
#                 oddeven = ' This is an odd number.'
#             elif i % 2 != 0:
#                 oddeven = ' This is an even number.'
#             print numType + str(i) + oddeven


# odd_even()

# def multiply (list, num):
#     for i in range(len(list)):
#         list[i] = list[i] * num
#     print list
# multiply([2,4,10,16], 5)

def layered_multiples(list,num):
    newList = []
    for i in range(len(list)):
        list[i] = list[i] * num
        innerList = []
        for i in range(0, list[i]):
            innerList.append(1)
        newList.append(innerList)
    print newList
layered_multiples([2,4,5], 3)