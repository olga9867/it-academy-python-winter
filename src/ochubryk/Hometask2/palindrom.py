number = int(input())
temp = number
result = 0
i = 0

while temp != 0:
    n = int(temp % (10 ** (i + 1)))
    num = int(n / (10 ** i))
    temp = temp - n
    result = result * 10 + num
    i += 1

if number == result:
    print("Число является палиндромом")
else:
    print("Число НЕ является палиндромом")
