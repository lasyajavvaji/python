def sum(n):
    m=2
    while True:
        x=n*m
        su=count(x)
        if su==n:
           return x
        m+=1

def count(x):
    total=0
    for digit in str(x):
        total+=int(digit)
    return total
    

n=int(input())
print(sum(n))