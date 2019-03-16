if __name__ == '__main__':
    str = [" a  b  c  d "," bc "," bu "]
    print("未去空格之前={0}".format(str))
    str1 =[i.strip() for i in str]
    print("去空格之后={0}".format(str1))