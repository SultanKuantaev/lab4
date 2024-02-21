a = int(input())
b = int(input())

def square(a,b):
    for i in range(a,b+1):
        
        if i*i > b:
            break
        yield i*i

s = square(a,b)
for i in s:
    print(i)