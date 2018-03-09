class MathDojo(object):
    def __init__(self, num):
            self.num = num

    def add(self, *nums):
        for nmbr in nums:
            if isinstance(nmbr, int) or isinstance(nmbr, float):
                self.num += nmbr
            elif isinstance(nmbr, list) or isinstance(nmbr, tuple):
                self.num = self.num + sum(nmbr)
        return self 

    def substract(self, *nums):
        for nmbr in nums:
            if isinstance(nmbr, int) or isinstance(nmbr,float):
                self.num -= nmbr
            elif isinstance(nmbr, list) or isinstance(nmbr, tuple):
                self.num = self.num - sum(nmbr)
        return self
        
    def result(self):
        print self.num
        return self

md = MathDojo(0)

# print md.add(2).add(2,5).substract(3,2).result()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).substract(2, [2,3], [1.1,2.3]).result()