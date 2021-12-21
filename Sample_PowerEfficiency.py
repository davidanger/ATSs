# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:52:35 2021

@author: DavidAnger
"""

import Driver
import time
import pyvisa
import numpy

PS1 = Driver.E3631A()
PS1._ser = pyvisa.ResourceManager().open_resource('USB0::0x2A8D::0x1102::MY59003498::0::INSTR')

LD1 = Driver.C6312A()
LD1._ser = pyvisa.ResourceManager().open_resource('ASRL6::INSTR')

setvin = [2.5,3.3,5.5]
setiout = numpy.arange(0.1,0.2,0.002)


PS1.begin()
LD1.begin()

file = open('EFF_out.txt', 'w')

LD1.set_mode('CCL')
time.sleep(0.1)
LD1.set_cc(0, setiout[0])

for i in range(setvin.__len__()):
    PS1.set_vi('CH1', setvin[i], 5.0)
    for j in range(setiout.__len__()):
        LD1.set_fast_cc(setiout[j], setiout[j])
        time.sleep(0.5)
        vvin = PS1.measure_v('CH1')
        viin = PS1.measure_i('CH1')
        vvout = LD1.measure_v()
        viout = LD1.measure_i()
        veff = vvout*viout/vvin/viin
        file.write('VIN '+str(vvin)+' IIN '+str(viin)+' VOUT '+str(vvout)+' IOUT '+str(viout)
                   +' EFF '+str(veff)+'\n')

file.close()

LD1.close()
PS1.close()    
