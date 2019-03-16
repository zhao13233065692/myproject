def checksex():
    name = input("请输入名字")
    sex = input("请输入性别")
    mdic = {"男":"yes","man":"yes","女":"no","felman":"no"}
    for k in mdic.keys():
        if sex=="男" or sex== "man":
            print("欢迎{0}先生".format(name))
            break
        elif sex=="女" or sex== "felman":
            print("欢迎{0}女士".format(name))
            break
        else:
            print("输入错误")
            break