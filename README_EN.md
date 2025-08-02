# HydraPy

**HydraPy** is a Python-based program for calculating thermal and hydraulic parameters in fuel assemblies of the VVER-1000 reactor core.

## 🧠 Motivation

Most Monte Carlo neutron transport codes (e.g., MCNP, Serpent, OpenMC) lack built-in thermal-hydraulic feedback modules. HydraPy is designed to bridge this gap, enabling thermal field and coolant behavior modeling to support multiphysics calculations.

The name *Hydra* refers to "hydraulics", and *Py* denotes the Python implementation.

## ⚙️ Functional Overview

- Coolant density and temperature calculations.
- Average fuel temperature for Doppler feedback.
- Axial heat generation profile consideration.
- Heat transfer coefficient computation using M.A. Mikheev's correlation for turbulent flow.
- Detailed thermal model of a fuel rod:
  - Gap heat conduction (helium),
  - Cladding conduction,
  - Convection to coolant.

## 📚 Methodology

- **Nodal approach** along the axial direction.
- **Parallel channel model** for fuel assemblies.
- Non-linear systems are solved numerically due to temperature-dependent properties.
- Water properties are obtained via the **IAPWS-IF97** library.

## 📥 Input Files

- `power.txt`: **Power distribution** (assemblies × axial layers) from neutronics codes (MCNP/Serpent/OpenMC).
- `inpHydraPy.txt`: **Configuration file** containing:
  - `average density`: Initial guesses for coolant density (iteratively updated).
  - `mesh`: Axial layer heights (uniform or non-uniform).

## 📤 Output Files

- `coolant-density.txt` — calculated coolant density in each axial layer and fuel assembly.
- `Tdopp.txt` — average fuel temperature per layer and assembly.

## 🚀 Usage

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the main program:
```bash
python main.py
```

## 🧾 License

HydraPy is open source. You may use, modify, and distribute it freely. However, the author does not take responsibility for any changes made by third parties.

## 👤 Author

Viktor Ilkovych  
2025
