import numpy as np
from numpy.typing import NDArray
from dataclasses import dataclass


@dataclass
class Inp:
    dens: NDArray[np.float64]  # density
    mesh: NDArray[np.float64]


@dataclass
class Fuel:
    power: NDArray[np.float64]
    Tdopp: NDArray[np.float64]  # temperature


@dataclass
class Coolant:
    dens: NDArray[np.float64]  # density
    temp: NDArray[np.float64]  # temperature
    cond: NDArray[np.float64]  # thermal conductivity coefficient
    visc: NDArray[np.float64]  # dynamic viscosity
    pran: NDArray[np.float64]  # prandtl number
    alpha: NDArray[np.float64]  # heat transfer coefficient
