if __name__ == '__main__':
    mlist1=[]
    mlist = list()
    # print(type(mlist))
    # print(type(mlist1))

    #使用append在列表尾部添加
    mlist.append("haohaoxuexi")
    print(mlist)
    # 使用insert在列表指定位置添加
    mlist.insert(0,"口号：")
    print(mlist)

    val=mlist.pop()
    print("mlist.pop={val}".format(val=val))
    #mlist.remove("口号：")
    # print(mlist)
    # del mlist
    #
    # print(mlist)
    l=mlist.clear()
    print(l)