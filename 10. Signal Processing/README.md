
# Signal Processing and Fourier Transforms

Signal processing involves the analysis, modification, and synthesis of signals such as sound, images, and scientific measurements. Fourier Transforms are a powerful tool used in signal processing to transform signals between time and frequency domains. Common applications include audio enhancement, image processing, and communications.

## Fourier Transforms
The Fourier Transform decomposes a function (signal) into its constituent frequencies. It is widely used for analyzing the frequency characteristics of signals.

In Numpy, the `np.fft` module provides functions to perform Fourier Transforms.

```python
import numpy as np

# Time domain signal
time = np.arange(0, 10, 0.1)
signal = np.sin(time)

# Fourier Transform
freq_domain = np.fft.fft(signal)

# Inverse Fourier Transform
time_domain = np.fft.ifft(freq_domain)
```

## Signal Filtering Techniques

Signal filtering is used to remove unwanted components from a signal or to extract useful parts of it.

### Types of Filters
1. **Low-pass Filter**: Allows signals with a frequency lower than a certain cutoff frequency to pass through and reduce the effect of higher frequency signals.
2. **High-pass Filter**: Allows signals with a frequency higher than a certain cutoff frequency to pass through and reduce the effect of lower frequency signals.
3. **Band-pass Filter**: Allows signals within a certain range of frequencies to pass through and reduce the effect of frequencies outside this range.


```python
# Example of a simple low-pass filter:
def low_pass_filter(signal, cutoff_freq, sampling_rate):
    fft_signal = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1/sampling_rate)
    
    filtered_fft_signal = fft_signal.copy()
    filtered_fft_signal[np.abs(frequencies) > cutoff_freq] = 0
    
    filtered_signal = np.fft.ifft(filtered_fft_signal)
    return filtered_signal

# Example usage
sampling_rate = 100  # Hz
cutoff_freq = 5  # Hz
filtered_signal = low_pass_filter(signal, cutoff_freq, sampling_rate)
```

## Discrete Fourier Transforms (DFT) and Inverse DFT

The Discrete Fourier Transform (DFT) converts a finite sequence of equally spaced samples of a function into a same-length sequence of equally spaced samples of the discrete-time Fourier transform (DTFT), which is a complex-valued function of frequency.

### DFT
Numpy provides the `np.fft.fft` function to compute the DFT of a signal.

```python
# Compute DFT
dft_signal = np.fft.fft(signal)
```

### Inverse DFT
To convert back to the time domain,NumPy provides `np.fft.ifft`.

```python
# Compute inverse DFT
time_signal = np.fft.ifft(dft_signal)
```

## Fast Fourier Transforms (FFT)

The Fast Fourier Transform (FFT) is an efficient algorithm to compute the DFT and its inverse. FFT reduces the computational complexity from \(O(N^2)\) to \(O(N \log N)\).

### FFT in Numpy
The `np.fft.fft` function uses the FFT algorithm for fast computation of the DFT.

```python
# Fast Fourier Transform
fft_signal = np.fft.fft(signal)

# Inverse Fast Fourier Transform
ifft_signal = np.fft.ifft(fft_signal)
```

### Practical Example: Noise Reduction
FFT can be used for noise reduction in signals by filtering out high-frequency noise components.

```python
def reduce_noise(signal, cutoff_freq, sampling_rate):
    fft_signal = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1/sampling_rate)
    
    fft_signal[np.abs(frequencies) > cutoff_freq] = 0
    
    clean_signal = np.fft.ifft(fft_signal)
    return clean_signal

# Example usage
noisy_signal = signal + 0.5 * np.random.randn(len(signal))
clean_signal = reduce_noise(noisy_signal, cutoff_freq, sampling_rate)
```

---