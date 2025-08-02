import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve

from config import NFA, NROW, NPIN, r1, r2, r3, Lzr, toKelvin
from data_models import Inp, Fuel, Coolant


def fuel_temperature(inp: Inp, fuel: Fuel, cool: Coolant):
    toCelsius = -toKelvin
    t_cool = cool.temp + toCelsius

    Stvel = np.pi * r1**2
    Vtvel = Stvel * inp.mesh * 1e-02

    qV = fuel.power / Vtvel[np.newaxis, :] / NPIN
    qL = qV * Stvel

    def Luo2(t):
        return 8.706 - 9.11e-03 * t + 3.992e-06 * t**2 - 5.004e-10 * t**3

    def Lhe(t):
        return 0.146 + 3.339e-04 * t - 4.219e-08 * t**2

    def meanLuo2(t1, t2):
        return Luo2(t1) if abs(t1 - t2) < 1e-03 else quad(Luo2, t1, t2)[0] / (t2 - t1)

    def meanLhe(t1, t2):
        return Lhe(t1) if abs(t1 - t2) < 1e-03 else quad(Lhe, t1, t2)[0] / (t2 - t1)

    RLa = 1.0 / (2.0 * np.pi * cool.alpha * r3)
    RLzr = np.log(r3 / r2) / (2.0 * np.pi * Lzr)

    def RLhe(t1, t2):
        return np.log(r2 / r1) / (2.0 * np.pi * meanLhe(t1, t2))

    def equations(vars, qL, tc, RLa):
        t1, t2, t3 = vars
        return [
            (t1 - t2) / RLhe(t1, t2) - qL,
            (t2 - t3) / RLzr - qL,
            (t3 - tc) / RLa - qL,
        ]

    def equation_t0(t0, t1, qV):
        return t0 - t1 - (qV * r1**2) / (4.0 * meanLuo2(t1, t0))

    t0 = np.full((NFA, NROW), 400.0)
    t1 = np.full((NFA, NROW), 400.0)

    t0_init = 400.0
    ts_init = [400.0, 400.0, 400.0]

    for fa in range(NFA):
        for row in range(NROW):
            solution_t1 = fsolve(
                equations, ts_init, args=(qL[fa, row], t_cool[fa, row], RLa[fa, row])
            )
            t1[fa, row] = solution_t1[0]

            solution_t0 = fsolve(equation_t0, t0_init, args=(t1[fa, row], qV[fa, row]))
            t0[fa, row] = solution_t0[0]

    xi_dopp = 0.7
    fuel.Tdopp = (1.0 - xi_dopp) * t0 + xi_dopp * t1 + toKelvin
