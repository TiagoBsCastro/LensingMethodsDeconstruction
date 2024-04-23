# LensingMethodsDeconstruction

Data and scripts from "A Deconstruction of Methods to Derive One-Point Lensing Statistics," evaluating different methods for lensing PDFs in weak and strong regimes.

## Overview

This repository contains the datasets and scripts used in the study "A Deconstruction of Methods to Derive One-Point Lensing Statistics." It provides tools and analysis for evaluating different methods, specifically N-Body, [PINOCCHIO](https://github.com/pigimonaco/Pinocchio), and [turboGL](https://github.com/valerio-marra/turboGL), for simulating lensing probability density functions (PDFs) in various regimes. For N-Body and PINOCCHIO, [SLICER](https://github.com/TiagoBsCastro/SLICER) was used to produce the lensing maps. The focus is on dark matter-dominated models and the utility of these methods in weak and strong lensing scenarios. 

## Repository Structure

LensingMethodsDeconstruction/
├── PDFs
│ ├── gamma
│ │ ├── NBody
│ │ ├── PINOCCHIO
│ │ └── PINOCCHIO_halos
│ ├── kappa
│ │ ├── NBody
│ │ ├── PINOCCHIO
│ │ └── PINOCCHIO_halos
│ ├── magn
│ │ ├── NBody
│ │ ├── PINOCCHIO
│ │ └── PINOCCHIO_halos
│ └── mu
│ ├── NBody
│ ├── PINOCCHIO
│ └── PINOCCHIO_halos
└── scripts
└── PDF
├── Box3
│ ├── Convergence
│ ├── Magnification
│ └── Shear
└── Box4
├── Convergence
├── Magnification
└── Shear


### Directory Descriptions

- **PDFs**: Contains lensing probability density functions (PDFs) for various lensing observables:
  - **gamma** (Shear)
  - **kappa** (Convergence)
  - **magn** (Magnitude)
  - **mu** (Magnification)
  
  Each subdirectory includes data from N-body simulations and the Pinocchio method, detailing PDFs as two columns: `x` and either `dP/dX` (for convergence) or `dP/dLogX` (for magnification, shear, and magnitude).

- **scripts**: Includes Python scripts and data used to extract PDFs from the Magneticum simulations. It also contains scripts to estimate the regimes in each variable where baryonic effects are minimal, supporting the analysis of data integrity and applicability in lensing studies.

## Usage

To use the scripts and data in this repository, navigate to the respective directory and refer to the specific README files within those directories for detailed instructions on executing the scripts or analyzing the data.

## Contributing

Contributions to this repository are welcome. Please fork the repository and submit pull requests with your suggested changes.

## Citation

If you use the data or scripts provided in this repository in your research, please cite the following paper:

- Alfradique, V., Castro, T.,... "A Deconstruction of Methods to Derive One-Point Lensing Statistics." (Year). Journal.

## License

This project is licensed under the GPL3 - see the [LICENSE](./LICENSE) file for details.

