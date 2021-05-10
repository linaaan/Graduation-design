import GadP
import mulgen as mul
import UAV
import numpy as np
import math
import clasidis as cl
import D2Djudge as D2j
import random


class Env_AL_HetNet():
    def __init__(self):
        self.pue = 0.25
        self.psbs = 1
        self.pmbs = 40
        self.Noise = 4**(-21)
        self.B = 10**8
        self.demDarate = 5*10**7
        self.state = None

    def generate_data(self):

        self.xua1, self.yua1 = UAV.UavNode(101, 101, 1, 1500)
        self.xua2, self.yua2 = UAV.UavNode(101, 301, 1, 1500)
        self.xua3, self.yua3 = UAV.UavNode(301, 101, 1, 1500)
        self.d2dsite = D2j.d2dju(10, 1500)
        self.x1, self.y1 = mul.multgr(1500, 10)  # 第一辆汽车
        self.x2, self.y2 = mul.multgr(1500, 10)
        self.x3, self.y3 = mul.multgr(1500, 5)  # 第一个行人
        self.x4, self.y4 = mul.multgr(1500, 5)

        self.d1 = cl.distAwiB(self.x1, self.y1)  # 判断在那个sbs内和距离对应sbs的距离
        self.d2 = cl.distAwiB(self.x2, self.y2)
        self.d3 = cl.distAwiB(self.x3, self.y3)
        self.d4 = cl.distAwiB(self.x4, self.y4)
        self.dua1 = cl.distAwiB(self.xua1, self.yua1)
        self.dua2 = cl.distAwiB(self.xua2, self.yua2)
        self.dua3 = cl.distAwiB(self.xua3, self.yua3)

        return

    def generate_site_band_sbs1(self):
        ps = 0.25   # w
        psbs = 1
        Noise = 4**(-21)
        B = 10**8
        Gsbmbuu = 0
        Gsbmbdd = 0
        Gsbmbdu = 0
        Gsbmbud = 0
        i = 1  # i是第一辆汽车移动的第几秒
        c1_u = []
        c1_d = []
        c2_u = []
        c2_d = []
        c3_u = []
        c3_d = []
        c4_u = []
        c4_d = []
        cua_u = []
        cua_d = []
        cmb_u = []
        cmb_d = []
        for i in range(1500):
            # -----------------------------------------------------------------------------------------------------------------------------------------
            # sbs1在i秒的所有ue的上行链路

            if self.d1[i]['cell'] == 'sbs1':
                G1 = GadP.uAbU(self.d1[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x1[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y1[i])**2
                    dd1 = np.sqrt(xx+yy)
                    if dd1 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd1)
                k1 = ps*G1
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c1u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同

                G1 = GadP.uAbD(self.d1[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x1[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y1[i])**2
                    dd1 = np.sqrt(xx+yy)
                    if dd1 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd1)
                k1 = psbs*G1
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c1d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            else:
                c1d = 'none'
                c1u = 'none'
            if self.d1[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down
            if self.d1[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            if self.d2[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                G2 = GadP.uAbU(self.d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x2[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y2[i])**2
                    dd2 = np.sqrt(xx+yy)
                    if dd2 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd2)
                k1 = ps*G2
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c2u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))

                # G1 = GadP.uAbU(d1[i]['distance'])
                G2 = GadP.uAbD(self.d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x2[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y2[i])**2
                    dd2 = np.sqrt(xx+yy)
                    if dd2 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd2)
                k1 = psbs*G2
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c2d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c2d = 'none'
                c2u = 'none'
            if self.d2[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down
            if self.d2[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            if self.d3[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                G3 = GadP.uAbU(self.d3[i]['distance'])  # 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x3[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y3[i])**2
                    dd3 = np.sqrt(xx+yy)
                    if dd3 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd3)
                k1 = ps*G3
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c3u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))

                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                G3 = GadP.uAbD(self.d3[i]['distance'])  # 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x3[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y3[i])**2
                    dd3 = np.sqrt(xx+yy)
                    if dd3 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd3)
                k1 = psbs*G3
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c3d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c3d = 'none'
                c3u = 'none'
            if self.d3[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down
            if self.d3[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            if self.d4[i]['cell'] == 'sbs1':
                # g1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                G4 = GadP.uAbU(self.d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x4[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y4[i])**2
                    dd4 = np.sqrt(xx+yy)
                    if dd4 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd4)
                k1 = ps*G4
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c4u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))

                # g1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                G4 = GadP.uAbD(self.d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x4[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y4[i])**2
                    dd4 = np.sqrt(xx+yy)
                    if dd4 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd4)
                k1 = psbs*G4
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c4d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c4d = 'none'
                c4u = 'none'
            if self.d4[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down
            if self.d4[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            if self.dua1[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                Gua = GadP.uAbU(self.dua1[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.xua1[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.yua1[i])**2
                    ddua = np.sqrt(xx+yy)
                    if ddua == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(ddua)
                k1 = ps*Gua
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                cuau = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.dua1[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))

                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                Gua = GadP.uAbD(self.dua1[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.xua1[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.yua1[i])**2
                    ddua = np.sqrt(xx+yy)
                    if ddua == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(ddua)
                k1 = psbs*Gua
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                cuad = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.dua1[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))
            else:
                cuad = 'none'
                cuau = 'none'
            if self.dua1[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.dua1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.dua1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down
            if self.dua1[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.dua1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.dua1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            # --------------------------------------------------------------------------------------------------------------------------------------------
            # sbs1和mbs间的上行链路 1个sbs和mbs之间只有一对上下行链路

            ks1 = psbs*GadP.bABu(np.sqrt((301-101)**2+(301-101)**2))
            ld2d = len(self.d2dsite[i]['up1x'])  # 此时场上有几个d2d
            mm = 0  # mm是第几个可用的d2d
            Gd2d = 0
            for mm in range(ld2d):
                xx = (self.d2dsite[i]['up1x'][mm] - 301)**2
                yy = (self.d2dsite[i]['up1y'][mm] - 301)**2
                dmbs = np.sqrt(xx+yy)
                Gd2d += GadP.MLU(dmbs)
            ks2 = Noise + Gsbmbuu + Gsbmbdu + ps*Gd2d
            rupmai = ks1/ks2
            cupma = B*math.log2(1+rupmai)

            # --------------------------------------------------------------------------------------------------------------------------------------------
            # sbs1和mbs间的下行链路 1个sbs和mbs之间只有一对上下行链路

            ks1 = psbs*GadP.bABd(np.sqrt((301-101)**2+(301-101)**2))
            ld2d = len(self.d2dsite[i]['up1x'])  # 此时场上有几个d2d
            mm = 0  # mm是第几个可用的d2d
            Gd2d = 0
            for mm in range(ld2d):
                xx = (self.d2dsite[i]['down2x'][mm] - 301)**2
                yy = (self.d2dsite[i]['down2y'][mm] - 301)**2
                dmbs = np.sqrt(xx+yy)
                Gd2d += GadP.MLD(dmbs)
            ks2 = Noise + Gsbmbud + Gsbmbdd + ps*Gd2d  # 暂时没有计算下行的
            rdownmai = ks1/ks2
            cdownma = B*math.log2(1+rdownmai)

            c1_u = np.append(c1_u, c1u)
            c1_d = np.append(c1_d, c1d)
            c2_u = np.append(c2_u, c2u)
            c2_d = np.append(c2_d, c2d)
            c3_u = np.append(c3_u, c3u)
            c3_d = np.append(c3_d, c3d)
            c4_u = np.append(c4_u, c4u)
            c4_d = np.append(c4_d, c4d)
            cua_u = np.append(cua_u, cuau)
            cua_d = np.append(cua_d, cuad)
            cmb_u = np.append(cmb_u, cupma)
            cmb_d = np.append(cmb_d, cdownma)

            C = [[c1_u, c1_d], [c2_u, c2_d], [c3_u, c3_d], [c4_u, c4_d], [cua_u, cua_d], [cmb_u, cmb_d]]
        return C

    def generate_site_band_sbs2(self):
        ps = 0.25   # w
        psbs = 1
        Noise = 4**(-21)
        B = 10**8
        Gsbmbuu = 0
        Gsbmbdd = 0
        Gsbmbdu = 0
        Gsbmbud = 0
        i = 1  # i是第一辆汽车移动的第几秒
        c1_u = []
        c1_d = []
        c2_u = []
        c2_d = []
        c3_u = []
        c3_d = []
        c4_u = []
        c4_d = []
        cua_u = []
        cua_d = []
        cmb_u = []
        cmb_d = []
        for i in range(1500):
            # -----------------------------------------------------------------------------------------------------------------------------------------
            # sbs1在i秒的所有ue的上行链路

            if self.d1[i]['cell'] == 'sbs2':
                G1 = GadP.uAbU(self.d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x1[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y1[i])**2
                    dd1 = np.sqrt(xx+yy)
                    if dd1 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd1)
                k1 = ps*G1
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c1u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同

                G1 = GadP.uAbD(self.d1[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x1[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y1[i])**2
                    dd1 = np.sqrt(xx+yy)
                    if dd1 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd1)
                k1 = psbs*G1
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c1d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down
            else:
                c1d = 'none'
                c1u = 'none'
            if self.d1[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.d1[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            if self.d2[i]['cell'] == 'sbs2':
                # G1 = GadP.uAbU(d1[i]['distance'])
                G2 = GadP.uAbU(self.d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x2[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y2[i])**2
                    dd2 = np.sqrt(xx+yy)
                    if dd2 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd2)
                k1 = ps*G2
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c2u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))

                # G1 = GadP.uAbU(d1[i]['distance'])
                G2 = GadP.uAbD(self.d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x2[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y2[i])**2
                    dd2 = np.sqrt(xx+yy)
                    if dd2 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd2)
                k1 = psbs*G2
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c2d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))
            else:
                c2d = 'none'
                c2u = 'none'
            if self.d2[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.d2[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            if self.d3[i]['cell'] == 'sbs2':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                G3 = GadP.uAbU(self.d3[i]['distance'])  # 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x3[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y3[i])**2
                    dd3 = np.sqrt(xx+yy)
                    if dd3 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd3)
                k1 = ps*G3
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c3u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))

                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                G3 = GadP.uAbD(self.d3[i]['distance'])  # 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x3[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y3[i])**2
                    dd3 = np.sqrt(xx+yy)
                    if dd3 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd3)
                k1 = psbs*G3
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c3d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))
            else:
                c3d = 'none'
                c3u = 'none'
            if self.d3[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.d3[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            if self.d4[i]['cell'] == 'sbs2':
                # g1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                G4 = GadP.uAbU(self.d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x4[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y4[i])**2
                    dd4 = np.sqrt(xx+yy)
                    if dd4 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd4)
                k1 = ps*G4
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c4u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))

                # g1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                G4 = GadP.uAbD(self.d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x4[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y4[i])**2
                    dd4 = np.sqrt(xx+yy)
                    if dd4 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd4)
                k1 = psbs*G4
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c4d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))
            else:
                c4d = 'none'
                c4u = 'none'
            if self.d4[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.d4[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            if self.dua2[i]['cell'] == 'sbs2':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                Gua = GadP.uAbU(self.dua2[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.xua2[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.yua2[i])**2
                    ddua = np.sqrt(xx+yy)
                    if ddua == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(ddua)
                k1 = ps*Gua
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                cuau = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.dua2[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))

                Gua = GadP.uAbD(self.dua2[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.xua2[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.yua2[i])**2
                    ddua = np.sqrt(xx+yy)
                    if ddua == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(ddua)
                k1 = psbs*Gua
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                cuad = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.dua2[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))
            else:
                cuad = 'none'
                cuau = 'none'
            if self.dua2[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.dua2[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.dua2[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.dua2[i]['cell'] == 'sbs3':
                Gsbmbuu += ps*GadP.MLU(self.dua2[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.dua2[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down

            # --------------------------------------------------------------------------------------------------------------------------------------------
            # sbs1和mbs间的上行链路 1个sbs和mbs之间只有一对上下行链路

            ks1 = psbs*GadP.bABu(np.sqrt((301-101)**2+(301-301)**2))
            ld2d = len(self.d2dsite[i]['up1x'])  # 此时场上有几个d2d
            mm = 0  # mm是第几个可用的d2d
            Gd2d = 0
            for mm in range(ld2d):
                xx = (self.d2dsite[i]['up1x'][mm] - 301)**2
                yy = (self.d2dsite[i]['up1y'][mm] - 301)**2
                dmbs = np.sqrt(xx+yy)
                Gd2d += GadP.MLU(dmbs)
            ks2 = Noise + Gsbmbuu + Gsbmbdu + ps*Gd2d
            rupmai = ks1/ks2
            cupma = B*math.log2(1+rupmai)

            # --------------------------------------------------------------------------------------------------------------------------------------------
            # sbs1和mbs间的下行链路 1个sbs和mbs之间只有一对上下行链路

            ks1 = psbs*GadP.bABd(np.sqrt((301-101)**2+(301-301)**2))
            ld2d = len(self.d2dsite[i]['up1x'])  # 此时场上有几个d2d
            mm = 0  # mm是第几个可用的d2d
            Gd2d = 0
            for mm in range(ld2d):
                xx = (self.d2dsite[i]['down2x'][mm] - 301)**2
                yy = (self.d2dsite[i]['down2y'][mm] - 301)**2
                dmbs = np.sqrt(xx+yy)
                Gd2d += GadP.MLD(dmbs)
            ks2 = Noise + Gsbmbud + Gsbmbdd + ps*Gd2d
            rdownmai = ks1/ks2
            cdownma = B*math.log2(1+rdownmai)

            c1_u = np.append(c1_u, c1u)
            c1_d = np.append(c1_d, c1d)
            c2_u = np.append(c2_u, c2u)
            c2_d = np.append(c2_d, c2d)
            c3_u = np.append(c3_u, c3u)
            c3_d = np.append(c3_d, c3d)
            c4_u = np.append(c4_u, c4u)
            c4_d = np.append(c4_d, c4d)
            cua_u = np.append(cua_u, cuau)
            cua_d = np.append(cua_d, cuad)
            cmb_u = np.append(cmb_u, cupma)
            cmb_d = np.append(cmb_d, cdownma)

            C = [[c1_u, c1_d], [c2_u, c2_d], [c3_u, c3_d], [c4_u, c4_d], [cua_u, cua_d], [cmb_u, cmb_d]]
        return C

    def generate_site_band_sbs3(self):
        ps = 0.25   # w
        psbs = 1
        Noise = 4**(-21)
        B = 10**8
        Gsbmbuu = 0
        Gsbmbdd = 0
        Gsbmbdu = 0
        Gsbmbud = 0
        i = 1  # i是第一辆汽车移动的第几秒
        c1_u = []
        c1_d = []
        c2_u = []
        c2_d = []
        c3_u = []
        c3_d = []
        c4_u = []
        c4_d = []
        cua_u = []
        cua_d = []
        cmb_u = []
        cmb_d = []
        for i in range(1500):
            # -----------------------------------------------------------------------------------------------------------------------------------------
            # sbs1在i秒的所有ue的上行链路

            if self.d1[i]['cell'] == 'sbs3':
                G1 = GadP.uAbU(self.d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x1[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y1[i])**2
                    dd1 = np.sqrt(xx+yy)
                    if dd1 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd1)
                k1 = ps*G1
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c1u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同

                G1 = GadP.uAbD(self.d1[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x1[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y1[i])**2
                    dd1 = np.sqrt(xx+yy)
                    if dd1 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd1)
                k1 = psbs*G1
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c1d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down
            else:
                c1d = 'none'
                c1u = 'none'
            if self.d1[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.d1[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down

            if self.d2[i]['cell'] == 'sbs3':
                # G1 = GadP.uAbU(d1[i]['distance'])
                G2 = GadP.uAbU(self.d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x2[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y2[i])**2
                    dd2 = np.sqrt(xx+yy)
                    if dd2 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd2)
                k1 = ps*G2
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c2u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))

                # G1 = GadP.uAbU(d1[i]['distance'])
                G2 = GadP.uAbD(self.d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x2[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y2[i])**2
                    dd2 = np.sqrt(xx+yy)
                    if dd2 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd2)
                k1 = psbs*G2
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c2d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))
            else:
                c2d = 'none'
                c2u = 'none'
            if self.d2[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.d2[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.d2[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d2[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down

            if self.d3[i]['cell'] == 'sbs3':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                G3 = GadP.uAbU(self.d3[i]['distance'])  # 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x3[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y3[i])**2
                    dd3 = np.sqrt(xx+yy)
                    if dd3 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd3)
                k1 = ps*G3
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c3u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))

                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                G3 = GadP.uAbD(self.d3[i]['distance'])  # 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x3[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y3[i])**2
                    dd3 = np.sqrt(xx+yy)
                    if dd3 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd3)
                k1 = psbs*G3
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c3d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))
            else:
                c3d = 'none'
                c3u = 'none'
            if self.d3[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.d3[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.d3[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d3[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down

            if self.d4[i]['cell'] == 'sbs3':
                # g1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                G4 = GadP.uAbU(self.d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.x4[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.y4[i])**2
                    dd4 = np.sqrt(xx+yy)
                    if dd4 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd4)
                k1 = ps*G4
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c4u = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))

                # g1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                G4 = GadP.uAbD(self.d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.x4[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.y4[i])**2
                    dd4 = np.sqrt(xx+yy)
                    if dd4 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd4)
                k1 = psbs*G4
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c4d = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))
            else:
                c4d = 'none'
                c4u = 'none'
            if self.d4[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.d4[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.d4[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.d4[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down

            if self.dua3[i]['cell'] == 'sbs3':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                Gua = GadP.uAbU(self.dua3[i]['distance'])
                ld2d = len(self.d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['up1x'][mm] - self.xua3[i])**2
                    yy = (self.d2dsite[i]['up1y'][mm] - self.yua3[i])**2
                    ddua = np.sqrt(xx+yy)
                    if ddua == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(ddua)
                k1 = ps*Gua
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                cuau = B*math.log2(1+rupi)
                # Gsbmbuu += ps*GadP.MLU(self.dua3[i]['MBSdis'])
                # Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-301)**2+(301-101)**2))

                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                Gua = GadP.uAbD(self.dua3[i]['distance'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (self.d2dsite[i]['down2x'][mm] - self.xua3[i])**2
                    yy = (self.d2dsite[i]['down2y'][mm] - self.yua3[i])**2
                    ddua = np.sqrt(xx+yy)
                    if ddua == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(ddua)
                k1 = psbs*Gua
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                cuad = B*math.log2(1+rdowni)
                # Gsbmbud += ps*GadP.MLD(self.dua3[i]['MBSdis'])
                # Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-301)**2+(301-101)**2))  # 因为无自身干扰，所以要舍去自身小区内的干扰值
            else:
                cuad = 'none'
                cuau = 'none'
            if self.dua3[i]['cell'] == 'sbs1':
                Gsbmbuu += ps*GadP.MLU(self.dua3[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.dua3[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            if self.dua3[i]['cell'] == 'sbs2':
                Gsbmbuu += ps*GadP.MLU(self.dua3[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同
                Gsbmbud += ps*GadP.MLD(self.dua3[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-301)**2))  # sbs和mbs之间的下行链路  down down

            # --------------------------------------------------------------------------------------------------------------------------------------------
            # sbs1和mbs间的上行链路 1个sbs和mbs之间只有一对上下行链路

            ks1 = psbs*GadP.bABu(np.sqrt((301-301)**2+(301-101)**2))
            ld2d = len(self.d2dsite[i]['up1x'])  # 此时场上有几个d2d
            mm = 0  # mm是第几个可用的d2d
            Gd2d = 0
            for mm in range(ld2d):
                xx = (self.d2dsite[i]['up1x'][mm] - 301)**2
                yy = (self.d2dsite[i]['up1y'][mm] - 301)**2
                dmbs = np.sqrt(xx+yy)
                Gd2d += GadP.MLU(dmbs)
            ks2 = Noise + Gsbmbuu + Gsbmbdu + ps*Gd2d
            rupmai = ks1/ks2
            cupma = B*math.log2(1+rupmai)

            # --------------------------------------------------------------------------------------------------------------------------------------------
            # sbs1和mbs间的下行链路 1个sbs和mbs之间只有一对上下行链路

            ks1 = psbs*GadP.bABd(np.sqrt((301-301)**2+(301-101)**2))
            ld2d = len(self.d2dsite[i]['up1x'])  # 此时场上有几个d2d
            mm = 0  # mm是第几个可用的d2d
            Gd2d = 0
            for mm in range(ld2d):
                xx = (self.d2dsite[i]['down2x'][mm] - 301)**2
                yy = (self.d2dsite[i]['down2y'][mm] - 301)**2
                dmbs = np.sqrt(xx+yy)
                Gd2d += GadP.MLD(dmbs)
            ks2 = Noise + Gsbmbud + Gsbmbdd + ps*Gd2d  # 暂时没有计算下行的
            rdownmai = ks1/ks2
            cdownma = B*math.log2(1+rdownmai)

            c1_u = np.append(c1_u, c1u)
            c1_d = np.append(c1_d, c1d)
            c2_u = np.append(c2_u, c2u)
            c2_d = np.append(c2_d, c2d)
            c3_u = np.append(c3_u, c3u)
            c3_d = np.append(c3_d, c3d)
            c4_u = np.append(c4_u, c4u)
            c4_d = np.append(c4_d, c4d)
            cua_u = np.append(cua_u, cuau)
            cua_d = np.append(cua_d, cuad)
            cmb_u = np.append(cmb_u, cupma)
            cmb_d = np.append(cmb_d, cdownma)

            C = [[c1_u, c1_d], [c2_u, c2_d], [c3_u, c3_d], [c4_u, c4_d], [cua_u, cua_d], [cmb_u, cmb_d]]
        return C

    def reset(self):
        # 重置到第一秒，此时d2d存在
        self.tcon = 1
        self.tcon1 = 1
        self.tcon2 = 1
        self.tcon3 = 1
        oct_up1 = 0
        oct_down1 = 0
        oct_up2 = 0
        oct_down2 = 0
        oct_up3 = 0
        oct_down3 = 0
        demDarateu = 5*10**7
        demDarated = 20*10**7
        self.generate_data()
        self.C_need1 = self.generate_site_band_sbs1()
        self.C_need2 = self.generate_site_band_sbs2()
        self.C_need3 = self.generate_site_band_sbs3()
        for i in range(6):
            Rup1 = 0.1*random.randint(1, 6)
            Rdown1 = 1 - Rup1
            Rup2 = 0.1*random.randint(1, 6)
            Rdown2 = 1 - Rup2
            Rup3 = 0.1*random.randint(1, 6)
            Rdown3 = 1 - Rup3
            if self.C_need1[i][0][1] != 'none':
                octu = (demDarateu/float(self.C_need1[i][0][1]))*Rup1/10
                oct_up1 += octu
            if self.C_need1[i][1][1] != 'none':
                octd = (demDarated/float(self.C_need1[i][1][1]))*Rdown1/10
                oct_down1 += octd
            if self.C_need2[i][0][1] != 'none':
                octu = (demDarateu/float(self.C_need2[i][0][1]))*Rup2/10
                oct_up2 += octu
            if self.C_need2[i][1][1] != 'none':
                octd = (demDarated/float(self.C_need2[i][1][1]))*Rdown2/10
                oct_down2 += octd
            if self.C_need3[i][0][1] != 'none':
                octu = (demDarateu/float(self.C_need3[i][0][1]))*Rup3/10
                oct_up3 += octu
            if self.C_need3[i][1][1] != 'none':
                octd = (demDarated/float(self.C_need3[i][1][1]))*Rdown3/10
                oct_down3 += octd
        self.state1 = [oct_up1, oct_down1]
        self.state2 = [oct_up2, oct_down2]
        self.state3 = [oct_up3, oct_down3]
        return

    def generate_next_state(self, s, a, sbs):
        oct_up1 = 0.0
        oct_down1 = 0.0
        oct_up2 = 0.0
        oct_down2 = 0.0
        oct_up3 = 0.0
        oct_down3 = 0.0
        demDarateu = 5*10**7
        demDarated = 20*10**7
        Rup = a*0.1
        Rdown = 1-Rup

        if sbs == 1:
            self.tcon1 += 1
            tcon = self.tcon1
            C_need1 = self.C_need1
            for i in range(6):
                if self.C_need1[i][0][tcon] != 'none':
                    octu = ((demDarated/float(C_need1[i][0][tcon]))*Rup)/10  # 单个用户0.006左右，核心论用户数150-200
                    oct_up1 = oct_up1+octu
                if self.C_need1[i][1][tcon] != 'none':
                    octd = ((demDarated/float(C_need1[i][1][tcon]))*Rdown)/10
                    oct_down1 = oct_down1+octd
            self.state1 = [oct_up1, oct_down1]
        elif sbs == 2:
            self.tcon2 += 1
            tcon = self.tcon2
            C_need2 = self.C_need2
            for i in range(6):
                if self.C_need2[i][0][tcon] != 'none':
                    octu = ((demDarateu/float(C_need2[i][0][tcon]))*Rup)/10
                    oct_up2 = oct_up2+octu
                if self.C_need2[i][1][tcon] != 'none':
                    octd = ((demDarated/float(C_need2[i][1][tcon]))*Rdown)/10
                    oct_down2 = oct_down2+octd
            self.state2 = [oct_up2, oct_down2]
        elif sbs == 3:
            self.tcon3 += 1
            tcon = self.tcon3
            C_need3 = self.C_need3
            for i in range(6):
                if self.C_need3[i][0][tcon] != 'none':
                    octu = ((demDarateu/float(C_need3[i][0][tcon]))*Rup)/10
                    oct_up3 = oct_up3+octu
                if self.C_need3[i][1][tcon] != 'none':
                    octd = ((demDarated/float(C_need3[i][1][tcon]))*Rdown)/10
                    oct_down3 = oct_down3+octd
            self.state3 = [oct_up3, oct_down3]

        return

    def step(self, action, sbs):
        # action应该包含上下行比例，和是哪个ue
        if sbs == 1:
            state = self.state1
            self.generate_next_state(state, action, 1)
            next_state = self.state1
        elif sbs == 2:
            state = self.state2
            self.generate_next_state(state, action, 2)
            next_state = self.state2
        elif sbs == 3:
            state = self.state3
            self.generate_next_state(state, action, 3)
            next_state = self.state3
        ca = 20
        da = 1
        cb = 10
        db = 6  # 奖励的常数项系数,DQN是向着奖励函数越来越高的方向收敛的，如何行动可以得到最大的reward
        if next_state[0] <= 0.3:  # up
            rup = ca*next_state[0]
        else:
            rup = -ca*next_state[0]+da

        if next_state[1] <= 1.0:  # down
            rdown = cb*next_state[1]
        else:
            rdown = -cb*next_state[1]+db

        reward = rup+rdown
        return state, action, reward, next_state

    # def tback(self):
    #     t = self.tcon
    #     return t

    # def tadd(self):
    #     self.tcon += 1
    #     return self.tcon
