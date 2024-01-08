import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def classic_view(data, step, output=None):
    """Display position according to time"""
    plt.ylabel("Position (m)")
    plt.xlabel("Time (s)")
    for i in range(len(data[..., 0])):
        plt.plot([j * step for j in range(len(data[0]))], data[i])
    if output is None:
        plt.show()
    else:
        plt.savefig(output)
    plt.clf()


def distance_view(data, step, output=None):
    """Display position according to time"""
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


def velocity_view(data, step, output=None):
    """Display position according to time"""
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


def position_versus_time_scatter(data, step, number, output=None):
    plt.ylabel("Position (m)")
    plt.xlabel("Time (s)")

    step_index = data.shape[1] // number
    cars_number = len(data[..., 0])

    for i in range(number):
        plt.scatter(
            [step * step_index * i for j in range(cars_number)],
            data[..., step_index * i],
            marker=".",
        )
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
        fig, animate, repeat=True, frames=len(data[0]), interval=0.001
    )
    if output is None:
        plt.show()
    else:
        writer = animation.FFMpegWriter(
            fps=15, metadata=dict(artist="Me"), bitrate=1800
        )
        ani.save(output, writer=writer)
    plt.clf()


def anim_roundabout(data, step, radius, output=None):
    """Blabla"""
    fig, ax = plt.subplots()

    plot_lim = radius + 10
    ax.set_xlim([-plot_lim, plot_lim])
    ax.set_ylim([-plot_lim, plot_lim])
    ax.set_aspect("equal", adjustable="box")

    (graph,) = plt.plot([], [], ".")
    (head,) = plt.plot([], [], "r.")

    time_text = ax.text(-plot_lim, plot_lim, "", fontsize=10)

    def animate(i):
        x_axis = radius * np.cos(data[..., i] / radius)
        y_axis = radius * np.sin(data[..., i] / radius)
        graph.set_data(x_axis[:-1], y_axis[:-1])
        head.set_data([x_axis[-1]], [y_axis[-1]])
        time_text.set_text("Timestamp: " + str(round(step * i, 1)))

        return graph, head, time_text

    ani = animation.FuncAnimation(
        fig, animate, repeat=True, frames=len(data[0]), interval=(1 / (step * 1000))
    )
    if output is None:
        plt.show()
    else:
        writer = animation.FFMpegWriter(
            fps=15, metadata=dict(artist="Me"), bitrate=1800
        )
        ani.save(output, writer=writer)
    plt.clf()


def compute_density(data, step, chunk_length, alpha_c):
    chunks_number = int(np.max(data) / chunk_length)
    data = data / chunk_length
    data = np.floor(data)

    density = np.zeros(shape=(chunks_number + 1, len(data[0])))

    for t in range(len(data[0])):
        for v in data[..., t]:
            density[int(v), t] += 1

    max_cars_per_chunk = chunk_length / alpha_c
    density = density / max_cars_per_chunk

    x_values = chunk_length * np.arange(0, chunks_number + 1)
    y_values = step * np.arange(0, len(density[0]))

    density = np.transpose(density)
    return density, x_values, y_values


def display_density(data, step, chunk_length, alpha_c, output=None, n_tirage=5):
    density, x_values, y_values = compute_density(data, step, chunk_length, alpha_c)
    incr = int(
        len(
            density[
                ...,
            ]
        )
        / n_tirage
    )
    for i in range(1, n_tirage):
        print(i * incr * step)
        y = density[i * incr, ...]
        # x = chunk_length * np.arange(0, len(y))
        plt.plot(x_values, y)
    plt.xlabel("Position (m)")
    plt.ylabel("Density")
    plt.show()


def density_heatmap(
    data,
    step,
    chunk_length,
    alpha_c,
    output=None,
    max_x_display=None,
    max_y_display=None,
):
    density, x_values, y_values = compute_density(data, step, chunk_length, alpha_c)

    print(density.shape)
    print(len(x_values), len(y_values))

    fig, ax = plt.subplots()
    im = ax.pcolormesh(x_values, y_values, density, label="")
    ax.set_xlabel("Position (m)")
    ax.set_ylabel("Time (s)")
    fig.colorbar(im, ax=ax)

    if output is None:
        plt.show()
    else:
        plt.savefig(output)
    plt.clf()


def distance_heatmap(data, step, output=None):
    ploted_data = np.diff(data, axis=0)
    x_values = np.array([step * j for j in range(len(ploted_data[0]))])
    y_values = np.array([j for j in range(len(ploted_data[..., 0]))])
    fig, ax = plt.subplots()
    im = ax.pcolormesh(x_values, y_values, ploted_data, label="aqzsdfgh")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Vehicle index")
    fig.colorbar(im, ax=ax)
    if output is None:
        plt.show()
    else:
        plt.savefig(output)
    plt.clf()


def velocity_heatmap(data, step, output=None):
    ploted_data = np.diff(data, axis=1) / step
    x_values = np.array([step * j for j in range(len(ploted_data[0]))])
    y_values = np.array([j for j in range(len(ploted_data[..., 0]))])
    fig, ax = plt.subplots()
    im = ax.pcolormesh(x_values, y_values, ploted_data)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Vehicle index")
    fig.colorbar(im, ax=ax)
    if output is None:
        plt.show()
    else:
        plt.savefig(output)
    plt.clf()
