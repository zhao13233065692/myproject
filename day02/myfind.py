if __name__ == '__main__':
    st="kjljljkjjljljl"
    sd=[i for i in st]
    #num=st.find("good",1)
    #num = st.find("lucky", 1)
    st1=set(st)
    print(st1)
    for i in st1:
        dic={"{0}的次数".format(i):st.count(i)}
        print(dic)

    print(type(True))