x = int(input())

divisor = 1

while divisor <= x:
    if x % divisor == 0:
        print(divisor, end=' ')
    divisor += 1
