n=int(input())
dishes=list(map(int,input().split()))
s=sorted(dishes)
sum=s[-1]+s[-2]
print(sum)