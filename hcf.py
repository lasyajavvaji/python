num = int(input("Enter number: "))
num1 = int(input("Enter number: "))
hcf=1
for i in range(1,min(num,num1)):
    if num%i==0 and num1%i==0:
        hcf=i
print(hcf)