if __name__ == '__main__':
    mlist = [1,2,3,4,5]
    mlen = len(mlist)
    print(mlen)
for i in mlist:
    print("mlist[{0}]={1}".format(i.__index__(),i))
    nlist =mlist[0:6]
    print("mlist id is {mlistid}".format(mlistid=id(mlist)))
    print("nlist id is {nlistid}".format(nlistid=id(nlist)))

mu=[1,2,3,4,5,6,7]
print(mu)
mu[0]=10
print(mu)
mdict = {"name":"张三","age":15}
for i in mdict.values():
   print(i)
for k,v in mdict.items():
   print("k值是：{0},value值是：{1}".format(k,v))
for i in mdict.values():
        print(i)
for i in mdict.keys():
    print(i)