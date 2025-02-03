num=int(input("enter number:"))
num1=int(input("enter another number:"))
l=[]
for i in range (num,num1,1):
    count=0
    for j in range(1,i+1,1):
        if(i%j==0):
            count+=1
    if count==2:
        l.append(i)
print(l)
            
 