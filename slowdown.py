import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.utils as tools
import simulation.ftl as ftl


def main_130():
    ALPHA_INF = 70

    STEP = 10
    DURATION = 100

    MAX_VEL = 40
    ALPHA_C = 3
    ALPHA_V = 70

    INITIAL = np.array([ALPHA_INF * j for j in range(25)])

    DIST_BRAKE = 500

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
        "max_time": 10,
        "rate": tools.compute_brake_rate(DIST_BRAKE),
        "min_alpha": 30,
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.slowdown, parameters)

    # visu.classic_view(r, STEP)
    # visu.classic_view(np.diff(r), STEP)

    visu.anim(r, STEP)


def main_110():
    ALPHA_INF = 60

    INITIAL = np.array([ALPHA_INF * j for j in range(25)])
    STEP = 50
    DURATION = 100

    MAX_VEL = 35
    ALPHA_C = 3
    ALPHA_V = 60

    DIST_BRAKE = 500

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
        "max_time": 10,
        "rate": tools.compute_brake_rate(DIST_BRAKE),
        "min_alpha": 47,
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.slowdown, parameters)

    visu.classic_view(r, STEP, scale_y=[0, 3500])

    # visu.anim(r, STEP)


def main_radar():
    ALPHA_INF = 50

    STEP = 0.2
    DURATION = 200

    MAX_VEL = 45
    ALPHA_C = 3
    ALPHA_V = 70

    INITIAL = np.array([ALPHA_INF * j for j in range(50)])

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
        "d_start": 3000,
        "d_end": 4000,
        "min_alpha": 30,
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.radar, parameters)

    # visu.classic_view(r, STEP)

    visu.anim(r, STEP)


main_radar()
main_130()
main_110()
