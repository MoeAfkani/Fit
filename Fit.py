#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 2018
An script to fit 3D data (x,y,y_err) on y =0.4 * (a + 1) *(b-x) - 0.434294 * 10.^(0.4 * (b-x) ) + c to find a,b,c
@author: M.Afkani , Afkani.ir
"""

# **********************************
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#np.random.seed(1729)
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 10,
        }
# **********************************

# The Fitting Function
def F(x,a,b,c):
    return 0.4 * (a + 1) *(b-x) - 0.434294 * 10.**(0.4 * (b-x) ) + c
# The Fitting Function
# **********************************
# Valid Data
xdata=[-23.75,-23.25,-22.75,-22.25,-21.75,-21.25,-20.75,-20.25,-19.75,-19.25,-18.75,-18.25,-17.75,-17.25]
ydata=[-6.269055,-5.968025,-4.990302,-4.197173,-3.811173,-3.547245,-3.399823,-3.274298,-3.179857,-3.077325,-2.958362,-2.881843,-2.792513,-2.706881]
yerr=[1.0,0.707107,0.229416,0.092057,0.059028,0.043561,0.036761,0.031814,0.028537,0.025359,0.022113,0.020249,0.01827,0.016554]

# Valid Data
# **********************************
popt, pcov = curve_fit(F, xdata, ydata , sigma=yerr )
popt
xpints= np.linspace(min(xdata),max(xdata), 10000)
plt.plot(xpints, F(xpints,*(popt)), 'r-', 
         label='Fit details:\n a=%5.5f$\pm$%.5e\n b=%5.5f$\pm$%.5e\n c=%5.5f$\pm$%.5e' %(popt[0],pcov[0][0],popt[1],pcov[0][1],popt[2],pcov[0][2]))
plt.errorbar(xdata, ydata, yerr=yerr,fmt='.k', color='black',
             ecolor='lightgray', elinewidth=3, capsize=3)
#plt.plot(xpints, F(xpints,*(popt-pcov[0])), 'b-', 
     #    label='Fit details:\n a=%5.5f$\pm$%.5e\n b=%5.5f$\pm$%.5e\n c=%5.5f$\pm$%.5e' %(popt[0],pcov[0][0],popt[1],pcov[0][1],popt[2],pcov[0][2]))
plt.title(r'$y =0.4 * (a+1) *(b-x) - 0.434294E(0.4 * (b-x) ) + c$', fontdict=font)
plt.legend(loc='best')
plt.savefig('Fit.pdf', format='pdf', dpi=1000)
plt.savefig('Fit.png', format='png', dpi=1000)
plt.show()
