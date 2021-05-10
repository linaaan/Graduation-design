import matplotlib.pyplot as plt


# SBS1 101,101 SBS2 101,301 SBS3 301,101 MBS 301,301

def map():
    # 地图
    plt.xlim(0, 400)
    plt.ylim(0, 400)
    # 垂直
    plt.axvline(0)
    plt.axvline(100)
    plt.axvline(200)
    plt.axvline(300)
    # 水平
    plt.axhline(0)
    plt.axhline(100)
    plt.axhline(200)
    plt.axhline(300)

    Xmbs = 260
    Ymbs = 260
    Xsbs1 = 130
    Ysbs1 = 130
    Xsbs2 = 165
    Ysbs2 = 360
    Xsbs3 = 330
    Ysbs3 = 66
    plt.plot(Xmbs, Ymbs, marker=(5, 1), markersize=30)
    plt.plot(Xsbs1, Ysbs1, marker='s', markersize=20)
    plt.plot(Xsbs2, Ysbs2, marker='s', markersize=20)
    plt.plot(Xsbs3, Ysbs3, marker='s', markersize=20)

    return
