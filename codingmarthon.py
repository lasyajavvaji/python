lenght=int(input())
scores=list(map(int,input().split()))
scores.sort(reverse=True)
sum=0
for i in scores[:lenght:]:
    sum+=i
print(sum)

