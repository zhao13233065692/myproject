import random
def huiwen():
    num = input("请输入一个字符串")
    num1 =[i for i in num]
    num2 =num1

    num1.reverse()
    if num.isdigit():
        if  len(num1)%2==1:


            if num1==num2:
                print("这是一个回文数")
            else:
                print("这不是一个回文数")
        else:
            print("这不是回文数")
    else:
        print("这不是数字")
