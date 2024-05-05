#include <iostream>
#include <vector>
#include <complex>
#include <cmath>

// Function to perform Fast Fourier Transform (FFT)
namespace my_fft {
    using namespace std;

    vector<complex<double>> fft(const vector<complex<double>>& input) {
        int n = input.size();
        
        if (n <= 1) // If there's only one or zero numbers, just return what we got
            return input;
        
        vector<complex<double>> even, odd;
        even.reserve(n/2);
        odd.reserve(n/2);
        
        // Divide the input into even and odd indices
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0)
                even.push_back(input[i]);
            else
                odd.push_back(input[i]);
        }
        
        // Doing FFT on even and odd sequences
        vector<complex<double>> even_fft = fft(even);
        vector<complex<double>> odd_fft = fft(odd);
        
        // Combine the results of FFT
        vector<complex<double>> result(n);
        for (int k = 0; k < n/2; k++) {
            complex<double> twiddle = polar(1.0, -2 * M_PI * k / n) * odd_fft[k];
            result[k] = even_fft[k] + twiddle;
            result[k + n/2] = even_fft[k] - twiddle;
        }
        
        return result;
    }
}

int main() {
    using namespace std;
    using namespace my_fft;

    vector<complex<double>> input = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    
    // Call the FFT function
    vector<complex<double>> output = fft(input);
    
    // Print the Fourier transform
    for (const auto& val : output) {
        cout << val << " ";
    }
    cout << endl;
    
    return 0;
}
