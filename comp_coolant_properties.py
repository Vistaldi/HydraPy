import numpy as np
from iapws import IAPWS97
from data_models import Inp, Fuel, Coolant
from config import NFA, NROW, PRESS, ENTHALPY_IN, Gv, ITERATIONS


def compute_coolant_properties(inp: Inp, fuel: Fuel, cool: Coolant):
    cool.dens[:, :] = inp.dens

    for _ in range(ITERATIONS):
        Gm = cool.dens * 1e3 * Gv

        enthalpy = np.zeros((NFA, NROW), dtype=np.float64)
        enthalpy[:, 0] = ENTHALPY_IN + fuel.power[:, 0] / Gm[:, 0] * 1e-3
        for row in range(1, NROW):
            enthalpy[:, row] = (
                enthalpy[:, row - 1] + fuel.power[:, row] / Gm[:, row] * 1e-3
            )

        for fa in range(NFA):
            for row in range(NROW):
                water = IAPWS97(P=PRESS, h=enthalpy[fa, row])
                cool.dens[fa, row] = water.rho * 1e-3
                cool.temp[fa, row] = water.T
