def make_bricks(small, big, goal):
  total = small + big * 5
  return total >= goal and goal % 5 <= small
