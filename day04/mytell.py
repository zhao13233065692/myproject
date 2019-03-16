if __name__ == '__main__':
    f = open(r"d:a.txt","r")

    fd = f.tell()
    print("fd={0}".format(fd))
    f.seek(10,0)

    fd = f.tell()
    print(fd)
    f.seek(10, 0)
    fd = f.tell()
    print(fd)