"""
合并区间
"""
a = [[1, 5], [4, 6], [7, 9], [1, 4]]
temp = []

def Sort(a=[]):
    index = sorted(a, key=lambda x:x[0])

    # 最后排序
    for i in range(len(index)):
        if i+1 < len(index):
            if index[i][0] == index[i+1][0]:
                if index[i][1] > index[i+1][1]:
                    index[i], index[i+1] = index[i+1], index[i]
    return index
# print(index)

Index = Sort(a)

length = len(Index)
res = []
for i in range(length):
    if res == []:
        res.append(Index[i])
    else:
        size= len(res)
        if res[size-1][0] <= Index[i][0] <= res[size-1][1]:
            res[size-1][1] = max(Index[i][1], res[size-1][1])
        else:
            res.append(Index[i])
print(res)