import numpy as np
from iapws import IAPWS97
from data_models import Coolant
from config import NFA, NROW, NPIN, PRESS, Gv, r3, t_tvel


def heat_transfer_coeff(cool: Coolant):
    for fa in range(NFA):
        for row in range(NROW):
            water = IAPWS97(T=cool.temp[fa, row], P=PRESS)
            cool.cond[fa, row] = water.k
            cool.visc[fa, row] = water.mu
            cool.pran[fa, row] = water.Prandt

    Gm = cool.dens * 1e3 * Gv / (NPIN + 18 + 1)
    d_tvel = np.sqrt(2.0 * np.sqrt(3.0) / np.pi) * t_tvel
    d3 = 2.0 * r3
    dg = (d_tvel**2 - d3**2) / d3
    Fc = np.pi * (d_tvel**2 - d3**2) / 4.0

    cool.alpha = (
        0.021 * cool.cond / dg * (Gm * dg / cool.visc / Fc) ** 0.8 * cool.pran**0.43
    )
