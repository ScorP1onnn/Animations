from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

#inspired from https://cvarin.github.io/CSci-Survival-Guide/fft.html

x = np.linspace(-100,100,1000)


def packet(A, t, w, T):
    return A * np.cos(w * t) * np.exp(-t ** 2 / T ** 2)




rcParams['axes.grid'] = True
rcParams['font.size'] = 14
rcParams['axes.labelsize'] = 22

A = 1.0
w = 5
T = 2.5

 ###############################################################################
# time axis
n = 1000
t = linspace(-150,150,n)
dt = t[1] - t[0]

 ###############################################################################

dp = 2.0*pi/(t[-1] - t[0])
p = arange(-n/2,n/2)*dp

 ###############################################################################
fig = figure(figsize=(9,9))
plt.subplots_adjust(bottom=0.2)

# time series
plt.subplot(211)
p1,=plt.plot(t, packet(A,t,w,T))
plt.title("Gaussian wavepacket")
plt.xlabel(r"$x$")
plt.ylabel(r"$\psi(x)$")
plt.xlim(-40,40)







signal = packet(A, t, w, T)
trans = np.fft.fftshift(np.fft.fft(signal)) * dt / sqrt(2.0 * pi)
num_spec = np.abs(trans) ** 2

plt.subplot(212)
p3,=plt.plot(p,num_spec)
plt.xlabel(r"$p$")
plt.ylabel(r"$|\overset{\sim}{\psi}(p)|^2$")


axSlider_1 = plt.axes([0.2, 0.1, 0.65, 0.03])

t_slider = Slider(
                ax=axSlider_1,
                label=r"Packet Width",
                valmin=0.05,
                valmax=20,
                valinit=5,
                valstep=0.05,
                closedmin=False,
                closedmax=True

)

a = 5

def update(value):
    time = t_slider.val
    print(time)


    p1.set_xdata(t)
    p1.set_ydata(packet(A,t,w,time))


    signal = packet(A, t, w, time)
    trans = np.fft.fftshift(np.fft.fft(signal)) * dt / sqrt(2.0 * pi)
    num_spec = np.abs(trans) ** 2

    p3.set_xdata(p)
    p3.set_ydata(num_spec)

    fig.canvas.draw_idle()

    return time


t_slider.on_changed(update)

plt.show()
