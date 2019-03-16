if __name__ == '__main__':
    st=input("请输入字符串")

    sd=set(st)
    for i in sd:
        if st.count(i)>=2:
            print("重复字符{0},重复的次数是{1}".format(i,st.count(i)))
    if len(st)>len(sd):
        print("含有重复字符")
