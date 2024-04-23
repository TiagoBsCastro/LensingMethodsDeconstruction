# PDF Analysis Tool

This script provides tools for analyzing probability density functions (PDFs) used in lensing studies, specifically designed to handle data from various simulation methods such as N-Body and PINOCCHIO. It offers functionality for reading PDF data, computing moving averages, and comparing PDFs to determine significant differences.

## Features

- **Read PDF Files**: Loads PDF data from text files into NumPy arrays.
- **Moving Average**: Calculates moving averages to smooth PDF data, with customizable window width.
- **Find Peak Indices**: Identifies the peak position in PDF data.
- **PDF Width Calculation**: Computes the width of a PDF based on its standard deviation.
- **Compare PDFs**: Compares PDFs from different simulation sources and highlights significant differences based on a threshold.

## Requirements

- Python 3.x
- NumPy library

Ensure that Python and NumPy are installed on your system. If NumPy is not installed, you can install it via pip:

```bash
pip install numpy
```

## Usage

Run the Script: Execute the script with the desired parameters to analyze your PDFs. You can modify the example usage at the end of the script to suit your specific analysis needs.

```python
compare_pdfs('Box3', '01.76_arcsec', 0.5)
```

This command compares PDFs for Box3 at a resolution of 01.76_arcsec, with a relative difference threshold of 0.5.

## Script Functions

* read_pdf_file(file_path): Reads a PDF file from the given path.
* find_peak_indices(pdf_data): Returns the index of the peak in the given PDF data.
* moving_average(data, width=10): Calculates the moving average of the data.
* pdf_width(pdf, jac=1.0): Calculates the width of the PDF.
* compare_pdfs(box, resolution, threshold, base_path='PDF'): Main function to compare PDFs across different conditions.
