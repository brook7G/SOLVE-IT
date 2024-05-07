import numpy as np
from scipy.fft import fft

def computeandPrintFFT(arr):
    # Check if the array is empty
    if not arr:
       print('Empty array')
       return

    # Convert the input list to a numpy array
    numpy_data = np.array(arr)

    # Compute the FFT of the input array using a library form SCIPY 
    fft_result = fft(numpy_data)

    # Compute the magnitude of each component
    magnitude = np.abs(fft_result)

    # Compute the phase of each component
    phase = np.angle(fft_result)

    # Print the results
    for i in range(len(fft_result)):
      print(f"Component {i+1}: Magnitude = {magnitude[i]}, Phase = {phase[i]}")


# Test with the custom test cases
computeandPrintFFT([1+2j, 3+4j, 5+ 6j])
computeandPrintFFT([])
computeandPrintFFT([7+8j])