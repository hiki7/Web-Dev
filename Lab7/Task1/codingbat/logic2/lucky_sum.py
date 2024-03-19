def lucky_sum(a, b, c):
  nums = [a, b, c]
  skip_index = -1
    
  if a == 13:
      return 0
  elif b == 13:
      skip_index = 1
  elif c == 13:
      skip_index = 2

  if skip_index != -1:
        return sum(nums[:skip_index])
  else:
        return sum(nums)
