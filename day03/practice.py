if __name__ == '__main__':
    L=["hello","world","BIM","Apple"]
    mlist=[i.lower() for i in L]
    print(mlist)
    L1 = ["hello",12.5,"world",3,"BIM",2.0,"Apple"]
    L2 =[i for i in L1 if isinstance(i,str)]
    mlist1 =[i.lower() for i in L2]
    print(mlist1)
    alist = list(range(1,11))
    blist =[]

    for i in alist:
        blist.append(i**2)
    print(blist)

    slist = ["张三","李四","王五","赵六"]
    nlist = [str(i)+j for i in alist if i % 2 == 0 for j in slist]
    print(nlist)
    xlist =[]
    for i in alist:
        if i%2==0:
            for j in slist:
                xlist.append(str(i)+j)
    print(xlist)