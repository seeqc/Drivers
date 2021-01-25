import InstrumentDriver
import numpy as np

#import qcodes as qc
from qcodes_contrib_drivers.drivers.NationalInstruments import PXIe_5654



class Driver(InstrumentDriver.InstrumentWorker):
    """ This class implements a simple signal generator driver"""

    

    def performOpen(self, options={}):
        """Perform the operation of opening the instrument connection"""
        self.sg = PXIe_5654.NI_RFSG("sg1","dev4")


    def performClose(self, bError=False, options={}):
        """Perform the close instrument connection operation"""
        self.sg.close()
        
        


    def performSetValue(self, quant, value, sweepRate=0.0, options={}):
        """Perform the Set Value instrument operation. This function should
        return the actual value set by the instrument"""
    
        if quant.name == 'frequency':
            self.sg[quant.name].set (value * 1e9)
            
        else:
            
            self.sg[quant.name].set(value)
            
        # just return the value
        return self.sg[quant.name].get()


    def performGetValue(self, quant, options={}):
        """Perform the Get Value instrument operation"""
        # proceed depending on quantity
        
        return self.sg[quant.name].get()
        
        


