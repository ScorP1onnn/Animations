import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Slider, Button, RadioButtons

print(f"Spherical Coordinates \n"
      f"Influence of each coordinate = 1\n"
      f"constant r = 2 \n"
      r"constant theta = 3"f"\n"
      r"constant phi = 4" )


i = int(input("Enter value: "))

if i == 1:
    fig = plt.figure()
    fig.set_size_inches(10, 10)
    plt.subplots_adjust(bottom=0.4)
    ax = fig.add_subplot(projection='3d')
    # ax.plot([0,2],[0,3],[0,3])
    xmin, xmax, ymin, ymax, zmin, zmax = -5, 5, -5, 5, -5, 5,
    ticks_frequency = 1
    ax.set(xlim=(xmin - 5, xmax + 5), ylim=(ymin - 5, ymax + 5), zlim=(zmin - 5, zmax + 5), aspect='auto')
    ax.grid(False)

    theta_fill = np.arange(0, 45, 0.5)
    x_fill = 5 * np.cos(theta_fill * (np.pi / 180))
    y_fill = 5 * np.sin(theta_fill * (np.pi / 180))

    plt.plot([-10, 10], [0, 0], [0, 0], color="blue", marker='>', markersize=4)
    plt.plot([0, 0], [-10, 10], [0, 0], color="green", marker='>', markersize=4)
    plt.plot([0, 0], [0, 0], [-10, 10], color="red", marker='^', markersize=4)

    x_init = 5 * np.cos(45 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))
    y_init = 5 * np.sin(45 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))
    z_init = 5 * np.cos(45 * (np.pi / 180))
    p_1, = plt.plot([0, x_init], [0, y_init], [0, z_init], linewidth=2, marker='.', markersize=7)

    p_2, = plt.plot([x_init, x_init], [0, y_init], [0, 0], linestyle="--", color="blue")
    p_3, = plt.plot([0, x_init], [y_init, y_init], [0, 0], linestyle="--", color="green")
    p_4, = plt.plot([x_init, x_init], [y_init, y_init], [0, z_init], linestyle="--", color="red")

    axSlider_1 = plt.axes([0.2, 0.3, 0.65, 0.03])
    axSlider_2 = plt.axes([0.2, 0.2, 0.65, 0.03])
    axSlider_3 = plt.axes([0.2, 0.1, 0.65, 0.03])

    r_slider = Slider(
        ax=axSlider_1,
        label="r",
        valmin=0,
        valmax=9,
        valinit=5,
        valstep=0.5,
        closedmin=False,
        closedmax=True

    )

    theta_slider = Slider(
        ax=axSlider_2,
        label=r"$\theta$",
        valmin=0,
        valmax=360,
        valinit=45,
        valstep=5,
        closedmin=True,
        closedmax=True

    )

    phi_slider = Slider(
        ax=axSlider_3,
        label=r"$\phi$",
        valmin=0,
        valmax=180,
        valinit=45,
        valstep=2,
        closedmin=True,
        closedmax=True

    )


    def update(val):
        r = r_slider.val
        theta = theta_slider.val
        phi = phi_slider.val

        # r * np.cos(theta * (np.pi / 180)) * np.sin(phi*((np.pi / 180)))
        p_1.set_xdata([0, r * np.cos(theta * (np.pi / 180)) * np.sin(phi * ((np.pi / 180)))])
        p_1.set_ydata([0, r * np.sin(theta * (np.pi / 180)) * np.sin(phi * ((np.pi / 180)))])
        p_1.set_3d_properties([0, r * np.cos(phi * ((np.pi / 180)))])
        # p_2.set_xdata(5 * np.cos(theta * (np.pi / 180)))
        # p_2.set_ydata(5 * np.sin(theta * (np.pi / 180)))

        x_new = r * np.cos(theta * (np.pi / 180)) * np.sin(phi * (np.pi / 180))
        y_new = r * np.sin(theta * (np.pi / 180)) * np.sin(phi * (np.pi / 180))
        z_new = r * np.cos(phi * (np.pi / 180))

        p_2.set_xdata([x_new, x_new])
        p_2.set_ydata([0, y_new])
        p_2.set_3d_properties([0, 0])

        p_3.set_xdata([0, x_new])
        p_3.set_ydata([y_new, y_new])
        p_3.set_3d_properties([0, 0])

        p_4.set_xdata([x_new, x_new])
        p_4.set_ydata([y_new, y_new])
        p_4.set_3d_properties([0, z_new])

        fig.canvas.draw_idle()


    r_slider.on_changed(update)
    theta_slider.on_changed(update)
    phi_slider.on_changed(update)

    plt.show()



