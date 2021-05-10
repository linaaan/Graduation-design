import numpy as np
import random

# 随机产生初始点


def InitialPoint(p):
    # p为每步行走的距离
    s = random.randint(0, 11)
    x = np.arange(0, 100, p)
    n = len(x)
    y = [1]*n
    if s == 0:  # (0, 3)
        x = np.arange(0, 100, p)
        y = [100]*n
    elif s == 1:  # (0, 6)
        x = np.arange(0, 100, p)
        y = [200]*n
    elif s == 2:  # (0, 9)
        x = np.arange(0, 100, p)
        y = [300]*n
    elif s == 3:  # (3, 12)
        yk = np.arange(300, 400, p)
        x = [100]*n
        for i in range(n):
            y[i] = yk[n-1-i]
    elif s == 4:  # (6, 12)
        yk = np.arange(300, 400, p)
        x = [200]*n
        for i in range(n):
            y[i] = yk[n-1-i]
    elif s == 5:  # (9, 12)
        yk = np.arange(300, 400, p)
        x = [300]*n
        for i in range(n):
            y[i] = yk[n-1-i]
    elif s == 6:  # (12, 9)
        xk = np.arange(300, 400, p)
        y = [300]*n
        for i in range(n):
            x[i] = xk[n-1-i]
    elif s == 7:  # (12, 6)
        xk = np.arange(300, 400, p)
        y = [200]*n
        for i in range(n):
            x[i] = xk[n-1-i]
    elif s == 8:  # (12, 3)
        xk = np.arange(300, 400, p)
        y = [100]*n
        for i in range(n):
            x[i] = xk[n-1-i]
    elif s == 9:  # (9,0)
        y = np.arange(0, 100, p)
        x = [300]*n
    elif s == 10:  # (6,0)
        y = np.arange(0, 100, p)
        x = [200]*n
    elif s == 11:  # (3,0)
        y = np.arange(0, 100, p)
        x = [100]*n

    return(x, y)


# x1, y1 = InitialPoint()
# print(x1)
# print(y1)
