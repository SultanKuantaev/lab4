n = int(input())

def divisibleby34(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

l34 = divisibleby34(n)
for i in l34:
    print(i)