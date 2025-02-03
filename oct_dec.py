num = int(input("Enter number: "))
base=1
rem=0
while num>0:
    n=num%10
    rem=rem+n*base
    num=num//10
    base=base*8
print(rem)
