a=input()
c=0
while True:
    c+=1
    rev=a[::-1]
    add=int(a)+int(rev)
    add1=str(add)
    if add1==add1[::-1]:
        print("palindrom",add1)
        print(c)
        break
    else:
        a=add1
    



