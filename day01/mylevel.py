if __name__ == '__main__':
    score = input("请输入你的成绩：")
    mscore = int(score)
    if mscore<=100 and mscore>=0:
        if mscore >=90:
            print("你是优秀的")
        elif mscore >=80:
            print("你很不错的")
        elif mscore >=70:
            print("你还可以的")
        elif mscore >=60:
            print("继续加油")
        else:
            print("有点菜菜的")
