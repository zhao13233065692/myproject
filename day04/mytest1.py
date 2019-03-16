if __name__ == '__main__':
    #提示输入
    age1 = input("请输入第一个人的年龄")
    age2 = input("请输入第二个人的年龄")
    #判断两人年龄的大小
    if int(age1)>int(age2):
        print("第一个人的年龄大")
    elif int(age1)<int(age2):
        print("第二个人的年龄大")
    else:
        print("两个人一样大")