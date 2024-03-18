def find_min (arr):
    return min(arr)

arr = []

for _ in range(4):
    x = int(input())
    arr.append(x)

print(find_min(arr))