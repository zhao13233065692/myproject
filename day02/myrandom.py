import random
if __name__ == '__main__':
    num = input("请输入一个数")
    num2 =random.randint(0,50)
    if num2 < int(num):
        print(num,">",num2)
    elif int(num) < num2:
        print(num,"<",num2)
    else:
        print(num,"=",num2)