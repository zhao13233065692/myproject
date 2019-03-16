if __name__ == '__main__':
    mfile = open(r"d:\a.txt")
    with mfile as a:
        mlist = a.readlines()
        print(a.readable())
        print(a.writable())
    print(mlist)
    with open(r"f:家和.txt","w") as a :
        mlist =["青青河水，蓝蓝的天\n我的家乡在天边"]
        a.writelines(mlist)