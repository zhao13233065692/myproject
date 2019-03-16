if __name__ == '__main__':
    #捕获异常代码
    try:
        print(5/" ")
    #捕获对应的异常
    #给异常起别名
    except TypeError as a:
        pass
        print("TypeError")
        print(a)
