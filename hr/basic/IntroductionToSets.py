def average(array):
    disti = set(array)
    lst=list(disti)
    tot=0
    n=0
    for i in lst:
        tot=tot+i
        n=n+1
    avg=tot/n
    return avg






if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)