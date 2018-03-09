'''
 @Author: Grizlly 
 * @Date: 2018-03-08 19:33:05 
 * @Last Modified by:   Grizzly 
 * @Last Modified time: 2018-03-08 19:33:05 
'''


class Solution(object):
    # def __init__(self, *args):
    #     super(Solution, self).__init__(*args))
    def boolcom(self, candidates, target, j):
        ans = []
        size = len(candidates)
        if target == 0:
            return []
        if size < j + 1 or target < 0:
            return [[-1]]
        n = 1
        while j + n < size:
            if candidates[j + n] != candidates[j]:
                break
            n += 1
        tmp1 = self.boolcom(candidates, target, j + n)
        tmp2 = self.boolcom(candidates, target - candidates[j], j + 1)
        if len(tmp2) == 0:
            ans.append([candidates[j]])
        elif tmp2 != [[-1]]:
            for i in range(len(tmp2)):
                ans.append([candidates[j] + tmp2])
        if len(tmp1) != 0 and tmp1 != [[-1]]:
            for i in range(len(tmp1)):
                ans.append(tmp1[i])
        if len(tmp2) != 0 and tmp1 == [[-1]] and tmp2 == [[-1]]:
            return [[-1]]
        return ans

    def combina(self, candidates, target):
        """
        :type candidate:list[int]
        :type target:int
        :rtype List[list[int]]
        """
        candidates.sort()
        ans = self.boolcom(candidates, target, 0)
        if ans == [[-1]]:
            return []
        return ans
