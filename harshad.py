num=int(input("enter number:"))
nmb=num
n=str(num)
sum=0
for char in n:
    nt=int(char)
    sum+=nt
if nmb%sum==0:
    print("true")
else:
    print("false")
