# Import libraries
%matplotlib inline

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets

def vec(mag,theta,phi):
    dx = mag * np.cos(np.pi / 180 * theta) * np.sin(np.pi/ 180 * phi)
    dy = mag * np.sin(np.pi / 180 * theta) * np.sin(np.pi/ 180 * phi)
    dz = mag * np.cos(np.pi/ 180 * phi)
    return dx,dy,dz




def cross(mag=5,theta=0,phi=90):
    fig = plt.figure()
    fig.set_size_inches(12, 12)
    ax = fig.add_subplot(111, projection='3d')
    xmin, xmax, ymin, ymax, zmin, zmax = -5, 5, -5, 5, -5, 5,
    #ax.set(xlim=(xmin - 5, xmax + 5), ylim=(ymin - 5, ymax + 5), zlim=(zmin - 20, zmax + 20), aspect='auto')
    ax.set(xlim=(xmin - 6, xmax + 6), ylim=(ymin - 6, ymax + 6), zlim=(zmin - 20, zmax + 20), aspect='auto')
    ax.plot([-11,11],[0,0],[0,0],color='black', marker='>', markersize=4)
    ax.plot([0,0],[-11,11],[0,0],color='black', marker='>', markersize=4)
    ax.plot([0,0],[0,0],[-40,40],color='black', marker='^', markersize=4)
    #ax.axis('off')
    ax.text(5,-1.5,0,"X-Axis")
    ax.text(0.5,5,0,"Y-Axis")
    
    
    dx = mag * np.cos(np.pi / 180 * theta) * np.sin(np.pi/ 180 * phi)
    dy = mag * np.sin(np.pi / 180 * theta) * np.sin(np.pi/ 180 * phi)
    dz = mag * np.cos(np.pi/ 180 * phi)
    
    v1 = np.asarray([dx,dy,dz])
    v2 = np.asarray(vec(5,90,90))
    v_cross = np.cross(v1,v2)
    
    ax.quiver([0,0,0],[0,0,0],[0,0,0],[v1[0],0,0],[dy,0,0],[dz,0,0],color=['red'],linewidth=2)
    ax.quiver([0,0,0],[0,0,0],[0,0,0],[0,v2[0],0],[0,v2[1],0],[0,v2[2],0],color=['blue'],linewidth=3)
    ax.quiver([0,0,0],[0,0,0],[0,0,0],[v_cross[0],0,0],[v_cross[1],0,0],[v_cross[2],0,0],color=['green'],linewidth=2)
    ax.text(0,5,45,f"v x w",fontsize=20,color='green')
    ax.text(3.2,5,47.4,f" = {np.round(v_cross[0],2)}i + {np.round(v_cross[1],2)}j + {np.round(v_cross[2],2)}k",fontsize=15)
    plt.show()
    
interactive_plot = interactive(cross,mag = (-10,10,0.2), theta = (0,360,1), phi= (0,180,1))
output = interactive_plot.children[-1]
interactive_plot
