import numpy as np
from data_models import Fuel, Coolant


def output(fuel: Fuel, cool: Coolant):
    """Saves fuel temperature and coolant density data to text files."""
    with open("Tdopp.txt", "wt") as fout:
        np.savetxt(fout, fuel.Tdopp, fmt="%10.5f", delimiter=" ")

    with open("coolant-density.txt", "wt") as fout:
        np.savetxt(fout, cool.dens, fmt="%10.5f", delimiter=" ")
