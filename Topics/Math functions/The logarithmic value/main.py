from math import log
x, y = int(input()), int(input())
print(round(log(x), 2) if y <= 0 or y == 1 else round(log(x, y), 2))
