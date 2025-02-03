num=list(map(int,input().split()))
result=[]
for i in range(0,len(num)-1):
    diff=num[i+1]-num[i]
    result.append(diff)
print(result)