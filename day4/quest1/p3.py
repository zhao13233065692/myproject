def email():
    email = input("请输入邮箱")
    sts = email.partition("@")
    st = sts[2].partition(".")
    if len(sts[0])>=6:
        if st[2]== "com" or st[2]=="cn":
            print("邮箱格式正确")
        else:
            print("邮箱要以.com或.cn结尾")
    else:
        print("用户名要大于6位")