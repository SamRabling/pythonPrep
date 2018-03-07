# for i in range(99, 100000):
#     if i % i == 0:
#         print i

# i = 7
# # for i in range(100, 100000):
# if i ** 2 == i * i:
#     print 'bar'
# elif i == (i % i == 0):
#     print 'foo'
# else:
#     print 'foobar'
def is_perfect_square(n):
    x = n // 2
    print x
    y = set([x])
    print y
    while x * x != n:
        x = (x + (n // x)) // 2
        print x
        if x in y: return False
        y.add(x)
    return True
print(is_perfect_square(25))
