import matplotlib.pyplot as plt
from pylab import *
import numpy as np
from matplotlib.widgets import Slider


fig = figure(figsize=(10,10))
plt.subplots_adjust(bottom=0.25)

x = np.linspace(3,5,1000)   #for one peak
#x = np.linspace(3,10,1000)   #for three peaks






def wave_function(n):
    sum = 0
    for i in range(n):
        m = i + 1
        sum = sum + np.exp((m*1j) * np.pi * x)

    sum = ((1 / np.sqrt(2 * np.pi * n))) * sum  #((1 / np.sqrt(2 * np.pi * n))) is some arbitrary normalisation parameter
    return sum

def fft(t):
    return np.abs((np.fft.fftshift(np.fft.fft(wave_function(t))) * (x[1] - x[0]) / sqrt(2.0 * pi)))**2

plt.subplot(311)
p1,=plt.plot(x,np.real(wave_function(1)),label=r'$\Psi(x)$')
plt.ylim(-0.5,2.5)
plt.legend()

plt.subplot(312)
p2,=plt.plot(x,(np.abs(wave_function(1) ** 2)),color='orange',label=r'$|\Psi(x)|^2$')
plt.ylim(0,5)
plt.legend()

dx = 1/len(x) ## sampling width
w = 1/dx

plt.subplot(313)
p = np.sort(np.fft.fftfreq(x.shape[0]))*w
p3,=plt.plot(p,fft(1),label=r'$\Psi(p)$')
plt.legend()




axSlider_1 = plt.axes([0.2, 0.1, 0.65, 0.03])
sp_slider = Slider(
                ax=axSlider_1,
                label=r"Number of waves",
                valmin=1,
                valmax=30,
                valinit=1,
                valstep=1,
                closedmin=True,
                closedmax=True

)


def update(value):
    n = sp_slider.val

    p1.set_ydata(np.real(wave_function(n)))
    p2.set_ydata(np.abs(wave_function(n) ** 2))

    p3.set_ydata(fft(n))
    fig.canvas.draw_idle()

sp_slider.on_changed(update)


plt.show()
