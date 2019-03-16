#自定义异常类
#该定义异常类是ValueError的子类
# 类中没有任何有效的代码，仅有一个占位有的pass
class xException(ValueError):
    pass
try:
    print("before raise xexception")
    #手动抛出异常
    # 注意 抛出的是自定义的异常
    raise xException
    print("After raise xexception")
except xException as a:
    print("catch exception")
#捕获自定义异常的父类
except ValueError as ve:
    print("catch valueError")
#捕获所以异常的父类
except Exception as e:
    print("exception")
    print(e)
else:
    print("try except else")
finally:
    print("finally")
if __name__ == '__main__':
    st=["aa\n","bb\n","cc\n"]
    s=[i.strip("\n") for i in st]
    print(st)
    print(s)