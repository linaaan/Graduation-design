import GadP
import mulgen as mul
import UAV
import numpy as np
import math
import clasidis as cl
import D2Djudge as D2j
import random


class Env_HetNet():
    def __init__(self):
        self.pue = 0.25
        self.psbs = 1
        self.pmbs = 40
        self.Noise = 4**(-21)
        self.B = 10**8
        self.demDarate = 5*10**7
        self.tcon = 1
        self.state = None

    def generate_site_band(self):
        ps = 0.25   # w
        psbs = 1
        pmbs = 40
        Noise = 4**(-21)
        B = 10**8

        xua, yua = UAV.UavNode(101, 101, 1, 1500)
        d2dsite = D2j.d2dju(10, 1500)
        x1, y1 = mul.multgr(1500, 10)  # 第一辆汽车
        x2, y2 = mul.multgr(1500, 10)
        x3, y3 = mul.multgr(1500, 5)  # 第一个行人
        x4, y4 = mul.multgr(1500, 5)

        d1 = cl.distAwiB(x1, y1)  # 判断在那个sbs内和距离对应sbs的距离
        d2 = cl.distAwiB(x2, y2)
        d3 = cl.distAwiB(x3, y3)
        d4 = cl.distAwiB(x4, y4)
        dua = cl.distAwiB(xua, yua)
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
        c1_umax = []
        c1_dmax = []
        c2_umax = []
        c2_dmax = []
        c3_umax = []
        c3_dmax = []
        c4_umax = []
        c4_dmax = []
        cua_umax = []
        cua_dmax = []
        cmb_dmax = []
        cmb_umax = []
        for i in range(1500):
            # -----------------------------------------------------------------------------------------------------------------------------------------
            # sbs1在i秒的所有ue的上行链路

            if d1[i]['cell'] == 'sbs1':
                G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['up1x'][mm] - x1[i])**2
                    yy = (d2dsite[i]['up1y'][mm] - y1[i])**2
                    dd1 = np.sqrt(xx+yy)
                    if dd1 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd1)
                k1 = ps*G1
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c1u = B*math.log2(1+rupi)
                c1umax = B*math.log(1+k1/Noise)
                Gsbmbuu += ps*GadP.MLU(d1[i]['MBSdis'])  # ue和mbs之间的链路 up up
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的链路 down up 数目和ue数量相同

            else:
                c1u = 'none'
                c1umax = 'none'

            if d2[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['up1x'][mm] - x2[i])**2
                    yy = (d2dsite[i]['up1y'][mm] - y2[i])**2
                    dd2 = np.sqrt(xx+yy)
                    if dd2 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd2)
                k1 = ps*G2
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c2u = B*math.log2(1+rupi)
                c2umax = B*math.log(1+k1/Noise)
                Gsbmbuu += ps*GadP.MLU(d2[i]['MBSdis'])
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c2u = 'none'
                c2umax = 'none'

            if d3[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                G3 = GadP.uAbU(d3[i]['distance'])  # 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['up1x'][mm] - x3[i])**2
                    yy = (d2dsite[i]['up1y'][mm] - y3[i])**2
                    dd3 = np.sqrt(xx+yy)
                    if dd3 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd3)
                k1 = ps*G3
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c3u = B*math.log2(1+rupi)
                c3umax = B*math.log(1+k1/Noise)
                Gsbmbuu += ps*GadP.MLU(d3[i]['MBSdis'])
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c3u = 'none'
                c3umax = 'none'

            if d4[i]['cell'] == 'sbs1':
                # g1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['up1x'][mm] - x4[i])**2
                    yy = (d2dsite[i]['up1y'][mm] - y4[i])**2
                    dd4 = np.sqrt(xx+yy)
                    if dd4 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(dd4)
                k1 = ps*G4
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                c4u = B*math.log2(1+rupi)
                c4umax = B*math.log(1+k1/Noise)
                Gsbmbuu += ps*GadP.MLU(d4[i]['MBSdis'])
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c4u = 'none'
                c4umax = 'none'

            if dua[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['up1x'][mm] - xua[i])**2
                    yy = (d2dsite[i]['up1y'][mm] - yua[i])**2
                    ddua = np.sqrt(xx+yy)
                    if ddua == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbU(ddua)
                k1 = ps*Gua
                k2 = Noise + ps*Gd2d
                rupi = k1/k2
                cuau = B*math.log2(1+rupi)
                cuaumax = B*math.log(1+k1/Noise)
                Gsbmbuu += ps*GadP.MLU(dua[i]['MBSdis'])
                Gsbmbdu += psbs*GadP.MLU(np.sqrt((301-101)**2+(301-101)**2))
            else:
                cuau = 'none'
                cuaumax = 'none'

            # -----------------------------------------------------------------------------------------------------------------------------------------
            # sbs1在i秒的所有ue的下行链路

            if d1[i]['cell'] == 'sbs1':
                G1 = GadP.uAbD(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['down2x'][mm] - x1[i])**2
                    yy = (d2dsite[i]['down2y'][mm] - y1[i])**2
                    dd1 = np.sqrt(xx+yy)
                    if dd1 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd1)
                k1 = ps*G1
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c1d = B*math.log2(1+rdowni)
                c1dmax = B*math.log(1+k1/Noise)
                Gsbmbud += ps*GadP.MLD(d1[i]['MBSdis'])  # ue和mbs之间的下行链路 up  down
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))  # sbs和mbs之间的下行链路  down down
            else:
                c1d = 'none'
                c1dmax = 'none'

            if d2[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                G2 = GadP.uAbD(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['down2x'][mm] - x2[i])**2
                    yy = (d2dsite[i]['down2y'][mm] - y2[i])**2
                    dd2 = np.sqrt(xx+yy)
                    if dd2 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd2)
                k1 = ps*G2
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c2d = B*math.log2(1+rdowni)
                c2dmax = B*math.log(1+k1/Noise)
                Gsbmbud += ps*GadP.MLD(d2[i]['MBSdis'])
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c2d = 'none'
                c2dmax = 'none'

            if d3[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                G3 = GadP.uAbD(d3[i]['distance'])  # 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['down2x'][mm] - x3[i])**2
                    yy = (d2dsite[i]['down2y'][mm] - y3[i])**2
                    dd3 = np.sqrt(xx+yy)
                    if dd3 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd3)
                k1 = ps*G3
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c3d = B*math.log2(1+rdowni)
                c3dmax = B*math.log(1+k1/Noise)
                Gsbmbud += ps*GadP.MLD(d3[i]['MBSdis'])
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c3d = 'none'
                c3dmax = 'none'

            if d4[i]['cell'] == 'sbs1':
                # g1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                G4 = GadP.uAbD(d4[i]['distance'])
                # Gua = GadP.uAbU(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['down2x'][mm] - x4[i])**2
                    yy = (d2dsite[i]['down2y'][mm] - y4[i])**2
                    dd4 = np.sqrt(xx+yy)
                    if dd4 == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(dd4)
                k1 = ps*G4
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                c4d = B*math.log2(1+rdowni)
                c4dmax = B*math.log(1+k1/Noise)
                Gsbmbud += ps*GadP.MLD(d4[i]['MBSdis'])
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))
            else:
                c4d = 'none'
                c4dmax = 'none'

            if dua[i]['cell'] == 'sbs1':
                # G1 = GadP.uAbU(d1[i]['distance'])
                # G2 = GadP.uAbU(d2[i]['distance'])
                # G3 = GadP.uAbU(d3[i]['distance']) 还没有判断其他是否在sbs内
                # G4 = GadP.uAbU(d4[i]['distance'])
                Gua = GadP.uAbD(dua[i]['distance'])
                ld2d = len(d2dsite[i]['up1x'])
                mm = 0  # mm是第几个可用的d2d
                Gd2d = 0
                for mm in range(ld2d):
                    xx = (d2dsite[i]['down2x'][mm] - xua[i])**2
                    yy = (d2dsite[i]['down2y'][mm] - yua[i])**2
                    ddua = np.sqrt(xx+yy)
                    if ddua == 0:  # d2d用户和ue重叠
                        Gd2d += 0
                    else:
                        Gd2d += GadP.uAbD(ddua)
                k1 = ps*Gua
                k2 = Noise + ps*Gd2d
                rdowni = k1/k2
                cuad = B*math.log2(1+rdowni)
                cuadmax = B*math.log(1+k1/Noise)
                Gsbmbud += ps*GadP.MLD(dua[i]['MBSdis'])
                Gsbmbdd += psbs*GadP.MLD(np.sqrt((301-101)**2+(301-101)**2))
            else:
                cuad = 'none'
                cuadmax = 'none'

            # --------------------------------------------------------------------------------------------------------------------------------------------
            # sbs1和mbs间的上行链路 1个sbs和mbs之间只有一对上下行链路

            ks1 = psbs*GadP.bABu(np.sqrt((301-101)**2+(301-101)**2))
            ld2d = len(d2dsite[i]['up1x'])  # 此时场上有几个d2d
            mm = 0  # mm是第几个可用的d2d
            Gd2d = 0
            for mm in range(ld2d):
                xx = (d2dsite[i]['up1x'][mm] - 301)**2
                yy = (d2dsite[i]['up1y'][mm] - 301)**2
                dmbs = np.sqrt(xx+yy)
                Gd2d += GadP.MLU(dmbs)
            ks2 = Noise + Gsbmbuu + Gsbmbdu + ps*Gd2d
            rupmai = ks1/ks2
            cupma = B*math.log2(1+rupmai)
            cupmax = B*math.log2(1+ks1/Noise)

            # --------------------------------------------------------------------------------------------------------------------------------------------
            # sbs1和mbs间的上行链路 1个sbs和mbs之间只有一对上下行链路

            ks1 = psbs*GadP.bABd(np.sqrt((301-101)**2+(301-101)**2))
            ld2d = len(d2dsite[i]['up1x'])  # 此时场上有几个d2d
            mm = 0  # mm是第几个可用的d2d
            Gd2d = 0
            for mm in range(ld2d):
                xx = (d2dsite[i]['down2x'][mm] - 301)**2
                yy = (d2dsite[i]['down2y'][mm] - 301)**2
                dmbs = np.sqrt(xx+yy)
                Gd2d += GadP.MLD(dmbs)
            ks2 = Noise + Gsbmbud + Gsbmbdd + ps*Gd2d  # 暂时没有计算下行的
            rdownmai = ks1/ks2
            cdownma = B*math.log2(1+rdownmai)
            cdownmax = B*math.log2(1+ks1/Noise)
            c1_u = np.append(c1_u, c1u)
            c1_umax = np.append(c1_umax, c1umax)
            c1_d = np.append(c1_d, c1d)
            c1_dmax = np.append(c1_dmax, c1dmax)
            c2_u = np.append(c2_u, c2u)
            c2_umax = np.append(c2_umax, c2umax)
            c2_d = np.append(c2_d, c2d)
            c2_dmax = np.append(c2_dmax, c2dmax)
            c3_u = np.append(c3_u, c3u)
            c3_umax = np.append(c3_umax, c3umax)
            c3_d = np.append(c3_d, c3d)
            c3_dmax = np.append(c3_dmax, c3dmax)
            c4_u = np.append(c4_u, c4u)
            c4_umax = np.append(c4_umax, c4umax)
            c4_d = np.append(c4_d, c4d)
            c4_dmax = np.append(c4_dmax, c4dmax)
            cua_u = np.append(cua_u, cuau)
            cua_umax = np.append(cua_umax, cuaumax)
            cua_d = np.append(cua_d, cuad)
            cua_dmax = np.append(cua_dmax, cuadmax)
            cmb_u = np.append(cmb_u, cupma)
            cmb_umax = np.append(cmb_umax, cupmax)
            cmb_d = np.append(cmb_d, cdownma)
            cmb_dmax = np.append(cmb_dmax, cdownmax)

            C = [c1_u, c1_d, c2_u, c2_d, c3_u, c3_d, c4_u, c4_d, cua_u, cua_d, cmb_u, cmb_d]
        return C

    def reset(self):
        # 重置到第一秒，此时d2d存在
        self.tcon = 0
        oct_up = 0
        oct_down = 0
        demDarate = 5*10**7
        self.C_need = self.generate_site_band()
        for i in range(12):
            if self.C_need[i][1] != 'none':
                Rup = random.randint(1, 6)
                Rdown = 10 - Rup
                octu = (demDarate/float(self.C_need[i][1]))*Rup/100
                octd = (demDarate/float(self.C_need[i][1]))*Rdown/100
                oct_up += octu
                oct_down += octd

        self.state = [oct_up, oct_down]
        return self.state

    def generate_next_state(self, s, a):
        # a=5
        self.tcon += 1
        tcon = self.tcon
        oct_up = 0.0
        oct_down = 0.0
        demDarated = 8*10**7
        demDarateu = 2*10**7
        C_need = self.C_need
        Rup = a
        Rdown = 10-a
        for i in range(12):
            if self.C_need[i][tcon] != 'none':
                octu = ((demDarateu/float(C_need[i][tcon]))*Rup)/100
                octd = ((demDarated/float(C_need[i][tcon]))*Rdown)/100
                oct_up = oct_up+octu
                oct_down = oct_down+octd
        return([oct_up, oct_down])

    def step(self, action):
        # action应该包含上下行比例，和是哪个ue
        state = self.state
        next_state = self.generate_next_state(state, action)
        self.state = next_state
        ca = 1
        da = 4
        cb = 0.1
        db = 0.2  # 奖励的常数项系数，瞎写的
        if next_state[0] <= 1:
            rup = ca*next_state[0]
        else:
            rup = -ca*next_state[0]+da

        if next_state[1] <= 1:
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