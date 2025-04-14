str1=input()
lst=list(str1)
lst1=sorted(lst)
count=0
sum=0
for i in lst1:
    for j in lst1:
        if i==j:
            count+=1
            if count%2==0:
                sum+=count
        else:
            break
print(sum)