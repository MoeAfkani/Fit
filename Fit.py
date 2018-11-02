#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 2018
An script to fit 3D data (x,y,y_err) on y =0.4 * (a + 1) *(b-x) - 0.434294 * 10.^(0.4 * (b-x) ) + c to find a,b,c
@author: M.Afkani , Afkani.ir
"""

# **********************************
import sys, os
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
# Read Valid Data
f = open(sys.argv[1],"r")
lines = f.readlines()
f.close()
f = open("newfile.txt","w")
for line in lines:
  if line!="#    x     y       error_y   "+"\n":
    f.write(line)
f.close()

file = open('newfile.txt')
lst = [] 
for line in file:
    lst.append([ float(x) for x in line.split()])
xdata = [ x[0] for x in lst]
ydata = [ x[1] for x in lst]
yerr  = [ x[2] for x in lst]
os.remove("newfile.txt") 
# Read Valid Data
# **********************************
popt, pcov = curve_fit(F, xdata, ydata , sigma=yerr )
popt
xpints= np.linspace(min(xdata),max(xdata), 100000)
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
