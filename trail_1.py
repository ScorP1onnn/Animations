import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import scipy.constants as const


L = 10

x = np.linspace(0,L,101)
print(x)

def wave_function(x,n,l):
    y = np.sqrt(2/l) * np.sin((n * np.pi * x)/l)
    return y

def energy(n,l):
    m = 1e-26 #mass
    e = (((np.pi**2) * (const.hbar ** 2))/(2*m*(l**2))) * 1e41

    e_n = (n ** 2) * e
    return e_n


a = wave_function(x,1,L)
b = a ** 2

fig, (ax1,ax2) = plt.subplots(1,2)
plt.subplots_adjust(bottom=0.25)

ax1.plot(x,a + energy(1,L))
ax1.set_ylim(-energy(10,L),energy(13,L))
ax1.set_yticks([energy(1,L)], labels=[f"1E"])
ax1.set_xticks([0,L],labels=[0,f"L"])
ax1.axhline(energy(1,L), color='grey', linestyle='--')
ax1.set_title(r"$\psi(x)$")
ax1.axvline(0, color='black')
ax1.axvline(L, color='black')


ax2.plot(x,b + energy(1,L))
ax2.set_ylim(-energy(10,L),energy(13,L))
ax2.set_yticks([energy(1,L)], labels=[f"1E"])
ax2.set_xticks([0,L],labels=[0,f"L"])
ax2.axhline(energy(1,L), color='grey', linestyle='--')
ax2.set_title(r"$|\psi(x)|^2$")
ax2.axvline(0, color='black')
ax2.axvline(L, color='black')


axSlider_1 = plt.axes([0.2, 0.1, 0.65, 0.03])

s_slider = Slider(
                ax=axSlider_1,
                label="n",
                valmin=1,
                valmax=10,
                valinit=1,
                valstep=1,
                closedmin=True,
                closedmax=True

)

def update(value):
    level = s_slider.val

    ax1.clear()
    ax2.clear()

    a_level = wave_function(x,level,L)
    b_level = a_level ** 2
    e_level = energy(level,L)


    ax1.plot(x,a_level + e_level)
    ax2.plot(x, b_level + e_level)

    ax1.set_ylim(-energy(10,L),energy(13,L))
    ax1.set_yticks([e_level], labels=[f"{level ** 2}E"])
    ax1.set_xticks([0,L],labels=[0,f"L"])
    ax1.axhline(e_level, color='grey', linestyle='--')
    ax1.axvline(0, color='black')
    ax1.axvline(L, color='black')
    ax1.set_title(r"$\psi(x)$")

    ax2.set_ylim(-energy(10,L),energy(13,L))
    ax2.set_yticks([e_level], labels=[f"{level ** 2}E"])
    ax2.set_xticks([0,L],labels=[0,f"L"])
    ax2.axhline(e_level, color='grey', linestyle='--')
    ax2.axvline(0, color='black')
    ax2.axvline(L, color='black')
    ax2.set_title(r"$|\psi(x)|^2$")

    fig.canvas.draw_idle()


s_slider.on_changed(update)

plt.show()
