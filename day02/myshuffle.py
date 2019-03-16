import  random
if __name__ == '__main__':
    st =input("请输入数字")
    mynum = [i for i in st]
    random.shuffle(mynum)
    print(mynum)
    mynum.sort()
    print(mynum)
    mynum.sort(reverse=True)
    print("翻转之后的列表为:{0}".format(mynum))