# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        l1 = self.mergeKLists(lists[0])
        l2 = self.mergeKLists(lists[1])
        head = self.mergeTwo(l1,l2)
        return head
    
    def mergeTwo(self,l1,l2):
        result = []
        if len(l1) == len(l2):
            for i,j in zip(a,b):
            # print(i,j)
            d = min(i,j)
            c = max(i,j)
            result.append(d)
            result.append(c)
        elif len(a)> len(b):
            for i,j in zip(a[:len(b)],b):
                f = min(i,j)
                g = max(i,j) 
                result.append(f)
                result.append(g)
            result.append(''.join(a[len(b):]))
        else:
            for i,j in zip(b[:len(a)],a):
                f = min(i,j)        
                g = max(i,j)
                result.append(f)
                result.append(g)
            result.append(''.join(b[len(a):]))
        return result
        # def maxmin(self,i,j):