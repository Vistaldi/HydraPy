import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad
from numpy.typing import NDArray


def compute_interval_means(f: NDArray[np.float64], mesh: NDArray[np.float64]) -> None:
    """
    Computes the average value of f in each interval defined by mesh and updates f.

    Parameters:
    f    : NDArray[np.float64] - function values at interval endpoints (shape [NFA, NROW])
    mesh : NDArray[np.float64] - height differences between layers (shape [NROW])

    Modifies:
    f    : Overwrites it with the computed interval averages.
    """
    NFA, NROW = f.shape  # Extract dimensions dynamically
    z = np.concatenate(([0], np.cumsum(mesh)))  # Compute absolute height coordinates

    for fa in range(NFA):
        # Linear interpolation for the current row
        linear_spline = interp1d(
            z[1:], f[fa, :], kind="linear", fill_value="extrapolate"
        )

        for row in range(NROW):
            a, b = z[row], z[row + 1]  # Interval boundaries
            integral, _ = quad(linear_spline, a, b)  # Compute integral
            f[fa, row] = integral / (b - a)  # Compute the average value
