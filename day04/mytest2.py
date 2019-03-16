import  random
if __name__ == '__main__':
    #生成一个整数
    num =random.randrange(999)
    print(num)
    #创建列表添加元素
    mlist =[]
    for i in range(6):
        mlist.append(random.randrange(999))
    nu=str(mlist).find(str(num))
    print(mlist)
    #判断这个数是否在序列中
    if nu!=-1:
        print("这个整数在序列中",end="")
    else:
        print("这个整数不在序列中",end="")
