import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def classic_view(data, step, output=None):
    """Display position according to time"""
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
        fig, animate, repeat=True, frames=len(data[0]), interval=step * 1000
    )
    if output is None:
        plt.show()
    else:
        ani.save(output)
