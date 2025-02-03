n=int(input("size of list"))
cost_10=int(input())
cost_01=int(input())
num=list(map(int,input().split()))
count0=0
count1=0
for i in num:
    if i==0:
        count0=count0+1
    else:
        count1=count1+1
mul0=count0*cost_01
mul1=count1*cost_10
if mul0>mul1:
    print(mul1)
else:
    print(mul0)
