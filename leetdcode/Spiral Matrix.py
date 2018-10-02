"""
螺旋矩阵
"""
a = [
    [1, 2, 3,7],
    [4, 5, 6,2], 
    [7, 8, 9,8],
    [2,4,7,1,9]
]

ans = []


# print(ans)
try:
    while True: # while 会循环至所有结果，不加的话只循环一次
        ans += a.pop(0)
# print(ans)
        for line in a:
            ans.append(line.pop())
        ans += a.pop()[::-1]
        for l in a[::-1]:
            ans.append(l.pop(0))
except:
    # print(ans)
print(ans)