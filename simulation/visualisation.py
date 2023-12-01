import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def classic_view(data, step, output=None, scale_y=None, scale_x=None):
    """Display position according to time"""
    if scale_y is not None:
        plt.ylim(scale_y)
    if scale_x is not None:
        plt.xlim(scale_x)
    for i in range(len(data[..., 0])):
        plt.plot([j * step for j in range(len(data[0]))], data[i])
    if output is None:
        plt.ylabel("Distance travelled")
        plt.xlabel("Time")
        plt.show()
    else:
        plt.savefig(output)
        plt.clf()


def anim(data, step, output=None):
    """Blabla"""
    fig, ax = plt.subplots()
    ax.set_xlim([-10, np.max(data) + 10])
    ax.set_ylim([-1, 1])

    ax.set_xlabel("Distance")

    (graph,) = plt.plot([], [], ".")
    time_text = ax.text(0, 0.8, "", fontsize=15)

    y_axis = [0 for i in range(len(data[..., 0]))]

    def animate(i):
        graph.set_data(data[..., i], y_axis)
        time_text.set_text("Timestamp: " + str(round(step * i, 1)))

        return graph, time_text

    ani = animation.FuncAnimation(
        fig, animate, repeat=True, frames=len(data[0]), interval=step * 0.25
    )
    if output is None:
        plt.show()
    else:
        ani.save(output)


def anim_roundabout(data, step, radius, output=None):
    """Blabla"""
    fig, ax = plt.subplots()

    plot_lim = radius + 10
    ax.set_xlim([-plot_lim, plot_lim])
    ax.set_ylim([-plot_lim, plot_lim])
    ax.set_aspect('equal', adjustable='box')

    graph, = plt.plot([], [], ".")
    time_text = ax.text(-plot_lim, plot_lim, "", fontsize=10)

    def animate(i):
        x_axis = radius * np.cos(data[..., i] / radius)
        y_axis = radius * np.sin(data[..., i] / radius)
        graph.set_data(x_axis, y_axis)
        time_text.set_text("Timestamp: " + str(round(step * i, 1)))

        return graph, time_text

    ani = animation.FuncAnimation(
        fig, animate, repeat=True, frames=len(data[0]), interval=step * 0.25
    )
    if output is None:
        plt.show()
    else:
        ani.save(output)
