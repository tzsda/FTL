import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.ftl as ftl
import simulation.utils as tools


def main():
    RADIUS = 20
    N = 5
    INITIAL = np.array([round((2 * np.pi * RADIUS) / N) * j for j in range(N)])
    STEP = 0.2
    DURATION = 70

    parameters = {"V": 10, "alpha_c": 10, "alpha_v": 20, "radius": RADIUS}
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.roundabout, parameters, tools.mod_radius, callback_parameters)

    # plt.plot([j * STEP for j in range(len(r[0]))], r[-1] -r[-2])
    # plt.show()

    # visu.classic_view(r, STEP)

    visu.anim_roundabout(r, STEP, RADIUS)


main()