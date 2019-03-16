


class myexcept(Exception):
    pass
    def show(self):
        print("双击666")
if __name__ == '__main__':
    me = myexcept()
    me.show()
    try:
       raise myexcept
    except myexcept as a:
        a.show()