from itertools import permutations

# >>> from itertools import permutations
# >>> print (permutations(['1','2','3']))
# <itertools.permutations object at 0x02A45210>
# >>>
# >>> print (list(permutations(['1','2','3'])))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
# >>>
# >>> print (list(permutations(['1','2','3'],2)))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# >>>
# >>> print (list(permutations('abc',3)))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]



from itertools import permutations
inList=[]
inList = input().split(' ')

lll=list(permutations(inList[0],int(inList[1])))
lll.sort()
for z in lll:
    print(''.join(z))
