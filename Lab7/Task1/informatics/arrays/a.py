n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    arr.append(x)

for i in range(0, n, 2):
    print(arr[i], end=" ")