elif i == 2:
    fig = plt.figure()
    fig.set_size_inches(10, 10)
    plt.subplots_adjust(bottom=0.4)
    ax = fig.add_subplot(projection='3d')
    # ax.plot([0,2],[0,3],[0,3])
    xmin, xmax, ymin, ymax, zmin, zmax = -5, 5, -5, 5, -5, 5,
    ticks_frequency = 1
    ax.set(xlim=(xmin - 10, xmax + 10), ylim=(ymin - 10, ymax + 10), zlim=(zmin - 10, zmax + 10), aspect='auto')
    ax.grid(False)

    r = 5
    theta = np.linspace(0, 360, 500)
    phi = np.linspace(0, 180, 500)

    plt.plot([-15, 15], [0, 0], [0, 0], color="blue", marker='>', markersize=4)
    plt.plot([0, 0], [-15, 15], [0, 0], color="green", marker='>', markersize=4)
    plt.plot([0, 0], [0, 0], [-15, 15], color="red", marker='^', markersize=4)

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 5 * np.outer(np.cos(u), np.sin(v))
    y = 5 * np.outer(np.sin(u), np.sin(v))
    z = 5 * np.outer(np.ones(np.size(u)), np.cos(v))

    print(x)
    # Plot the surface
    l = ax.plot_surface(x, y, z)

    # Set an equal aspect ratio
    ax.set_aspect('auto')

    axSlider_1 = plt.axes([0.2, 0.3, 0.65, 0.03])

    r_slider = Slider(
        ax=axSlider_1,
        label="r",
        valmin=0,
        valmax=9,
        valinit=5,
        valstep=0.5,
        closedmin=False,
        closedmax=True

    )


    def update(val):
        r = r_slider.val

        ax.clear()
        xmin, xmax, ymin, ymax, zmin, zmax = -5, 5, -5, 5, -5, 5,
        ax.set(xlim=(xmin - 10, xmax + 10), ylim=(ymin - 10, ymax + 10), zlim=(zmin - 10, zmax + 10), aspect='auto')
        ax.grid(False)

        x_new = r * np.outer(np.cos(u), np.sin(v))
        y_new = r * np.outer(np.sin(u), np.sin(v))
        z_new = r * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot([-15, 15], [0, 0], [0, 0], color="blue", marker='>', markersize=4)
        ax.plot([0, 0], [-15, 15], [0, 0], color="green", marker='>', markersize=4)
        ax.plot([0, 0], [0, 0], [-15, 15], color="red", marker='^', markersize=4)

        l = ax.plot_surface(x_new, y_new, z_new)

        fig.canvas.draw_idle()


    r_slider.on_changed(update)

    plt.show()
elif i == 3:
    fig = plt.figure()
    fig.set_size_inches(10, 10)
    plt.subplots_adjust(bottom=0.4)
    ax = fig.add_subplot(projection='3d')
    # ax.plot([0,2],[0,3],[0,3])
    xmin, xmax, ymin, ymax, zmin, zmax = -5, 5, -5, 5, -5, 5,
    ticks_frequency = 1
    ax.set(xlim=(xmin - 5, xmax + 5), ylim=(ymin - 5, ymax + 5), zlim=(zmin - 5, zmax + 5), aspect='auto')
    ax.grid(False)

    r = 5
    theta = np.linspace(0, 360, 500)
    phi = np.linspace(0, 180, 500)

    plt.plot([-10, 10], [0, 0], [0, 0], color="blue", marker='>', markersize=4)
    plt.plot([0, 0], [-10, 10], [0, 0], color="green", marker='>', markersize=4)
    plt.plot([0, 0], [0, 0], [-10, 10], color="red", marker='^', markersize=4)

    x_init = r * np.cos(90 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))
    y_init = r * np.sin(90 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))
    z = r * np.cos(phi * (np.pi / 180))

    p1, = plt.plot(x_init, y_init, z)

    # l=ax.add_collection3d(plt.fill_between(y_init,z), zdir='x')

    axSlider_1 = plt.axes([0.2, 0.1, 0.65, 0.03])
    theta_slider = Slider(
        ax=axSlider_1,
        label=r"$\theta$",
        valmin=0,
        valmax=360,
        valinit=90,
        valstep=5,
        closedmin=True,
        closedmax=True

    )


    def update(val):
        theta_new = theta_slider.val

        p1.set_xdata(r * np.cos(theta_new * (np.pi / 180)) * np.sin(phi * (np.pi / 180)))
        p1.set_ydata(r * np.sin(theta_new * (np.pi / 180)) * np.sin(phi * (np.pi / 180)))
        p1.set_3d_properties(r * np.cos(phi * (np.pi / 180)))

        fig.canvas.draw_idle()


    theta_slider.on_changed(update)

    plt.show()

