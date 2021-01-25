#from ctypes import (CDLL, WinDLL,Structure, POINTER,
#                    c_float, c_int, c_ubyte, c_ushort, c_uint, c_ulonglong,
#                    c_void_p, c_char_p, c_char)
import InstrumentDriver
import SC5510A

class Driver(InstrumentDriver.InstrumentWorker):
    """ This class implements a simple signal generator driver"""

    def performOpen(self, options={}):
        """Perform the operation of opening the instrument connection"""
        self.sc=SC5510A.SC5510A(b'100024C1')
        self.sc.connect()

    def performClose(self, bError=False, options={}):
        """Perform the close instrument connection operation"""
        pass
        # self._lib.sc5505a_CloseDevice(self._handle)

    def performSetValue(self, quant, value, sweepRate=0.0, options={}):
        """Perform the Set Value instrument operation.
        
        This function should return the actual value set by the instrument
        
        """
        
        qname = quant.name
        
        # Channel 1
        if qname == 'Frequency Channel 1':
            ret=self.sc.set_frequency(value)
            self._check_return('Frequency Channel 1', ret)
        elif qname == 'Power Channel 1':
            ret= self.sc.set_power(value)
            self._check_return('Power Channel 1', ret)
        elif qname == 'Output Channel 1':
            ret=self.sc.set_output(value)
            self._check_return('Output Channel 1', ret)
        else:
            raise RuntimeError('Unknown attribute %s' % qname)
        return value

    def performGetValue(self, quant, options={}):
        """Perform the Get Value instrument operation"""
        qname = quant.name
        self._lib.sc5505a_StoreCurrentState(self._handle, params)
        if qname == 'Frequency':
            return float(self.sc.get_frequency())
        elif qname == 'Power':
            return float(self.sc.get_power())
        elif qname == 'Output':
            return bool(self.sc.get_output())
        else:
            raise RuntimeError('Unknown attribute %s' % qname)

    def _check_return(self, name, ret_code):
        """Check the return code for library function call.

        """
        if ret_code == 0:
            pass
        else:
            raise RuntimeError('An error occured setting %s: %d' % (name, ret_code))

