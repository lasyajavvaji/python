'''It checks for duplicate values in list in one element is repeated more than once it print's true otherwise it prints false'''
nums=list(map(int,input().split()))
res=set()
for i in nums:
    if i in res:
        continue
    else:
        res.add(i)
if len(res)==len(nums):
    print("False")
else:
    print("True")

'''Here we used set because set doesn't contain any duplicate value'''