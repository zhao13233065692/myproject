#创建一个类
#这个类是继承自Exception(所有异常的父类）
#这个类扩展了一个方法show

class myexcept(Exception):
    pass
    def show(self):
        print("hehe")
if __name__ == '__main__':
    #创建一个对象
    me = myexcept()
    #调用对象方法
    me.show()
    try:
        #手动抛出自定义异常
        raise myexcept
    except myexcept as a:
        print("raise myexception")
        #调用了自定义异常的扩展了的方法
        a.show()