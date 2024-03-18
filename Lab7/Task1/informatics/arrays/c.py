n = int(input())
arr = []
count = 0

for _ in range(n):
    x = int(input())
    arr.append(x)

for i in range(0, n):
    if arr[i] > 0:
        count += 1

print(count)