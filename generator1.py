n = int(input())

def square(n):
    n2 = 1
    while( n2 < n):
        yield n2*n2
        n2 += 1
        if (n2*n2) >= n:
            break


square1 = square(n)

for i in square1:
    print(i)