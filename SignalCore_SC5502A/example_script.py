# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:38:00 2020

@author: Caleb Jordan
"""

from sc5502a import SC5502A

s1 = SC5502A(b'100021B8')

s1.connect()

s1.set_clock_ref(0, 0, 1, 0)

s1.set_frequency(3.5e9)

s1.set_power(-13.50)

s1.set_output(1)

s1.get_device_info()
s1.get_status()
s1.get_rf_params()

print(f'Temperature: {s1.get_temperature():.3f}')