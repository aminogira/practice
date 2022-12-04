from itertools import product
A=[]
B=[]
A = input().split(' ')
B = input().split(' ')
for i in range(0, len(A)):
    A[i] = int(A[i])
for i in range(0, len(B)):
    B[i] = int(B[i])
P = [A, B]
lll=list(product(*P))
for z in lll:
    print(z, end= " ")




