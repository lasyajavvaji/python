num=int(input("enter number:"))
nmb=num
l=len(str(num))
arm=0
for i in range(l):
    n=int(num%10)
    arm+=n**l
    num=num//10

print(arm)
if nmb==arm:
    print("armstrong")
else:
    print("not armstrong")