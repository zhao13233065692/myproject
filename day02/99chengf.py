if __name__ == '__main__':
    s = [1,2,3,4,5,6,7,8,9]
    for i in s:
        for j in s:
            if j<=i:
                s1=str(j * i)
                s1=s1.rjust(2," ")
                num=str(i)+"*"+str(j)+"="+s1
                print(num,end=" ")
            else:
                print(" ")
                break