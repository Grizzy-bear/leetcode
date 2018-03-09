class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        result = []
        for i in range(nums.index(tar),len(nums)):
            if s[i] == s[i+1]:
                res.append(i)
                if s[i+1] !=s[i+2]:
                    res.append(i+1)
            else:
                break
        result.append(res[0])
        result.append(res[-1])
        return result