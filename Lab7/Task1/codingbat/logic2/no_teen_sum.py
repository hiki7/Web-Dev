def no_teen_sum(a, b, c):
  nums = [a, b, c]
  sum = 0
  
  for i in range(len(nums)):
    sum += fix_teen(nums[i])
  
  return sum

def fix_teen(n):
  if n >= 13 and n <= 19:
    if n == 15 or n == 16:
      return n
    return 0
  return n
