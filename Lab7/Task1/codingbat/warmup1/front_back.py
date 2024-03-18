def front_back(str):
  if len(str) >= 2:
        first_char = str[0]
        last_char = str[-1]

        new_str = last_char + str[1:-1] + first_char
        return new_str
  else:
        return str
