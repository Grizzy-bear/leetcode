class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = []
        v = str(x)
        if x < 0:
            for i in v:
                if i == "-":
                    continue
                a.append(i)
            if a[-1] == "0":
                a.pop(-1)
            b = sorted(a, reverse=True)
            b.insert(0,"-")
        else:
            for i in v:
                a.append(i)
            b = sorted(a,reverse=True)
        return ''.join(b)

# d = input()
d = 123
print(Solution().reverse(d))