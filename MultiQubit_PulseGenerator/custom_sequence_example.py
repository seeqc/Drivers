# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:13:00 2020

@author: check
"""
import numpy as np
import matplotlib.pyplot as plt

import sequence
import pulses
import gates
import qubits

##Define pulses###

pulseA = pulses.Gaussian(True)
pulseA.width = 10e-9
pulseA.plateau = 50e-9
pulseA.frequency = 30e6
pulseA.amplitude = 1

pulseB=pulses.Gaussian(True)
pulseB.plateau = 100e-9
pulseA.width = 10e-9
pulseB.frequency=30e6
pulseB.amplitude = 1

##Create Gates##

gateA = gates.CustomGate(pulseA, 'XY')
gateB = gates.CustomGate(pulseB, 'XY')


##Create Sequence and Add Gates##

test_sequence = sequence.Sequence(1)
test_sequence.add_gate_to_all(gateA)
test_sequence.add_gate_to_all(gateB)
test_sequence.add_gate_to_all(gateA)
test_waveform=sequence.SequenceToWaveforms(1)


### Set Pulse Spacing

test_waveform.dt=100e-9

###Set parameters that would normally be handled by GUI###

test_waveform.n_pts=1e5

test_waveform.trim_start = False
qubit=qubits.Transmon(6e9,4e9,1.83e-25,1,0,0.5)
test_waveform.qubits[0] = qubit
pulse=pulses.Gaussian(True)
pulse.width = 0e-9
pulse.plateau = 0.1e-6
pulse.amplitude = 1
pulse.frequency = 100e6
test_waveform.sample_rate = 1200e6

test_waveform.pulses_1qb_xy[0]=pulse
test_waveform.pulses_1qb_z[0]=pulse

test_waveform.perform_predistortion_z=False

test_waveform.number_readout_waveforms=1
test_waveform.readout_match_main_size=False
test_waveform.readout_i_offset=0
test_waveform.readout_i_offset2=0
test_waveform.readout_q_offset=0
test_waveform.readout_q_offset2=0
test_waveform.readout_predistort=False
test_waveform.readout_trig_duration = 0.0

test_waveform.readout.frequencies[0]=30e6
test_waveform.readout.iq_ratio = 1
test_waveform.readout.iq_skew = 1 * np.pi / 180
test_waveform.readout.n_records = 1

test_waveform.readout_delay = 0

phases = 2 * np.pi * np.array([0.8847060, 0.2043214, 0.9426104, 0.6947334, 0.8752361, 0.2246747,0.6503154, 0.7305004, 0.1309068])


pulse_readout = pulses.Square(complex=True)
pulse_readout.plateau = 500e-9
pulse_readout.frequency=30e6
pulse_readout.amplitude=1
test_waveform.pulses_readout[0] = pulse_readout


###Generate Waveform from Sequence###

waveform=test_waveform.get_waveforms(test_sequence)


plt.plot(np.real(waveform['xy']).T)
