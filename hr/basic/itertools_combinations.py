
from itertools import combinations


inList = []
inList = input().split(' ')
word=inList[0]
maxLen = int(inList[1])
word =''.join(sorted(word))
lll = list(combinations(word, 1))
lll.sort()
for x in range(2, maxLen+1):
    ll=list(combinations(word, x))
    ll.sort()
    for w in ll:
        lll.append(w)


for z in lll:
    print(''.join(z))

# >>> from itertools import combinations
# >>>
# >>> print (list(combinations('12345',2)))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
# >>>
# >>> A = [1,1,3,3,3]
# >>> print (list(combinations(A,4)))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
