if __name__ == '__main__':
    print("输入两个数，计算除法")
    print("输入q退出")
    while True:
        print("\t")
        num1 = input("First Number")
        if num1=="q":
            break
        num2 = input("Second Number")
        if num2=="q":
            break
        try:
            resu = int(num1) / int(num2)
        except ZeroDivisionError as a:
            print("division error")
        else:
            print("result = {0}".format(resu))
