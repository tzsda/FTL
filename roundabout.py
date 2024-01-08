import numpy as np

import simulation.euler as simu
import simulation.visualisation as visu
import simulation.ftl as ftl
import simulation.utils as tools


def main():
    RADIUS = 20
    N = 20
    INITIAL = np.array([round((2 * np.pi * RADIUS) / N) * j for j in range(N)])
    STEP = 0.2
    DURATION = 200

    parameters = {
        "V": 15,
        "alpha_c": 3,
        "alpha_v": 20,
        "radius": RADIUS,
        "t_start": 20,
        "t_end": 150,
        "alpha_min": 0,
        "eps": 1e-4,
    }
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP, tools.mod_radius, callback_parameters)
    r = m.compute(INITIAL, ftl.roundabout, parameters)

    visu.anim_roundabout(r, STEP, RADIUS)


def jami_1():
    RADIUS = 14
    N = 10
    INITIAL = np.array([(2 * np.pi * RADIUS) * (j / N) for j in range(N)])
    STEP = 0.2
    DURATION = 60

    parameters = {
        "V": 18,
        "alpha_c": 4,
        "alpha_v": 17,
        "radius": RADIUS,
        "t_start": 1,
        "t_end": 10,
        "step": STEP,
        "alpha_min": 6,
        "eps": 1e-4,
        "alpha_inf": 25,
    }
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP, tools.mod_radius, callback_parameters)
    r = m.compute(INITIAL, ftl.roundabout, parameters)

    visu.anim_roundabout(r, STEP, RADIUS, "jami1.mp4")


def jami_2():
    RADIUS = 14
    N = 15
    INITIAL = np.array([(2 * np.pi * RADIUS) * (j / N) for j in range(N)])
    STEP = 0.2
    DURATION = 60

    parameters = {
        "V": 25,
        "alpha_c": 3,
        "alpha_v": 17,
        "radius": RADIUS,
        "t_start": 1,
        "t_end": 8,
        "step": STEP,
        "alpha_min": 0,
        "eps": 1e-4,
        "alpha_inf": 25,
    }
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP, tools.mod_radius, callback_parameters)
    r = m.compute(INITIAL, ftl.roundabout, parameters)

    visu.anim_roundabout(r, STEP, RADIUS, "jami2.mp4")


def jami_3():
    RADIUS = 14
    N = 24
    INITIAL = np.array([(2 * np.pi * RADIUS) * (j / N) for j in range(N)])
    STEP = 0.2
    DURATION = 60

    parameters = {
        "V": 18,
        "step": STEP,
        "alpha_c": 3,
        "alpha_v": 6.5,
        "radius": RADIUS,
        "t_start": 1,
        "t_end": 6,
        "alpha_min": 0,
        "eps": 1e-4,
        "alpha_inf": 5,
    }
    callback_parameters = {"eps": 1e-4, "radius": RADIUS}

    m = simu.EulerMethod(DURATION, STEP, tools.mod_radius, callback_parameters)
    r = m.compute(INITIAL, ftl.roundabout, parameters)

    visu.anim_roundabout(r, STEP, RADIUS, "jami3.mp4")


# main()

jami_3()
