# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 2018

@author: Olivier Pare Labrosse
"""

from scipy.io import loadmat
from IPython import get_ipython
import numpy as np
import scipy as sp
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import transforms
from glob import glob
import pickle

class TAspectrum:
    def __init__(self):
        self.Nwavelength = 0                           # Default value for the Hamamatsu detector is 2059
        self.Ntimedelays = 0
        self.wavelength = np.array([])
        self.timedelays = np.array([])
        self.spectrum = np.array([])
        
        self.PumpPower = 0
        self.PowerUnits = "uJ"
        self.PumpWavelength = 0
        self.PumpSpectrumPath = "N/A"


        self.folder = "N/A"                       
        self.filename = "N/A"
        
        
    def correct_GVD(self, algo = "shift"):
        if algo == "shift":
            print("Ask Kamil.")
        elif algo == "fft":
            print("Ask me later.")
        
    def __call__(self):
        print("Description of the TA spectrum/experiment here")
        self.SmallDict = {
                "Number of Wavelengths": self.Nwavelength,
                "Number of Time Points": self.Ntimedelays,
                "Pump Power (" + self.PowerUnits + ")": self.PumpPower,
                "Pump Wavelength": self.PumpWavelength,
                "Pump Spectrum Path": self.PumpSpectrumPath,
                "File Path": self.folder + self.filename }

        get_ipython().run_line_magic('matplotlib', 'inline')
        try:
            self.plot()
        except:
            pass
        get_ipython().run_line_magic('matplotlib', 'qt5')
        return self.SmallDict
    
    def set_pump_wavelength(self,PumpWavelength):
        self.PumpWavelength = PumpWavelength
        print("Pump Wavelength set to : "+ str(self.PumpWavelength) + " nm")
    def get_pump_wavelength(self):
        return self.PumpWavelength
        
    def get_metadata_from_file(self):
        A = loadmat(self.folder + self.filename)
        data = A["out"]
        self.wavelength = np.round(data[1:,0],1)
        self.wavelength = self.wavelength[:-1]
        self.timedelays = data[0,1:]/1000
        self.Nwavelength = len(self.wavelength)
        self.Ntimedelays = len(self.timedelays)      
        print("Metadata successfully acquired from : " + self.folder + self.filename)
        
    def load_spectrum(self):
        A = loadmat(self.folder + self.filename)
        data = A["out"]
        self.spectrum = np.flipud(data[1:-1,1:].transpose())
        
    def plot(self):
        lim = [self.wavelength[0],self.wavelength[-1],self.timedelays[0],self.timedelays[-1]]
        plt.imshow(self.spectrum,aspect = 5,extent=lim)
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Time delay (ps)")
        plt.show()
        
    
        
        