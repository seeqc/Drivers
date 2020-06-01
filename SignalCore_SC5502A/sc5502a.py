# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:27:31 2020

@author: Caleb Jordan
"""

import ctypes
    
class deviceInfo_t(ctypes.Structure):
    """
    Structure definition for device info
    """
    _fields_ = [('productSerialNumber', ctypes.c_uint32),
                ('rfModuleSerialNumber', ctypes.c_uint32),
                ('firmwareRevision', ctypes.c_float),
                ('synthHardwareRevision', ctypes.c_float),
                ('signalHardwareRevision', ctypes.c_float),
                ('calDate', ctypes.c_uint32),
                ('manDate', ctypes.c_uint32)]
    
    def print_params(self):
        print('\n-Device Info-\n'
              + f'\tproductSerialNumber: {self.productSerialNumber:x}\n'
              + f'\trfModuleSerialNumber: {self.rfModuleSerialNumber:x}\n'
              + f'\tfirmwareRevision: {self.firmwareRevision:.1f}\n'
              + f'\tsynthHardwareRevision: {self.synthHardwareRevision}\n'
              + f'\tsignalHardwareRevision: {self.signalHardwareRevision}\n'
              + f'\tcalDate (Y-M-D-H): {(self.calDate & 0xFF000000) >> 24}'
              + f'-{(self.calDate & 0x00FF0000) >> 16}'
              + f'-{(self.calDate & 0x0000FF00) >> 8}'
              + f'-{(self.calDate & 0x000000FF)}\n'
              + f'\tmanDate (Y-M-D-H): {(self.manDate & 0xFF000000) >> 24}'
              + f'-{(self.manDate & 0x00FF0000) >> 16}'
              + f'-{(self.manDate & 0x0000FF00) >> 8}'
              + f'-{(self.manDate & 0x000000FF)}\n'
              )
    
    
class deviceStatus_t(ctypes.Structure):
    """
    Structure definition for device status
    """
    _fields_ = [('tcxoPllLock', ctypes.c_uint8),
                ('vcxoPllLock', ctypes.c_uint8),
                ('finePllLock', ctypes.c_uint8),
                ('coarsePllLock', ctypes.c_uint8),
                ('sumPllLock', ctypes.c_uint8),
                ('extRefDetected', ctypes.c_uint8),
                ('refClkOutEnable', ctypes.c_uint8),
                ('extRefLockEnable', ctypes.c_uint8),
                ('alcOpen', ctypes.c_uint8),
                ('fastTuneEnable', ctypes.c_uint8),
                ('standbyEnable', ctypes.c_uint8),
                ('rfEnable', ctypes.c_uint8),
                ('pxiClkEnable', ctypes.c_uint8)]
    
    def print_params(self):
        print('\n-Device Status-\n'
              + '\ttcxoPllLock: ' + str(self.tcxoPllLock) + '\n'
              + '\tvcxoPllLock: ' + str(self.vcxoPllLock) + '\n'
              + '\tfinePllLock: ' + str(self.finePllLock) + '\n'
              + '\tcoarsePllLock: ' + str(self.coarsePllLock) + '\n'
              + '\tsumPllLock: ' + str(self.sumPllLock) + '\n'
              + '\textRefDetected: ' + str(self.extRefDetected) + '\n'
              + '\trefClkOutEnable: ' + str(self.refClkOutEnable) + '\n'
              + '\textRefLockEnable: ' + str(self.extRefLockEnable) + '\n'
              + '\talcOpen: ' + str(self.alcOpen) + '\n'
              + '\tfastTuneEnable: ' + str(self.fastTuneEnable) + '\n'
              + '\tstandbyEnable: ' + str(self.standbyEnable) + '\n'
              + '\trfEnable: ' + str(self.rfEnable) + '\n'
              + '\tpxiClkEnable: ' + str(self.pxiClkEnable)
              )
    
    
class rfParameters_t(ctypes.Structure):
    """
    Structure definition for rf parameters
    """
    _fields_ = [('frequency', ctypes.c_longlong),
                ('powerLevel', ctypes.c_float),
                ('rfEnable', ctypes.c_uint8),
                ('alcOpen', ctypes.c_uint8),
                ('autoLevelEnable', ctypes.c_uint8),
                ('fastTune', ctypes.c_uint8),
                ('tuneStep', ctypes.c_uint8),
                ('referenceSetting', ctypes.c_uint8)]
    
    def print_params(self):
        print('\n-Device RF Params-\n'
              + '\tfrequency: ' + str(self.frequency) + '\n'
              + '\tpowerLevel: ' + str(self.powerLevel) + '\n'
              + '\trfEnable: ' + str(self.rfEnable) + '\n'
              + '\talcOpen: ' + str(self.alcOpen) + '\n'
              + '\tautoLevelEnable: ' + str(self.autoLevelEnable) + '\n'
              + '\tfastTune: ' + str(self.fastTune) + '\n'
              + '\ttuneStep: ' + str(self.tuneStep) + '\n'
              + '\treferenceSetting: ' + str(self.referenceSetting))
 


class SC5502A():
    """
    Class for SignalCore SC5502A rf source
    """
    def __init__(self, address, log=False):
        
        self.address = address
        self.log = log
        
        self._handle = ctypes.c_int(0)
        
        self.LB_DLL = 'C:\\Program Files\\SignalCore\\SC5502A\\api\\c\\lib\\x64\\sc5502a.dll'

        try:
            self.lb_dll = ctypes.windll.LoadLibrary(self.LB_DLL)
            
        except Exception as e:
            s = 'Unable to load SignalCore DLL, please put sc5502a.dll in instrumentserver directory ' + str(e)
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
        self.lb_dll.sc5502a_SearchDevices(ctypes.byref(pointers), ctypes.byref(size))
        
        # Parse and print results
        num_devices = size.value
        
        if num_devices > 0:
            print(f'{num_devices} SC5502A modules found')
        for i in range(size.value):
            print(f'\nDevice Id: {pointers[i]}')
            
        status = self.lb_dll.sc5502a_OpenDevice(pointers[0], ctypes.byref(self._handle))
        
        if status == 0:
            print('Connected')
        
    def get_status(self):
        """Return status structure
        """
        deviceStatus = deviceStatus_t()
        self.lb_dll.sc5502a_GetDeviceStatus(self._handle, ctypes.byref(deviceStatus))
        deviceStatus.print_params()
        return deviceStatus
        
    def get_rf_params(self):
        """Return rf parameter structure
        """
        rfParameters = rfParameters_t()
        self.lb_dll.sc5502a_GetRfParameters(self._handle, ctypes.byref(rfParameters))
        rfParameters.print_params()
        return rfParameters
        
    def get_device_info(self):
        """Return device info structure
        """
        deviceInfo = deviceInfo_t()
        self.lb_dll.sc5502a_GetDeviceInfo(self._handle, ctypes.byref(deviceInfo))
        deviceInfo.print_params()
        return deviceInfo
        
    def get_frequency(self):
        """Get RF frequency in Hz"""
        rfParameters = rfParameters_t()
        self.lb_dll.sc5502a_GetRfParameters(self._handle, ctypes.byref(rfParameters))
        return float(rfParameters.frequency)
        
    def set_frequency(self, freq_Hz):
        """Set frequency in Hz"""
        return self.lb_dll.sc5502a_SetFrequency(self._handle, ctypes.c_ulonglong(int(freq_Hz)))
    
    def get_power(self):
        """Returns RF power in dBm"""
        rfParameters = rfParameters_t()
        self.lb_dll.sc5502a_GetRfParameters(self._handle, ctypes.byref(rfParameters))
        return float(rfParameters.powerLevel)
    
    def set_power(self, power_dBm):
        """Set RF Power (dBm)"""
        return self.lb_dll.sc5502a_SetPowerLevel(self._handle, ctypes.c_float(power_dBm))
    
    def get_output(self):
        """Get RF Output (1 or 0)"""
        rfParameters = rfParameters_t()
        self.lb_dll.sc5502a_GetRfParameters(self._handle, ctypes.byref(rfParameters))
        return(rfParameters.rfEnable)
    
    def set_output(self, output):
        """Set RF Output"""
        return self.lb_dll.sc5502a_SetRfOutput(self._handle, ctypes.c_uint8(output))
    
    def get_temperature(self):
        """Get temperature of module"""
        temp = ctypes.c_float()
        self.lb_dll.sc5502a_GetTemperature(self._handle, ctypes.byref(temp))
        return temp.value
    
    def set_clock_ref(self, lockExtRef, enableRefOut, enable100, enablePXI10):
        """Set Clock and Reference Values
        :lockExtRef:    Whether to lock to an external reference
        :enableRefOut:  Enables the reference output port
        :enable100:     If enableRefOut=1, ref is 10 MHz. Change to 1 to output 100 MHz
        :enablePXI10:   PXI 10 MHz output 
        """
        self.lb_dll.sc5502a_SetClockReference(self._handle, 
                                              ctypes.c_uint8(lockExtRef),
                                              ctypes.c_uint8(enableRefOut),
                                              ctypes.c_uint8(enable100),
                                              ctypes.c_uint8(enablePXI10))