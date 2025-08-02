import logging
import numpy as np

from config import NROW
from data_models import Inp, Fuel
from find import line_search

# Set up the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_inp(inp: Inp):
    """Reads input data from inpHydraPy.txt"""
    file_path = "./inpHydraPy.txt"
    try:
        with open(file_path, "rt") as finp:
            line_search(finp, "average density")
            inp.dens = np.fromfile(finp, dtype=np.float64, count=NROW, sep=" ")

            line_search(finp, "mesh")
            inp.mesh = np.fromfile(finp, dtype=np.float64, count=NROW, sep=" ")
    except (OSError, ValueError) as e:
        logger.exception(f"Error reading file {file_path}: {e}")
        raise


def read_fuel_data(fuel: Fuel):
    """Reads fuel power distribution from serp-power1-sum.txt"""
    file_path = "./power.txt"
    try:
        fuel.power = np.loadtxt(file_path, dtype=np.float64)
    except (OSError, ValueError) as e:
        logger.exception(f"Error reading file {file_path}: {e}")
        raise
