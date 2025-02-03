num=int(input("enter number:"))
sum=0
while num>0:
    r=num%10
    sum+=r
    num=int(num/10)
print(sum)