n = int(input())
arr = []
count = 0

for _ in range(n):
    x = int(input())
    arr.append(x)

for i in range(1, n-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        count += 1

print(count)