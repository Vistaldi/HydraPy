# HydraPy

## English Version

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

- `inpHydraPy.txt` — initial conditions (mesh, coolant density, etc.).
- `coolant-density.txt` — calculated coolant density in each layer and assembly.
- `Tdopp.txt` — average fuel temperature per layer and assembly (used for neutron physics calculations).

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

---

## Українська версія

# HydraPy

**HydraPy** — це Python-програма для розрахунку теплових і гідравлічних параметрів у паливних збірках активної зони реактора типу ВВЕР-1000.

## 🧠 Причина створення

Більшість нейтронно-фізичних Монте-Карло кодів (MCNP, Serpent, OpenMC та ін.) не мають вбудованих теплогідравлічних модулів для врахування зворотних зв’язків. HydraPy створена для вирішення цієї задачі: вона виконує розрахунок теплового поля та гідравлічних параметрів як зовнішній модуль з можливістю інтеграції.

Назва *Hydra* походить від "гидра", а *Py* — вказує на реалізацію мовою Python.

## ⚙️ Функціональне призначення

- Розрахунок густини та температури теплоносія.
- Обчислення середньої температури палива (для ефекту Доплера).
- Врахування просторового розподілу тепловиділення.
- Розрахунок коефіцієнта тепловіддачі за формулою М.А. Міхєєва.
- Реалізація моделі теплопередачі у паливному елементі:
  - теплообмін у зазорі (гелій),
  - оболонка твела,
  - теплообмін з теплоносієм.

## 📚 Методика

- **Нодальний підхід** по висоті.
- **Паралельні канали** — обчислення у кожній паливній збірці окремо.
- Нелінійна система рівнянь, розв'язується чисельно.
- Використовується бібліотека **IAPWS-IF97** для точних термодинамічних властивостей води.

## 📥 Вхідні файли

- `inpHydraPy.txt` — початкові умови (mesh, густина тощо).
- `coolant-density.txt` — результатна густина теплоносія по шарах.
- `Tdopp.txt` — середня температура палива (для нейтронно-фізичних розрахунків).

## 🚀 Запуск

1. Встановіть залежності:
```bash
pip install -r requirements.txt
```

2. Запустіть розрахунок:
```bash
python main.py
```

## 🧾 Ліцензія

HydraPy поширюється на умовах відкритої ліцензії. Ви можете вільно використовувати, змінювати і поширювати цей код, однак автор не несе відповідальності за будь-які зміни, зроблені сторонніми особами.

## 👤 Автор

Віктор Ількович  
2025
