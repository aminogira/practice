

# nn = int(input())
# line = input()
# list = [int(x) for x in line.split()]
# t = tuple(list)
#
# print(t)
#
# print(hash(t))

l=[1,2]
t=(1,2)

print(hash(t))
print(hash((1,2)))

print(hash(hash((1,2))))


def solve(tt):
   return hash(tt)

tt = (2,4,5,6,7,8)
print(solve(tt))


#3713081631934410656