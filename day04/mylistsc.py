if __name__ == '__main__':
    #把两个字符串进行全排列
    mlist = [m+n for m in 'abc' for n in 'xyz']
    print(mlist)

    #遍历键值对
    ndict = {"x":"a","y":"b","z":"c"}
    for i,j in ndict.items():
        print(i,"=",j)
