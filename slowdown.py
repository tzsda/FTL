import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.core as tools


def main():
    INITIAL = np.array([100 * j for j in range(30)])
    STEP = 0.2
    DURATION = 50

    MAX_VEL = 30
    ALPHA_C = 10
    ALPHA_V = 50

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": 60,
        "max_time": DURATION - DURATION // 3,
        "rate": 2,
        "min_alpha": tools.compute_alpha(MAX_VEL, MAX_VEL-30, ALPHA_C, ALPHA_V)
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, simu.FTL_slowdown, parameters)

    # visu.classic_view(r, STEP)

    visu.anim(r, STEP, None)


main()
