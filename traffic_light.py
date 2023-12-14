import numpy as np

import matplotlib.pyplot as plt

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.ftl as ftl


def main():
    N = 25
    INITIAL = np.array([3 * j for j in range(N)]) # np.array([0, 90, 130 ])
    INITIAL = np.sort(INITIAL)

    print(INITIAL)
    STEP = 0.2
    DURATION = 100

    parameters = {"V": 16, "alpha_c": 6, "alpha_v": 30, "alpha_inf": 60}
    parameters_2 = {"V": 26, "alpha_c": 3, "alpha_v": 50, "alpha_inf": 80}

    name = str(N) + '-'
    for k,v in parameters.items():
        name += str(k) + str(v) + "-"

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.traffic_light, parameters)

    # visu.velocity_view(r, STEP, name + "velocity.png")
    # visu.classic_view(r, STEP, name + ".png")
    visu.distance_heatmap(r, STEP, "")

    # visu.anim(r, STEP)


main()
