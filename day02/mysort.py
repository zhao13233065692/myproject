import random

if __name__ == '__main__':
    mysu=[8,2,5,4,1,6,7]
    mysu.sort()
    print(mysu)
    random.shuffle(mysu)#shuffle 在随机函数中
    print(mysu)
    mysu.reverse()
    print("mysu.reverse={po}".format(po=mysu))

    print(sorted(mysu))
    print(sorted(mysu,reverse=True))