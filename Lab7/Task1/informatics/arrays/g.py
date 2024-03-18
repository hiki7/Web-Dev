n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    arr.append(x)

arr.reverse()

for i in range(n):
    print(arr[i], end=" ")