class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        if size <= numRows or numRows == 1:
            return s
        ans = ''
        i = 0
        while i < numRows:
            j = i
            if i == 0 or i == numRows - 1:
                while j < size:
                    ans += s[j]
                    j += 2*numRows - 2
                    if 2 * numRows - 2 == 0:
                        break
            else:
                while j < size:
                    ans += s[j]
                    j += 2*(numRows - i) - 2
                    if j >= size:
                        break
                    ans += s[j]
                    j += 2*i
            i += 1
        return ans
a = "asdsfdsfd"
print(Solution().convert(a,3))