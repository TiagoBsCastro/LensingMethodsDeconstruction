# LensingMethodsDeconstruction

[![arXiv](https://img.shields.io/badge/arXiv-2405.00147-brightgreen)](https://arxiv.org/abs/2405.00147) [![DOI](https://zenodo.org/badge/790708834.svg)](https://zenodo.org/doi/10.5281/zenodo.11093019)

<div align="justify">

Data and scripts from "A Deconstruction of Methods to Derive One-Point Lensing Statistics" for evaluating different methods for lensing PDFs in weak and strong regimes.

## Overview

This repository contains the datasets and scripts used in the study "A Deconstruction of Methods to Derive One-Point Lensing Statistics." It provides tools and analysis for evaluating different methods, specifically N-Body, [PINOCCHIO](https://github.com/pigimonaco/Pinocchio), and [turboGL](https://github.com/valerio-marra/turboGL), for simulating lensing probability density functions (PDFs) in various regimes. For N-Body and PINOCCHIO, [SLICER](https://github.com/TiagoBsCastro/SLICER) was used to produce the lensing maps. The focus is on dark matter-dominated models and the utility of these methods in weak and strong lensing scenarios. 

## Repository Structure

```plaintext
LensingMethodsDeconstruction/
├── PDFs
│   ├── gamma
│   │   ├── NBody
│   │   ├── PINOCCHIO
│   │   └── PINOCCHIO_halos
│   ├── kappa
│   │   ├── NBody
│   │   ├── PINOCCHIO
│   │   ├── PINOCCHIO_halos
│   │   └── turboGL
│   │       ├── z=0.96
│   │       │   └── 1.76_arcsec
│   │       ├── z=1.98
│   │       │   └── 1.76_arcsec
│   │       ├── z=3.08
│   │       │   └── 1.76_arcsec
│   │       └── z=4.90
│   │           └── 1.76_arcsec
│   ├── magn
│   │   ├── NBody
│   │   ├── PINOCCHIO
│   │   └── PINOCCHIO_halos
│   └── mu
│       ├── NBody
│       ├── PINOCCHIO
│       └── PINOCCHIO_halos
└── scripts
    └── PDF
        ├── Box3
        │   ├── Convergence
        │   ├── Magnification
        │   └── Shear
        └── Box4
            ├── Convergence
            ├── Magnification
            └── Shear
```

### Directory Descriptions

- **PDFs**: Contains lensing probability density functions (PDFs) for various lensing observables:
  - **gamma** (Shear)
  - **kappa** (Convergence)
  - **magn** (Magnitude)
  - **mu** (Magnification)
  
Each subdirectory includes data from N-body simulations and the Pinocchio method, detailing PDFs as two columns: `x` and either `dP/dX` (for convergence) or `dP/dLogX` (for magnification, shear, and magnitude).

- **scripts**: Includes Python scripts and data used to extract PDFs from the [Magneticum](https://magneticum.org) simulations. It also contains scripts to estimate the regimes in each variable where baryonic effects are minimal, supporting the analysis of data integrity and applicability in lensing studies.

## Usage

To use the scripts and data in this repository, navigate to the respective directory and refer to the specific [README](./scripts/README.md) file within the directory for detailed instructions on executing the scripts or analyzing the data.

## Contributing

Contributions to this repository are welcome. Please fork the repository and submit pull requests with your suggested changes.

## Citation

If you use the data or scripts provided in this repository in your research, please cite the following paper:

@article{Alfradique:2024fkb,
    author = "Alfradique, Viviane and Castro, Tiago and Marra, Valerio and Quartin, Miguel and Giocoli, Carlo and Monaco, Pierluigi",
    title = "{A deconstruction of methods to derive one-point lensing statistics}",
    eprint = "2405.00147",
    archivePrefix = "arXiv",
    primaryClass = "astro-ph.CO",
    month = "4",
    year = "2024"
}

## License

This project is licensed under the GPL3 - see the [LICENSE](./LICENSE) file for details.

</div>

