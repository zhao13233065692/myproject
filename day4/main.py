import day4.quest1.p1 as c1
import day4.quest1.p2 as b1
import day4.quest1.p3 as e1
import day4.quest1.p4 as h1
if __name__ == '__main__':
    mdict = {
        1:"1:输入用户姓名及性别",
        2:"2:随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"3:输入一个邮箱判断是否合法",
        4:"4:输入一行字符串，判断是否是回文数",
        5:"5:退出",
             }
    for v in mdict.values():
        print(v)
    while True:
        num = input("请输入编号")
        nu =int(num)
        if nu==1:
            c1.checksex()
            continue
        elif nu==2:
            b1.binji()
        elif nu==3:
            e1.email()
        elif nu==4:
            h1.huiwen()
        elif nu==5:
            break
