choco=[4,5,0,1,9,0,5,0]
non=[]
zeros=[]
for i in choco:
    if i!=0:
        non.append(i)
    else:
        zeros.append(i)
ans=non+zeros
print(ans)

