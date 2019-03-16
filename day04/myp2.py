if __name__ == '__main__':
    name = input("请输入用户名")
    pwd = input("请输入密码")
    n="*".find(name)
    m=name.find("!")
    x=name.find("-")
    n1 = pwd.find("*")
    m1= pwd.find("!")
    x1 = pwd.find("-")
    if n==-1 and m==-1 and x==-1:
        if name.isalnum() and len(name)>=6 and len(name)<=16:
            print("用户名合法")
        else:
            print("用户名不合法")

    else:
        print("用户名含有非法字符")
    if n1==-1 or m1==-1 or x1==-1:
        if pwd.isalnum() and len(pwd)>=6 and len(pwd)<=16:
            print("密码合法")
        else:
            print("密码不合法")

    else:
        print("密码含有非法字符")