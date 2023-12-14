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
    ALPHA_INF = 200

    INITIAL = np.array([ALPHA_INF * j for j in range(25)])
    STEP = 0.2
    DURATION = 100

    MAX_VEL = 35
    ALPHA_C = 3
    ALPHA_V = 4

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
    ALPHA_INF = 70

    STEP = 0.2
    DURATION = 130

    MAX_VEL = 45
    ALPHA_C = 6
    ALPHA_V = 30

    INITIAL = np.array([ALPHA_INF * j for j in range(50)])

    s_jam = INITIAL[-1] + 100

    parameters = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_V,
        "alpha_inf": ALPHA_INF,
        "d_start": INITIAL[-1]+ 100,
        "d_end": INITIAL[-1] + 100 + 400,
        "min_alpha": 10,
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.radar, parameters)


    visu.distance_heatmap(r, STEP)

    # visu.anim(r, STEP)


def main_accident():
    ALPHA_INF = 100

    STEP = 0.2
    DURATION = 100

    MAX_VEL = 40
    ALPHA_C = 3
    ALPHA_V = 10

    INITIAL = np.array([ALPHA_INF // 3 * j for j in range(2 * 50)])

    parameters_foreward = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_C + 10,
        "alpha_inf": ALPHA_INF,
        "t_start": 10,
        "t_end": 200,
        "alpha_min": 0,
    }



    parameters_backward = {
        "V": MAX_VEL,
        "alpha_c": ALPHA_C,
        "alpha_v": ALPHA_C + 10,
        "alpha_inf": ALPHA_INF,
        "t_start": 10,
        "t_end": 100,
        "alpha_min": 0,
    }

    m = simu.EulerMethod(DURATION, STEP)
    r = m.compute(INITIAL, ftl.accident, parameters_backward)

    # visu.distance_heatmap(r, STEP)

    #visu.classic_view(np.take(r, np.unique(np.random.randint(0, r.shape[0], 35)) ,axis=0), STEP )

    visu.anim(r, STEP)


main_accident()
# main_radar()
# main_130()
# main_110()
