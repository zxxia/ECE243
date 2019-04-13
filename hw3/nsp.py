# -*- coding: utf-8 -*-
"""
ECE C143/C243 Homework-3
Helper functions for Neural Signal Processing

"""
import numpy as np
import matplotlib.pyplot as plt

def GeneratePoissonSpikeTrain( T, rate ):
#GENERATEPOISSONSPIKETRAIN Summary of this function goes here
#   T in ms
#   r in spikes/s
#   returns spike_train, a collection of spike times

    spike_train = np.array(0)
    time = 0

    while time <= T:
        time_next_spike = np.random.exponential(1/rate * 1000)
        time = time + time_next_spike
        spike_train = np.append(spike_train,time)

    #discard last spike if happens after T
    if (spike_train[np.size(spike_train)-1] > T) :
        spike_train = spike_train[:-1]
    return spike_train

"""
Input S is spike_times described in Jupyter Notebook.
"""

def PlotSpikeRaster(S):
    gap = 3
    mark = 5
    pad = 30

    numSpikeTrains = np.size(S);
    for s in range(numSpikeTrains):
        offset = pad + gap + s*(gap+mark)
        train = S[s]
        if np.size(train)!=0 :
            train = train[:]
            for t in train.T :
                plt.plot([t,t], [offset, offset+mark], color=[0,0,0])

    plt.xlabel('Time (ms)')
    plt.ylim([0,offset+mark+gap+pad])
