# a = 71
# if len(a) == 4:
#     pass
# elif len(a) == 3:
#     pass
# elif len(a) == 2:
#     pass
# else:
#     pass:
#把减法翻着来
values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
lst = ''
for i in range(0, len(values)):
    while a > values[i]:
        a -= values[i]
        lst += numerals[i]
print(lst)
c = "LXX"
# b = numerals.index("X")
# print(b)
result = []
for i in c:
    # print(i)
    b = numerals.index(i)
    n = values[b]
    result.append(n)
# print(result)
res = 0
for j in result:
    # j += j
    res = res + j
print(res+1)
