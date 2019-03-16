print("输入两个数，计算除法")
print("输入q退出")
while True:
    print("\t")
    fnum = input("First number:")
    if fnum=="q":
        break
    snum = input("Second number:")
    if snum=="q":
        break
    #捕获异常，如果发生则进入异常的分支代码块
    try:
        res = int(fnum)/int(snum)
    #异常分支代码块
    #在代码中处理异常
    #注意此处的代码只有一个pass
    #表示什么都不做
    except ZeroDivisionError as e:
        pass
    #如果么有发生异常，则执行这段代码
    else:
        print("result ={0}".format(res))
    finally:
        #print("在这里处理一些收尾工作")
        pass