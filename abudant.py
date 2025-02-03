def fact(st):
    if st==1:
        return 1
    return st*fact(st-1)
num=int(input("enter number:"))
nmb=num
sum=0
n=str(num)
for char in n:
    st=int(char)
    f=fact(st)
    sum+=f
print(sum)
