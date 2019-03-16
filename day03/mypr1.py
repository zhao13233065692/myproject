import random
if __name__ == '__main__':
    sts = input("请输入年月日")
    st =int(sts)
    Y = st//10000
    M = st//100%100
    D = st%100
    print("这是{0}年中的第{1}".format(Y,((M-1)*30+D)))
ss =input("请输入第一人的出生月份")
yy = input("请输入第二人的出生月份")
dd = int(ss)
ff = int(yy)
print(type(dd))
print(type(ff))
if dd % ff==1:
    print("非常有缘")
elif dd % ff==2:
    print("比较有缘")
elif dd % ff==3:
    print("缘分一般")
elif dd % ff==4:
    print("有仇")
print()

st =str(random.choice(range(3)))
print(st)
mlist =[]
for i in range(5):
    mlist.append(random.randrange(10))
sts =str(mlist).find(st)
print("mlist={0}".format(mlist))
print(sts)
mlist.sort()
print(mlist)



