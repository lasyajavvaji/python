def marks(n,k,l1,l2):
    c=0
    for i in l1:
        for j in l2:
            if j<=i:
                c+=1
    return c
n=int(input())
l1=list(map(int,input().split()))
k=int(input())
l2=list(map(int,input().split()))
print(marks(n,k,l1,l2))