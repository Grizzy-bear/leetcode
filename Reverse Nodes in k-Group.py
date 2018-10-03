# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head = list(head)
        i = 0
        temp = []
        while i < len(head) and i+k <= len(head):
            if i == 0:
                temp.extend(head[i+k-1::-1])
                i = i+k
                # i = i +n-1
            else:
                temp.extend(head[i+k-1:i-1:-1])
                i = i +k
        if k ==1 :
            temp.append(head[-1])
        else:
            
            temp.extend(head[i:])
        # print(head[i:-1])
        # print(head[3:])
        return temp
tes = [1,2,3,4,5]

print(Solution().reverseKGroup(tes,2))