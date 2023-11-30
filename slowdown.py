import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.core as tools


def main_130():
    ALPHA_INF = 100

    INITIAL = np.array([ALPHA_INF * j for j in range(25)])
    STEP = 0.2
    DURATION = 50

    MAX_VEL = 468
    ALPHA_C = 10
    ALPHA_V = 40

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
        "max_time": 20,
        "rate": tools.compute_brake_rate(MAX_VEL),
        "min_alpha": tools.compute_alpha(MAX_VEL, MAX_VEL - 72, ALPHA_C, ALPHA_V)
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, simu.FTL_slowdown, parameters)

    visu.classic_view(r, STEP, "130.png")

    # visu.anim(r, STEP)


def main_110():
    ALPHA_INF = 100

    INITIAL = np.array([ALPHA_INF * j for j in range(25)])
    STEP = 0.2
    DURATION = 50

    MAX_VEL = 396
    ALPHA_C = 10
    ALPHA_V = 40

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
        "max_time": 20,
        "rate": tools.compute_brake_rate(MAX_VEL),
        "min_alpha": tools.compute_alpha(MAX_VEL, MAX_VEL - 36, ALPHA_C, ALPHA_V)
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, simu.FTL_slowdown, parameters)

    visu.classic_view(r, STEP, "100.png")

    # visu.anim(r, STEP)

main_130()
main_110()
