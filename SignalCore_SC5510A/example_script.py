# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:38:00 2020

@author: Caleb Jordan
"""

from sc5510a import SC5510A

s1 = SC5510A(b'100024C1')

s1.connect()

# s1.set_clock_ref(0, 0, 1, 0)
freq = 3.5e9
s1.set_frequency(freq)
print(f'Set Frequency: {freq}\nGet Frequency: {s1.get_frequency()}\n')

pwr = -10
s1.set_power(pwr)
print(f'Set Power: {pwr}\nGet Power: {s1.get_power()}\n')


s1.set_output(1)

# s1.get_device_info()
# s1.get_status()
# s1.get_rf_params()

print(f'Temperature: {s1.get_temperature()}')