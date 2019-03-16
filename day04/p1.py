if __name__ == '__main__':
    mlist = ["zhang","wang","li","zhao","qian","sun","zhao"]
    i=1
    print(len(mlist))

    while i < len(mlist):
        j = 0
        temp = ""
        while j < len(mlist)-i:
            if len(mlist[j]) >= len(mlist[j+1]):
                temp = mlist[j]
                mlist[j] = mlist[j+1]
                mlist[j+1] = temp
                j += 1

            i += 1
            i = 0
    while i < len(mlist):
        print(mlist[i])
        i += 1