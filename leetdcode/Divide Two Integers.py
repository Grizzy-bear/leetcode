import datetime
start = datetime.datetime.now()
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        
        a = dividend
        b = divisor
        # print(a,b)
        if a >b :
            # i = a
            j = 0
            i = a
            while i >b:
                # i = a
                # j = 0
                if i >0 :
                    i = a-b
                    a = i
                    j += 1
                    # print(j,i)
                else:
                    break
            return j,i
end = datetime.datetime.now()
print(end - start)