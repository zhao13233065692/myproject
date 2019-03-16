if __name__ == '__main__':
    arr1 = [1,2,3,4,5]
    arr = [1,2,3,4,5,6,7,8,9]
    for i in arr1:

            for a in arr[5:0:-1]:
                if i < a:
                    print(" ",end="")

            for b in arr[0:9]:
                    if b <= 2*i-1:
                        print("*",end="")
                    else:
                        print("")
                        break

    print("")
    for i in arr1:

            for a in arr[0:5]:
                if a <=i:
                    print(" ",end="")

            for b in arr[8:0:-1]:
                    if 2*i-1 <= b:
                        print("*",end="")
                    else:
                        print("")
                        break