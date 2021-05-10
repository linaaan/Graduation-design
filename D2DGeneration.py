import GenerationNode as GN
import RandomInitialPoint as RI

# 产生相同轨迹的D2D通信用户，v是速度或者t*v，即每次移动的距离，n1是一对D2D用户重复运动多少次，进进出出多少次


def GeD2D(v, n1):
    lc = 0
    x = []
    y = []
    x3 = []
    y3 = []
    for lc in range(n1):
        x1, y1 = RI.InitialPoint(v)
        x1, y1 = GN.Generation(x1, y1, v)
        x.append(x1)
        y.append(y1)
        num = len(x1)
        i = 0
        x2 = [0]
        y2 = [0]
        for i in range(num):
            x2.append(x1[i])
            y2.append(y1[i])
        x3.append(x2)
        y3.append(y2)
    return(x, y, x3, y3)

# aa, bb, tt, uu = GeD2D(10, 2)
# print(aa[0])
# print(tt[0])
# 输出数据为x[[1,2,3][1,2,3]]y[[1,2,3][1,2,3]] tt[0][0]输出第一个数组的第一个 x是跑在前面的车 x3是跑在后面的车
