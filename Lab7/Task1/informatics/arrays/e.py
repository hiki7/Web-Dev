n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    arr.append(x)

for i in range(1, n):
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0) :
        print("YES")
        break
else:
    print("NO")

# Alternative solution:
# for i in range(1, n):
#     if arr[i] * arr[i - 1] > 0:
#         print("YES")
#         break 
# else:
#     print("NO") 
