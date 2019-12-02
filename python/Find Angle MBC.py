import math
AB = input()
BC = input()
deg = math.degrees(math.atan2(float(AB), float(BC)))
print(str(round(deg))+"°")