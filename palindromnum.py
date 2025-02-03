num=int(input("enter number:"))
reverse=0
nmb=num
while num>0:
    n=num%10
    reverse=(reverse*10)+n
    num=num//10
print(reverse)
if nmb==reverse:
    print("palindrome")
else:
    print(" not palindrome")
