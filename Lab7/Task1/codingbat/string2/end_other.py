def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  return a[-len(b):] == b or b[-len(a):] == a
  
# Alternative solution
# def end_other(a, b):
#   a = a.lower()
#   b = b.lower()
#   return (b.endswith(a) or a.endswith(b))