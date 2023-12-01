import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.ftl as ftl


def main():
    INITIAL = np.array([5 * j for j in range(8)])
    STEP = 0.2
    DURATION = 70

    parameters = {"V": 16, "alpha_c": 3, "alpha_v": 30, "alpha_inf": 60}

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.traffic_light, parameters)

    # visu.classic_view(r, STEP)

    visu.anim(r, STEP, None)


main()
