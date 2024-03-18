n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    arr.append(x)

for i in range(0, n):
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")