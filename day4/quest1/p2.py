import random
def binji():
    mlist = [random.randrange(55) for i in range(10)]
    print("第一个列表是{0}".format(mlist))
    nlist = [random.randrange(55) for i in range(15)]
    print("第二个列表是{0}".format(nlist))
    mset = set(mlist)
    nset = set(nlist)
    kset=nset.union(mset)
    print("他们的并集是{0}".format(kset))