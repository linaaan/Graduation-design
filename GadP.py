'''
Ag 为发送/接收天线增益(dbi)  ple为路径损失幂指数
slsd 为阴影损失标准差
Pr 为接收功率 d为接受和发送天线的距离
h 为天线高度(m) 认为接收和发送的天线高度相同
wlps 为传播信号的波长(m)
refr 为反射率 plf 路径损耗因子,一般为3到5
Pt 发射功率(dbm)    区分手机和基站？
工作频率1900Mhz
移动节点发送功率 24dbm 0.25w 中继微基站30dbm 1w 宏基站46dbm 40w
热噪声-174dbm
'''
import numpy as np
import math


def uAbU(dis):
    # ue和基站的上行链路增益
    Ag = 17
    ple = 3
    slsd = 7
    Pt = 0.25  # w
    h = 35
    refr = 0.3
    plf = 5
    wlps = 0.16
    Pt = 10

    Pr = (Pt/((4*(np.pi**2))*((dis/wlps)**plf)))*(1+refr**2+2*refr*math.cos(4*np.pi*(h**2)/(dis*wlps)))
    G = math.sqrt(Pr/(Pt*Ag*(dis**(-ple))*(10**(-slsd/10))))
    return G


def uAbD(dis):
    # ue和基站的下行链路增益
    Ag = 17
    ple = 3
    slsd = 7
    Pt = 1
    h = 35
    refr = 0.3
    plf = 5
    wlps = 0.16
    Pt = 10

    Pr = (Pt/((4*(np.pi**2))*((dis/wlps)**plf)))*(1+refr**2+2*refr*math.cos(4*np.pi*(h**2)/(dis*wlps)))
    G = math.sqrt(Pr/(Pt*Ag*(dis**(-ple))*(10**(-slsd/10))))
    return G


def uAd(dis):
    # ue和D2D之间的链路增益，上下行相同，只是距离不同，分别和两个D2D节点进行处理
    Ag = 17
    ple = 3
    slsd = 7
    Pt = 0.25
    h = 35
    refr = 0.3
    plf = 5
    wlps = 0.16
    Pt = 10

    Pr = (Pt/((4*(np.pi**2))*((dis/wlps)**plf)))*(1+refr**2+2*refr*math.cos(4*np.pi*(h**2)/(dis*wlps)))
    G = math.sqrt(Pr/(Pt*Ag*(dis**(-ple))*(10**(-slsd/10))))
    return G


def bABu(dis):
    # sbs和mbs之间的上行增益
    Ag = 17
    ple = 3
    slsd = 7
    Pt = 1
    h = 35
    refr = 0.3
    plf = 5
    wlps = 0.16
    Pt = 10

    Pr = (Pt/((4*(np.pi**2))*((dis/wlps)**plf)))*(1+refr**2+2*refr*math.cos(4*np.pi*(h**2)/(dis*wlps)))
    G = math.sqrt(Pr/(Pt*Ag*(dis**(-ple))*(10**(-slsd/10))))
    return G


def bABd(dis):
    # sbs和mbs之间的下行链路增益
    Ag = 17
    ple = 3
    slsd = 7
    Pt = 40
    h = 35
    refr = 0.3
    plf = 5
    wlps = 0.16
    Pt = 10

    Pr = (Pt/((4*(np.pi**2))*((dis/wlps)**plf)))*(1+refr**2+2*refr*math.cos(4*np.pi*(h**2)/(dis*wlps)))
    G = math.sqrt(Pr/(Pt*Ag*(dis**(-ple))*(10**(-slsd/10))))
    return G


def MLD(dis):
    #  各种链路和mbs之间的下行链路增益
    Ag = 17
    ple = 3
    slsd = 7
    Pt = 40
    h = 35
    refr = 0.3
    plf = 5
    wlps = 0.16
    Pt = 10

    Pr = (Pt/((4*(np.pi**2))*((dis/wlps)**plf)))*(1+refr**2+2*refr*math.cos(4*np.pi*(h**2)/(dis*wlps)))
    G = math.sqrt(Pr/(Pt*Ag*(dis**(-ple))*(10**(-slsd/10))))
    return G


def MLU(dis):
    # 各种链路和mbs之间的上行链路增益
    Ag = 17
    ple = 3
    slsd = 7
    Pt = 1
    h = 35
    refr = 0.3
    plf = 5
    wlps = 0.16
    Pt = 10

    Pr = (Pt/((4*(np.pi**2))*((dis/wlps)**plf)))*(1+refr**2+2*refr*math.cos(4*np.pi*(h**2)/(dis*wlps)))
    G = math.sqrt(Pr/(Pt*Ag*(dis**(-ple))*(10**(-slsd/10))))
    return G


# print(Pr)
# print(G)
# print(s)
