if __name__ == '__main__':
    st=range(0,101)
    for i in st:
        i=str(i)
        print(i.rjust(3," "),end=" ")
        i=int(i)
        if i%10==9:
            print()
