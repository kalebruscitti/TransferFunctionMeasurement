import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.constants import *
from scipy.interpolate import interp1d

'''
Generate Transfer Function

Script to generate a CSV file which contains the Amplitude and Phase changes due to a given Transfer Function.

CSV File is then intended to be loaded into LabVIEW to send to the AWG.

Edit the variables 'amplitude' and 'phase' in the TransferFunction function below.

'''

# Define the Frequency Range to generate points for
lowest_frequency = 5*mega
highest_frequency = 200*mega
frequency_step_size = 122950*20
# It is best to set this to the cantilever resonance frequency so that your frequency points match the frequencies that the AWG will sample.

filename = 'fun_xfer.csv'
verbose = False # set to True to see details, False to run faster
load_from_file = False # set to True if loading xfer function from a file.

'''
def TransferFunction(f):
    data = pd.read_csv("data/awg_hand_measurements.csv", header=None, names=["Frequency (Hz)","Amplitude (V)", "Phase (deg)"])
    ampf = interp1d(data.iloc[:,0].values[:15], data.iloc[:,1].values[:15], kind='quadratic', bounds_error=False, fill_value=1)
    amplitude = ampf(f)  # Put the Amplitude Transfer Function here
    phase = f/(10*mega) # Put the Phase Transfer Function here
    return amplitude, phase
'''
def load_from_file(path):
    data = pd.read_csv(path, header=None, names=["Frequency (Hz)","Amplitude (V)", "Phase (deg)"])
    ampf = interp1d(data.iloc[:,0].values[:15], data.iloc[:,1].values[:15], kind='quadratic', bounds_error=False, fill_value=1)
    phif = interp1d(data.iloc[:,0].values[:15], np.zeros(15), kind='quadratic', bounds_error=False, fill_value=1)
    return ampf, phif


def af(f):
    return 1

def pf(f):
    return 0

def TransferFunction(f, ampf=af, phif=pf):
    amplitude = ampf(f)
    phase = phif(f)
    return amplitude, phase

def compute_data(highest_frequency, lowest_frequency, frequency_step_size, ampf=af,phif=pf):
    steps = (highest_frequency - lowest_frequency)/frequency_step_size + 1 # add one to get a point at the last freq
    freq_range = np.linspace(lowest_frequency, highest_frequency, int(steps))

    # init arrays
    data = np.zeros([0,2])
    a_list = []
    p_list = []
    # fill arrays
    for f in freq_range:
        item = TransferFunction(f, ampf, phif)
        item = np.reshape(np.asarray(item), (1,2)) # format as [amp, phase] 
        data = np.append(data, item,axis=0)

    return data


def invert(data):
    data[:,0] = 1/(data[:,0]/np.amin(data[:,0]))
    data[:,1] = -1*data[:,1]
    return data

# graphing
if verbose:
    plt.plot(freq_range, data[:,0])
    plt.title("Amplitude")
    plt.show()
    plt.plot(freq_range, data[:,1])
    plt.title("Phase")
    plt.show()

def savetocsv(filename,data):
    np.savetxt(filename, data, delimiter=',') # save as csv
    print("File saved as " + filename)


