n=int(input())
transactions=list(map(int,input().split()))
sum=0
for i in transactions:
    if i>=5:
        sum+=i
print(sum)