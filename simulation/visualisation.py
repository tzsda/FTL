import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def classic_view(data, step, output=None, scale_y=None, scale_x=None):
    """Display position according to time"""
    if scale_y is not None:
        plt.ylim(scale_y)
    if scale_x is not None:
        plt.xlim(scale_x)
    plt.ylabel("Distance travelled (m)")
    plt.xlabel("Time (s)")
    for i in range(len(data[..., 0])):
        plt.plot([j * step for j in range(len(data[0]))], data[i])
    if output is None:
        plt.show()
    else:
        plt.savefig(output)
    plt.clf()


def distance_view(data, step, output=None, scale_y=None, scale_x=None):
    """Display position according to time"""
    if scale_y is not None:
        plt.ylim(scale_y)
    if scale_x is not None:
        plt.xlim(scale_x)
    plt.ylabel("Gap between vehicles (m)")
    plt.xlabel("Time (s)")
    ploted_data = np.diff(data, axis=0)
    for i in range(len(ploted_data[..., 0])):
        plt.plot([j * step for j in range(len(ploted_data[0]))], ploted_data[i])
    if output is None:
        plt.show()
    else:
        plt.savefig(output)
    plt.clf()

def velocity_view(data, step, output=None, scale_y=None, scale_x=None):
    """Display position according to time"""
    if scale_y is not None:
        plt.ylim(scale_y)
    if scale_x is not None:
        plt.xlim(scale_x)
    plt.ylabel("Velocity (m/s)")
    plt.xlabel("Time (s)")
    ploted_data = np.diff(data, axis=1) / step
    for i in range(len(ploted_data[..., 0])):
        plt.plot([j * step for j in range(len(ploted_data[0]))], ploted_data[i])
    if output is None:
        plt.show()
    else:
        plt.savefig(output)
    plt.clf()


def anim(data, step, output=None):
    """Blabla"""
    fig, ax = plt.subplots()
    ax.set_xlim([-10, np.max(data) + 10])
    ax.set_ylim([-1, 1])
    ax.get_yaxis().set_visible(False)

    ax.set_xlabel("Distance (m)")

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
        writer = animation.FFMpegWriter(
            fps=15, metadata=dict(artist='Me'), bitrate=1800)
        ani.save(output, writer=writer)
    plt.clf()


def anim_roundabout(data, step, radius, output=None):
    """Blabla"""
    fig, ax = plt.subplots()

    plot_lim = radius + 10
    ax.set_xlim([-plot_lim, plot_lim])
    ax.set_ylim([-plot_lim, plot_lim])
    ax.set_aspect("equal", adjustable="box")

    graph, = plt.plot([], [], ".")
    time_text = ax.text(-plot_lim, plot_lim, "", fontsize=10)

    def animate(i):
        x_axis = radius * np.cos(data[..., i] / radius)
        y_axis = radius * np.sin(data[..., i] / radius)
        graph.set_data(x_axis, y_axis)
        time_text.set_text("Timestamp: " + str(round(step * i, 1)))

        return graph, time_text

    ani = animation.FuncAnimation(
        fig, animate, repeat=True, frames=len(data[0]), interval=0.05 / step
    )
    if output is None:
        plt.show()
    else:
        writer = animation.FFMpegWriter(
            fps=15, metadata=dict(artist='Me'), bitrate=1800)
        ani.save(output, writer=writer)
    plt.clf()


def distance_heatmap(data, step, output=None):
    plt.ylabel("Gap between vehicles (m)")
    plt.xlabel("Time (s)")
    
    ploted_data = np.diff(data, axis=0)
    x_values = np.array([step * j for j in range(len(ploted_data[0]))])
    y_values = np.array([j for j in range(len(ploted_data[..., 0]))])
    fig, ax = plt.subplots()
    im = ax.pcolormesh(x_values, y_values, ploted_data)
    fig.colorbar(im, ax=ax)
    if output is None:
        plt.show()
    else:
        plt.savefig(output)
