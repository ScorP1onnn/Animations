# Import libraries
%matplotlib inline
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive
import ipywidgets as widgets
from mpl_toolkits import mplot3d


curve = np.linspace(0,9, 101)



def tangent(x0):
    m = np.exp(x0)
    c = np.exp(x0)
    y = m*(curve-x0) + c
    return y

def draw_blue_line(x):
    if x == 4:
        return tangent(4)
    else:
        m = (np.exp(4) - np.exp(x))/(4-x)
        y = m*(curve-4) + np.exp(4)
        return y

def line(x=3):
    plt.figure()
    plt.plot(curve,np.exp(curve),color='red',label=r'$e^x$')
    plt.plot(curve,tangent(4),color='orange',label='Tangent at x = 4')
    if x <= 4:
        plt.scatter([x,4],[np.exp(x),np.exp(4)],s=100,color='blue') # facecolor='none' for hollow marker
        plt.plot(curve,draw_blue_line(x),color='blue')
    else:
        plt.scatter([4,x],[np.exp(4),np.exp(x)],s=100,color='blue') # facecolor='none' for hollow marker
        plt.plot(curve,draw_blue_line(x),color='blue')

    plt.xlim(0,7)
    plt.ylim(-100,350)
    plt.legend(loc='upper left')
    plt.show()

#make interactive slider
interactive_plot = interactive(line,x=(0,6.1,0.2))
output = interactive_plot.children[-1]
interactive_plot
