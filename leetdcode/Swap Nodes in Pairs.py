li = [11, 22, 33, 44, 55]
# print(li.index(11))
# print(len(li) % 2)
res = []
if len(li) % 2 == 1:
    # li.pop()
    i = 0
    # print(li)
    # for i in range(len(li)):
    while i < len(li) and i+1 < len(li):
        # pass
        # print(i)
        # print(li[i])
        # m = li.index(li[i])
        # n = li.index(li[i + 1])
        m = li.index(li[i])
        n = li.index(li[i + 1])
        li[m],li[n] = li[n],li[m]
        res.append(li[m])
        res.append(li[n])
        i = i+ 2
        print(m, n)
    res.append(li[-1])
    print(res)
else:
    i = 0
    # print(li)
    # for i in range(len(li)):
    while i < len(li) and i+1 < len(li):
        # pass
        # print(i)
        # print(li[i])
        # m = li.index(li[i])
        # n = li.index(li[i + 1])
        m = li.index(li[i])
        n = li.index(li[i + 1])
        li[m],li[n] = li[n],li[m]
        res.append(li[m])
        res.append(li[n])
        i = i+ 2
        print(m, n)
    print(res)

