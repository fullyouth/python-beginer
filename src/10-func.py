# 函数
import math
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-9))

# 空函数
def nop():
    pass

# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return (nx, ny)

(x, y) = move(100, 100, 60, math.pi / 6)
print(x, y)