elif i ==4:

    fig = plt.figure()
    fig.set_size_inches(10, 10)
    plt.subplots_adjust(bottom=0.4)
    ax = fig.add_subplot(projection='3d')
    # ax.plot([0,2],[0,3],[0,3])
    xmin, xmax, ymin, ymax, zmin, zmax = -5, 5, -5, 5, -5, 5,
    ticks_frequency = 1
    ax.set(xlim=(xmin - 5, xmax + 5), ylim=(ymin - 5, ymax + 5), zlim=(zmin - 5, zmax + 5), aspect='auto')
    ax.grid(False)

    r = 5
    theta = np.linspace(0, 360, 500)
    phi = np.linspace(0, 180, 500)

    theta_grid, phi_grid = np.meshgrid(theta, phi)

    theta_grid = np.asarray(theta_grid)
    phi_grid = np.asarray(phi_grid)

    plt.plot([-10, 10], [0, 0], [0, 0], color="blue", marker='>', markersize=4)
    plt.plot([0, 0], [-10, 10], [0, 0], color="green", marker='>', markersize=4)
    plt.plot([0, 0], [0, 0], [-10, 10], color="red", marker='^', markersize=4)

    phi_init = 45

    x_init = r * np.cos(theta * (np.pi / 180)) * np.sin(45 * (np.pi / 180))
    y_init = r * np.sin(theta * (np.pi / 180)) * np.sin(45 * (np.pi / 180))
    z = r * np.cos(45 * (np.pi / 180))

    p1, = plt.plot(x_init, y_init, z)
    p2, = plt.plot([0, r * np.cos(45 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))],
                   [0, r * np.sin(45 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))],
                   [0, r * np.cos(45 * (np.pi / 180))], linestyle="--")
    p3, = plt.plot([0, r * np.cos(135 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))],
                   [0, r * np.sin(135 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))],
                   [0, r * np.cos(45 * (np.pi / 180))], linestyle="--")
    p4, = plt.plot([0, r * np.cos(225 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))],
                   [0, r * np.sin(225 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))],
                   [0, r * np.cos(45 * (np.pi / 180))], linestyle="--")
    p5, = plt.plot([0, r * np.cos(315 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))],
                   [0, r * np.sin(315 * (np.pi / 180)) * np.sin(45 * (np.pi / 180))],
                   [0, r * np.cos(45 * (np.pi / 180))], linestyle="--")

    axSlider_3 = plt.axes([0.2, 0.1, 0.65, 0.03])
    phi_slider = Slider(
        ax=axSlider_3,
        label=r"$\phi$",
        valmin=0,
        valmax=180,
        valinit=45,
        valstep=2,
        closedmin=True,
        closedmax=True

    )


    def update(val):
        phi = phi_slider.val

        p1.set_xdata(r * np.cos(theta * (np.pi / 180)) * np.sin(phi * (np.pi / 180)))
        p1.set_ydata(r * np.sin(theta * (np.pi / 180)) * np.sin(phi * (np.pi / 180)))
        p1.set_3d_properties(r * np.cos(phi * (np.pi / 180)))

        p2.set_xdata([0, r * np.cos(45 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))])
        p2.set_ydata([0, r * np.sin(45 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))])
        p2.set_3d_properties([0, r * np.cos(phi * (np.pi / 180))])

        p3.set_xdata([0, r * np.cos(135 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))])
        p3.set_ydata([0, r * np.sin(135 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))])
        p3.set_3d_properties([0, r * np.cos(phi * (np.pi / 180))])

        p4.set_xdata([0, r * np.cos(225 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))])
        p4.set_ydata([0, r * np.sin(225 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))])
        p4.set_3d_properties([0, r * np.cos(phi * (np.pi / 180))])

        p5.set_xdata([0, r * np.cos(315 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))])
        p5.set_ydata([0, r * np.sin(315 * (np.pi / 180)) * np.sin(phi * (np.pi / 180))])
        p5.set_3d_properties([0, r * np.cos(phi * (np.pi / 180))])

        fig.canvas.draw_idle()


    phi_slider.on_changed(update)

    plt.show()


