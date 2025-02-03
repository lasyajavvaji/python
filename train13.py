def is_prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
        else:
            return True
def sum(x):
    s=0
    for i in range(2,x+1):
        if is_prime(i):
            s=s+i
    return s


x=int(input())
print(sum(x))