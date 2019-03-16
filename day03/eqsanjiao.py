def sanjiao(num):
    for i in range(1,num+1):
        for j in  range(num,0,-1):
            print("*",end=" ")
            if i==j:
                print()
                break
def chengfa(num):
    for i in range(1,num+1):
        for j in range(1,num+1):

            print(str(i).ljust(1," "),"*",j,"=",str(i*j).rjust(2," "),end="  ")
            if i==j:
                print(" ")
                break
def shushu(num):
    for i in range(1,101):
        print(str(i).rjust(3, " "), end=" ")
        if i%10==0:
            print()