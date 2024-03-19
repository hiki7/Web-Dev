def sum13(nums):
  sum = 0
  
  skip = False
  
  for i in range(len(nums)):
    if skip:
      skip = False
      continue
    if nums[i] == 13:
      skip = True
      continue
    
    sum += nums[i]
  
  return sum
