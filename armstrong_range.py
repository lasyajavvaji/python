num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

for n in range(num1, num2 + 1):
    l = len(str(n))
    temp = n
    arm = 0  # Reset arm for each number
    while temp != 0:
        num = temp % 10
        arm += num ** l
        temp = temp // 10
    if n == arm:
        print(f"{n} is an Armstrong number")
