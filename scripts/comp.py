import os
import numpy as np

def read_pdf_file(file_path):
    """Reads a PDF file and returns it as a NumPy array."""
    return np.loadtxt(file_path)

def find_peak_indices(pdf_data):
    """Finds the index of the peak in the PDF data."""
    peak_index = np.argmax(pdf_data[:, 1])
    return peak_index

def moving_average(data, width=10):
    """
    Calculates the moving average of the given data with the same length as the input.

    :param data: NumPy array containing the data.
    :param width: Width of the moving average window.
    :return: NumPy array of the moving average values.
    """
    if width < 1:
        raise ValueError("Width must be at least 1.")

    # Ensure width is odd for symmetric averaging
    if width % 2 == 0:
        width += 1

    # Convolve with a ones array of length 'width' and divide by width for the average
    return np.convolve(data, np.ones(width)/width, 'same')

def pdf_width(pdf, jac=1.0):
    """
    Calculates the width of the PDF based on one standard deviation from the mean, in bin units.

    :param pdf: NumPy array containing the PDF data in two columns (x, y).
    :param jac: Jacobian of the relation between the first axis and the variable of the probability function. (default 1.0)
    :return: Width of the PDF based on standard deviation, in pixel units.
    """
    # Calculate weighted x values (assuming y represents probabilities)
    weight      = (pdf * jac)[1:, 1] * np.diff(pdf[:, 0])
    weighted_x  = pdf[1:, 0] * weight
    weighted_x2 = pdf[1:, 0]**2 * weight

    # Calculate the mean and standard deviation of the weighted x values
    mean = np.sum(weighted_x)/np.sum(weight)
    std = np.sqrt(np.sum(weighted_x2)/np.sum(weight) - mean**2)

    # Find indices where x is one standard deviation away from the mean
    lower_bound_index = np.argmin(np.abs(pdf[:, 0] - (mean - std)))
    upper_bound_index = np.argmin(np.abs(pdf[:, 0] - (mean + std)))

    # Calculate and return the width in pixel units
    width = upper_bound_index - lower_bound_index
    return width

def compare_pdfs(box, resolution, threshold, base_path='PDF'):
    """Compares PDFs of 'dm' and 'bao' files for a given box and resolution."""

    categories, vs = (['Convergence', 'Magnification', 'Shear'], ['kappa', 'log_mu', 'log_gamma'])

    for category, var in zip(categories, vs):

        pattern_dm = f'{base_path}/{box}/{category}/{var}_hr_dm_{resolution}_pdf_{{}}.txt'
        pattern_bao = f'{base_path}/{box}/{category}/{var}_hr_bao_{resolution}_pdf_{{}}.txt'

        for z in range(1, 6):

            file_dm = pattern_dm.format(f'z{z}')
            file_bao = pattern_bao.format(f'z{z}')

            if os.path.exists(file_dm) and os.path.exists(file_bao):
                pdf_dm = read_pdf_file(file_dm) 
                # Get the PDF width
                if 'log' in 'var':
                    jac = 1.0/pdf_dm[:, 0]
                else:
                    jac = 1.0
                wdm = int(pdf_width(pdf_dm, jac)//10)
                pdf_dm[:, 1] = moving_average(pdf_dm[:, 1], wdm)
                pdf_bao = read_pdf_file(file_bao)
                # Get the PDF width
                if 'log' in 'var':
                    jac = 1.0/pdf_bao[:, 0]
                else:
                    jac = 1.0
                wbao = int(pdf_width(pdf_bao, jac)//10)
                pdf_bao[:, 1] = moving_average(pdf_bao[:, 1], wbao)

                # Calculate relative difference
                relative_diff = 2 * np.abs(pdf_dm[:, 1] - pdf_bao[:, 1]) / np.abs(pdf_dm[:, 1] + pdf_bao[:, 1])
                relative_diff = np.nan_to_num(relative_diff)  # Handle division by zero

                # Find the peak index
                peak_index = find_peak_indices(pdf_dm)

                # Find the first two values around the peak where the relative difference crosses the threshold
                threshold_indices = np.where(relative_diff > threshold)[0]
                near_peak_indices = [0, -1]                
                if np.any(threshold_indices < peak_index):
                    near_peak_indices[0] = threshold_indices[threshold_indices<peak_index][np.abs(threshold_indices[threshold_indices<peak_index] - peak_index).argmin()]
                if np.any(threshold_indices>peak_index):
                    near_peak_indices[1] = threshold_indices[threshold_indices>peak_index][np.abs(threshold_indices[threshold_indices>peak_index] - peak_index).argmin()]

                if len(near_peak_indices) > 0:
                    region = pdf_dm[near_peak_indices, 0]
                    if near_peak_indices[0] == 0:
                        region[0] = - np.inf
                    if near_peak_indices[1] == -1:
                        region[1] = np.inf
                    print(f'Box: {box}, Category: {category}, z{z}, Resolution: {resolution}')
                    print(f'First two values around the peak where relative difference < {threshold*100}%:')
                    print(region)
                else:
                    print(f'Box: {box}, Category: {category}, z{z}, Resolution: {resolution}')
                    print(f'No values found near peak with relative difference < {threshold*100}%')

# Example usage
compare_pdfs('Box3', '01.76_arcsec', 0.5)
