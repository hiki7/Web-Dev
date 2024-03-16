x = int(input())

sum = 0

while x > 0:
    digit = x % 10
    sum += digit
    x //= 10
    
print(sum)
