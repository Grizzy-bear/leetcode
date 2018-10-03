import numpy as np

class Solution:
    # def __init__(self):
    #     self.core()
    #     self.addTwoNumbers()

    def addTwoNumbers(self,l1,l2):
        l3 = []
        result = []
        # self.core()
        if len(l1) < len(l2):
            l1 = list(l1)
            l3 = np.pad(l1,(0,len(l2)-len(l1)),'constant')
            # core(l2,l3)
            # print(self.core(l2,l3))
            self.out(self.core(l2,l3))
            # result = self.core(l2,l3)
            # Sum = ''.join(str(i) for i in result)
            # print
            # return l2,l3
        elif len(l1)>len(l2):
            l2 = list(l2)
            l3 = np.pad(l2,(0,len(l1)-len(l2)),'constant')
            self.out(self.core(l1,l3))
            # print(self.core(l1,l3))
            # return l1,l3
        else:
            self.out(self.core(l1,l2))``
            # print(self.core(l1,l2))
            # return l1,l2
            # pass

    def core(self,la,lb):
        result = []
        add = 0
        length = len(la)
        for k in range(length):
            if (la[k] + lb[k] + add) / 10 <=0:
                result.append(la[k]+lb[k]+add)

            else:
                result.append((la[k]+lb[k]+add)%10)
                add = (la[k]+lb[k]+add)/10
        return result
    def out(self,resulta):
        Sum = ''.join(str(i) for i in resulta)
        print(Sum)


# l1 = [1,2,4,7]
# l2 = [5,8,3]
l1 = input("数组一：")
l2 = input("数组二：")
Solution().addTwoNumbers(l1,l2)