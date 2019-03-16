if __name__ == '__main__':
    mst = "u can up no zuo no dead"
    mm = mst.strip()
    print(mm)
    #只能去掉每个字符串前后的空格
    print(mm.isalnum())
    mbool = mst.startswith("u")
    print(mbool)
    ebool = mst.endswith("d")
    print(ebool)
    st ="uon io"
    nst = st.ljust(10,"*")
    print(nst)
    s = st.center(20,"-")
    print(s)
    ss = mst.partition(",")
    print("ss={0}".format(ss))
