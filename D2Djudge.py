import D2DGeneration as D2D
import numpy as np


def judgeIf(i1, i2, i3, m1x, m1y, n1x, n1y, m2x, m2y, n2x, n2y, m3x, m3y, n3x, n3y):  # m1x是前面的车的x n1x是后面的车的x 暂时设置3个D2D
    siteupx = []
    siteupy = []
    sitedownx = []
    sitedowny = []
    j1 = 0
    j2 = 0
    j3 = 0
    l1 = len(m1x)
    l2 = len(m2x)
    l3 = len(m3x)
    if i1 == l1:
        j1 = 'change'
    if i2 == l2:
        j2 = 'change'
    if i3 == l3:
        j3 = 'change'

    if i1 != 0 and i1 != l1:
        siteupx = np.append(siteupx, m1x[i1])
        siteupy = np.append(siteupy, m1y[i1])
        sitedownx = np.append(sitedownx, n1x[i1])
        sitedowny = np.append(sitedowny, n1y[i1])
    if i2 != 0 and i2 != l2:
        siteupx = np.append(siteupx, m2x[i2])
        siteupy = np.append(siteupy, m2y[i2])
        sitedownx = np.append(sitedownx, n2x[i2])
        sitedowny = np.append(sitedowny, n2y[i2])
    if i3 != 0 and i3 != l3:
        siteupx = np.append(siteupx, m3x[i3])
        siteupy = np.append(siteupy, m3y[i3])
        sitedownx = np.append(sitedownx, n3x[i3])
        sitedowny = np.append(sitedowny, n3y[i3])

    return j1, j2, j3, siteupx, siteupy, sitedownx, sitedowny


def d2dju(v, n):  # 速度和跑的轮次，返回的是一个所有的数组
    x11, y11, x12, y12 = D2D.GeD2D(v, n)
    x21, y21, x22, y22 = D2D.GeD2D(v, n)
    x31, y31, x32, y32 = D2D.GeD2D(v, n)
    le1 = 0
    le2 = 0
    le3 = 0
    b = 0
    for b in range(n):
        le1 += len(x11[b])
        le2 += len(x21[b])
        le3 += len(x31[b])
    le = min(le1, le2, le3)
    i = 0
    i1 = 0
    i2 = 0
    i3 = 0
    j1 = 0
    j2 = 0
    j3 = 0
    siteall = []
    while i < le:
        k1, k2, k3, s11, s12, s21, s22 = judgeIf(i1, i2, i3, x11[j1], y11[j1], x12[j1], y12[j1], x21[j2], y21[j2], x22[j2], y22[j2], x31[j3], y31[j3], x32[j3], y32[j3])
        ll1 = len(x11[j1])
        ll2 = len(x21[j2])
        ll3 = len(x31[j3])
        a = {}
        a['time'] = i
        a['up1x'] = s11
        a['up1y'] = s12
        a['down2x'] = s21
        a['down2y'] = s22
        siteall = np.append(siteall, a)
        if k1 == 'change':
            j1 += 1
            i1 -= ll1
        else:
            i1 += 1
        if k2 == 'change':
            j2 += 1
            i2 -= ll2
        else:
            i2 += 1
        if k3 == 'change':
            j3 += 1
            i3 -= ll3
        else:
            i3 += 1
        i += 1
    return siteall



# print(a[3]['up1x'][0])  # 输出是单个数字
# a = d2dju(10, 3)
# b = len(a[3]['up1x'])
# print(b)

# b = judgeIf(dd, x1[0])
# if c:
#     print('ture')
# elif b:
#     print('ture')
# else:
#     print('false')
