s1=input().upper()
s2=input().upper()
l1=list(s1)
l2=list(s2)
str=""
for i in l1:
    if i not in l2:
        str=str+i
if str=="":
    print("empty")
else:
    print(str)

