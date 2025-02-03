n=int(input())
stairs=list(map(int,input().split()))
for i in stairs:
    if i%3==0:
        continue
    else:
        modulus=i%3
        if modulus==2:
            print("add 1 stair")
        else:
            print("remove 1 stair")