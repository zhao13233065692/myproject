def myfunction(*name):
    print(name)
def myfun(**name):
    print(name)


if __name__ == '__main__':
  myfunction("6","18")
  myfun(name="张三",age=18,sex="男")