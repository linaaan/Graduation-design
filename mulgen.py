import RandomInitialPoint as RI
import GenerationNode as GN
import numpy as np


def multgr(n, v):
    # n 是圈数 v是速度
    i = 0
    x = []
    y = []
    for i in range(n):
        x1, y1 = RI.InitialPoint(v)
        x1, y1 = GN.Generation(x1, y1, v)
        x = np.append(x, x1)
        y = np.append(y, y1)
    return(x, y)


# xx, yy = multgr(3, 20)
# print(xx)

# car =  multgr(1, 20)
# print('car:', car)