n=int(input())
num=list(map(int,input().split()))
avg=0.0
for i in range(0,n-1):
    avg=(num[i]+num[i+1])/2
    if avg>num[i]:
        num[i]=0
    else:
        num[i+1]=0
        
print(num)
