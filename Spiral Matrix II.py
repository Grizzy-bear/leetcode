# 填充螺旋矩阵
"""
3: 3 2 2 1 1
4: 4 3 3 2 2 1 1
5: 5 4 4 3 3 2 2 1 1

"""
# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

temp = []
i = 1
while i <= 5**2:
    temp.append(i)
    i += 1
# print(temp)

j = 5
while True:
    tempA = temp[:j]
    del temp[:j]
    for m in range(j-1):
        tempB = temp[m:j-1]