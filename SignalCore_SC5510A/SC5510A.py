# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:27:31 2020

@author: Caleb Jordan
"""

import ctypes
    
class date(ctypes.Structure):
    _fields_ = [
        ('year', ctypes.c_ubyte),
        ('month', ctypes.c_ubyte),
        ('day', ctypes.c_ubyte),
        ('hour', ctypes.c_ubyte)
    ]

class deviceInfo_t(ctypes.Structure):
    """
    Structure definition for device info
    """
    _fields_ = [('product_serial_number', ctypes.c_ulong),
                ('hardware_revision', ctypes.c_float),
                ('firmware_revision', ctypes.c_float),
                ('man_date', date)]
    
    def print_params(self):
        print('\n-Device Info-\n'
              + f'\tproduct_serial_number: {self.product_serial_number:x}\n'
              + f'\thardware_revision: {self.hardware_revision:.2f}\n'
              + f'\tfirmware_revision: {self.firmware_revision:.2f}\n'
              + f'\tman_date: {self.man_date.year}'
              + f'-{self.man_date.month}'
              + f'-{self.man_date.day}'
              + f'-{self.man_date.hour}\n'
              )

class operateStatus_t(ctypes.Structure):
    """
    Structure definition for operate status
    """

    _fields_ = [
        ('rf1_lock_mode', ctypes.c_ubyte),
        ('rf1_loop_gain', ctypes.c_ubyte),
        ('device_access', ctypes.c_ubyte),
        ('rf2_standby', ctypes.c_ubyte),
        ('rf1_standby', ctypes.c_ubyte),
        ('auto_pwr_disable', ctypes.c_ubyte),
        ('alc_mode', ctypes.c_ubyte),
        ('rf1_out_enable', ctypes.c_ubyte),
        ('ext_ref_lock_enable', ctypes.c_ubyte),
        ('ext_ref_detect', ctypes.c_ubyte),
        ('ref_out_select', ctypes.c_ubyte),
        ('list_mode_running', ctypes.c_ubyte),
        ('rf1_mode', ctypes.c_ubyte),
        ('over_temp', ctypes.c_ubyte),
        ('pxi_clk_enable', ctypes.c_ubyte),
        ('harmonic_ss', ctypes.c_ubyte)
    ]

class listMode_t(ctypes.Structure):
    """
    Structure definition for list mode
    """
    _fields_ = [
        ('sss_mode', ctypes.c_ubyte),
        ('sweep_dir', ctypes.c_ubyte),
        ('tri_waveform', ctypes.c_ubyte),
        ('hw_trigger', ctypes.c_ubyte),
        ('step_on_hw_trigger', ctypes.c_ubyte),
        ('return_to_start', ctypes.c_ubyte),
        ('trig_out_enable', ctypes.c_ubyte),
        ('trig_out_on_cycle', ctypes.c_ubyte)
    ]

class pllStatus_t(ctypes.Structure):
    """
    Structure definition for PLL status
    """
    _fields_ = [
        ('sum_pll_ld', ctypes.c_ubyte),
        ('crs_pll_ld', ctypes.c_ubyte),
        ('fine_pll_ld', ctypes.c_ubyte),
        ('crs_ref_pll_ld', ctypes.c_ubyte),
        ('crs_aux_pll_ld', ctypes.c_ubyte),
        ('ref_100_pll_ld', ctypes.c_ubyte),
        ('ref_10_pll_ld', ctypes.c_ubyte),
        ('rf2_pll_ld', ctypes.c_ubyte)
    ]

class deviceStatus_t(ctypes.Structure):
    """
    Structure definition for device status
    """
    _fields_ = [
        ('list_mode', listMode_t),
        ('operate_status', operateStatus_t),
        ('pll_status', pllStatus_t)
    ]

    def print_params(self):
        print('\n-Device Status-\n'
                + '\tlist_mode:\n'
                + f'\t\tsss_mode: {self.list_mode.sss_mode}\n'
                + f'\t\tsweep_dir: {self.list_mode.sweep_dir}\n'
                + f'\t\ttri_waveform: {self.list_mode.tri_waveform}\n'
                + f'\t\thw_trigger: {self.list_mode.hw_trigger}\n'
                + f'\t\tstep_on_hw_trigger: {self.list_mode.step_on_hw_trigger}\n'
                + f'\t\treturn_to_start: {self.list_mode.return_to_start}\n'
                + f'\t\ttrig_out_enable: {self.list_mode.trig_out_enable}\n'
                + f'\t\ttrig_out_on_cycle: {self.list_mode.trig_out_on_cycle}\n'
                + '\toperate_status:\n'
                + f'\t\trf1_lock_mode: {self.operate_status.rf1_lock_mode}\n'
                + f'\t\trf1_loop_gain: {self.operate_status.rf1_loop_gain}\n'
                + f'\t\tdevice_access: {self.operate_status.device_access}\n'
                + f'\t\trf2_standby: {self.operate_status.rf2_standby}\n'
                + f'\t\trf1_standby: {self.operate_status.rf1_standby}\n'
                + f'\t\tauto_pwr_disable: {self.operate_status.auto_pwr_disable}\n'
                + f'\t\talc_mode: {self.operate_status.alc_mode}\n'
                + f'\t\trf1_out_enable: {self.operate_status.rf1_out_enable}\n'
                + f'\t\text_ref_lock_enable: {self.operate_status.ext_ref_lock_enable}\n'
                + f'\t\text_ref_detect: {self.operate_status.ext_ref_detect}\n'
                + f'\t\tref_out_select: {self.operate_status.ref_out_select}\n'
                + f'\t\tlist_mode_running: {self.operate_status.list_mode_running}\n'
                + f'\t\trf1_mode: {self.operate_status.rf1_mode}\n'
                + f'\t\tover_temp: {self.operate_status.over_temp}\n'
                + f'\t\tpxi_clk_enable: {self.operate_status.pxi_clk_enable}\n'
                + f'\t\tharmonic_ss: {self.operate_status.harmonic_ss}\n'
                + '\tpll_status:\n'
                + f'\t\tsum_pll_ld: {self.pll_status.sum_pll_ld}\n'
                + f'\t\tcrs_pll_ld: {self.pll_status.crs_pll_ld}\n'
                + f'\t\tfine_pll_ld: {self.pll_status.fine_pll_ld}\n'
                + f'\t\tcrs_ref_pll_ld: {self.pll_status.crs_ref_pll_ld}\n'
                + f'\t\tcrs_aux_pll_ld: {self.pll_status.crs_aux_pll_ld}\n'
                + f'\t\tref_100_pll_ld: {self.pll_status.ref_100_pll_ld}\n'
                + f'\t\tref_10_pll_ld: {self.pll_status.ref_10_pll_ld}\n'
                + f'\t\trf2_pll_ld: {self.pll_status.rf2_pll_ld}\n'
                )

class rfParameters_t(ctypes.Structure):
    """
    Structure definition for rf parameters
    """
    _fields_ = [('rf1_freq', ctypes.c_ulonglong),
                ('start_freq', ctypes.c_ulonglong),
                ('stop_freq', ctypes.c_ulonglong),
                ('step_freq', ctypes.c_ulonglong),
                ('sweep_dwell_time', ctypes.c_ulong),
                ('sweep_cycles', ctypes.c_ulong),
                ('buffer_points', ctypes.c_ulong),
                ('rf_level', ctypes.c_float),
                ('rf2_freq', ctypes.c_ushort)]
    
    def print_params(self):
        print('\n-Device RF Params-\n'
              + '\trf1_freq: ' + str(self.rf1_freq) + ' Hz\n'
              + '\tstart_freq: ' + str(self.start_freq) + '\n'
              + '\tstop_freq: ' + str(self.stop_freq) + '\n'
              + '\tstep_freq: ' + str(self.step_freq) + '\n'
              + '\tsweep_dwell_time: ' + str(self.sweep_dwell_time) + '\n'
              + '\tsweep_cycles: ' + str(self.sweep_cycles) + '\n'
              + '\tbuffer_points: ' + str(self.buffer_points) + '\n'
              + '\trf_level: ' + str(self.rf_level) + ' dBm\n'
              + '\trf2_freq: ' + str(self.rf2_freq) + ' MHz')

class SC5510A():
    """
    Class for SignalCore SC5510A rf source
    """
    def __init__(self, address, log=False):
        
        self.address = address
        self.log = log
        
        self._handle = ctypes.c_int(0)
        
        self.LB_DLL = 'C:\\Program Files\\SignalCore\\SC5510A\\api\\scipci\\c\\lib\\x64\\sc5510a.dll'

        try:
            self.lb_dll = ctypes.windll.LoadLibrary(self.LB_DLL)
            
        except Exception as e:
            s = 'Unable to load SignalCore DLL, please put sc5510a.dll in instrumentserver directory ' + str(e)
            raise ValueError(s)
        
    def connect(self):
        """
        Connect to device. Assumes one and only one device is connected.
        """

        # Max devices and descriptor size from header file
        MAXDEVICES = 128
        MAXDESCRIPTORSIZE = 9      
        
        # Create memory pointers
        string_buffers = [ctypes.create_string_buffer(MAXDESCRIPTORSIZE) for i in range(MAXDEVICES)]
        pointers = (ctypes.c_char_p*MAXDEVICES)(*map(ctypes.addressof, string_buffers))
        
        size = ctypes.c_int(0)
        
        # Call dll
        self.lb_dll.sc5510a_search_devices(ctypes.byref(pointers), ctypes.byref(size))
        
        # Parse and print results
        num_devices = size.value
        
        if num_devices > 0:
            print(f'{num_devices} SC5510A modules found')
        for i in range(size.value):
            print(f'\nDevice Id: {pointers[i]}')
            
        status = self.lb_dll.sc5510a_open_device(pointers[0], ctypes.byref(self._handle))
        
        if status == 0:
            print('Connected')
        
    def get_status(self):
        """Return status structure
        """
        deviceStatus = deviceStatus_t()
        self.lb_dll.sc5510a_get_device_status(self._handle, ctypes.byref(deviceStatus))
        deviceStatus.print_params()
        return deviceStatus
        
    def get_rf_params(self):
        """Return rf parameter structure
        """
        rfParameters = rfParameters_t()
        self.lb_dll.sc5510a_get_rf_parameters(self._handle, ctypes.byref(rfParameters))
        rfParameters.print_params()
        return rfParameters
        
    def get_device_info(self):
        """Return device info structure
        """
        deviceInfo = deviceInfo_t()
        self.lb_dll.sc5510a_get_device_info(self._handle, ctypes.byref(deviceInfo))
        deviceInfo.print_params()
        return deviceInfo
        
    def get_frequency(self):
        """Get RF frequency in Hz"""
        rfParameters = rfParameters_t()
        self.lb_dll.sc5510a_get_rf_parameters(self._handle, ctypes.byref(rfParameters))
        return float(rfParameters.rf1_freq)
        
    def set_frequency(self, freq_Hz):
        """Set frequency in Hz"""
        return self.lb_dll.sc5510a_set_freq(self._handle, ctypes.c_ulonglong(int(freq_Hz)))
    
    def get_power(self):
        """Returns RF power in dBm"""
        rfParameters = rfParameters_t()
        self.lb_dll.sc5510a_get_rf_parameters(self._handle, ctypes.byref(rfParameters))
        return float(rfParameters.rf_level)
    
    def set_power(self, power_dBm):
        """Set RF Power (dBm)"""
        return self.lb_dll.sc5510a_set_level(self._handle, ctypes.c_float(power_dBm))
    
    def get_output(self):
        """Get RF Output (1 or 0)"""
        rfParameters = rfParameters_t()
        self.lb_dll.sc5510a_get_rf_parameters(self._handle, ctypes.byref(rfParameters))
        return(rfParameters.rfEnable)
    
    def set_output(self, output):
        """Set RF Output"""
        return self.lb_dll.sc5510a_set_output(self._handle, ctypes.c_uint8(output))
    
    def get_temperature(self):
        """Get temperature of module"""
        temp = ctypes.c_float()
        self.lb_dll.sc5510a_get_temperature(self._handle, ctypes.byref(temp))
        return temp.value
    
    def set_clock_ref(self, lockExtRef, enableRefOut, enable100, enablePXI10):
        """Set Clock and Reference Values
        :lockExtRef:    Whether to lock to an external reference
        :enableRefOut:  Enables the reference output port
        :enable100:     If enableRefOut=1, ref is 10 MHz. Change to 1 to output 100 MHz
        :enablePXI10:   PXI 10 MHz output 
        """
        self.lb_dll.sc5510a_set_clock_reference(self._handle, 
                                              ctypes.c_uint8(lockExtRef),
                                              ctypes.c_uint8(enableRefOut),
                                              ctypes.c_uint8(enable100),
                                              ctypes.c_uint8(enablePXI10))