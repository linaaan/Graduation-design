import math

# 对产生的移动节点求与基站的距离，并判断是否在基站的小区内，哪个小区
# x1, y1 = RI.InitialPoint(10)
# x1, y1 = GN.Generation(x1, y1, 10)


def distAwiB(x, y):
    fenAd = []
    i = 0
    length1 = len(x)
    for i in range(length1):
        qwer1 = math.sqrt(((x[i]-101)**2+(y[i]-101)**2))
        qwer2 = math.sqrt(((x[i]-101)**2+(y[i]-301)**2))
        qwer3 = math.sqrt(((x[i]-301)**2+(y[i]-101)**2))
        qwer4 = math.sqrt(((x[i]-301)**2+(y[i]-301)**2))
        if qwer1 <= 100:
            a = {}
            a['distance'] = qwer1
            a['MBSdis'] = qwer4
            a['cell'] = 'sbs1'
            fenAd.append(a)
        elif qwer2 <= 100:
            a = {}
            a['distance'] = qwer2
            a['MBSdis'] = qwer4
            a['cell'] = 'sbs2'
            fenAd.append(a)
        elif qwer3 <= 100:
            a = {}
            a['distance'] = qwer3
            a['MBSdis'] = qwer4
            a['cell'] = 'sbs3'
            fenAd.append(a)
        else:
            a = {}
            a['distance'] = qwer4
            a['cell'] = 'other'
            fenAd.append(a)
    return fenAd

# mm = distAwiB(x1, y1)

# if mm[0]['cell'] == 'sbs1': 直接调用字典数据
#     print('在第一个小区里面')
# else:
#     print('在外面')
