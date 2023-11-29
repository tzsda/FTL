import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu


def main():
    INITIAL = np.array([5 * j for j in range(8)])
    STEP = 0.2
    DURATION = 20

    parameters = {"V": 30, "alpha_c": 10, "alpha_v": 40, "alpha_inf": 60}

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, simu.FTL_traffic_light, parameters)

    # visu.classic_view(r, STEP)

    visu.anim(r, STEP, None)


main()

