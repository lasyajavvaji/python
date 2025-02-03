n = int(input())
nums = list(map(int, input().split()))

dict1 = {}
for digit in nums:
    if digit in dict1:
        dict1[digit] += 1
    else:
        dict1[digit] = 1

majority_element = -1
for i, count in dict1.items():
    if count > n // 2:
        majority_element = i
        break

print(majority_element)
