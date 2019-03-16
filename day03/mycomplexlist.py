if __name__ == '__main__':
    mlist=list(range(1,11))
    nlist = [i**2 for i in mlist ]
    print(nlist)
    klist = [
        "good ","good ","study",
        " good ","good","study ",
        "good "," good"," study",
        " good ","good"," study ",
        "good ","good ","study",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
        " day ","day"," up",
             ]
    mlist1 = [i.strip() for i in klist]
    print(mlist1)
    mdic={}
    for i in set(mlist1):

        mdic[i] = mlist1.count(i)
    print(mdic)
    #查看是否有重复字符串
    if len(set(mlist1))<len(mlist1):
        print("该列表中有字符串重复")
    #查看重复字符串的名称和重复次数
    for i in set(mlist1):
        if mlist1.count(i)>=2:
            print("{0}是重复字符串，重复次数是{1}次".format(i,mlist1.count(i)))
    #将去重后的字符串作为字典的键和值
    for i in set(mlist1):
        mdic[i] = i

    print(mdic)