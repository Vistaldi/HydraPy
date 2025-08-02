import time
import numpy as np
from config import NFA, NROW
from data_models import Inp, Fuel, Coolant
from input import read_inp, read_fuel_data
from comp_coolant_properties import compute_coolant_properties
from comp_means import compute_interval_means
from heat_transfer_coeff import heat_transfer_coeff
from fuel_temperature import fuel_temperature
from output import output


def initialize_objects():
    """Initialize input, fuel, and coolant data structures."""
    inp = Inp(
        dens=np.zeros(NROW, dtype=np.float64),
        mesh=np.zeros(NROW, dtype=np.float64),
    )

    fuel = Fuel(
        power=np.zeros((NFA, NROW), dtype=np.float64),
        Tdopp=np.zeros((NFA, NROW), dtype=np.float64),
    )

    cool = Coolant(
        dens=np.zeros((NFA, NROW), dtype=np.float64),
        temp=np.zeros((NFA, NROW), dtype=np.float64),
        cond=np.zeros((NFA, NROW), dtype=np.float64),
        visc=np.zeros((NFA, NROW), dtype=np.float64),
        pran=np.zeros((NFA, NROW), dtype=np.float64),
        alpha=np.zeros((NFA, NROW), dtype=np.float64),
    )

    return inp, fuel, cool


def main():
    start_time = time.time()
    inp, fuel, cool = initialize_objects()

    print("Reading input data... ", end="")
    read_inp(inp)
    read_fuel_data(fuel)
    print("done.")

    print("Computing coolant properties... ", end="")
    compute_coolant_properties(inp, fuel, cool)
    print("done.")

    print("Computing means... ", end="")
    compute_interval_means(cool.dens, inp.mesh)
    compute_interval_means(cool.temp, inp.mesh)
    print("done.")

    print("Computing heat transfer coefficient... ", end="")
    heat_transfer_coeff(cool)
    print("done.")

    print("Computing fuel temperature... ", end="")
    fuel_temperature(inp, fuel, cool)
    print("done.")

    print("Writing output... ", end="")
    output(fuel, cool)
    print("done.")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.1f} seconds")


if __name__ == "__main__":
    main()
