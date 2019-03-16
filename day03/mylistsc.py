if __name__ == '__main__':
    # mlist = [i for i in range(1,11) if i % 2==0]
    # print(mlist)
    mlist=["a","b","c","d"]
    nlist=list(range(1,5))

    llist = [a+str(b) for a in mlist  for b in nlist if b%2==0]
    print(llist)