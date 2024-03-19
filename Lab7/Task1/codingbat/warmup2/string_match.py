def string_match(a, b):
  shorter_string = min(len(a), len(b))
  count = 0
  
  for i in range(shorter_string - 1):
    a_substr = a[i:i+2]
    b_substr = b[i:i+2]
    
    if a_substr == b_substr:
      count += 1
      
  return count
