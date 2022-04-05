"""
--------------------------------------------------------------------------
Main Run Script
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

import audio_recording as audio
import sound_conversion as conversion
import spi_screen as display
import buttons
import time
CENTER = 4

import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    disp = display.SPI_Display()
    disp.text(["Esau's", "Guitar","Tuner!"], fontsize=40, justify=CENTER, align=CENTER)
    
    button = buttons.Buttons()
    
    record_flag = False
    note_to_check = None
    delay = 2
    
    e2_target_note = 82.4
    a2_target_note = 110
    d3_target_note = 146.8
    g3_target_note = 196
    b3_target_note = 246.9
    e4_target_note = 329.6
    
    while(record_flag == False):
        
        if(GPIO.input(button.e2) == 0):
            record_flag = True
            note_to_check = e2_target_note
        
        if(GPIO.input(button.a2) == 0):
            record_flag = True
            note_to_check = a2_target_note
            
        if(GPIO.input(button.d3) == 0):
            record_flag = True
            note_to_check = d3_target_note

        if(GPIO.input(button.g3) == 0):
            record_flag = True
            note_to_check = g3_target_note

        if(GPIO.input(button.b3) == 0):
            record_flag = True
            note_to_check = b3_target_note

        if(GPIO.input(button.e4) == 0):
            record_flag = True
            note_to_check = e4_target_note

        if(record_flag == True):
            disp.text(["Listening..."], fontsize=40, justify=CENTER, align=CENTER)
            audio.record("output.wav")
            dom_freq = conversion.convert("output.wav")
            print(dom_freq)
            
            if(dom_freq < note_to_check - 1):
                disp.text(["Note", "Is","Flat"], fontsize=40, fontcolor=(255,255,0), justify=CENTER, align=CENTER)
                time.sleep(delay)
                
            elif(dom_freq > note_to_check + 1):
                disp.text(["Note", "Is","Sharp"], fontsize=40, fontcolor=(255,0,0), justify=CENTER, align=CENTER)
                time.sleep(delay)
                
            else:
                disp.text(["String", "In","Tune!"], fontsize=40, fontcolor=(0,255,0), justify=CENTER, align=CENTER)
                time.sleep(delay)
            
            record_flag = False
            note_to_check = None
            disp.text(["Esau's", "Guitar","Tuner!"], fontsize=40, justify=CENTER, align=CENTER)
    
        
        time.sleep(0.1)