class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = x
        if -2147483648<a < 2147483648:
            j = len(x)-1
            if len(a)%2 == 1:
                i = 0
                while i < len(a)/2:
                    if a[i] == a[j-i]:
                        # print("回文")
                        i += 1
                    # print("是回文")
                print("yes")
            elif len(a)%2 == 0:
                i = 0
                while i < len(a)/2:
                    if a[i] == a[j-i]:
                        i += 1
                print("en")
            else:
                print("非回文数字")
        else:
            print("false")