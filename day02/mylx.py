if __name__ == '__main__':
    num = input("请输入菱形的行数")
    num = int(num)
    print(type(num))
    num=num//2
    print(num)
    i = 1
    while i <= num+1:
        j=0
        while j<=num-i:
            print(" ",end="")
            j+=1

        j=0
        while j<2*i-1:
            print("*",end="")
            j+=1
        print()
        i+=1
    i=1
    while i <= num+1:
        j = 1
        while j <= i:
            print(" ", end="")
            j += 1

        j = 2*num
        while j > 2 * i - 1:
            print("*", end="")
            j -= 1
        print()
        i += 1