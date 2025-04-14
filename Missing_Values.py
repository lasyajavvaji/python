'''Finds missing value in given list if list contains 3,0,1 in range of 0 t0 3 the list misses 2 so the output must be 2'''
n=int(input())
nums=list(map(int,input().split()))
num=sorted(nums)
for i in range(0,n+1):
       if i not in nums:
              print(i)
