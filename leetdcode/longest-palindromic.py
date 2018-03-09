#利用while自增
class Solution:
    def lengthOfLongestSubstring(self,s):
        lens = len(s)
        # print(lens)
        if lens < 2:
            # print(s)
            return s
        maxlen = 0
        maxl = 0
        maxr = 0
        i = 0
        # lens = 14
        while i < lens:
            if (lens - i) < maxlen//2:
                break
            j = i#0
            k = i#0
            # i += 1
            # print(j,k)
            while (k<lens-1) and (s[k+1] == s[j]):#寻找相同的回文，如果没有就为false
                k = k+1
                print("k:",k)
                # print(type(k))
            i = k+1#5
            # print("i",i)
            while (j>0) and (k<lens-1) and (s[j-1] == s[k+1]):#寻找具有核心的回文，如果没有就fasle
                j = j -1
                k = k+1
                print("j",j,"k",k)
        # k=2 j=0
            print(j)
            if k-j+1 > maxlen:
                maxlen = k-j+1
                maxl = j
                maxr = k
        return s[maxl:maxr+1]