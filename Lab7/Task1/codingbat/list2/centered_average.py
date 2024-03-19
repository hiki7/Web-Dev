def centered_average(nums):
  max_value = max(nums)
  min_value = min(nums)
  
  nums.remove(max_value)
  nums.remove(min_value)
  
  return sum(nums) / len(nums)
    
