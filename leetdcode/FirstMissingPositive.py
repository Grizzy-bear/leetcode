'''
 @Author: Grizlly 
 * @Date: 2018-03-09 00:42:54 
 * @Last Modified by:   Grizzly 
 * @Last Modified time: 2018-03-09 00:42:54 
'''


class Solution:
    def cau1(self, i, list1):
        if list1[i] + list1[i] == list1[i + 3]:
            if list1[i] + list1[i + 1] == list1[i + 4]:
                cau1(i + 1, list1)
            # pass
            else:
                return list1[i + 1] + 1
        else:
            return list1[i] + 1

    def cau(self, i, list1):

        if list1[i] + list1[i] == list1[i + 1]:
            if list1[i] + list1[i + 1] == list1[i + 2]:
                ans1 = self.cau1(i + 1, list1)
                return ans1
            else:
                # print(list1[i+2])
                return list1[i + 1] + 1
            # print(list1[i+1])
        else:

            return list1[i] + 1

    def firstMissingPositive(self, nums):
        """
    :type nums: List[int]
    :rtype: int
    """
        nums.sort()
        print(nums)
        if 1 not in nums:
            return 1
        else:
            print("ok")
            i = nums.index(1)
            return self.cau(i, nums)


nums = [3, 4, -1, 0, 1, 2, 5, 6, 7]
print(Solution().firstMissingPositive(nums))
