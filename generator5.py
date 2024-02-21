n = int(input())

def fromnto0(n):
    for i in range(n+1):
        yield n - i

w = fromnto0(n)
for i in w:
    print(i)