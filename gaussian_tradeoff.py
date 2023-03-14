import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model
from matplotlib.widgets import Slider

fig = plt.figure()
fig.set_size_inches(8, 8)
plt.subplots_adjust(bottom=0.4)


x = np.linspace(-100,100,1000)


def guass(x, x_0, s):
    m = np.exp(-0.5 * (((x - x_0) / s) ** 2))
    n = (s * np.sqrt(2 * np.pi))
    y = (m / n)
    return y

std = 6
mean = 0
m = np.exp(-0.5 * (((x - mean) / std) ** 2))
n = (std * np.sqrt(2 * np.pi))
y = (m / n)


#plt.plot(x,y)
#plt.show()

y_fft = np.fft.fftshift(np.abs(np.fft.fft(y))/np.sqrt(len(y)))

gm = Model(guass)

params=gm.make_params(x_0=0,s=0.02)

out = gm.fit(y_fft,params,x=x)

print(out.fit_report())

#plt.plot(x,y)
#plt.plot(x,y_fft)
#plt.show()

p1,=plt.plot(x,y,color='blue', label='Original Gaussian')
p2,=plt.plot(x,y_fft,color='orange',label="Fourier Transform of Gaussian")
plt.legend()
#plt.plot(x,out.best_fit,color='red')

axSlider_1 = plt.axes([0.2, 0.1, 0.65, 0.03])

s_slider = Slider(
                ax=axSlider_1,
                label=r"$\sigma$",
                valmin=0.05,
                valmax=10,
                valinit=5,
                valstep=0.05,
                closedmin=False,
                closedmax=True

)

def update(value):
    std = s_slider.val

    mean = 0
    m = np.exp(-0.5 * (((x - mean) / std) ** 2))
    n = (std * np.sqrt(2 * np.pi))
    y = (m / n)

    y_fft = np.fft.fftshift(np.abs(np.fft.fft(y)) / np.sqrt(len(y)))

    p1.set_xdata(x)
    p1.set_ydata(y)

    p2.set_xdata(x)
    p2.set_ydata(y_fft)

    fig.canvas.draw_idle()

s_slider.on_changed(update)

plt.show()
