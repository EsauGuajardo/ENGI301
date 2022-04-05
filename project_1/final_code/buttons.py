"""
--------------------------------------------------------------------------
Buttons Class
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

import Adafruit_BBIO.GPIO as GPIO

class Buttons():

    e2 = None
    a2 = None
    d3 = None
    g3 = None
    b3 = None
    e4 = None
    
    def __init__(self, e2="P2_3", a2="P2_10", 
                       d3="P2_8", g3="P2_6",
                       b3="P2_4", e4="P2_2"):

        self.e2 = e2
        self.a2 = a2
        self.d3 = d3
        self.g3 = g3
        self.b3 = b3
        self.e4 = e4

        self._setup()
    
    
    def _setup(self):
        
        GPIO.setup(self.e2, GPIO.IN)
        GPIO.setup(self.a2, GPIO.IN)
        GPIO.setup(self.d3, GPIO.IN)
        GPIO.setup(self.g3, GPIO.IN)
        GPIO.setup(self.b3, GPIO.IN)
        GPIO.setup(self.e4, GPIO.IN)