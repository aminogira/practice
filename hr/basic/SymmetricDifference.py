if __name__ == '__main__':
    m = int(input())
    arrM = list(map(int, input().split()))
    n = int(input())
    arrN = list(map(int, input().split()))

    setM = set(arrM)
    setN = set(arrN)

    dif = setM.difference(setN)
    dif.update(setN.difference(setM))
    lst = list(dif)
    lst.sort()

    for i in lst:
        print(i)

