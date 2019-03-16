def func(*name):
    print(name)
def func1(**name):
    print(name)

if __name__ == '__main__':

    func("吃","喝","完了")
    func1(name="张三",age=18,sex="nan")