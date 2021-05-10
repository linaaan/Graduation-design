import numpy as np
import random
import math


def GenerationW(x1, y1, p):
    m = len(x1)
    j = 1
    zh = 100/3
    while j == 1:  # 产生移动节点

        if math.ceil(x1[-1]/zh) == 3 and math.ceil(y1[-1]/zh) == 3:  # (3,3)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                else:
                    # right
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])  # 向下走，注意m
                    break
                else:
                    # right
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走,注意m
                    break

        if math.ceil(x1[-1]/zh) == 3 and math.ceil(y1[-1]/zh) == 6:  # (3,6)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                else:
                    # right
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])  # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break

        if math.ceil(x1[-1]/zh) == 3 and math.ceil(y1[-1]/zh) == 9:  # (3,9)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                else:
                    # right
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                else:
                    # right
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 100)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(0, 100, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break

        if math.ceil(x1[-1]/zh) == 6 and math.ceil(y1[-1]/zh) == 9:  # (6,9)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                else:
                    # right
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if math.ceil(x1[-1]/zh) == 6 and math.ceil(y1[-1]/zh) == 6:  # (6,6)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if math.ceil(x1[-1]/zh) == 6 and math.ceil(y1[-1]/zh) == 3:  # (6,3)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 200)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                else:
                    # right
                    x2 = np.arange(100, 200, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if math.ceil(x1[-1]/zh) == 9 and math.ceil(y1[-1]/zh) == 3:  # (9,3)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                else:
                    # right
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(0, 100, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                else:
                    # right
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 100)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if math.ceil(x1[-1]/zh) == 9 and math.ceil(y1[-1]/zh) == 6:  # (9,6)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                else:
                    # right
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(100, 200, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 200)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if math.ceil(x1[-1]/zh) == 9 and math.ceil(y1[-1]/zh) == 9:  # (9,9)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                else:
                    # right
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(300, 400, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                else:
                    # right
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(300, 400, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(200, 300, p)
                    for i in range(m):
                        x1 = np.append(x1, 300)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(200, 300, p)
                    for i in range(m):
                        y1 = np.append(y1, 300)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
    return(x1, y1)



def GenerationCeshi(x1, y1):
    m = len(x1)-1
    j = 1
    while j == 1:  # 产生移动节点

        if x1[-1] == 3 and y1[-1] == 3:  # (3,3)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                else:
                    # right
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])  # 向下走，注意m
                    break
                else:
                    # right
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走,注意m
                    break

        if x1[-1] == 3 and y1[-1] == 6:  # (3,6)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                else:
                    # right
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])  # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break

        if x1[-1] == 3 and y1[-1] == 9:  # (3,9)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                else:
                    # right
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                else:
                    # right
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(4, 7)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 3)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(0, 3)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                    break

        if x1[-1] == 6 and y1[-1] == 9:  # (6,9)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                else:
                    # right
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if x1[-1] == 6 and y1[-1] == 6:  # (6,6)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if x1[-1] == 6 and y1[-1] == 3:  # (6,3)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走
                else:
                    # right
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(7, 10)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走
                elif r > 1:
                    # straight
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 6)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                else:
                    # right
                    x2 = np.arange(3, 6)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if x1[-1] == 9 and y1[-1] == 3:  # (9,3)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                else:
                    # right
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(4, 7)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(0, 3)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                    break
                else:
                    # right
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 3)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if x1[-1] == 9 and y1[-1] == 6:  # (9,6)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走
                elif r > 1:
                    # straight
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                else:
                    # right
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(7, 10)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走
                else:
                    # right
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(3, 6)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 6)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m

        if x1[-1] == 9 and y1[-1] == 9:  # (9,9)

            if x1[-1] > x1[-2] and y1[-1] == y1[-2]:  # 由左到右
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                elif r > 1:
                    # straight
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                else:
                    # right
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m

            elif x1[-1] < x1[-2] and y1[-1] == y1[-2]:  # 由右到左
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                elif r > 1:
                    # straight
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                else:
                    # right
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break

            elif x1[-1] == x1[-2] and y1[-1] > y1[-2]:  # 由下到上
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
                elif r > 1:
                    # straight
                    y2 = np.arange(10, 13)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[i])  # 向上走
                    break
                else:
                    # right
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break

            elif x1[-1] == x1[-2] and y1[-1] < y1[-2]:  # 由上到下
                r = random.randint(0, 9)
                i = 0
                if r < 1:
                    # left
                    x2 = np.arange(10, 13)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[i])  # 向右走
                    break
                elif r > 1:
                    # straight
                    y2 = np.arange(6, 9)
                    for i in range(m):
                        x1 = np.append(x1, 9)
                        y1 = np.append(y1, y2[m-1-i])   # 向下走，注意m
                else:
                    # right
                    x2 = np.arange(6, 9)
                    for i in range(m):
                        y1 = np.append(y1, 9)
                        x1 = np.append(x1, x2[m-1-i])  # 向左走，注意m
    return(x1, y1)
