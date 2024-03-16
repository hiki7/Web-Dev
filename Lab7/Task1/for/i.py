x = int(input())

divisor = 1
count = 0

while divisor <= x:
    if x % divisor == 0:
        count+=1
    divisor += 1

print(count)