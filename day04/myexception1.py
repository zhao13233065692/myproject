if __name__ == '__main__':
    try:
        f = open("good.text","r")
        f.close()
    except Exception as e:
        print(e)
    else:
        print("excetion else")
    finally:
        print("finally")