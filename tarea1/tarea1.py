#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 06 00:45:49 2022

@author: pablo
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal.signaltools as sig
from splane import analyze_sys, pretty_print_bicuad_omegayq

R1=1
R2=1

num = np.array([0,1,-R2/R1]) 
den = np.array([0,1,1])
pretty_print_bicuad_omegayq(num,den)
tarea1 = sig.TransferFunction(num,den)
plt.close('all')
analyze_sys(tarea1, 'Tarea 1 - Pablo Vecchio')

