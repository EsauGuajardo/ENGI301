"""
--------------------------------------------------------------------------
Sound Conversion
--------------------------------------------------------------------------
License:   
Copyright 2022 Esau Guajardo

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
"""

import numpy as np
from scipy.io import wavfile

def convert(outputFile):

    rate, data = wavfile.read(outputFile)

    fft_data = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(fft_data))

    index = np.argmax(np.abs(fft_data))
    dom_freq = np.abs(freqs[index]*rate)
    
    if(dom_freq < 166.8 and dom_freq > 162.8):
        dom_freq = dom_freq / 2
    elif(dom_freq < 222 and dom_freq > 218):
        dom_freq = dom_freq / 2
    elif(dom_freq < 295.6 and dom_freq > 291.6):
        dom_freq = dom_freq / 2
    elif(dom_freq > 370):
        dom_freq = dom_freq / 2
        
    return dom_freq

# https://www.mathworks.com/help/matlab/ref/fft.html
# https://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python
