#定义的函数当v等于0时抛出异常
def fun(v):
    if v==0:
        raise  Exception("GOOD")
try:
    fun(0)
except Exception as a:
    print("except->{0}".format(a))
    pass
print("good")