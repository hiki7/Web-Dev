def front_times(str, n):
  front = str[:3]
  new_str = ""
  for _ in range(n):
    new_str += front
  return new_str
