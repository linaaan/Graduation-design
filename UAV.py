import numpy as np
import math


xs = 101
ys = 101


def UavNode(xs, ys, t, n):
    # xs ys是旋转圆点坐标 t是采集时间,就是采集等于50*t n 是旋转圈数
    r = 50
    L = 2*np.pi*r
    t1 = L/50*t
    t1 = round(t1)  # 四舍五入取整
    angle = 2*np.pi/t1
    x = []
    y = []
    x2 = []
    y2 = []
    i = 0
    j = 0
    for i in range(t1):
        x1 = xs+r*math.cos(angle*i)
        y1 = ys+r*math.sin(angle*i)
        x2 = np.append(x2, x1)
        y2 = np.append(y2, y1)
    for j in range(n):
        x = np.append(x, x2)
        y = np.append(y, y2)
    return x, y


# Uavx, Uavy = UavNode(xs, ys, 1, 2)
# # print(len(xx))
# print('Uavx:', Uavx)
# print('Uavy:', Uavy)
