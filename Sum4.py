class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        res = []
        for i,a in enumerate(nums):
            # print(a)
            for j,b in enumerate(nums[i+1:]):
                # print(a,b)
                for k,c in enumerate(nums[i+2:]):
                    # print(a,b,c)
                    for z,d in enumerate(nums[i+3:]):
                        # print(a,b,c,d)
                        if a +b+c+d == target:
                            result.append(sorted([a,b,c,d]))
        for i in result:
            if not i in res:
                res.append(i)
        return res
