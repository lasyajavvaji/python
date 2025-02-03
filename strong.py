
def strong(n):
    if n==1 or n==0:
        return 1
    return n*strong(n-1)

nmb=int(input("enter:"))
num=nmb
s=0

while num>0:
    n=num%10
    s+=strong(n)
    num=num//10
if nmb==s:
    print("strong")
else:
    print("not strong")