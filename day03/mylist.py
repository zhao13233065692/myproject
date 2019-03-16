if __name__ == '__main__':
    klist = [
    "good ","good ","study",
    " good ","good","study ",
    "good "," good"," study",
    " good ","good"," study ",
    "good ","good ","study",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
         ]
    kset = set(klist)
    for i in kset:
        if klist.count(i)>=2:
            print("重复字符{0},出现次数是{1}".format(i,klist.count(i)))
    if len(klist)>len(kset):
        print("字符有重复")
    print(kset)
    #把列表字符串去空格放入新列表
    ss = [i.strip() for i in klist]
    #把新列表放入集合去重
    ss1 = set(ss)
    #遍历放入字典
    div={}
    for i in ss1:
        num=ss.count(i)
        div.setdefault(i,num)
    print(div)