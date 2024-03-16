v = int(input("v: "))
t = int(input("t: "))
s = 109

temp = v * t
position = temp % s

if position < 0:
    position += 109

print(position)