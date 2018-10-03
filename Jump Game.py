# 深度递归便可实现

def jump(i=0,a=[2,3,1,1,4]):
    if a[i] > len(a)-1:
        print("error")
    elif a[i] == len(a) -1:
        print("good")
    else:
        print("正在调整""")
        index = int(a[i])
        b = a[index+1:]
        jump(a=b)
jump()