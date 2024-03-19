def round_sum(a, b, c):
  sum = 0
  nums = [a, b, c]
  
  for i in range(len(nums)):
    sum += round10(nums[i])
  
  return sum

def round10(num):
  rem = num % 10
  
  if rem >= 5:
    return num + (10 - rem)
  else:
    return num - rem
