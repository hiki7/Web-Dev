def make_chocolate(small, big, goal):
  max_big_bars = goal // 5

  used_big_bars = min(max_big_bars, big)

  remaining_goal = goal - (used_big_bars * 5)
  
  if remaining_goal <= small:
    return remaining_goal
  else:
    return -1
