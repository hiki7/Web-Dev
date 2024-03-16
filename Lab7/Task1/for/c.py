a = int(input())
b = int(input())

start = int(a ** 0.5) + 1

end = int(b ** 0.5)

for i in range(start, end + 1):
    print(i ** 2, end=' ')
