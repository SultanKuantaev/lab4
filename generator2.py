n = int(input())

def even_to_n(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
evens = even_to_n(n)
for i in evens:
    print(i)