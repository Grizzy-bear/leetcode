class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d1 = {}
        d2 = "abcdefghijklmnopqrstuvwxyz"
        d3 = []
        d4 = []
        # s = 's'
        # key = "a"
        # for i in range(10):
        #     d1.setdefault(key,[]).append(i)
        # print(d1)
        for i in d2:
            d3.append(i)
        # print(d3)
        # for i in range(9):
        #     print(d3[i:i+3])
        #     i +=3
        i = 0
        while i <= 16:
            # print(d3[i:i+3])
            # d4 = d3[i:i+3]
            d4.append(d3[i:i+3])
            i +=3
        # print(d4)
        d4[-1] = ['p', 'q', 'r','s']
        d4.append(['t','u','v'])
        d4.append(['w','x','y','z'])

        # print()
        # print(d4)
        for i in range(10):
            if i == 0:
                continue
            # print(i)
            if i == 1:
                d1.setdefault(i,[])
                # print(d1)
                continue
            d1.setdefault(i,[]).append(d4[i-2])
            # inp = '34'
            inp = digits
            d5 = []
            d6 = []
            for i in inp:
                j = int(i)
                # i = int(i)
                # print(d4{key:i})
                # print(d1[j])
                d5.append(d1[j])
            # print(d5)
            import itertools
            for k in d5:
                # print(k)
                for l in k:
                    # print(l)
                    # z = itertools.product()
                    d6.append(l)
                    # for m in l:
                    #     print()
            # print(d6)
            z = itertools.product(d6[0],d6[1])
            for i in z:
                # print(''.join(i))
                return ''.join(i)